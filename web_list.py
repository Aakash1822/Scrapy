def loading_web_list():       
    tree = XMLCorpusReader('.', [config.web_list_XML])
    root = tree.xml()
    for web in root.iter(config.web_list_xml_main_tag_name):
        # get xml child nodes name with value(e.g {url:'http://google.com',name:'google'}) - dictionary format
        config.web_list.append(web.attrib)
        # get urls only.
        config.urls_list.append(web.get(config.wel_list_xml_url_attribute))