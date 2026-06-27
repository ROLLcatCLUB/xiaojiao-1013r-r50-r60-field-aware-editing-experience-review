from __future__ import annotations

from field_aware_editing_experience_1013R_R50_R60_common import validate_stage


if __name__ == "__main__":
    payload, code = validate_stage("R53")
    print(f"{payload['stage']}: {payload['status']}")
    raise SystemExit(code)
