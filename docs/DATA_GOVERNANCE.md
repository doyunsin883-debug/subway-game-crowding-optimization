# Data provenance and publication boundary / 데이터 출처와 공개 범위

## Why this repository is a separate public edition

The competition provides subway crowding and station 2D/3D sample assets for service discovery. The participation pledge asks entrants to confirm rights for each source used in a prototype. We found no explicit blanket permission to redistribute the sample ZIP, its GLB/SHP models, or record-level derivatives on GitHub. Thus this repository **does not contain them**. The private full prototype and deployed contest demonstration are separate artifacts.

공모전 자료를 서비스 기획에 활용하는 것과 원본 파일을 제3자에게 재배포하는 것은 다릅니다. 샘플 ZIP·GLB/SHP·행 단위 재생값의 공개 배포 권한이 명확하지 않아 이 저장소에서 제외했습니다. 이를 “공모전에서 공개된 파일이므로 자유 라이선스”라고 해석하지 않았습니다.

## Inventory / 데이터 목록

| Material | Origin | Public repo decision |
|---|---|---|
| 4th-line June car crowd CSVs | Competition sample supplied to entrants | **Excluded**: all raw rows and reconstructed visit/replay JSON |
| Dongmyo station GLB and SHP | Competition spatial sample | **Excluded**: models, textures, coordinates, thumbnails derived from the model |
| Safety-facility sample | Competition sample | **Excluded**: source tables/geocoordinates |
| Seoul Metro station-hour boarding CSV | [data.go.kr dataset](https://www.data.go.kr/data/15099330/fileData.do), listed “no restrictions” | Source link and methodological description only; no CSV mirror |
| Analysis output | Produced during project | Rounded, aggregate metrics only; no row-level reconstruction |
| Citizen/admin design & formulas | Original project work | Described as prose, Mermaid diagrams, and synthetic code |
| Synthetic demo | Newly generated for this repository | Included; visibly labeled synthetic |
| Application/pledge, personal details, keys | Contest/admin material | **Excluded** |

## Public interface caveat / 공개 시연 주의

The earlier contest prototype was deployed separately. A public website can expose downloadable assets even without GitHub. Continued external distribution of the supplied station GLB or detailed replay should be resolved with the organizer/rightsholder. This portfolio repo does **not** link to or embed those asset URLs.

기존 별도 배포 웹에서도 GLB나 상세 재생 파일이 정적 자산으로 전달될 수 있습니다. GitHub 공개판을 분리했다고 기존 웹 자산의 권리 문제가 자동으로 해결되지는 않습니다. 원권리자에게 웹 시연 범위까지 확인하는 것이 필요합니다.

## Submission integrity / 공모전 성실성

- The project is identified as a competition submission; no claim of Seoul Metro/KALDA endorsement.
- Pre-existing crowd information, rewards, and mobility-nudge examples are cited; “world first” is not claimed.
- Synthetic scenario outputs are not described as actual field effect.
- The team's own source/design contribution is documented without reproducing restricted input assets.
- The official participation pledge, application, personal contact, and signature are not published.

Official contest notice: [data.go.kr](https://www.data.go.kr/bbs/ntc/selectNotice.do?originId=NOTICE_0000000005068). Dataset terms for any future addition should be checked **per dataset**, not inferred from the portal's general name.
