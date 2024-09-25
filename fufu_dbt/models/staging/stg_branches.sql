SELECT
    branch_id,
    name AS branch_name,
    location AS branch_location,
    type
FROM {{ ref('src_branches') }}
