# Methods / 수학과 알고리즘

This document distinguishes **implemented prototype logic**, **scenario analysis**, and **future optimization**. / 이 문서는 **현재 구현**, **시나리오 분석**, **향후 최적화**를 구분합니다.

## 1. Data engineering and quality / 데이터 처리와 품질

**Implemented.** The project parsed 69 competition CSVs (390,865 rows), reconstructed train visits, and retained 9,909 visits with all ten nonnegative car values. Quality checks counted 1,367,783 negative **cells**, 85,125 missing cells, and 1,500 duplicate records. These counts have different denominators; negative cells must not be described as negative rows.

**구현:** 공모전 제공 CSV 69개(390,865행)에서 열차 방문을 재구성하고 10칸 값이 모두 유효한 9,909건을 분리했습니다. 음수 **셀** 1,367,783개, 누락 셀 85,125개, 중복 레코드 1,500건을 확인했습니다. 각각의 분모가 다릅니다.

For the operator baseline, other observation days at the **same station and hour** supply a mean car-crowding level. The public hourly boarding series supplies a median boarding count. The selected observation date is excluded:

```text
crowd_baseline(s,h,d) = mean { crowd(s,h,d') : d' != d }
board_baseline(s,h,d) = median { board(s,h,d') : d' != d }
deviation_pp = observed_crowd - crowd_baseline
```

The code displays sample counts. A recorded interval between supplied train observations is **not** the complete timetable. / 코드에는 표본 수를 함께 표시합니다. 제공된 관측 열차 사이의 간격을 전체 배차표로 해석하지 않습니다.

## 2. Chronological forecasting / 시계열 예측

**Implemented.** Two XGBoost regressors were compared with “carry forward the current car value.” Training dates: June 17–22, tuning June 23–24, holdout June 25–28, 2026. The final holdout was not used to fit or choose tree count. This is a date-split backtest, not external prospective validation.

Features for the next-station model: current car value, mean of valid cars, adjacent-car mean, car index, origin and next-station codes, hour/minute/weekday, and boarding/alighting aggregates from the **completed previous hour**. Passenger type is a fare class; it is not a person's inferred age or sex.

```text
MAE = mean(abs(y_hat - y))                 [percentage points]
RMSE = sqrt(mean((y_hat - y)^2))           [percentage points]
persistence_next = current car value
```

| Task / 과제 | Holdout N | XGBoost MAE | Persistence MAE | Interpretation / 해석 |
|---|---:|---:|---:|---|
| Next station / 다음 역 | 39,763 | 2.40 pp | 2.72 pp | Improvement within this June holdout |
| Next 10 minutes / 다음 10분 | 21,020 | 9.96 pp | 9.66 pp | Baseline wins on MAE; not a production claim |

The next-station model's 90th-percentile absolute error was 5.36 pp. A prototype recommendation requires a predicted source-target spread of at least **10.72 pp = 2 × 5.36 pp**. This is a conservative engineering threshold, not a calibrated guarantee.

**한국어:** 다음 역 모델은 보류 구간에서 기준선보다 MAE가 낮았지만, 다음 10분 모델은 더 높았습니다. 더 복잡한 모델이라는 이유만으로 운영에 투입하지 않습니다.

## 3. Current mission ranking / 현재 미션 순위화

**Implemented heuristic, not a solved global OR program.**

1. Reject a frame with fewer than three valid current-and-predicted cars.
2. Identify high-crowding origins at or above the valid-car 75th percentile.
3. For each candidate target, estimate walking time as `ceil(0.35 × car-index gap)` minutes.
4. Reject targets above the walk-time limit or with predicted source-target gap below 10.72 pp.
5. Choose the **lowest predicted target**, breaking ties by shorter walk. Present a voluntary mission.

**한국어:** 유효 객차가 3칸 미만이면 제안하지 않습니다. 상위 25% 혼잡 구역에서 출발하고, 예측 격차와 이동시간 조건을 통과한 후보 중 예측 혼잡도가 가장 낮은 칸을 선택합니다. 승객에게 강제하지 않습니다.

