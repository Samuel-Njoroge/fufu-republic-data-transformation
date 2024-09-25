SELECT
    menu_item_id,
    item_name,
    category AS item_category,
    price AS cost_of_item,
    is_standard
FROM {{ ref('src_menu_items') }}