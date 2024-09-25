SELECT
    order_id,
    branch_id,
    customer_id,
    payment_method_id,
    order_date_time AS date_of_order,
    order_type,
    total_amount
FROM {{ ('src_orders') }}