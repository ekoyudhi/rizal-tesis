from otree.api import Currency as c, currency_range
from ._builtin import Page
from .models import Constants

class Pengantar(Page):
    #pass
    def is_displayed(self):
        return self.round_number == 1
    
    form_model = 'player'
    form_fields = ['q1','q2','q3','q4','q5','q6','q7','q8','q9']

    def error_message(player, values):
        solutions = dict(q1=2,q2=2,q3=1,q4=1,q5=4,q6=2,q7=1,q8=2,q9=3)
        error_messages= dict()
        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Jawaban Salah'
        return error_messages

class Persiapan(Page):
    def is_displayed(self):
        return self.round_number == 1

class Pilihwaktu(Page):
    #pass
    form_model = 'player'
    form_fields = ['waktu']
    
    def before_next_page(self):
        waktu = self.player.waktu
        self.participant.vars['waktu'] = waktu
        if waktu == 30:
            self.participant.vars['base_omset'] = 10000000
            self.participant.vars['base_biaya'] = 30
        elif waktu == 45:
            self.participant.vars['base_omset'] = 5000000
            self.participant.vars['base_biaya'] = 45
        elif waktu == 60:
            self.participant.vars['base_omset'] = 2000000
            self.participant.vars['base_biaya'] = 60
        else:
            self.participant.vars['base_omset'] = 0
            self.participant.vars['base_biaya'] = 0
    
    def vars_for_template(self):
        r = self.round_number
        return {'round':r}
    
class Task(Page):
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

class Results(Page):
    #pass
    def vars_for_template(self):
        r = self.round_number
        return {'round':r}

class Lapor(Page):
    #pass
    form_model = 'player'
    form_fields = ['omset_input']

    def vars_for_template(self):
        r = self.round_number
        return {'round':r}

class Akhir(Page):
    def is_displayed(self):
        return self.round_number == 3


page_sequence = [Pengantar, Persiapan, Pilihwaktu, Task, Results, Lapor, Akhir]
