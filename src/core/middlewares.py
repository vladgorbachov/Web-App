import pstats
from django.conf import settings
from datetime import datetime
from time import perf_counter
import cProfile
from io import StringIO

from pip._vendor.urllib3.packages.six import StringIO


class PerformanceMonitoringMiddleware:
    def __init__(self, get_response):
        # self.pr = cProfile.Profile()
        self.get_response = get_response

    def __call__(self, request):
        pr = cProfile.Profile()
        start = perf_counter()
        pr.enable()
        response = self.get_response(request)
        pr.disable()
        s = StringIO()
        ps = pstats.Stats(pr, stream=s).sort_stats('cumulative')
        ps.print_stats(settings.LOG_RECORDS_COUNT)
        finish = perf_counter()

        if finish - start > settings.MAX_RESPONSE_TIME:
            with open(f'{datetime.today().strftime("%Y-%m-%d")}_performance.log', 'a') as f:
                f.write(f'URI: {request.path} \n')
                f.write(f'METHOD: {request.method}\n')
                if request.GET:
                    f.write(f'GET: {request.GET}\n')
                if request.POST:
                    f.write(f'POST: {request.POST}\n')

                f.write(f'DEBUG INFO:  + {s.getvalue()} \n')
                f.write('_' * 20 + '\n')


        return response