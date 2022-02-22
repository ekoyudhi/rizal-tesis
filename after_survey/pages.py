from distutils.log import error
from modulefinder import AddPackagePath
import random
from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants, Player


class Survey(Page):
    form_model = 'player'
    form_fields = ['s1','s2','s3','s4','s5','s6','s7','s8','s9','s10','s11']

class Ambilpay(Page):
    form_model = 'player'
    form_fields = ['angka_random']

    def before_next_page(self):
        periode = self.participant.vars['periode']
        list1 = list(range(1, (periode+1)))
        rnd = random.choice(list1)
        self.participant.vars['periode_terpilih'] = rnd

class Prosespay(Page):
    form_model = 'player'
    form_fields = ['periode_terpilih','payoff_real']

    def vars_for_template(self):
        #player = self.player.participant.get_players()
        #player = self.player.participant.vars
        periode_terpilih = self.participant.vars['periode_terpilih']
        payoff_awal = self.participant.vars['payoff_awal_'+str(periode_terpilih)]
        return{'periode_terpilih':periode_terpilih,'payoff_real':payoff_awal}
    
class Hasilpay(Page):
    pass


page_sequence = [Survey, Ambilpay, Prosespay ,Hasilpay]
#page_sequence = [Prosespay]
