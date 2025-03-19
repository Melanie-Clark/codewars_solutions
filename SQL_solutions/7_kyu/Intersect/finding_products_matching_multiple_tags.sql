/*
Imagine you are managing an e-commerce platform. It offers a diverse range of products, each tagged with various attributes to 
help customers filter and find items that match their preferences. These tags could represent categories, features, styles, 
or any other relevant attributes.

You want to implement a feature that allows customers to filter products by selecting multiple tags. 
Specifically, when a customer selects several tags, the platform should display only those products that are associated with 
all the selected tags. This ensures that the search results precisely match the customer's combined tag preferences.

We have a product_tags table:

product_id (int): Unique identifier for each product
tag (varchar): Tag associated with the product
The table may contain duplicate rows where the same product is associated with the same tag multiple times.

For our task, we want to find products that are tagged with both Electronics and Gadgets. 
The query should return product_id values in desc order for products that are associated with both of these tags.

*/

SELECT DISTINCT(product_id)
FROM product_tags
WHERE tag = 'Electronics' AND product_id IN (
  SELECT product_id
  FROM product_tags
  WHERE tag = 'Gadgets')
order by product_id DESC;

-- refactored using INTERSECT:
SELECT product_id FROM product_tags WHERE tag IN ('Electronics')
INTERSECT
SELECT product_id FROM product_tags WHERE tag IN ('Gadgets')
ORDER BY product_id DESC