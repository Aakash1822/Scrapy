def loading_web_content_regex():
    tree = XMLCorpusReader('.', [config.web_content_regex_file])
    root = tree.xml()
    for web in root.iter(config.we_content_regex_list_main_tag_name):
        # web.attrib = dictionary format,{'url:zzz','content':zzz, 'date:zzz',etc...}
        config.web_content_regex.append(web.attrib)