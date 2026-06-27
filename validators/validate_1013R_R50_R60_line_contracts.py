from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HTML = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R21_page_copy_binds_unified_package" / "prep_room_page_copy_binds_unified_package_1013R_R21.html"
OUT = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R50_R60_field_aware_editing_experience" / "artifacts" / "prep_room_line_contracts_1013R_R50_R60.json"


def main() -> int:
    html = HTML.read_text(encoding="utf-8")
    checks = {
        "line_contract_function_exists": "function lineContractsFor" in html,
        "line_contract_renderer_exists": "function renderLineContracts" in html,
        "line_contract_dom_marker_exists": 'data-r50-line-contracts="true"' in html,
        "line_contract_row_marker_exists": 'data-r50-line-contract="true"' in html,
        "line_has_canonical_field_key": "data-canonical-field-key" in html,
        "line_has_target_field_key": "data-target-field-key" in html,
        "line_has_applied_false": 'data-applied="false"' in html,
        "line_has_formal_apply_false": 'data-formal-apply-allowed="false"' in html,
        "modal_exposes_line_count": "data-r50-line-contract-count" in html,
        "preview_state_keeps_line_contracts": "line_contracts:" in html,
        "old_big_blob_grid_removed_from_main_card": "r50-modal-grid" not in re.sub(r"<style.*?</style>", "", html, flags=re.S),
    }
    payload = {
        "stage": "1013R_R50_R60_LINE_CONTRACTS_WITHIN_FIELD_EDIT_CARD",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "r21_html": str(HTML.relative_to(ROOT)),
        "boundary": {
            "same_r21_page": True,
            "new_static_page_created": False,
            "provider_called": False,
            "model_called": False,
            "formal_apply_performed": False,
        },
    }
    OUT.parent.mkdir(parents=True, exist_ok=True)
    OUT.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")
    print(json.dumps(payload, ensure_ascii=False, indent=2))
    return 0 if payload["status"] == "PASS" else 1


if __name__ == "__main__":
    raise SystemExit(main())
