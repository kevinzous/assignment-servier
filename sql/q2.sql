-- aggregate sales at client and product_type granularity 
WITH agg_sales AS (
    SELECT
        tr.client_id,
        LOWER(pm.product_type) AS product_type, -- lower case product_type since used as pivot column 
        SUM(tr.prod_price * tr.prod_qty) AS total_sales
    FROM `MY_DATA_SET.TRANSACTION` AS tr
    LEFT JOIN `MY_DATA_SET.PRODUCT_NOMENCLATURE` AS pm ON tr.prop_id = pm.product_id
    GROUP BY client_id, product_type
)

SELECT *
FROM agg_sales
PIVOT (
    --aggregated columns
    SUM(total_sales) AS ventes
    --pivot column
    FOR product_type IN ("meuble", "deco")
)
