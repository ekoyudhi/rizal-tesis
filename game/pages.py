from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants
import random

class Awal(Page):
    def before_next_page(self):
        if self.round_number == 1:
            self.participant.vars['periode'] = Constants.num_rounds
            b1= [1,2,3]
            b2= [4,5,6]
            b3= [7,8,9]
            b4= [10,11,12]
            b5= [13,14,15]
            lst_r = [b1,b2,b3,b4,b5]
            x = random.randint(Constants.num_audit,Constants.num_audit_max)
            r_list = []
            # if x <= len(lst_r):
            #     r_l = random.sample(range(1,6),x)
            #     for i in r_l:
            #         r_list.append(lst_r[i-1][random.randint(0,2)])
            # else:
            #     r_l = random.sample(range(1,6),5)
            #     for i in r_l:
            #         r_list.append(lst_r[i-1][random.randint(0,2)])
            #     loop = True
            #     while(loop):
            #         s = random.randint(1,15)
            #         if s not in r_list:
            #             r_list.append(s)
            #             if len(r_list) == x:
            #                 loop = False
            for n in range(1, Constants.num_rounds+1):
                rnd = random.randint(20,40)
                rnd1 = random.randint(1,100)
                if rnd1 <= rnd:
                    r_list.append(n)
            #r_list = random.sample(range(1,Constants.num_rounds+1),Constants.num_audit)
            r_list.sort()
            self.participant.vars['audit'] = r_list
            idx = 1
            for r in r_list:
                self.participant.vars['rand_audit_'+str(idx)] = r
                idx+=1
                #self.participant.vars['rand_audit_2'] = r_list[1]
                #self.participant.vars['rand_audit_3'] = r_list[2]
            #t_4 = random.sample([1,1,1,1,1,2,2,2,2,2,3,3,3,3,3],15)
            t_4 = random.choices([1,2,3], k = Constants.num_rounds)
            self.participant.vars['treatment_4'] =  t_4

    # def is_displayed(self):
    #     return self.round_number == 1
    
    def vars_for_template(self):
        r = self.round_number
        return {'round':r}

class Notif(Page):
    def is_displayed(self):
        treatment = self.session.config['treatment']
        displayed = False
        if treatment == 0:
            displayed = False
        else:
            if self.round_number == 1:
                displayed = True
            else:
                displayed = False
        
        return displayed
    
    def vars_for_template(self):
        wait_seconds = self.session.config['wait_seconds']
        return {'wait_seconds': wait_seconds,
                'image_14_prefilled': 'images/image_14_prefilled.jpg'}

class Ambilwaktu(Page):
    form_model = 'player'
    form_fields = ['waktu']
    
    def before_next_page(self):
        waktu = self.player.waktu
        self.participant.vars['waktu'] = waktu
        if waktu == 30:
            self.participant.vars['base_omset'] = 7500000
            self.participant.vars['base_biaya'] = 30
        elif waktu == 45:
            self.participant.vars['base_omset'] = 6500000
            self.participant.vars['base_biaya'] = 45
        elif waktu == 60:
            self.participant.vars['base_omset'] = 5500000
            self.participant.vars['base_biaya'] = 60
        else:
            self.participant.vars['base_omset'] = 0
            self.participant.vars['base_biaya'] = 0
    
    def vars_for_template(self):
        r = self.round_number
        au = self.participant.vars['audit']
        return {'round':r,
                'audit':au,
                'tarif_pajak': Constants.tarif_pajak}

class Maingame(Page):
    form_model = 'player'
    form_fields = ['performance', 'total_omset', 'total_biaya']
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
               'round':r,
               'tarif_pajak': Constants.tarif_pajak}

class Hasil(Page):
    def vars_for_template(self):
        r = self.round_number
        base_omset = self.participant.vars['base_omset']
        base_biaya = self.participant.vars['base_biaya']
        wait_seconds = self.session.config['wait_seconds']
        return {'round':r,
                'base_omset': base_omset,
                'base_biaya': base_biaya,
                'tarif_pajak': Constants.tarif_pajak,
                'wait_seconds': wait_seconds}
    
    def before_next_page(self):
        treatment = self.session.config['treatment']
        def get_prefilled(treatment):
            if treatment == 0:
                prefilled_persen = 0
            elif treatment == 1:
                prefilled_persen = random.randint(25,99)
            elif treatment == 2:
                prefilled_persen = 100
            elif treatment == 3:
                prefilled_persen = random.randint(101,175)
            return prefilled_persen

        if treatment == 4:
            t_4 = self.participant.vars['treatment_4']
            prefilled_persen = get_prefilled(t_4[self.round_number-1])
        else:
            prefilled_persen = get_prefilled(treatment)
        
        prefilled_omset = round(prefilled_persen / 100 * self.player.total_omset, -3)

        self.participant.vars['prefill_persen'] = prefilled_persen
        self.participant.vars['prefill_omset'] = prefilled_omset
        self.player.prefill_persen = prefilled_persen

class Laporpajak(Page):
    form_model = 'player'
    form_fields = ['omset_input','payoff_awal']

    # def get_timeout_seconds(player):
    #     waktu = 60
    #     return waktu
        
    def vars_for_template(self):
        r = self.round_number
        treatment = self.session.config['treatment']
        prefilled_omset = self.participant.vars['prefill_omset']
        wait_seconds = self.session.config['wait_seconds']
        return {'round':r,
                'treatment':treatment,
                'tarif_pajak': Constants.tarif_pajak,
                'prefilled_omset': prefilled_omset,
                'wait_seconds': wait_seconds}

    def before_next_page(self):
        self.participant.vars['payoff_awal_'+ str(self.round_number)] = self.player.payoff_awal
        self.participant.vars['total_payoff_'+ str(self.round_number)] = self.player.payoff_awal

#randomlist 3 dari 0 s.d. 10
class Periksapajak(Page):
    form_model = 'player'
    form_fields = ['total_payoff', 'audit', 'restitusi', 'denda']

    def is_displayed(self):
        r = list()
        num_audit = len(self.participant.vars['audit'])
        for x in range(num_audit):
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
        wait_seconds = self.session.config['wait_seconds']
        return {'round':r,
                'tarif_pajak': Constants.tarif_pajak,
                'audit': 'ya',
                'wait_seconds': wait_seconds}

class Tandaterima(Page):
    def vars_for_template(self):
        r = self.round_number
        omset = self.player.omset_input
        pph = Constants.tarif_pajak * omset
        return {'round':r,
                'tarif_pajak': Constants.tarif_pajak,
                'omset':omset,
                'pph':pph}


page_sequence = [Notif, Awal, Ambilwaktu, Maingame, Hasil, Laporpajak, Tandaterima, Periksapajak]
#page_sequence = [Awal, Notif, Ambilwaktu, Periksapajak]
