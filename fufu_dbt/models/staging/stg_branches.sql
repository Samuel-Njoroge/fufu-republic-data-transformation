select
    branch_id,
    name,
    location,
    type
from {{ ref('src_branches') }}
