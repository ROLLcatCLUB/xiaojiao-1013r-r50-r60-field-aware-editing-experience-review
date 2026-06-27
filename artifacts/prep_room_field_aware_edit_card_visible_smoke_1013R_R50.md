# 1013R_R50_FIELD_AWARE_EDIT_CARD_VISIBLE_SMOKE

状态：`PASS`

## Checks

- `twelve_field_entries_visible`: True
- `edit_card_identity_visible`: True
- `aliases_visible`: True
- `material_requests_gate_visible`: True

## Summary

- page_edit_item_count: 12
- canonical_field_count: 12
- alias_count: 6
- material_requests_present: True
- orphan_ui: 0
- standalone_blue_card_allowed: False

## Boundary

- `do_not_rollback_r21=True`
- `do_not_create_new_page=True`
- `do_not_modify_r36=True`
- `provider_model_call_allowed=False`
- `runtime_integration_allowed=False`
- `database_write_allowed=False`
- `feishu_write_allowed=False`
- `memory_write_allowed=False`
- `formal_apply_allowed=False`
- `standalone_blue_card_allowed=False`
- `preview_only=True`
