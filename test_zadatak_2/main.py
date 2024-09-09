import requests
import geojson

url = "https://plovput.li-st.net/getObjekti/"

response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    print("Podaci su uspješno dohvaćeni.")
else:
    print("Greška pri dohvaćanju podataka s API-ja.")
    exit()

features = data['features']

print(f"Ukupan broj zapisa (objekata sigurnosti plovidbe): {len(features)}")

filtered_features = [feature for feature in features if feature['properties'].get('tip_objekta') == 16]
print(f"Broj zapisa s tipom objekta 16: {len(filtered_features)}")

filtered_data = geojson.FeatureCollection(filtered_features)

with open('filtered_obekti.geojson', 'w') as f:
    geojson.dump(filtered_data, f)

print("Filtrirani objekti su spremljeni u 'filtered_obekti.geojson'.")
