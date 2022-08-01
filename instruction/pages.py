from otree.api import Currency as c, currency_range
from ._builtin import Page
from .models import Constants

class Instruksi1(Page):
    def is_displayed(self):
        return self.round_number == 1

class Instruksi2(Page):
    def is_displayed(self):
        return self.round_number == 1
    
    def vars_for_template(self):
        return {
            'image_1': 'images/image_1.jpg',
            'image_2': 'images/image_2.jpg',
            'image_3': 'images/image_3.jpg',
            'image_4': 'images/image_4.jpg',
        }

class Instruksi3(Page):
    def is_displayed(self):
        return self.round_number == 1
    
    def vars_for_template(self):
        return {
            'image_5': 'images/image_5.jpg'
        }

class Instruksi4(Page):
    def is_displayed(self):
        return self.round_number == 1
    
    def vars_for_template(self):
        return {
            'image_6': 'images/image_6.jpg'
        }

class Instruksi5(Page):
    def is_displayed(self):
        return self.round_number == 1
    
    def vars_for_template(self):
        return {
            'image_7': 'images/image_7.jpg'
        }

class Instruksi6(Page):
    def is_displayed(self):
        return self.round_number == 1
    
    def vars_for_template(self):
        return {
            'image_8': 'images/image_8.jpg',
            'image_9': 'images/image_9.jpg',
            'image_10': 'images/image_10.jpg',
            'image_11': 'images/image_11.jpg',
            'image_11_2': 'images/image_11_2.jpg',
            'image_12': 'images/image_12.jpg',
            'image_13': 'images/image_13.jpg',
        }

class Instruksi7(Page):
    def is_displayed(self):
        return self.round_number == 1
    
    def vars_for_template(self):
        return {
            'instruksi': 'files/instruksi.pdf'
        }

class Pengantar(Page):
    #pass
    def is_displayed(self):
        return self.round_number == 1
    
    form_model = 'player'
    form_fields = ['q1','q2','q3','q4','q5','q6','q7','q8','q9']

    def error_message(player, values):
        solutions = dict(q1=2,q2=4,q3=1,q4=2,q5=4,q6=2,q7=4,q8=2,q9=3)
        error_messages= dict()
        for field_name in solutions:
            if values[field_name] != solutions[field_name]:
                error_messages[field_name] = 'Jawaban Salah'
        return error_messages

class Persiapan(Page):
    def vars_for_template(self):
        r = self.round_number
        return {'round':r,
                'tarif_pajak': Constants.tarif_pajak}

class Pilihwaktu(Page):
    #pass
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
        return {'round':r,
                'tarif_pajak': Constants.tarif_pajak}
    
class Task(Page):
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

class Results(Page):
    #pass
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

class Lapor(Page):
    #pass
    form_model = 'player'
    form_fields = ['omset_input']

    def vars_for_template(self):
        r = self.round_number
        wait_seconds = self.session.config['wait_seconds']
        return {'round':r,
                'tarif_pajak': Constants.tarif_pajak,
                'wait_seconds': wait_seconds}

class Akhir(Page):
    def is_displayed(self):
        return self.round_number == Constants.num_rounds

class Tandaterima(Page):
    def vars_for_template(self):
        r = self.round_number
        omset = self.player.omset_input
        pph = Constants.tarif_pajak * omset
        return {'round':r,
                'tarif_pajak': Constants.tarif_pajak,
                'omset':omset,
                'pph':pph}


page_sequence = [Instruksi1, 
                Instruksi2, 
                Instruksi3, 
                Instruksi4, 
                Instruksi5, 
                Instruksi6,
                Instruksi7,
                Pengantar, 
                Persiapan, 
                Pilihwaktu, 
                Task, 
                Results, 
                Lapor,
                Tandaterima,
                Akhir]