**Important proxy:** A car's on-board crowding value is used as a boarding-door-zone signal. Actual platform queue length has not been measured. Accessibility, arrival time, and car capacity must become hard field constraints before operational use.

## 4. OR formulation for a later pilot / 향후 운영연구 정식화

This is a **proposed** constrained assignment, not code already validated in the prototype:

```text
minimize  a * max_j(q_j)
        + b * sum_j((q_j/N)^2)
        + c * sum_i(walk_i)
        - d * sum_i(p_accept_i * expected_gain_i)
```

Subject to: `walk_i <= personal_limit_i`, accessible route available, arrival before train, target capacity, safety stop state, and voluntary choice. A no-offer option is always allowed. `q_j` counts **all** riders, not only app users. The weights and individual acceptance probabilities require field logs and calibration.

## 5. Cohort and Monte Carlo / 코호트와 몬테카를로

The operator screen's 400-person agent model allocates synthetic waiting people across ten door zones in proportion to the observed car-crowding vector. It uses assumed acceptance 35% and completion 80%; a deterministic ID hash makes replay stable. These are **synthetic sensors**.

The separate Monte Carlo analysis samples 464 historical peak vectors (complete ten-car visits with mean crowding at least 80%), normalizes each to a 400-person **assumed** platform queue, and runs 3,000 draws per app-reach scenario. Other assumptions: eligibility 60%, acceptance 35%, completion 80%, maximum move two cars. Moves flow from above-average queues to the least occupied nearby eligible queue if a gap of at least two people remains.

```text
expected eligible completions ≈ N * reach * eligible * accept * complete
D_max = (max(q_before) - max(q_after)) / max(q_before)
HHI(q) = sum_j((q_j / N)^2)
```

The simulation output's percentile spread describes variability **within this model**, not a confidence interval for a field effect. / 백분위 범위는 모형 내 변동성이지 실제 현장 개선 효과의 신뢰구간이 아닙니다.

## 6. Off-peak energy / 비첨두 에너지

The full prototype's entrance map uses **four synthetic entrances**. Its illustrative power rule assumes three 6 kW escalators and only permits one 6 kW standby scenario if the modeled count at entrance 3 falls to zero. It is not aligned to actual plant drawings or a power meter. Merely redirecting passengers does not prove savings.

```text
potential_kWh = (P_run - P_idle) * verified_standby_hours * availability
potential_KRW = potential_kWh * electricity_tariff
```

A real control proposal requires an alternate accessible route, evacuation review, operator authorization, equipment state, and metered energy. Station HVAC is a separate BMS integration problem.

## 7. Engineering economics / 경제성공학

For an explicitly **assumed** one-station pilot: ten eligible trains per day, 30 days, 15% app reach. The model yields about 1,570 completed moves/month. Assume KRW 200 marginal reward cost per completion, KRW 2 million monthly operations, and KRW 20 million integration capital amortized over 36 months. Monthly modeled cost is about KRW 2.87 million; break-even public value is about **KRW 1,828 per completed move**, before energy. None of these monetary values is a vendor quote or measured social benefit.

```text
monthly_cost = fixed_ops + completions * reward_unit_cost + capex / 36
break_even_value_per_completion = monthly_cost / completions
NPV = -initial_capex + sum_t((benefit_t - cost_t) / (1+r)^t)
```

For a partner, incremental value depends on **new visits**, not coupon redemptions alone:

```text
partner_net = redemptions * (incremental_visit_share * contribution_per_visit
                            - partner_coupon_burden)
```

## 8. What the public code demonstrates / 공개 코드의 범위

`src/synthetic_policy.py` implements a data-free miniature of quality checks, constrained ranking, and queue metrics. It uses a conspicuously synthetic vector, has no historical data, does not train XGBoost, and cannot reproduce the private backtest. / 공개 코드는 원천 데이터 없이 의사결정 절차를 설명하는 최소 예시입니다.
