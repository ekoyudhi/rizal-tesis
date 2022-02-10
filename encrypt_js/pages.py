from ._builtin import Page, WaitPage
from .models import Constants, Player, Group

class Pre(Page):
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
        return{'legend_list': legend_list,
               'task_list': task_list,
               'task_width': task_width}

class Results(Page):
    pass

page_sequence = [Pre,
                 Task,
                 Results]
