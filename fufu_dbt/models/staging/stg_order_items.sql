SELECT
    order_item_id,
    order_id AS item_order_id,
    menu_item_id,
    quantity AS total_number
FROM {{ ref('src_order_items') }}