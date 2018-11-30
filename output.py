def show_output():    
    for web_num in range(len(config.total_products_list)):
        website = config.total_products_list[web_num]
        print website[config.init_num].get('web')
        for product_num in range(len(website)):
            dic = website[product_num]
            print dic.get('name'),'------------', dic.get('price')