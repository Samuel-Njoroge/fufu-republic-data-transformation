SELECT
    inventory_id,
    branch_id,
    menu_item_id,
    quantity AS total_items_left
FROM {{ ref('src_inventory') }}
