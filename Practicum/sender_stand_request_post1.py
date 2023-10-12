import configuration
import requests
import data


def post_products_kits(products_ids):
    return requests.post(configuration.URL_SERVICE + configuration.PRODUCTS_KITS_PATH,  # подставляем полный url
                         json=products_ids,  # тут тело
                         headers=data.headers)  # а здесь заголовки


response = post_products_kits(data.product_ids);
print(response.status_code)
print(response.json())
