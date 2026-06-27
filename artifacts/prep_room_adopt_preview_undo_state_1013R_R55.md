# 1013R_R55_ADOPT_PREVIEW_AND_UNDO_STATE

状态：`PASS`

## Checks

- `preview_state_exists`: True
- `adopt_preview_exists`: True
- `undo_preview_exists`: True
- `applied_false`: True
- `formal_apply_false`: True

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
