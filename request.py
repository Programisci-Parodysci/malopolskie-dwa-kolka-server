import requests


def register_user(email, password):
    url = 'http://localhost:5000/register'
    data = {
        'email': email,
        'password': password
    }

    response = requests.post(url, json=data)
    print(response.json())


def login_user(email, password):
    url = 'http://localhost:5000/login'
    data = {
        'email': email,
        'password': password
    }

    response = requests.post(url, json=data)

    if response.status_code == 200:
        token = response.json()['token']
        print(f'Zalogowano. Token: {token}')
        return token
    else:
        print(response.json())
        return None


def add_gpx(token, gpx_content):
    url = 'http://localhost:5000/add_gpx'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }
    data = {
        'gpx_file': gpx_content
    }

    response = requests.post(url, headers=headers, json=data)
    print(response.json())


def get_all_gpx(token):
    url = 'http://localhost:5000/get_gpx'
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        gpx_files = response.json().get('gpx_files', [])
        print("Pobrane pliki GPX:")
        for gpx in gpx_files:
            print(gpx)
    else:
        print(response.json())

def get_by_name(token, name):
    url = 'http://localhost:5000/get_gpx/{}'.format(name)
    headers = {
        'Authorization': f'Bearer {token}',
        'Content-Type': 'application/json'
    }

    response = requests.get(url, headers=headers)
    print("dupa")
    if response.status_code == 200:
        print("dupa2")
        gpx_files = response.json().get('gpx_files', [])
        print("dupa3")
        print(gpx_files)
    else:
        print("dupa5")
        print(response.json())


email = 'marekbetoniarek@kurczaczek.pl'
password = 'tereferekuku'

# Rejestracja
register_user(email, password)

# Logowanie
token = login_user(email, password)

