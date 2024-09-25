SELECT
    customer_id,
    first_name AS customer_first_name,
    last_name AS customer_last_name,
    email_address AS customer_email_address,
    phone_number 
FROM {{ ref('src_customers') }}
