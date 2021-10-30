import base64

from ximilar.client import  GenericTaggingClient




def auto_tagger(number):
    generic_client = GenericTaggingClient(token="YOUR XIMILAR CLIENT TOKEN HERE")
    file = number
    file_name = f"Images\\{file}.jpeg"
    with open(file_name, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    result = generic_client.tags([{"_base64": f"data:image/jpeg;base64,{encoded_string}"}])
    tags = result['records'][0]['_tags']
    tags_as_list = ','
    for x in tags:
        if x['prob'] >= 0.7:
            tags_as_list = tags_as_list + x['name'] + ','
    print(file_name,tags_as_list)
    return(tags_as_list)

#print(auto_tagger(file_number)) will return the tags. file_number is the name of the file (it should be a integer , ex. 19.jpeg)
