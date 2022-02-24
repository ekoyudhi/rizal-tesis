from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Awal(Page):
    def before_next_page(self):
        self.participant.vars['periode'] = Constants.num_rounds
        r_list = random.sample(range(1,Constants.num_rounds+1),Constants.num_audit)
        r_list.sort()
        idx = 1
        for r in r_list:
            self.participant.vars['rand_audit_'+str(idx)] = r
            idx+=1
            #self.participant.vars['rand_audit_2'] = r_list[1]
            #self.participant.vars['rand_audit_3'] = r_list[2]

    def is_displayed(self):
        return self.round_number == 1
    
    def vars_for_template(self):
        r = self.round_number
        return {'round':r}

class Notif(Page):
    def is_displayed(self):
        return self.round_number == 1
    pass

class Ambilwaktu(Page):
    form_model = 'player'
    form_fields = ['waktu']
    
    def before_next_page(self):
        waktu = self.player.waktu
        self.participant.vars['waktu'] = waktu
        if waktu == 30:
            self.participant.vars['base_omset'] = 8000000
            self.participant.vars['base_biaya'] = 30
        elif waktu == 45:
            self.participant.vars['base_omset'] = 6500000
            self.participant.vars['base_biaya'] = 45
        elif waktu == 60:
            self.participant.vars['base_omset'] = 5500000
            self.participant.vars['base_biaya'] = 50
        else:
            self.participant.vars['base_omset'] = 0
            self.participant.vars['base_biaya'] = 0
    
    def vars_for_template(self):
        r = self.round_number
        return {'round':r}

class Maingame(Page):
    form_model = 'player'
    form_fields = ['performance', 'mistakes', 'total_omset', 'total_biaya']
    #if Constants.use_timeout:
    #    #timeout_seconds = Constants.seconds_per_period
    
    def get_timeout_seconds(player):
        waktu = player.participant.vars['waktu']
        return waktu
    
    def vars_for_template(self):
        legend_list = [j for j in range(26)]
        task_list = [j for j in range(Constants.letters_per_word)]
        task_width = 90/Constants.letters_per_word
        r = self.round_number
        return{'legend_list': legend_list,
               'task_list': task_list,
               'task_width': task_width,
               'round':r}

class Hasil(Page):
    def vars_for_template(self):
        r = self.round_number
        return {'round':r}

class Laporpajak(Page):
    form_model = 'player'
    form_fields = ['omset_input','prefill_persen','payoff_awal']

    def get_timeout_seconds(player):
        waktu = 60
        return waktu

    def vars_for_template(self):
        r = self.round_number
        treatment = self.session.config['treatment']
        return {'round':r,
                'treatment':treatment}

    def before_next_page(self):
        self.participant.vars['payoff_awal_'+ str(self.round_number)] = self.player.payoff_awal
        self.participant.vars['total_payoff_'+ str(self.round_number)] = self.player.payoff_awal

#randomlist 3 dari 0 s.d. 10
class Periksapajak(Page):
    form_model = 'player'
    form_fields = ['total_payoff']

    def is_displayed(self):
        r = list()
        for x in range(Constants.num_audit):
            r.append(self.participant.vars['rand_audit_'+ str(x+1)])
        
        if (self.round_number in r):
            return True
        else:
            return False
        #r_1 = self.participant.vars['rand_audit_1']
        #r_2 = self.participant.vars['rand_audit_2']
        #r_3 = self.participant.vars['rand_audit_3']
        # if (self.round_number == r_1):
        #     return True
        # elif (self.round_number == r_2):
        #     return True
        # elif (self.round_number == r_3):
        #     return True
        # else:
        #     return False

    def before_next_page(self):
        self.participant.vars['total_payoff_'+ str(self.round_number)] = self.player.total_payoff

    def vars_for_template(self):
        r = self.round_number
        return {'round':r}
    


page_sequence = [Awal, Notif, Ambilwaktu, Maingame, Hasil, Laporpajak, Periksapajak]
#page_sequence = [Awal, Notif, Ambilwaktu, Periksapajak]
