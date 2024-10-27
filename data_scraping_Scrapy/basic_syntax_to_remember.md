### start a Scrapy project, enter in terminal:
```bash
scrapy startproject <project_name>
```

## Scrapy Shell commands
### to locate and test commands before the actual scraping, enter in terminal:
```bash
scrapy shell
```

### fetch a url response, enter in terminal:
```bash
fetch('url.com')
```

### fetch a url, enter in terminal:
```bash
fetch('url.com')
```

HTML will be stored in response variable

### test data from the HTML, enter in terminal:
```bash
response.css('div.product-name').get()
products = response.css('div.product-name')             # stores the array of all divs with the similar class name to products
len(products)                                           # checks the length of products

products.css('a.product-item-link').get()
products.css('a.product-item-link ::text').get()        # will return the text only
products.css('a.product-item-link ::text').getall()     # return array of all target class

products.css('span.price ::text').get()
products.css('span.price a::text').get()
products.css('span.price a::text').get().replace('','') # replace a text

products.css('a.product-item-link').attrib['href']
```

### to export an output or file, enter in terminal:
```bash
scrapy crawl <name_of_spider> -o <name>.json
scrapy crawl <name_of_spider> -o <name>.csv

# -O  capital 'O' replaces the file
# -o  small 'o' appends to the file
```
