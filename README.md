# SUBWAY GAME — Crowding Optimization for Urban Rail

**Industrial engineering · operations research · data analysis · human-centered operations**

[한국어 README](README.ko.md) · [Synthetic interactive demo](https://doyunsin883-debug.github.io/subway-game-crowding-optimization/) · [Methods](docs/METHODS.md) · [Architecture](docs/ARCHITECTURE.md) · [Evidence & limits](docs/EVIDENCE.md)

> A portfolio-safe research and demonstration repository for a submission to the **2026 Seoul Metro / KALDA “Subway Crowding and Safety Facility Data Utilization Service Discovery Competition.”** The interactive demo contains only synthetic values and original schematic graphics. Competition-provided raw data, station GLB/SHP assets, detailed replay files, credentials, and participant documents are intentionally absent.

## One-minute overview

Crowding information alone does not redistribute passengers. SUBWAY GAME asks a narrower operations question: **which voluntary, feasible move should be suggested to which passenger, and how will operators know whether it helped?** The full prototype separates a simple citizen interface from an operations console. At peaks, it suggests a nearby less crowded boarding-door zone. Off peak, it can propose a safe alternative entrance. A longer 14-day mission tests flexible departure/entry choices. Quiz and reward loops support participation.

The operational loop is:

```text
historical observations → quality gate → baseline / forecast
→ feasible mission candidates → citizen accepts / declines / completes
→ aggregated operations metrics → policy comparison → revise policy
```

The system is a **simulation prototype**, not a live Seoul Metro feed or measured field intervention. The full deployed prototype uses competition-provided spatial assets; this public repository deliberately does not mirror those assets or its detailed replay data. The linked demo is a separate synthetic reconstruction.

## What I built and what remains proposed

| Component | Implemented in the full prototype | Evidence boundary |
|---|---|---|
| Citizen experience | Mobile-first missions, progress, quiz, weather, train notice, Korean/English/Japanese | Mission arrival is self-reported in the prototype |
| Operations console | Station/date replay, 10-car crowding, policy controls, synthetic cohort response, 3D station view | Historical replay and synthetic sensors are labeled separately |
| Data engineering | Quality counts, 10-car visit reconstruction, public boarding aggregation | Source observations are not distributed here |
| Prediction | XGBoost next-station and next-10-minute models with chronological holdout | The next-10-minute model did **not** beat the persistence MAE baseline |
| Mission allocation | High-crowding source, predicted spread threshold, nearest feasible target ranking | Learned individual acceptance and global optimization are **proposed**, not validated |
| Policy evaluation | Deterministic cohort simulation and Monte Carlo counterfactual | Not a causal field estimate |
| Energy | Entrance-demand and escalator standby scenario | No power meter or verified savings |

## Research questions

1. **Data analysis:** How do we build an honest station × hour × car baseline with missing or invalid observations?
2. **OR:** How can we balance maximum queue, concentration, walking burden, capacity, accessibility, and voluntary acceptance?
3. **Experiment design:** Does issuing a mission improve whole-platform outcomes once non-users and spillovers are counted?
4. **Engineering economics:** Under what adoption, coupon, integration, and energy assumptions could a pilot be worth operating?

## Key results, correctly scoped

- The supplied June 2026 data was screened at **390,865 rows across 69 CSV files**. After reconstruction, **9,909 complete 10-car visits** were available. These are observational records, not platform queue sensors.
- A chronological holdout (train: June 17–24; holdout: June 25–28) gave next-station crowding **MAE 2.40 percentage points** versus **2.72** for persistence. Next-10-minute crowding gave **9.96** versus **9.66**; the simple baseline was better on that MAE.
- In a mechanistic Monte Carlo scenario (3,000 draws per coverage setting; 400 **assumed** waiting people per train), mean reduction in the maximum simulated door-zone queue was approximately **0.8%, 2.3%, and 4.7%** at 5%, 15%, and 30% app reach. These are **model outputs**, not real-world impact estimates. See [evidence and limitations](docs/EVIDENCE.md).

## Explore the repository

- [Architecture and system mind map](docs/ARCHITECTURE.md) — separate citizen and operator views, information flow, source labels.
- [Mathematical methods and implementation details](docs/METHODS.md) — baselines, model validation, mission ranking, simulation, energy, and economics.
- [Evidence, limitations, and field trial](docs/EVIDENCE.md) — what was observed, assumed, validated, and still unknown.
- [Operating model and daily quiz plan](docs/OPERATIONS.md) — 10-question safety program, 14-day missions, rewards, staffing, and stop rules.
- [Data and copyright boundaries](docs/DATA_GOVERNANCE.md) — why original competition assets are excluded.
- [Synthetic demo guide](docs/DEMO.md) — how to inspect the interactive example.
- [Runnable synthetic policy example](src/synthetic_policy.py) — self-contained Python standard-library reconstruction, not the private data pipeline.

## Reproduce the public example

```bash
python src/synthetic_policy.py
```

No package installation or data download is required. The script prints a synthetic 10-car mission decision, queue metrics, and the assumptions it used. Open `site/index.html` locally or use the linked GitHub Pages demo for the citizen/operator interaction. **Its values are generated for demonstration and must not be compared with the private observation-based results above.**

## Attribution and rights

Competition organizer: Seoul Metro; host: Korea Land & Transport Data Association (KALDA). The underlying competition data and station models remain with their respective rightsholders. This repository does not grant a license to copy them. A separate public boarding dataset used during the project is listed by [data.go.kr](https://www.data.go.kr/data/15099330/fileData.do) with “no restrictions” on use; the original CSV is not mirrored here. The repo contains original prose, diagrams, and a synthetic demo. No association or endorsement by the organizers is implied.

## Contact / portfolio discussion

For a technical interview, start with the [architecture](docs/ARCHITECTURE.md), then the [methods](docs/METHODS.md) and [evidence](docs/EVIDENCE.md). I can explain the decisions, error analysis, and pilot design without distributing restricted source assets.
