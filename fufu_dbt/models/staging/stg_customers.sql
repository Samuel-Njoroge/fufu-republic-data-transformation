select
    customer_id,
    first_name,
    last_name,
    email_address,
    phone_number
from {{ ref('src_customers') }}
