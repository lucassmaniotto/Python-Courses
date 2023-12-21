class URLExtractor:
    def __init__(self, url):
        self.url = self.sanitize_url(url)
        self.validate_url()

    def sanitize_url(self, url):
        if type(url) == str:
            return url.strip()
        else:
            return ""
    
    def validate_url(self):
        if not bool(self.url):
            raise LookupError("Invalid URL!")

    def get_base_url(self):
        base_url = self.url[:self.url.find("?")]
        return base_url

    def get_url_params(self):
        url_params = self.url[self.url.find("?")+1:]
        return url_params
    
    def get_param_value(self, search_param):
        index_param = self.get_url_params().find(search_param)
        index_value = index_param + len(search_param) + 1
        end_index = self.get_url_params().find("&", index_value)

        if end_index == -1:
            end_index = len(self.get_url_params())

        value = self.get_url_params()[index_value:end_index]

        return value
