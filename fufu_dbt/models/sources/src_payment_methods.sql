select * from {{ source('raw', 'payment_methods') }}
