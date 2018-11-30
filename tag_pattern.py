def check_current_product_tag_patterns(cur_domain):
    for web in config.web_content_regex:
        check_web = re.findall(str(web.get(config.we_content_regex_xml_url_attribute)), cur_domain)
        if(len(check_web) != config.init_num) :
            =
            config.current_products_pattern = web.get(‘products_all’)
            
            config.current_product_name_pattern = web.get(‘products_title’)
         
            config.current_product_price_pattern = web.get(‘products_price’)
            break