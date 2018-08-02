from esipy import EsiApp
esi_app = EsiApp()
app = esi_app.get_latest_swagger

# Using App, both "app" are the same at the end
from esipy import App

# App.create(url, strict=True)
# with url = the swagger spec URL, leave strict to default
#app = App.create(url="https://esi.tech.ccp.is/latest/swagger.json?datasource=tranquility")


market_order_operation = app.op['get_markets_region_id_orders'](
    region_id=10000002,
    type_id=34,
    order_type='all',
)

# basic client, for public endpoints only
from esipy import EsiClient
client = EsiClient(
    retry_requests=True,  # set to retry on http 5xx error (default False)
    headers={'User-Agent': 'Something CCP can use to contact you and that define your app'},
    raw_body_only=False,  # default False, set to True to never parse response and only return raw JSON string content.
)

# do the request
response = client.request(market_order_operation)
# use it: response.data contains the parsed result of the request.
for l in range(0,len(response.data)):
   print(response.data[l].price)

#print(response.data[0].order_id)

## to get the headers objects, you can get the header attribute
#print(response.header)

from esipy import EsiSecurity

# creating the security object using the app
security = EsiSecurity(
    app=app,
    redirect_uri='https://callback.com/you/set/on/developers/eveonline',
    client_id='you client id',
    secret_key='the_secret_key',
)

# creating the security object without app, using default TQ sso URL
security = EsiSecurity(
    redirect_uri='https://callback.com/you/set/on/developers/eveonline',
    client_id='you client id',
    secret_key='the_secret_key',
)

# when you have a security object, you need to give it to the client
# so he knows where to get auth headers for authed endpoints.
# --> simplified client
client = EsiClient(security=security)