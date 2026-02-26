
  create view "warehouse"."staging"."stg_sales__dbt_tmp"
    
    
  as (
    with src as (
  select
    order_id,
    order_date,
    customer_id,
    product_id,
    quantity,
    unit_price,
    country
  from staging.sales_raw
)
select * from src
  );