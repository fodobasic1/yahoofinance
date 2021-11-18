from django.conf import settings


# A helper method for building URLs
# The base URL for all 4 symbols is the same, only difference is s= param
# That base URL is stored in settings.py
# Also, if URL contains diff versions, this is easier way to control it.
def build_query_from_symbol(symbol):
    # Need to encode ' = '
    if (symbol == 'GC=F'):
        symbol = 'GC%3DF'

    url = settings.RSS_URL.format(symbol)
    return url
