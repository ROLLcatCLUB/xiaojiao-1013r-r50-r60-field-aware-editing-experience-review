# 1013R R50-R60 Field-Aware Editing Experience Review

This is a lightweight GPT review package for the current prep-room R21 page copy.

## Scope

R50-R60 does not create a new static page. The implementation is attached to the existing R21 carrier page:

`artifacts/prep_room_page_copy_binds_unified_package_1013R_R21_R50_R60.html`

The goal is to verify that field-aware editing can be seen and tested on the current sample-room page without losing the existing R21/R48/R49 base.

## What This Stage Actually Does

- Keeps the current R21 page copy as the page carrier.
- Uses the R48 recovered canonical field ledger and R49 page bindings.
- Opens the existing edit-card modal for canonical fields.
- Shows canonical field identity inside the edit card.
- Routes candidate fixtures to the matching field instead of a free-floating blue card.
- Splits candidate content into field-internal line contracts.
- Keeps preview-only boundaries:
  - no provider call
  - no model call
  - no database write
  - no Feishu write
  - no memory write
  - no formal apply

## Important Product Note

The bottom-left "12 prep fields" strip is a temporary debug / review entry point. It is not intended to be the final teacher-facing product shape.

The product target remains:

`model/generated candidate -> canonical teaching-design field -> field line contract -> existing edit card -> teacher preview/adopt gate -> later formal package export`

In other words, generated content should eventually land inside the lesson-plan fields, not stay as a separate external panel.

## What This Stage Does Not Claim

- It does not connect a real model/provider/runtime.
- It does not generate final teaching-plan content from a live prompt.
- It does not write candidate text into the formal lesson plan.
- It does not solve the final teacher-facing navigation design.
- It does not treat R45-R47 as a field standard.
- It does not create a new independent sample page.

## Current Review Status

Recommended status:

`R50_R60 = REVIEW_READY_WITH_NOTES`

The stage is ready for GPT review as a field-aware editing smoke package, but should not be described as complete generation-to-lesson-plan runtime.

## Key Counts

- canonical_field_count: 12
- page_edit_item_count: 12
- alias_count: 6
- material_requests_present: true
- missing_canonical_raw_patch_rejected: true
- orphan_ui: 0
- line_contracts_visible: true
- existing_edit_card_reused: true
- body_overflow_fixed_with_modal_scroll: true

## Review Questions

1. Are all current edit items still bound to canonical field keys?
2. Does the edit card expose the canonical field identity clearly enough for debugging?
3. Do candidate fixtures land inside the existing edit card rather than becoming separate body cards?
4. Are candidate contents split into field-internal line contracts instead of one large blob?
5. Is the bottom-left field strip acceptable as a temporary debug/review entry, assuming it will later be hidden or redesigned?
6. Is the next stage correctly defined as generation landing into teaching-design fields, not another static panel?

## Suggested Next Stage

`R61_FIELD_GENERATION_TO_LESSON_PLAN_FIELD_CONTRACT`

Suggested goal:

Teacher intent or model candidate should target a canonical teaching-design field, produce line-level candidate patches, show them in the existing edit card, and only update the page preview after teacher action.

Suggested boundaries:

- still no formal apply
- still no database/writeback
- still no Feishu/memory write
- no new page
- if a test route/page is needed, explicitly mark it as a side test page first

