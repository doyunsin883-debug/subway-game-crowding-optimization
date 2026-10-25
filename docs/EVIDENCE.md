# Evidence, limitations, and field validation / 근거·한계·실증 계획

## Evidence ladder / 증거 단계

| Claim type | Available now | What it supports / 무엇을 의미하나 |
|---|---|---|
| Historical observation / 과거 관측 | June 2026 4th-line car crowding and public station boarding counts | Descriptive patterns within the observed period |
| Chronological backtest / 날짜 분리 검증 | Two prediction tasks, simple persistence comparison | Predictive error on held-out June dates, not a deployed forecast SLA |
| Mechanistic counterfactual / 기계적 반사실 | 3,000 Monte Carlo draws per assumed app reach | Sensitivity to assumptions, not causal impact |
| Interaction prototype / 시연 | Citizen and operator views, shared simulated state | UX and information-flow feasibility |
| Field causal estimate / 현장 인과효과 | **Not available** | Requires operator-approved trial and real sensors |

## Observed sample / 관측 자료

- Competition-provided June CSVs: 69 files, 390,865 rows, 29 stations.
- 13,526 reconstructed train visits; 9,909 complete ten-car nonnegative visits.
- 464 complete visits met the scenario's “mean car crowding ≥ 80%” peak-frame selection.
- Public Seoul Metro station-hour board/alight counts served as aggregate contextual features. Fare class is **not** true individual age, sex, or location.
- The station 2D/3D sample provides geometry, **not** a live sensor-aligned pedestrian map.

Raw observations, exact source rows, detailed derived replays, and station models are not in this public repository. / 원본 관측·상세 파생 재생 파일·역사 모델은 이 공개 저장소에 없습니다.

## Backtest / 예측 평가

| Model | Holdout | MAE | Persistence MAE | RMSE | Persistence RMSE |
|---|---:|---:|---:|---:|---:|
| Next station / 다음 역 | 39,763 car targets | 2.40 pp | 2.72 pp | 3.63 pp | 4.28 pp |
| Next 10 minutes / 다음 10분 | 21,020 car targets | 9.96 pp | 9.66 pp | 16.48 pp | 19.40 pp |

**Interpretation / 해석:** The next-station model improved on a very simple baseline in this holdout; the 10-minute model did not improve MAE. There has been no independently audited leakage review, new-season test, drift study, or real-time deployment evaluation.

## Scenario result / 조건부 시나리오 결과

The following uses the original private-data analysis but publishes only **rounded aggregate outputs**. It is a model scenario, not proof of real platform improvement.

| Assumed app reach | Mean completed moves per 400-person train | Mean maximum-queue reduction | Mean HHI reduction |
|---:|---:|---:|---:|
| 5% | 1.8 | 0.8% | 0.3% |
| 15% | 5.2 | 2.3% | 0.8% |
| 30% | 10.1 | 4.7% | 1.5% |

**Assumptions:** 400 waiting passengers/train; on-board car crowding normalized into door-zone queue shares; 60% mission-eligible; 35% acceptance; 80% completion; two-car walk maximum; 3,000 draws each. Sensor data for platform queues, real app take-up, car capacities, and actual walking safety is absent.

**주의:** 객차 안 혼잡률을 승강장 대기열의 대리변수로 사용했습니다. 모형이 나타내는 2.3%는 “실제 서울역 혼잡 개선율”이 아닙니다. 각 가정의 현장 추정 전에는 정책 효과를 주장할 수 없습니다.

## Threats to validity / 타당성 위협

1. **Proxy mismatch:** Occupied cars and queues at doors are related but not identical.
2. **Selection:** App users differ from non-users; volunteers may already walk differently.
3. **Interference:** Moving one rider changes the options and queue of others.
4. **Temporal transfer:** June days do not establish seasonal, event, or incident performance.
5. **Measurement:** Prototype arrival is a tap, not verified geolocation or boarding.
6. **Safety:** A lightly loaded car may be unsuitable if a door, lift, or platform is obstructed.
7. **Energy:** No meter, equipment duty cycle, or HVAC telemetry was available.
8. **Incentives:** Coupon redemption does not automatically create incremental commercial benefit.

## Field trial blueprint / 현장 실증 설계

**Phase 0 — contract and instrumentation / 계약·계측.** Obtain permitted data and spatial asset terms; integrate platform counts, train arrivals, equipment state and energy meters; approve accessible/evacuation routes; establish privacy retention and an emergency stop.

**Phase 1 — shadow mode / 그림자 운영.** For about four weeks, generate but do not display missions. Compare recommendations with operator judgment and measure false/unsafe suggestions.

**Phase 2 — limited randomized trial / 제한적 무작위 실험.** Randomize comparable train-time clusters to mission or no-mission; log all riders at the zone level, both app users and non-users. Define the intention-to-treat effect:

```text
ITT = mean(platform_outcome | mission offered cluster)
    - mean(platform_outcome | control cluster)
```

Primary outcome: maximum door-zone queue or validated density. Guardrails: no worsening of a high-risk zone, no accessibility loss, no increase in delays, complaints, or safety events. Secondary: completion, travel burden, reward cost, metered kWh when applicable. Report effect size **with uncertainty**, not just a percentage.

**Phase 3 — cost-benefit and expansion / 경제성·확대.** Recalculate marginal benefit using measured delays, incidents, energy, and partner incremental visits. Expand only when safety and pre-registered performance criteria are met.

## Prior art / 선행 사례

Car crowd information and incentives already exist. The portfolio's contribution is the combined **decision → voluntary action → operator observation → policy learning** workflow and its explicit evidence boundary, not a claim of worldwide first invention.

- [Seoul city subway app information](https://english.seoul.go.kr/service/movement/public-transportation/)
- [Île-de-France Mobilités real-time occupancy](https://www.iledefrance-mobilites.fr/en/actualites/affluence-temps-reel-trains)
- [Singapore LTA travel planning / incentives](https://www.lta.gov.sg/content/ltagov/en/getting_around/public_transport/plan_your_journey.html)
- [TU Delft/KTH simulation of car-specific information](https://repository.tudelft.nl/record/uuid:1e47d9f5-d4b9-48ce-ad14-50efe8300e0a)
- [Gamification field study showing engagement need not imply more transit trips](https://www.sciencedirect.com/science/article/pii/S1369847817304527)
