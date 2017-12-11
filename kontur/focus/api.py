import json
import logging
from functools import partial
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urljoin, urlopen

logger = logging.getLogger(__name__)


class FocusClient(object):
    """
    API client for SKB Kontur Focus
    https://focus.kontur.ru/site/capabilities/api

    Basic usage:
      cl = FocusClient(api_key)
      res = cl.req(inn=inn)
    """
    API_VERSION = 'api3'
    API_PREFIX = 'https://focus-api.kontur.ru'

    def __init__(self, api_key):
        self.api_key = api_key

    def _query(self, method, **kwargs):
        logger.info('Executing "/%(method)s" with params: %(kwargs)s', {
            'method': method,
            'kwargs': kwargs,
        })
        url = urljoin(self.API_PREFIX, '/'.join([self.API_VERSION, method]))
        kwargs.setdefault('key', self.api_key)
        request = Request('?'.join([url, urlencode(kwargs)]))
        try:
            with urlopen(request, timeout=10) as rp:
                data = rp.read()
                data = data.decode(rp.headers.get_content_charset('UTF-8'))
                logger.debug('Raw response: %s', data)
                result = json.loads(data)
                logger.debug('API JSON response: %s', result)
        except HTTPError as e:
            logger.exception('HTTP error: %s', str(e))
            raise
        except URLError as e:
            logger.exception('URL error: %s', str(e))
            raise
        except Exception as e:
            logger.exception('Unexpected error: %s', str(e))
            raise
        return result

    def __getattr__(self, name):
        return partial(self._query, name)
