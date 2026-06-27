# 1013R_R51_FIELD_PATCH_TO_EXISTING_EDIT_CARD_SMOKE

状态：`PASS`

## Checks

- `legal_patches_route_to_existing_edit_card`: True
- `missing_canonical_patch_rejected`: True
- `mismatch_patch_rejected`: True
- `standalone_blue_card_rejected`: True
- `work_object_patch_applied_false`: True

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
