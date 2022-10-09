WITH
-- generate a calendar table containing each day of year 2020
dim_calendar AS (
    SELECT date
    FROM
        UNNEST(GENERATE_DATE_ARRAY('2020-01-01', '2020-12-31', INTERVAL 1 DAY)) AS date
),

-- aggreagate sales tables at the day granularity
fact_daily_sales AS (
    SELECT
        date,
        SUM(prod_price * prod_qty) AS daily_total_sales
    FROM `MY_DATA_SET.TRANSACTION`
    GROUP BY date
)

SELECT
    dim_calendar.date,
    COALESCE(fact_daily_sales.daily_total_sales, 0) AS ventes
FROM dim_calendar
LEFT JOIN fact_daily_sales USING (date)
ORDER BY dim_calendar.date
