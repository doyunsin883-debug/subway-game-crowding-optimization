# Synthetic interactive demonstration / 합성 시연 안내

[Open the GitHub Pages demo](https://doyunsin883-debug.github.io/subway-game-crowding-optimization/) or open [`site/index.html`](../site/index.html) locally. No installation, account, external API, source dataset, or station model is needed.

## Walkthrough / 시연 순서

1. Choose **Peak / 혼잡**. A synthetic 10-car profile appears. The recommended car is selected with a transparent score based on predicted crowd difference and walking distance.
2. On the **Citizen / 시민** panel, accept and complete the mission. The progress and reward counter change. Switch to **Operator / 관리자** to see modeled completed moves and queue metrics.
3. Switch to **Off-peak / 평상**. The screen shows entrance numbers rather than a 3D model. The energy tile is explicitly “potential, not metered”; no device is controlled.
4. Change the assumed app reach or acceptance slider to see the effect of participation. Operators should compare **all 400 synthetic passengers**, not only those shown a mission.
5. Read the methodology and limitation labels before interpreting any number.

**한국어:** 이 페이지는 취업 포트폴리오용 축약 시연입니다. 원래 대회 시연의 실제 관측 재생, Netlify Functions, GLB 3D, 공모전 데이터는 싣지 않았습니다. 합성 데이터의 수치가 바뀌는 것은 실제 지하철 인원의 이동이 아닙니다.

## Demonstrated transitions / 보여주는 상태 전이

```text
IDLE → OFFERED → ACCEPTED → MOVING → COMPLETED
                       ↘ DECLINED
```

The full prototype also supports date selection, historical replay, multilingual UI, weather, quiz, 14-day missions, and a shared API. The public static demo focuses on the decision loop and evidence boundary; it does not pretend to reproduce every production feature.

## Safe interpretation / 해석 범위

- Car crowd percentages, passenger queues, reward completions, entrance split, and electricity are **fabricated inputs or scenario assumptions**.
- No location tracking, ticketing integration, actual arrival confirmation, or station equipment control occurs.
- The demo cannot validate the observation-based ML scores. See [evidence](EVIDENCE.md) for those separate results.
