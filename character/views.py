from django.shortcuts import render
import json
import hashlib
import requests

# Create your views here.

def character_info(request):
    character_name = request.GET.get('name').title()

    resource = 'characters'
    ts = '1'
    private_key = '78ee68a850dd288d9a477ca04d4d33905615c261'
    public_key = 'a0dd9b7e52bad9b160e83a4fd419da06'
    raw_hash = ts + private_key + public_key
    hash = hashlib.md5(raw_hash.encode('utf-8')).hexdigest()
    url = 'http://gateway.marvel.com/v1/public/{}?limit=100&ts={}&apikey={}&hash={}&name={}'.format(resource, ts, public_key, hash, character_name)
    character_content = json.loads(requests.get(url).content.decode('utf-8'))

    if character_content['data']['results'][0]['description'] != '':
        description = character_content['data']['results'][0]['description']
    else:
        description = 'Description Not Found.'
    image = character_content['data']['results'][0]['thumbnail']['path'] + '.jpg'


    context = {
        'character_name': character_name,
        'description': description,
        'image': image,
    }
    return render(request, "character.html", context)

#hash = 5355d7efe2c744cbb995018975e64cff

# http://gateway.marvel.com/v1/public/characters?limit=100&ts=1&apikey=a0dd9b7e52bad9b160e83a4fd419da06&hash=5355d7efe2c744cbb995018975e64cff&name=Galactus