# GPT Review Prompt: 1013R R50-R60 Field-Aware Editing Experience

Please review this lightweight package as a continuation of R48/R49.

## Review Target

Review whether R50-R60 correctly attaches a field-aware editing smoke experience to the existing R21 prep-room page copy.

Do not judge this as completed model generation runtime. It is a visible smoke and field-contract package.

## Files To Inspect

- `README.md`
- `artifacts/prep_room_page_copy_binds_unified_package_1013R_R21_R50_R60.html`
- `artifacts/validate_1013R_R50_R60_line_contracts_result.json`
- `artifacts/prep_room_line_contracts_1013R_R50_R60.json`
- `validators/field_aware_editing_experience_1013R_R50_R60_common.py`
- `validators/validate_1013R_R50_R60_line_contracts.py`
- `r48_r49_refs/prep_room_recovered_field_ledger_1013R_R48.json`
- `r48_r49_refs/validate_1013R_R49_canonical_field_keys_apply_result.txt`
- `source_refs/prep_room_in_page_model_quality_loop_1013R_R45_R47.py`

## Expected Finding

Expected result:

`R50_R60 = REVIEW_READY_WITH_NOTES`

Reason:

- The same R21 page copy is still the carrier.
- Current page edit items retain canonical field identity.
- The edit card can display canonical field identity.
- Candidate content is routed to the existing edit card.
- Candidate content is split into line-level contracts.
- Preview remains preview-only.
- No model/provider/runtime/formal apply is connected.

## Must Not Pass If

Reject or request patch if any of these are true:

- A new page replaces the current R21 carrier.
- Candidate content appears only as a separate page body blue card.
- Candidate content is only one large blob in "after/advice" with no line contracts.
- Field identity is missing from the edit card.
- Candidate fixtures can enter without canonical_field_key.
- material_requests becomes formal lesson-plan content.
- Any model/provider/database/Feishu/memory/formal apply side effect is present.

## Product Note

The bottom-left "12 prep fields" strip is a temporary debug/review entry point. The user does not want this as the final teacher-facing behavior.

The product direction should be:

`generate into teaching-design fields -> show per-field/per-line candidate contracts -> teacher preview/adopt gate`

## Suggested Next Stage

If this package passes with notes, recommend:

`R61_FIELD_GENERATION_TO_LESSON_PLAN_FIELD_CONTRACT`

R61 should make the generated candidate land in the corresponding lesson-plan field and line contract, not in a separate external panel.

