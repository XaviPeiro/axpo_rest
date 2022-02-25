from data_services.models import RatedTimesCar


class Metrics:

    def get_most_frequently_voted(self, q: int):
        return RatedTimesCar.objects.all().order_by("times_voted")[:q]
