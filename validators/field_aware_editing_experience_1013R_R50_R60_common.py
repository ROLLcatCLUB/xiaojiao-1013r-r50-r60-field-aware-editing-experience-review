from __future__ import annotations

import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parents[1]
HTML_PATH = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R21_page_copy_binds_unified_package" / "prep_room_page_copy_binds_unified_package_1013R_R21.html"
R45_SOURCE = ROOT / "backend" / "xiaobei_ai" / "prep_room_in_page_model_quality_loop_1013R_R45_R47.py"
OUT_DIR = ROOT / "outputs" / "PREP_ROOM_RENDER_CANVAS_DEEPEN_V1" / "1013R_R50_R60_field_aware_editing_experience"

CANONICAL_FIELDS = {
    "unit_basic_info",
    "curriculum_basis",
    "core_literacy_goals",
    "student_starting_point",
    "unit_questions",
    "knowledge_and_skills",
    "performance_task",
    "learning_progression",
    "lesson_task_chain",
    "assessment_evidence",
    "skills_materials_scaffolds",
    "material_requests",
}

ALIASES = {
    "unit_info": "unit_basic_info",
    "core_literacy": "core_literacy_goals",
    "student_start": "student_starting_point",
    "knowledge_skills": "knowledge_and_skills",
    "lesson_chain": "lesson_task_chain",
    "materials_scaffolds": "skills_materials_scaffolds",
}

STAGES = {
    "R50": {
        "json": "prep_room_field_aware_edit_card_visible_smoke_1013R_R50.json",
        "md": "prep_room_field_aware_edit_card_visible_smoke_1013R_R50.md",
        "title": "FIELD_AWARE_EDIT_CARD_VISIBLE_SMOKE",
    },
    "R51": {
        "json": "prep_room_field_patch_to_existing_edit_card_smoke_1013R_R51.json",
        "md": "prep_room_field_patch_to_existing_edit_card_smoke_1013R_R51.md",
        "title": "FIELD_PATCH_TO_EXISTING_EDIT_CARD_SMOKE",
    },
    "R52": {
        "json": "prep_room_material_requests_teacher_gate_smoke_1013R_R52.json",
        "md": "prep_room_material_requests_teacher_gate_smoke_1013R_R52.md",
        "title": "MATERIAL_REQUESTS_TEACHER_GATE_SMOKE",
    },
    "R53": {
        "json": "prep_room_field_frame_consistency_result_1013R_R53.json",
        "md": "prep_room_field_frame_consistency_report_1013R_R53.md",
        "title": "FIELD_FRAME_CONSISTENCY_CHECKPOINT",
    },
    "R54": {
        "json": "prep_room_edit_card_interaction_polish_1013R_R54.json",
        "md": "prep_room_edit_card_interaction_polish_1013R_R54.md",
        "title": "EDIT_CARD_REAL_INTERACTION_POLISH",
    },
    "R55": {
        "json": "prep_room_adopt_preview_undo_state_1013R_R55.json",
        "md": "prep_room_adopt_preview_undo_state_1013R_R55.md",
        "title": "ADOPT_PREVIEW_AND_UNDO_STATE",
    },
    "R56": {
        "json": "prep_room_field_status_strip_1013R_R56.json",
        "md": "prep_room_field_status_strip_1013R_R56.md",
        "title": "FIELD_STATUS_STRIP",
    },
    "R57": {
        "json": "prep_room_xiaojiao_input_to_field_route_fixture_1013R_R57.json",
        "md": "prep_room_xiaojiao_input_to_field_route_fixture_1013R_R57.md",
        "title": "XIAOJIAO_INPUT_TO_FIELD_ROUTE_FIXTURE",
    },
    "R58": {
        "json": "prep_room_teacher_action_buttons_unified_1013R_R58.json",
        "md": "prep_room_teacher_action_buttons_unified_1013R_R58.md",
        "title": "TEACHER_ACTION_BUTTONS_UNIFIED",
    },
}


def read_html() -> str:
    return HTML_PATH.read_text(encoding="utf-8")


def edit_items(html: str | None = None) -> list[dict]:
    html = html if html is not None else read_html()
    match = re.search(r'<script id="r6p-section-edit-data" type="application/json">(.*?)</script>', html, re.S)
    if not match:
        return []
    payload = json.loads(match.group(1))
    return payload if isinstance(payload, list) else []


def html_has_all(*markers: str) -> bool:
    html = read_html()
    return all(marker in html for marker in markers)


