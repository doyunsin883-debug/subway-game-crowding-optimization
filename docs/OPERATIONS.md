# Operating model / 실제 운영 체계

This is a **proposed pilot runbook**, not an assertion that Seoul Metro has adopted the service. / 아래 내용은 **현장 도입 제안**이며 서울교통공사의 실제 운영 절차가 아닙니다.

## Daily rider loop / 시민의 하루

1. Show weather and an explicitly labeled train notice.
2. Offer at most one time-sensitive, feasible movement mission. A rider can decline with no penalty.
3. At peaks, offer a nearby lower-crowding car zone. Off peak, offer an alternative entrance only after accessible route screening.
4. Log offer → accept → moving → completion or decline. The prototype uses self-report; field use needs consented verification.
5. Update the published reward rule and explain how many successful tasks remain.

**한국어:** 시민에게는 관제용 수치 대신 지금 필요한 행동과 보상 진도만 제공합니다. 혼잡 시간의 객차 이동과 평상시의 출입구 이동은 서로 다른 화면·정책으로 처리합니다.

## Ten safety quiz questions per day / 하루 10문항 안전 퀴즈

Proposed editorial mix: **4 emergency-response**, **3 platform/train safety**, **2 rail-use rules and current legal guidance**, **1 station facility/wayfinding** question. “Subway law” questions must cite the exact current official provision or operator rule; a model-generated answer is never the sole source of legal interpretation.

제안 출제 비율: **위기 대응 4**, **승강장·열차 안전 3**, **지하철 이용 규칙·관련 법령 2**, **역 시설·동선 1**. 법률·규정 문항은 시행일과 공식 근거를 저장하고 담당자 검수를 거친 뒤 게시합니다.

| Stage | Owner | Record / 관리 기록 |
|---|---|---|
| Draft and tag | Content editor | Topic, difficulty, answer, one-sentence feedback, official source |
| Safety review | Operator safety lead | Unsafe advice check, accessibility and incident consistency |
| Legal/rule review | Legal or rules owner | Version, effective date, official citation, expiry trigger |
| Publish | Content operator | 10-question daily set, duplicate and difficulty balance |
| Monitor | Data analyst | Completion, wrong-answer rate, dropout, repeat patterns |
| Withdraw | Safety/legal lead | Immediate removal when incident guidance or regulation changes |

Review cadence: daily set generation, weekly review of common wrong answers, monthly safety/legal audit, immediate withdrawal after a relevant policy change. Rewards should favor learning and completion, not quick guessing. Abuse controls should detect repeated automated attempts without collecting unnecessary identity data.

## 14-day demand-shift mission / 2주 수요 분산 미션

The full prototype simulates a **5,000-account**, **1,000-daily-active** cohort for 14 days. The assumed time-flexible share is 30%, acceptance 35%, completion 80%. These are scenario inputs, not measured rider segments. A real system should ask riders for preferences and permitted routes, then learn acceptance from opt-in logs.

전체 프로토타입은 **총 5,000명·일일 활성 1,000명·14일** 가정으로 반응을 시뮬레이션합니다. 시간 조정 가능 30%, 수락 35%, 완료 80%는 실측치가 아닙니다. 실제로는 사용자가 제공한 통행 선호와 수락 로그로 보정해야 합니다.

Eligibility rules should consider added travel time, alternate station accessibility, work/school constraints, weather, service disruptions, and reward value. No mission should use presumed gender or exact age derived from aggregate fare-class data.

## Reward and partner settlement / 보상·제휴 정산

- Display the published success threshold before a user accepts; the concept uses a **70% combined mission success threshold** and progress toward a **20-mission reward**.
- Separate virtual progress from issued coupons. Real coffee/meal vouchers require a signed partner agreement, issue/redemption identifiers, refund/fraud rules, tax treatment, and customer support.
- Compare incremental partner visits with coupon burden. Redemptions alone do not prove partner profit.
- Avoid concentrating all rewards on commuters who have the most time flexibility; monitor equity and accessibility.

**한국어:** 시연의 커피 쿠폰 표시는 실제 발행된 제휴 쿠폰이 아닙니다. 운영 시에는 제휴 계약·정산·부정사용 처리·고객 대응 절차를 갖춰야 합니다.

## Operator rhythm and stop rules / 관제 주기와 중단 기준

**Before service:** quality and timestamp checks; sensor heartbeat; station access/evacuation map; approved crowd thresholds; human duty officer.

**During peak:** compare observed zone counts with same-station/time history; suppress low-confidence or unsafe missions; monitor offered/accepted/moving/completed/declined and non-user queues; stop if any high-risk zone worsens.

**During off peak:** monitor entrance counts and equipment state. Any standby proposal needs an alternate accessible route, safety review, actual equipment command authorization, and an energy meter. Mission completion never directly triggers escalator control.

**After service:** reconcile logs, survey perceived burden, retrain/retune only after drift review, publish cost and outcome dashboards with uncertainty.

**Stop conditions:** emergency, congestion spillover, blocked accessible route, missed boarding window, sensor outage, equipment fault, material rise in delay/complaints, or operator override.

## RACI-style responsibilities / 담당 주체

| Workstream | Accountable / 책임 | Consulted / 협의 |
|---|---|---|
| Safety and stop policy | Station operator / safety office | Accessibility and incident teams |
| Data quality and prediction | Data science lead | Transport planning |
| Mission policy | Operations research lead | Station operator, UX lead |
| Quiz content | Content lead | Safety and legal owner |
| Reward settlement | Partnership lead | Finance, customer support |
| Privacy and retention | Privacy officer | Security, legal |
| Field impact evaluation | Independent evaluation lead | Operations, data science |

## Rollout gates / 단계별 도입

1. **Data contract and rights check:** sensors, timetables, geometry rights, privacy basis, station safety.
2. **Four-week shadow mode:** recommendations are computed but not shown; review unsafe/false suggestions.
3. **Four-week limited trial:** cluster-randomized offer/control periods, with all-rider outcomes and stop rules.
4. **Decision gate:** expand only if safety and pre-registered congestion/cost metrics pass.
5. **Multi-station operations:** service-level monitoring, drift checks, periodic quiz/legal audit, partner reconciliation.