# Dodanie pliku GPX, jeśli logowanie było udane
if token:
    gpx_content = """<?xml version="1.0" encoding="UTF-8"?>
<gpx creator="StravaGPX" version="1.1" xmlns="http://www.topografix.com/GPX/1/1" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance" xsi:schemaLocation="http://www.topografix.com/GPX/1/1 http://www.topografix.com/GPX/1/1/gpx.xsd">
 <metadata>
  <name>traska</name>
  <author>
   <name>Kajetan Ożóg</name>
   <link href="https://www.strava.com/athletes/58231011"/>
  </author>
  <copyright author="OpenStreetMap contributors">
   <year>2020</year>
   <license>https://www.openstreetmap.org/copyright</license>
  </copyright>
  <link href="https://www.strava.com/routes/3105417438725084864"/>
 </metadata>
 <trk>
  <name>Rożnowskie w 5K</name>
  <link href="https://www.strava.com/routes/3105417438725084864"/>
  <type>cycling</type>
  <trkseg>
   <trkpt lat="49.7139" lon="20.63509">
    <ele>276.77000000000004</ele>
   </trkpt>
   <trkpt lat="49.713800000000006" lon="20.63464">
    <ele>277.40000000000003</ele>
   </trkpt>
   <trkpt lat="49.71374" lon="20.63409">
    <ele>278.02000000000004</ele>
   </trkpt>
   <trkpt lat="49.71372" lon="20.633460000000003">
    <ele>279.15</ele>
   </trkpt>
   <trkpt lat="49.71371251492275" lon="20.632384999496157">
    <ele>280.42</ele>
   </trkpt>
   <trkpt lat="49.71370501989697" lon="20.63130999932389">
    <ele>282.39000000000004</ele>
   </trkpt>
   <trkpt lat="49.713697514922664" lon="20.63023499948364">
    <ele>284.57000000000005</ele>
   </trkpt>
   <trkpt lat="49.71369000000001" lon="20.629160000000002">
    <ele>285.86</ele>
   </trkpt>
   <trkpt lat="49.71372" lon="20.62882">
    <ele>286.21000000000004</ele>
   </trkpt>
   <trkpt lat="49.71390500352715" lon="20.627920003230805">
    <ele>287.67</ele>
   </trkpt>
   <trkpt lat="49.714090000000006" lon="20.62702">
    <ele>289.55</ele>
   </trkpt>
   <trkpt lat="49.71421" lon="20.62575">
    <ele>291.07000000000005</ele>
   </trkpt>
   <trkpt lat="49.71426" lon="20.62547">
    <ele>291.52</ele>
   </trkpt>
   <trkpt lat="49.714470000000006" lon="20.624630000000003">
    <ele>294.51000000000005</ele>
   </trkpt>
   <trkpt lat="49.71464" lon="20.62375">
    <ele>296.67</ele>
   </trkpt>
   <trkpt lat="49.714670000000005" lon="20.623540000000002">
    <ele>298.56000000000006</ele>
   </trkpt>
   <trkpt lat="49.714670000000005" lon="20.62331">
    <ele>299.44000000000005</ele>
   </trkpt>
   <trkpt lat="49.71463000000001" lon="20.62299">
    <ele>300.13</ele>
   </trkpt>
   <trkpt lat="49.714330000000004" lon="20.621730000000003">
    <ele>301.45000000000005</ele>
   </trkpt>
   <trkpt lat="49.714310000000005" lon="20.621440000000003">
    <ele>302.08</ele>
   </trkpt>
   <trkpt lat="49.71432" lon="20.6213">
    <ele>302.49</ele>
   </trkpt>
   <trkpt lat="49.714400000000005" lon="20.621000000000002">
    <ele>303.81</ele>
   </trkpt>
   <trkpt lat="49.71455" lon="20.62075">
    <ele>306.55</ele>
   </trkpt>
   <trkpt lat="49.71468" lon="20.62047">
    <ele>308.04</ele>
   </trkpt>
   <trkpt lat="49.71500000401877" lon="20.61950500632709">
    <ele>311.84</ele>
   </trkpt>
   <trkpt lat="49.715320000000006" lon="20.618540000000003">
    <ele>315.78</ele>
   </trkpt>
   <trkpt lat="49.71573000290135" lon="20.617715007022053">
    <ele>320.67</ele>
   </trkpt>
   <trkpt lat="49.71614" lon="20.61689">
    <ele>325.91</ele>
   </trkpt>
   <trkpt lat="49.71637000172304" lon="20.61625500304217">
    <ele>328.40000000000003</ele>
   </trkpt>
   <trkpt lat="49.71660000000001" lon="20.615620000000003">
    <ele>331.27</ele>
   </trkpt>
   <trkpt lat="49.716840000000005" lon="20.61496">
    <ele>334.98</ele>
   </trkpt>
   <trkpt lat="49.71707000724853" lon="20.61404334195712">
    <ele>338.74</ele>
   </trkpt>
   <trkpt lat="49.717300007263496" lon="20.61312667523091">
    <ele>342.14000000000004</ele>
   </trkpt>
   <trkpt lat="49.717530000000004" lon="20.61221">
    <ele>345.74000000000007</ele>
   </trkpt>
   <trkpt lat="49.7177" lon="20.61174">
    <ele>346.79</ele>
   </trkpt>
   <trkpt lat="49.718000001793364" lon="20.611110003713637">
    <ele>347.71000000000004</ele>
   </trkpt>
   <trkpt lat="49.718300000000006" lon="20.610480000000003">
    <ele>347.68000000000006</ele>
   </trkpt>
   <trkpt lat="49.717753335436356" lon="20.609986655566317">
    <ele>350.1</ele>
   </trkpt>
   <trkpt lat="49.71720666877752" lon="20.60949332224022">
    <ele>351.77000000000004</ele>
   </trkpt>
   <trkpt lat="49.716660000000005" lon="20.609">
    <ele>354.90000000000003</ele>
   </trkpt>
   <trkpt lat="49.716530000000006" lon="20.60885">
    <ele>355.55</ele>
   </trkpt>
   <trkpt lat="49.71643" lon="20.60867">
    <ele>356.52</ele>
   </trkpt>
   <trkpt lat="49.71603" lon="20.60809">
    <ele>360.44000000000005</ele>
   </trkpt>
   <trkpt lat="49.7156" lon="20.6076">
    <ele>366.24</ele>
   </trkpt>
   <trkpt lat="49.71506333608554" lon="20.607039987678146">
    <ele>372.07</ele>
   </trkpt>
   <trkpt lat="49.714526669471326" lon="20.606479987733067">
    <ele>378.38000000000005</ele>
   </trkpt>
   <trkpt lat="49.71399" lon="20.60592">
    <ele>386.24</ele>
   </trkpt>
   <trkpt lat="49.713770000000004" lon="20.605710000000002">
    <ele>390.92</ele>
   </trkpt>
   <trkpt lat="49.713530000000006" lon="20.60553">
    <ele>393.64000000000004</ele>
   </trkpt>
   <trkpt lat="49.71332" lon="20.605500000000003">
    <ele>395.47</ele>
   </trkpt>
   <trkpt lat="49.71263999997134" lon="20.60553666769556">
    <ele>398.73</ele>
   </trkpt>
   <trkpt lat="49.71195999993111" lon="20.60557333436438">
    <ele>398.62</ele>
   </trkpt>
   <trkpt lat="49.71128" lon="20.605610000000002">
    <ele>397.96000000000004</ele>
   </trkpt>
   <trkpt lat="49.71105000000001" lon="20.605600000000003">
    <ele>397.87000000000006</ele>
   </trkpt>
   <trkpt lat="49.71063" lon="20.60554">
    <ele>397.87000000000006</ele>
   </trkpt>
   <trkpt lat="49.71007" lon="20.605410000000003">
    <ele>398.15000000000003</ele>
   </trkpt>
   <trkpt lat="49.70933" lon="20.605300000000003">
    <ele>395.98</ele>
   </trkpt>
   <trkpt lat="49.709050000000005" lon="20.605220000000003">
    <ele>395.06</ele>
   </trkpt>
   <trkpt lat="49.708920000000006" lon="20.605140000000002">
    <ele>393.54</ele>
   </trkpt>
   <trkpt lat="49.708690000000004" lon="20.60488">
    <ele>392.73</ele>
   </trkpt>
   <trkpt lat="49.70864" lon="20.60442">
    <ele>394.17</ele>
   </trkpt>
   <trkpt lat="49.708510000000004" lon="20.60388">
    <ele>397.4800000000001</ele>
   </trkpt>
   <trkpt lat="49.70844" lon="20.6035">
    <ele>401.83</ele>
   </trkpt>
   <trkpt lat="49.70853" lon="20.602990000000002">
    <ele>408.47</ele>
   </trkpt>
   <trkpt lat="49.70857" lon="20.60265">
    <ele>410.54</ele>
   </trkpt>
   <trkpt lat="49.70858000376287" lon="20.6017150002169">
    <ele>419.29</ele>
   </trkpt>
   <trkpt lat="49.70859" lon="20.60078">
    <ele>426.77000000000004</ele>
   </trkpt>
   <trkpt lat="49.70862" lon="20.60049">
    <ele>430.7300000000001</ele>
   </trkpt>
   <trkpt lat="49.70875" lon="20.599780000000003">
    <ele>438.31</ele>
   </trkpt>
   <trkpt lat="49.709045006676234" lon="20.59853500754357">
    <ele>449.05000000000007</ele>
   </trkpt>
   <trkpt lat="49.709340000000005" lon="20.59729">
    <ele>459.27</ele>
   </trkpt>
   <trkpt lat="49.70937000000001" lon="20.597">
    <ele>459.27</ele>
   </trkpt>
   <trkpt lat="49.70933" lon="20.596320000000002">
    <ele>467.61</ele>
   </trkpt>
   <trkpt lat="49.70931" lon="20.595280000000002">
    <ele>480.69000000000005</ele>
   </trkpt>
   <trkpt lat="49.709340000000005" lon="20.59505">
    <ele>480.69000000000005</ele>
   </trkpt>
   <trkpt lat="49.70958500562218" lon="20.59390500587397">
    <ele>492.87</ele>
   </trkpt>
   <trkpt lat="49.709830000000004" lon="20.592760000000002">
    <ele>504.62000000000006</ele>
   </trkpt>
   <trkpt lat="49.7100750044389" lon="20.59174500510175">
    <ele>517.7700000000001</ele>
   </trkpt>
   <trkpt lat="49.71032" lon="20.59073">
    <ele>526.97</ele>
   </trkpt>
   <trkpt lat="49.710440000000006" lon="20.59046">
    <ele>528.97</ele>
   </trkpt>
   <trkpt lat="49.71072" lon="20.58998">
    <ele>532.6899999999999</ele>
   </trkpt>
   <trkpt lat="49.7109" lon="20.58951">
    <ele>535.0</ele>
   </trkpt>
   <trkpt lat="49.710950000000004" lon="20.58923">
    <ele>537.24</ele>
   </trkpt>
   <trkpt lat="49.71105000000001" lon="20.58892">
    <ele>542.1400000000001</ele>
   </trkpt>
   <trkpt lat="49.711490000000005" lon="20.588220000000003">
    <ele>549.0400000000001</ele>
   </trkpt>
   <trkpt lat="49.71187500263111" lon="20.587435006266084">
    <ele>554.61</ele>
   </trkpt>
   <trkpt lat="49.71226" lon="20.586650000000002">
    <ele>562.23</ele>
   </trkpt>
   <trkpt lat="49.71256" lon="20.58593">
    <ele>567.8000000000001</ele>
   </trkpt>
   <trkpt lat="49.71289" lon="20.585220000000003">
    <ele>574.26</ele>
   </trkpt>
   <trkpt lat="49.71313000000001" lon="20.584880000000002">
    <ele>577.97</ele>
   </trkpt>
   <trkpt lat="49.713210000000004" lon="20.58461">
    <ele>579.4</ele>
   </trkpt>
   <trkpt lat="49.713260000000005" lon="20.584370000000003">
    <ele>580.23</ele>
   </trkpt>
   <trkpt lat="49.713350000000005" lon="20.583660000000002">
    <ele>583.35</ele>
   </trkpt>
   <trkpt lat="49.713420000000006" lon="20.58349">
    <ele>583.35</ele>
   </trkpt>
   <trkpt lat="49.713710000000006" lon="20.582910000000002">
    <ele>589.6800000000001</ele>
   </trkpt>
   <trkpt lat="49.71376" lon="20.582720000000002">
    <ele>590.16</ele>
   </trkpt>
   <trkpt lat="49.713770000000004" lon="20.58249">
    <ele>590.01</ele>
   </trkpt>
   <trkpt lat="49.71372" lon="20.58209">
    <ele>589.49</ele>
   </trkpt>
   <trkpt lat="49.713680000000004" lon="20.581950000000003">
    <ele>588.43</ele>
   </trkpt>
   <trkpt lat="49.71365" lon="20.581770000000002">
    <ele>587.95</ele>
   </trkpt>
   <trkpt lat="49.71361" lon="20.58106">
    <ele>587.0200000000001</ele>
   </trkpt>
   <trkpt lat="49.713680000000004" lon="20.580470000000002">
    <ele>587.0600000000001</ele>
   </trkpt>
   <trkpt lat="49.713640000000005" lon="20.58032">
    <ele>586.69</ele>
   </trkpt>
   <trkpt lat="49.71352" lon="20.58011">
    <ele>586.48</ele>
   </trkpt>
   <trkpt lat="49.71345" lon="20.579680000000003">
    <ele>588.09</ele>
   </trkpt>
   <trkpt lat="49.71341" lon="20.578860000000002">
    <ele>593.1899999999999</ele>
   </trkpt>
   <trkpt lat="49.71343" lon="20.57845">
    <ele>596.02</ele>
   </trkpt>
   <trkpt lat="49.71351000000001" lon="20.577810000000003">
    <ele>600.69</ele>
   </trkpt>
   <trkpt lat="49.71359000433184" lon="20.576805001852964">
    <ele>608.16</ele>
   </trkpt>
   <trkpt lat="49.71367000000001" lon="20.5758">
    <ele>616.7900000000001</ele>
   </trkpt>
   <trkpt lat="49.71372" lon="20.575280000000003">
    <ele>620.8</ele>
   </trkpt>
   <trkpt lat="49.713710000000006" lon="20.57517">
    <ele>621.75</ele>
   </trkpt>
   <trkpt lat="49.713550000000005" lon="20.5747">
    <ele>624.57</ele>
   </trkpt>
   <trkpt lat="49.713300000000004" lon="20.57428">
    <ele>629.46</ele>
   </trkpt>
   <trkpt lat="49.713240000000006" lon="20.574080000000002">
    <ele>631.8000000000001</ele>
   </trkpt>
   <trkpt lat="49.71313000000001" lon="20.57346">
    <ele>634.4000000000001</ele>
   </trkpt>
   <trkpt lat="49.71307" lon="20.573230000000002">
    <ele>637.84</ele>
   </trkpt>
   <trkpt lat="49.71287" lon="20.57272">
    <ele>642.6200000000001</ele>
   </trkpt>
   <trkpt lat="49.712700000000005" lon="20.572110000000002">
    <ele>647.8100000000001</ele>
   </trkpt>
   <trkpt lat="49.712590000000006" lon="20.57175">
    <ele>650.63</ele>
   </trkpt>
   <trkpt lat="49.71243000203165" lon="20.57106499779437">
    <ele>658.27</ele>
   </trkpt>
   <trkpt lat="49.712270000000004" lon="20.57038">
    <ele>666.4100000000001</ele>
   </trkpt>
   <trkpt lat="49.712250000000004" lon="20.5701">
    <ele>669.1400000000001</ele>
   </trkpt>
   <trkpt lat="49.71229" lon="20.569560000000003">
    <ele>672.97</ele>
   </trkpt>
   <trkpt lat="49.71228000000001" lon="20.56897">
    <ele>673.59</ele>
   </trkpt>
   <trkpt lat="49.7122" lon="20.56785">
    <ele>674.44</ele>
   </trkpt>
   <trkpt lat="49.71217000000001" lon="20.567500000000003">
    <ele>678.1700000000001</ele>
   </trkpt>
   <trkpt lat="49.71202" lon="20.56691">
    <ele>681.2800000000001</ele>
   </trkpt>
   <trkpt lat="49.711940000000006" lon="20.566480000000002">
    <ele>683.1400000000001</ele>
   </trkpt>
   <trkpt lat="49.71198500216009" lon="20.56577000081238">
    <ele>684.5600000000001</ele>
   </trkpt>
   <trkpt lat="49.712030000000006" lon="20.565060000000003">
    <ele>685.23</ele>
   </trkpt>
   <trkpt lat="49.71206" lon="20.56481">
    <ele>685.4100000000001</ele>
   </trkpt>
   <trkpt lat="49.71219000000001" lon="20.564580000000003">
    <ele>685.61</ele>
   </trkpt>
   <trkpt lat="49.71229" lon="20.564290000000003">
    <ele>686.36</ele>
   </trkpt>
   <trkpt lat="49.7124" lon="20.56407">
    <ele>686.5100000000001</ele>
   </trkpt>
   <trkpt lat="49.712650000000004" lon="20.5637">
    <ele>686.0</ele>
   </trkpt>
   <trkpt lat="49.71273" lon="20.5635">
    <ele>685.5300000000001</ele>
   </trkpt>
   <trkpt lat="49.712740000000004" lon="20.56334">
    <ele>685.25</ele>
   </trkpt>
   <trkpt lat="49.71267" lon="20.56296">
    <ele>685.62</ele>
   </trkpt>
   <trkpt lat="49.71266000000001" lon="20.56277">
    <ele>685.95</ele>
   </trkpt>
   <trkpt lat="49.71269" lon="20.562520000000003">
    <ele>686.9300000000001</ele>
   </trkpt>
   <trkpt lat="49.71266000000001" lon="20.562260000000002">
    <ele>687.76</ele>
   </trkpt>
   <trkpt lat="49.71257000000001" lon="20.56183">
    <ele>689.6800000000001</ele>
   </trkpt>
   <trkpt lat="49.712480000000006" lon="20.561490000000003">
    <ele>691.9200000000001</ele>
   </trkpt>
   <trkpt lat="49.71246000000001" lon="20.561220000000002">
    <ele>694.89</ele>
   </trkpt>
   <trkpt lat="49.71246000000001" lon="20.560730000000003">
    <ele>698.35</ele>
   </trkpt>
   <trkpt lat="49.71249" lon="20.560090000000002">
    <ele>702.23</ele>
   </trkpt>
   <trkpt lat="49.71256" lon="20.55967">
    <ele>701.83</ele>
   </trkpt>
   <trkpt lat="49.71285" lon="20.558470000000003">
    <ele>701.1800000000001</ele>
   </trkpt>
   <trkpt lat="49.71308500209053" lon="20.55777000344253">
    <ele>699.74</ele>
   </trkpt>
   <trkpt lat="49.71332" lon="20.557070000000003">
    <ele>700.0200000000001</ele>
   </trkpt>
   <trkpt lat="49.71349000000001" lon="20.556700000000003">
    <ele>699.84</ele>
   </trkpt>
   <trkpt lat="49.71387000000001" lon="20.55601">
    <ele>697.7700000000001</ele>
   </trkpt>
   <trkpt lat="49.714275000939246" lon="20.555550003803727">
    <ele>692.3600000000001</ele>
   </trkpt>
   <trkpt lat="49.71468" lon="20.555090000000003">
    <ele>685.0200000000001</ele>
   </trkpt>
   <trkpt lat="49.71490000000001" lon="20.554810000000003">
    <ele>678.4</ele>
   </trkpt>
   <trkpt lat="49.71501000000001" lon="20.554640000000003">
    <ele>676.8900000000001</ele>
   </trkpt>
   <trkpt lat="49.71531" lon="20.554060000000003">
    <ele>666.61</ele>
   </trkpt>
   <trkpt lat="49.71555000000001" lon="20.553710000000002">
    <ele>660.3800000000001</ele>
   </trkpt>
   <trkpt lat="49.71582" lon="20.553250000000002">
    <ele>654.3000000000001</ele>
   </trkpt>
   <trkpt lat="49.716010000000004" lon="20.55282">
    <ele>651.93</ele>
   </trkpt>
   <trkpt lat="49.71634" lon="20.552210000000002">
    <ele>652.4300000000001</ele>
   </trkpt>
   <trkpt lat="49.71638" lon="20.552010000000003">
    <ele>652.5500000000001</ele>
   </trkpt>
   <trkpt lat="49.71632" lon="20.551090000000002">
    <ele>654.25</ele>
   </trkpt>
   <trkpt lat="49.71641" lon="20.550910000000002">
    <ele>655.1800000000001</ele>
   </trkpt>
   <trkpt lat="49.716440000000006" lon="20.55076">
    <ele>655.1800000000001</ele>
   </trkpt>
   <trkpt lat="49.71645" lon="20.5503">
    <ele>656.6200000000001</ele>
   </trkpt>
   <trkpt lat="49.71651000000001" lon="20.549850000000003">
    <ele>658.0600000000001</ele>
   </trkpt>
   <trkpt lat="49.716570000000004" lon="20.549650000000003">
    <ele>660.09</ele>
   </trkpt>
   <trkpt lat="49.71660000000001" lon="20.54914">
    <ele>663.1400000000001</ele>
   </trkpt>
   <trkpt lat="49.71658000000001" lon="20.548820000000003">
    <ele>665.52</ele>
   </trkpt>
   <trkpt lat="49.716480000000004" lon="20.54813">
    <ele>669.6</ele>
   </trkpt>
   <trkpt lat="49.716460000000005" lon="20.547530000000002">
    <ele>671.6700000000001</ele>
   </trkpt>
   <trkpt lat="49.71652" lon="20.54651">
    <ele>677.1400000000001</ele>
   </trkpt>
   <trkpt lat="49.71663" lon="20.54568">
    <ele>681.61</ele>
   </trkpt>
   <trkpt lat="49.716945005434894" lon="20.544550007549763">
    <ele>683.7700000000001</ele>
   </trkpt>
   <trkpt lat="49.71726" lon="20.54342">
    <ele>688.71</ele>
   </trkpt>
   <trkpt lat="49.71741" lon="20.54331">
    <ele>685.85</ele>
   </trkpt>
   <trkpt lat="49.717740000000006" lon="20.542990000000003">
    <ele>679.9300000000001</ele>
   </trkpt>
   <trkpt lat="49.718" lon="20.542650000000002">
    <ele>678.5500000000001</ele>
   </trkpt>
   <trkpt lat="49.718180000000004" lon="20.542340000000003">
    <ele>677.85</ele>
   </trkpt>
   <trkpt lat="49.71826" lon="20.542260000000002">
    <ele>676.96</ele>
   </trkpt>
   <trkpt lat="49.71838" lon="20.54223">
    <ele>674.0600000000001</ele>
   </trkpt>
   <trkpt lat="49.718990000000005" lon="20.542330000000003">
    <ele>666.52</ele>
   </trkpt>
   <trkpt lat="49.719240000000006" lon="20.54231">
    <ele>662.64</ele>
   </trkpt>
   <trkpt lat="49.71936" lon="20.542330000000003">
    <ele>659.8000000000001</ele>
   </trkpt>
   <trkpt lat="49.71949000000001" lon="20.5424">
    <ele>656.42</ele>
   </trkpt>
   <trkpt lat="49.719910000000006" lon="20.542900000000003">
    <ele>645.96</ele>
   </trkpt>
   <trkpt lat="49.720110000000005" lon="20.543020000000002">
    <ele>643.1300000000001</ele>
   </trkpt>
   <trkpt lat="49.72025000000001" lon="20.543200000000002">
    <ele>641.14</ele>
   </trkpt>
   <trkpt lat="49.720560000000006" lon="20.543760000000002">
    <ele>631.3700000000001</ele>
   </trkpt>
   <trkpt lat="49.720690000000005" lon="20.543930000000003">
    <ele>626.6700000000001</ele>
   </trkpt>
   <trkpt lat="49.72092000000001" lon="20.544320000000003">
    <ele>620.83</ele>
   </trkpt>
   <trkpt lat="49.72101000000001" lon="20.544510000000002">
    <ele>618.4300000000001</ele>
   </trkpt>
   <trkpt lat="49.721340000000005" lon="20.544960000000003">
    <ele>610.09</ele>
   </trkpt>
   <trkpt lat="49.72158" lon="20.54523">
    <ele>604.4900000000001</ele>
   </trkpt>
   <trkpt lat="49.72167" lon="20.54529">
    <ele>602.1800000000001</ele>
   </trkpt>
   <trkpt lat="49.72177000000001" lon="20.545330000000003">
    <ele>599.6</ele>
   </trkpt>
   <trkpt lat="49.72185" lon="20.545340000000003">
    <ele>595.6400000000001</ele>
   </trkpt>
   <trkpt lat="49.72236" lon="20.545270000000002">
    <ele>583.71</ele>
   </trkpt>
   <trkpt lat="49.72247" lon="20.5453">
    <ele>582.89</ele>
   </trkpt>
   <trkpt lat="49.72279" lon="20.545460000000002">
    <ele>579.37</ele>
   </trkpt>
   <trkpt lat="49.72307000000001" lon="20.54568">
    <ele>574.3000000000001</ele>
   </trkpt>
   <trkpt lat="49.723470000000006" lon="20.546110000000002">
    <ele>567.9300000000001</ele>
   </trkpt>
   <trkpt lat="49.724050000000005" lon="20.54651">
    <ele>564.57</ele>
   </trkpt>
   <trkpt lat="49.724250000000005" lon="20.54671">
    <ele>562.8100000000001</ele>
   </trkpt>
   <trkpt lat="49.72430000000001" lon="20.5468">
    <ele>561.58</ele>
   </trkpt>
   <trkpt lat="49.72448000000001" lon="20.54747">
    <ele>552.8000000000001</ele>
   </trkpt>
   <trkpt lat="49.724520000000005" lon="20.547770000000003">
    <ele>548.25</ele>
   </trkpt>
   <trkpt lat="49.724560000000004" lon="20.54867">
    <ele>540.75</ele>
   </trkpt>
   <trkpt lat="49.724520000000005" lon="20.54898">
    <ele>539.46</ele>
   </trkpt>
   <trkpt lat="49.724450000000004" lon="20.549190000000003">
    <ele>539.48</ele>
   </trkpt>
   <trkpt lat="49.72444" lon="20.54934">
    <ele>539.45</ele>
   </trkpt>
   <trkpt lat="49.72457000000001" lon="20.54992">
    <ele>535.66</ele>
   </trkpt>
   <trkpt lat="49.724590000000006" lon="20.5501">
    <ele>534.9</ele>
   </trkpt>
   <trkpt lat="49.72458" lon="20.550210000000003">
    <ele>534.2800000000001</ele>
   </trkpt>
   <trkpt lat="49.724430000000005" lon="20.550780000000003">
    <ele>532.6</ele>
   </trkpt>
   <trkpt lat="49.72442" lon="20.55092">
    <ele>531.81</ele>
   </trkpt>
   <trkpt lat="49.72446" lon="20.55103">
    <ele>530.5500000000001</ele>
   </trkpt>
   <trkpt lat="49.72455" lon="20.55113">
    <ele>527.33</ele>
   </trkpt>
   <trkpt lat="49.724650000000004" lon="20.551190000000002">
    <ele>525.75</ele>
   </trkpt>
   <trkpt lat="49.72475000000001" lon="20.551170000000003">
    <ele>525.75</ele>
   </trkpt>
   <trkpt lat="49.72511" lon="20.55093">
    <ele>519.08</ele>
   </trkpt>
   <trkpt lat="49.725190000000005" lon="20.550900000000002">
    <ele>517.45</ele>
   </trkpt>
   <trkpt lat="49.72556" lon="20.55082">
    <ele>512.49</ele>
   </trkpt>
   <trkpt lat="49.725660000000005" lon="20.55077">
    <ele>511.65999999999997</ele>
   </trkpt>
   <trkpt lat="49.725950000000005" lon="20.55056">
    <ele>509.34000000000003</ele>
   </trkpt>
   <trkpt lat="49.72605" lon="20.55054">
    <ele>507.90000000000003</ele>
   </trkpt>
   <trkpt lat="49.72612" lon="20.550610000000002">
    <ele>504.36</ele>
   </trkpt>
   <trkpt lat="49.72628" lon="20.55085">
    <ele>504.36</ele>
   </trkpt>
   <trkpt lat="49.7265" lon="20.551070000000003">
    <ele>504.36</ele>
   </trkpt>
   <trkpt lat="49.726820000000004" lon="20.55132">
    <ele>504.36</ele>
   </trkpt>
   <trkpt lat="49.72695" lon="20.55152">
    <ele>504.36</ele>
   </trkpt>
   <trkpt lat="49.727090000000004" lon="20.551920000000003">
    <ele>504.36</ele>
   </trkpt>
   <trkpt lat="49.72731" lon="20.55319">
    <ele>504.36</ele>
   </trkpt>
   <trkpt lat="49.72737" lon="20.553420000000003">
    <ele>504.36</ele>
   </trkpt>
   <trkpt lat="49.727785004411395" lon="20.554424991563582">
    <ele>504.36</ele>
   </trkpt>
   <trkpt lat="49.7282" lon="20.55543">
    <ele>504.36</ele>
   </trkpt>
   <trkpt lat="49.728350000000006" lon="20.55564">
    <ele>376.91</ele>
   </trkpt>
   <trkpt lat="49.72842000000001" lon="20.5557">
    <ele>376.91</ele>
   </trkpt>
   <trkpt lat="49.72856" lon="20.555760000000003">
    <ele>376.91</ele>
   </trkpt>
   <trkpt lat="49.72889000000001" lon="20.55582">
    <ele>376.91</ele>
   </trkpt>
   <trkpt lat="49.729000000000006" lon="20.5559">
    <ele>376.91</ele>
   </trkpt>
   <trkpt lat="49.72908" lon="20.55601">
    <ele>376.91</ele>
   </trkpt>
   <trkpt lat="49.729390001423056" lon="20.556594996169785">
    <ele>376.91</ele>
   </trkpt>
   <trkpt lat="49.7297" lon="20.557180000000002">
    <ele>376.91</ele>
   </trkpt>
  </trkseg>
 </trk>
</gpx>"""

    add_gpx(token, gpx_content)

    gpx_name = 'traska'
    headers = {'Authorization': f'Bearer {token}'}
    response = requests.get(f'http://localhost:5000/get_gpx_by_name/{gpx_name}', headers=headers)

    print(response.json())
