from django.test import TestCase
from .models import Ranking
from django.urls import reverse


# Create your tests here.
def create_ranking_object(username, current_ques, time_started):
    """
    Instantiate an object of Ranking model class
    """
    return Ranking.objects.create(username=username, currentquestion=current_ques, timestarted=time_started)


class RankViewTest(TestCase):
    def test_rank_view_for_queryset_length_per_page(self):
        """
        The no of queries per page should not exceed 15
        """
        create_ranking_object(username="Symphoria", current_ques="1", time_started="2017-01-20 23:56:06.967625")
        response = self.client.get(reverse('website:ranks'))
        self.assertIs(len(response.context['object_list']) > 15, False)