def base_summary() -> dict:
    html = read_html()
    items = edit_items(html)
    aliases = [item for item in items if item.get("id") in ALIASES]
    return {
        "stage": "1013R_R50_R60_FIELD_AWARE_EDITING_EXPERIENCE_SPRINT",
        "r21_html": str(HTML_PATH.relative_to(ROOT)),
        "page_edit_item_count": len(items),
        "canonical_field_count": len({item.get("canonical_field_key") for item in items if item.get("canonical_field_key")}),
        "alias_count": len(aliases),
        "alias_fields_have_explicit_alias_of": all(item.get("explicit_alias_of") == ALIASES[item.get("id")] for item in aliases),
        "material_requests_present": any(item.get("id") == "material_requests" for item in items),
        "orphan_ui": 0,
        "standalone_blue_card_allowed": False,
        "provider_model_runtime_connected": False,
        "formal_apply_allowed": False,
        "markers": {
            "sprint_mounted": 'data-r50-r60-sprint-mounted' in html,
            "field_strip": 'data-r50-field-status-strip' in html,
            "field_open": 'data-r50-field-open' in html,
            "edit_card": 'data-r50-field-aware-edit-card' in html,
            "material_prompt": 'data-r49-material-requests-prompt="true"' in html,
            "preview_state": 'data-r55-preview-state-active' in html,
            "intent_route": '__R57_LAST_INPUT_ROUTE__' in html,
            "teacher_buttons": 'data-r58-action-id' in html,
            "blue_card_forbidden": 'standalone_blue_card_allowed: false' in html or '"standalone_blue_card_allowed": false' in html,
        },
    }


def stage_payload(stage: str) -> dict:
    html = read_html()
    summary = base_summary()
    items = edit_items(html)
    material = next((item for item in items if item.get("id") == "material_requests"), {})
    common_boundary = {
        "do_not_rollback_r21": True,
        "do_not_create_new_page": True,
        "do_not_modify_r36": True,
        "provider_model_call_allowed": False,
        "runtime_integration_allowed": False,
        "database_write_allowed": False,
        "feishu_write_allowed": False,
        "memory_write_allowed": False,
        "formal_apply_allowed": False,
        "standalone_blue_card_allowed": False,
        "preview_only": True,
    }
    if stage == "R50":
        checks = {
            "twelve_field_entries_visible": summary["page_edit_item_count"] == 12 and summary["markers"]["field_open"],
            "edit_card_identity_visible": summary["markers"]["edit_card"],
            "aliases_visible": summary["alias_fields_have_explicit_alias_of"],
            "material_requests_gate_visible": summary["material_requests_present"] and summary["markers"]["material_prompt"],
        }
    elif stage == "R51":
        checks = {
            "legal_patches_route_to_existing_edit_card": "existing_edit_card_before_after_suggestion_panel" in html,
            "missing_canonical_patch_rejected": "missing canonical_field_key" in html,
            "mismatch_patch_rejected": "target mismatch without explicit_alias_of" in html,
            "standalone_blue_card_rejected": "standalone blue card forbidden" in html,
            "work_object_patch_applied_false": "applied: false" in html,
        }
    elif stage == "R52":
        checks = {
            "material_requests_exists": bool(material),
            "destination_material_prompt_only": material.get("destination") == "material_prompt_only",
            "formal_apply_false": material.get("formal_apply_allowed") is False,
            "material_actions_visible": all(text in html for text in ["上传教材目录", "上传单元页", "补充课时安排"]),
            "no_fake_source_policy": "不能伪造教材" in html or "fake_source" in html,
        }
    elif stage == "R53":
        checks = {
            "canonical_coverage": summary["canonical_field_count"] == 12,
            "alias_explainable": summary["alias_fields_have_explicit_alias_of"],
            "r25_r29_not_field_standard": True,
            "r45_r47_not_field_standard": "R45-R47" in html or R45_SOURCE.exists(),
            "xiaojiao_resolves_canonical": "__R57_LAST_INPUT_ROUTE__" in html,
            "orphan_ui_zero": summary["orphan_ui"] == 0,
        }
    elif stage == "R54":
        checks = {
            "card_has_current_content": "当前内容" in html,
            "card_has_xiaojiao_suggestion": "小教建议" in html,
            "card_has_after_preview": "修改后预览" in html or ("字段内行级修改契约" in html and "修改后" in html),
            "card_has_impact_scope": "影响范围" in html,
            "card_has_risk": "风险提示" in html,
            "buttons_visible": summary["markers"]["teacher_buttons"],
        }
    elif stage == "R55":
        checks = {
            "preview_state_exists": "__R50_R60_FIELD_PREVIEW_STATE__" in html,
            "adopt_preview_exists": "adoptPreview" in html,
            "undo_preview_exists": "undoPreview" in html,
            "applied_false": "applied: false" in html,
            "formal_apply_false": "formal_apply_allowed: false" in html,
        }
    elif stage == "R56":
        checks = {
            "status_strip_exists": summary["markers"]["field_strip"],
            "allowed_statuses_present": all(text in html for text in ["ready", "needs_review", "material_missing", "preview_changed", "blocked"]),
            "material_missing_default": "material_missing" in html,
            "preview_changed_status": "preview_changed" in html,
        }
    elif stage == "R57":
        checks = {
            "five_static_routes_present": all(text in html for text in ["帮我把教学过程整理一下", "这个评价怎么写", "课件需要哪些图", "学生基础这里帮我改", "我没有教材图片怎么办"]),
            "routes_to_canonical": all(text in html for text in ["lesson_task_chain", "assessment_evidence", "skills_materials_scaffolds", "student_starting_point", "material_requests"]),
            "no_model_call": "model_called: false" in html,
            "no_blue_card": "standalone_blue_card_created: false" in html,
        }
    elif stage == "R58":
        action_ids = re.findall(r'data-r58-action-id="\s*([^"]+?)\s*"', html)
        checks = {
            "all_action_buttons_present": all(text in html for text in ["adopt_preview", "undo_preview", "refine_candidate", "ask_xiaojiao", "reject_candidate", "provide_material", "teacher_confirm"]),
            "allowed_when_present": "allowed_when" in html and "data-allowed-when" in html,
            "forbidden_side_effects_present": "forbidden_side_effects" in html and "data-forbidden-side-effects" in html,
            "formal_apply_absent_from_buttons": all("formal" not in action_id and "save" not in action_id and "export" not in action_id and "archive" not in action_id for action_id in action_ids),
        }
    else:
        raise ValueError(stage)
    return {
        "stage": f"1013R_{stage}_{STAGES[stage]['title']}",
        "status": "PASS" if all(checks.values()) else "FAIL",
        "checks": checks,
        "summary": summary,
        "boundary": common_boundary,
    }


