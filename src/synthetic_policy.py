"""Portfolio-safe miniature of the SUBWAY GAME decision loop.

All ten values below are invented for demonstration. No competition data,
station geometry, personal data, trained weights, or private replay is loaded.
This program is not the June 2026 validation pipeline.
"""

from __future__ import annotations

from dataclasses import dataclass
from math import ceil


SYNTHETIC_CROWD_PCT = (48, 55, 76, 122, 105, 88, 73, 46, 41, 49)
SYNTHETIC_NEXT_STATION_PCT = (50, 57, 74, 115, 102, 82, 69, 44, 39, 48)
ASSUMED_WAITING = 400
P90_ABSOLUTE_ERROR_FROM_PRIVATE_BACKTEST_PP = 5.36
MIN_PREDICTED_GAP_PP = 2 * P90_ABSOLUTE_ERROR_FROM_PRIVATE_BACKTEST_PP


@dataclass(frozen=True)
class Mission:
    from_car: int
    to_car: int
    predicted_gap_pp: float
    walk_minutes: int


def upper_quartile(values: tuple[float, ...]) -> float:
    ordered = sorted(values)
    return ordered[int(0.75 * (len(ordered) - 1))]


def choose_mission(
    observed: tuple[float, ...],
    predicted: tuple[float, ...],
    from_car: int,
    max_walk_minutes: int = 5,
) -> Mission | None:
    """Mirror the prototype's transparent, constrained ranking rule."""
    if len(observed) != 10 or len(predicted) != 10:
        raise ValueError("The illustrative train must have ten cars.")
    if not 1 <= from_car <= 10:
        raise ValueError("from_car must be 1..10.")
    origin = from_car - 1
    if observed[origin] < upper_quartile(observed):
        return None

    candidates: list[tuple[float, int, int]] = []
    for target in range(10):
        if target == origin:
            continue
        walk = ceil(abs(target - origin) * 0.35)
        gap = predicted[origin] - predicted[target]
        if walk <= max_walk_minutes and gap >= MIN_PREDICTED_GAP_PP:
            candidates.append((predicted[target], walk, target))
    if not candidates:
        return None
    _, walk, target = min(candidates)
    return Mission(from_car, target + 1, round(predicted[origin] - predicted[target], 1), walk)


def largest_remainder(weights: tuple[float, ...], total: int) -> list[int]:
    """Allocate all synthetic waiting people; no person disappears in rounding."""
    if total < 0 or any(value < 0 for value in weights):
        raise ValueError("Total and weights must be nonnegative.")
    weight_sum = sum(weights)
    if weight_sum == 0:
        return [0] * len(weights)
    exact = [value * total / weight_sum for value in weights]
    counts = [int(value) for value in exact]
    remaining = total - sum(counts)
    order = sorted(range(len(weights)), key=lambda i: (-(exact[i] - counts[i]), i))
    for index in order[:remaining]:
        counts[index] += 1
    return counts


def metrics(counts: list[int]) -> dict[str, float]:
    total = sum(counts)
    if total == 0:
        return {"max_queue": 0, "hhi": 0.0}
    return {
        "max_queue": max(counts),
        "hhi": round(sum((value / total) ** 2 for value in counts), 5),
    }


def main() -> None:
    mission = choose_mission(
        SYNTHETIC_CROWD_PCT, SYNTHETIC_NEXT_STATION_PCT, from_car=4
    )
    before = largest_remainder(SYNTHETIC_CROWD_PCT, ASSUMED_WAITING)
    after = before.copy()
    if mission:
        after[mission.from_car - 1] -= 1  # one hypothetical volunteer
        after[mission.to_car - 1] += 1
    print("SOURCE: SYNTHETIC_ONLY")
    print("Observed-like inputs (%):", SYNTHETIC_CROWD_PCT)
    print("Predicted-like inputs (%):", SYNTHETIC_NEXT_STATION_PCT)
    print("Mission decision:", mission)
    print("400-person assumed queue before:", before, metrics(before))
    print("After one hypothetical completed move:", after, metrics(after))
    print("No field effect, live sensor, or actual passenger movement is inferred.")


if __name__ == "__main__":
    main()
