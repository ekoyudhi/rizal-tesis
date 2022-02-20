from ._builtin import Page, WaitPage
from .models import Constants, Player, Group

class Welcome(Page):
    pass

class Pengantar(Page):
    #pass
    form_model = 'player'
    form_fields = ['q1','q2','q3','q4','q5','q6','q7','q8']

    def error_message(player, values):
        solutions = dict(q1=1,q2=1,q3=1,q4=1,q5=1,q6=1,q7=1,q8=1)
        error_messages= dict()
        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Jawaban Salah'
        return error_messages

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

class Lapor(Page):
    #pass
    form_model = 'player'
    form_fields = ['omset_input']

class Post(Page):
    pass

page_sequence = [Welcome, Pengantar, Pre, Task, Results, Lapor, Post]