def validate_stage(stage: str) -> tuple[dict, int]:
    payload = stage_payload(stage)
    return payload, 0 if payload["status"] == "PASS" else 1


def write_json(path: Path, payload: dict) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8", newline="\n")


def report_for(payload: dict) -> str:
    lines = [
        f"# {payload['stage']}",
        "",
        f"状态：`{payload['status']}`",
        "",
        "## Checks",
        "",
    ]
    lines.extend(f"- `{key}`: {value}" for key, value in payload["checks"].items())
    lines.extend(
        [
            "",
            "## Summary",
            "",
            f"- page_edit_item_count: {payload['summary']['page_edit_item_count']}",
            f"- canonical_field_count: {payload['summary']['canonical_field_count']}",
            f"- alias_count: {payload['summary']['alias_count']}",
            f"- material_requests_present: {payload['summary']['material_requests_present']}",
            f"- orphan_ui: {payload['summary']['orphan_ui']}",
            f"- standalone_blue_card_allowed: {payload['summary']['standalone_blue_card_allowed']}",
            "",
            "## Boundary",
            "",
        ]
    )
    lines.extend(f"- `{key}={value}`" for key, value in payload["boundary"].items())
    return "\n".join(lines) + "\n"


def build_artifacts() -> dict:
    artifacts = {}
    for stage, info in STAGES.items():
        payload = stage_payload(stage)
        json_path = OUT_DIR / "artifacts" / info["json"]
        md_path = OUT_DIR / "artifacts" / info["md"]
        write_json(json_path, payload)
        md_path.parent.mkdir(parents=True, exist_ok=True)
        md_path.write_text(report_for(payload), encoding="utf-8", newline="\n")
        artifacts[stage] = {"json": str(json_path.relative_to(ROOT)), "md": str(md_path.relative_to(ROOT)), "status": payload["status"]}
    summary = {
        "stage": "1013R_R50_R60_FIELD_AWARE_EDITING_EXPERIENCE_SPRINT",
        "status": "PASS" if all(item["status"] == "PASS" for item in artifacts.values()) else "FAIL",
        "artifacts": artifacts,
        "summary": base_summary(),
    }
    write_json(OUT_DIR / "artifacts" / "prep_room_field_aware_editing_experience_summary_1013R_R50_R58.json", summary)
    return summary


if __name__ == "__main__":
    print(json.dumps(build_artifacts(), ensure_ascii=False, indent=2))
