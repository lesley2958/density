# Run this with python3, enter your API key when prompted. You should obtain your api key from
# the density website.
import requests


auth_key = input("Enter your API Auth Key");
BASE_URL = "https://density.adicu.com"
headers = {"Authorization": auth_key}
payload = {"auth_token": auth_key}


response = requests.get(BASE_URL + "/latest", headers=headers, params=payload)
r = response.json()


assert 'building_name' in r['data'][0]

#test building_id
res = requests.get(BASE_URL + "/latest/building/62", headers=headers, params=payload)
r = res.json()

assert "parent_id" in r['data'][0]
assert r['data'][0]['parent_id'] == 62
print ("/latest/building/building_id: OK")


#test /group_id
res = requests.get(BASE_URL + "/latest/group/147", headers=headers, params=payload)
r = res.json()

assert "group_id" in r['data'][0]
assert r['data'][0]['group_id'] == 147
print ("/latest/group_id: OK")


#test /window/building/id
res = requests.get(BASE_URL + "/window/2014-10-10T08:00/2014-10-10T21:30/building/75", headers=headers, params=payload)
r = res.json()
assert "parent_id" in r['data'][0], "error with window/time/building/id end point"
assert r['data'][0]['parent_id'] == 75, "error window/time/building/id end point "
print("/window/Building_id: OK")


#test /window/building/id
res = requests.get(BASE_URL + "/window/2014-10-10T08:00/2014-10-10T21:30/group/155", headers=headers, params=payload)
r = res.json()
assert "group_id" in r['data'][0], "error with window/time/group_id end point"
assert r['data'][0]['group_id'] == 155, "error window/time/group_id end point "
print("/window/group_id: OK")


#test /day/date/group_id
res = requests.get(BASE_URL + "/day/2014-10-10/group/155", headers=headers, params=payload)
r = res.json()
assert "group_id" in r['data'][0], "error with day/date/group_id end point"
assert r['data'][0]['group_id'] == 155, "error day/date/group_id end point "
print("/day/date/group_id: OK")


#test /day/date/group_id
res = requests.get(BASE_URL + "/day/2014-10-10/building/75", headers=headers, params=payload)
r = res.json()
assert "parent_id" in r['data'][0], "error with day/date/building_id end point"
assert r['data'][0]['parent_id'] == 75, "error day/date/building_id end point "
print("/day/date/group_id: OK")

#print("Sample Output: \n {}".format(r))