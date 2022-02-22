from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)

doc = """
Instruction
"""


class Constants(BaseConstants):
    players_per_group = None
    num_rounds = 3
    name_in_url = 'instruction'

    letters_per_word = 1

    use_timeout = True
    seconds_per_period = 60

class Subsession(BaseSubsession):
    pass
    # dictionary = models.StringField()

    # def creating_session(self):
    #     # Create dictionary
    #     letters = list(string.ascii_uppercase)
    #     random.shuffle(letters)
    #     numbers = []
    #     N = list(range(100, 1000))
    #     for i in range(27):
    #         choice = random.choice(N)
    #         N.remove(choice)
    #         numbers.append(choice)
    #     d = [letters, numbers]
    #     dictionary = dict([(d[0][i], d[1][i]) for i in range(26)])
    #     self.dictionary = json.dumps(dictionary)

class Group(BaseGroup):
    pass

class Player(BasePlayer):
    q1 = models.IntegerField(choices=[[1,'Indonesia'],[2,'Nusa Makmur']], label='Nama negara')
    q2 = models.IntegerField(choices=[[1,'Tidak Wajib'],[2,'Wajib']], label='Apakah wajib membayar pajak')
    q3 = models.IntegerField(choices=[[1,'10 Periode'],[2,'12 Periode']], label='Anda harus melaporkan pajak dalam berapa periode?')
    q4 = models.IntegerField(choices=[[1,'Laba (Rugi)'],[2,'Omset']], label='Dasar pengenaan pajak')
    q5 = models.IntegerField(choices=[[1,'Tidak ada'],[2,'Ada, dari 2% ke 1% dari Laba'],[3,'Ada, dari 1%; ke 0,5% dari Laba'],[4,'Ada, dari 1% ke 0,5% dari Omset']], label='Apakah ada penurunan tarif, berapa nilainya?')
    q6 = models.IntegerField(choices=[[1,'a'],[2,'b'],[3,'c'],[4,'d']], label='Pilih penghitungan pajak yang tepat (Anda dapat menggunakan kalkulator)<br><img src="https://i.ibb.co/BPmT7cp/2022-02-21-195502.png" alt="2022-02-21-195502" border="0"><br>')
    q7 = models.IntegerField(choices=[[1,'30% dari total pelaporan, yaitu 3 dari 10 periode pelaporan pajak'],[2,'probabilitias 10% s.d 50% pada akhir setiap periode pelaporan pajak']], label='Berapa probabilitas pemeriksaan yang dilakukan oleh Nusa Makmur?')
    q8 = models.IntegerField(choices=[[1,'sebesar 100% dari selisih pajak yang kurang dibayar'],[2,'sebesar 200% dari selisih pajak yang kurang dibayar'],[3,'sebesar 300% dari selisih pajak yang kurang dibayar']], label='Besar total denda jika terdapat pajak yang masing kurang dibayar?')
    q9 = models.IntegerField(choices=[[1,'a'],[2,'b'],[3,'c']], label='Jika Anda menjadi petugas pemeriksa pajak, pilih hitungan denda yang tepat (Anda dapat menggunakan kalkulator)<br><img src="https://i.ibb.co/thYj5CN/2022-02-21-195538.png" alt="2022-02-21-195538" border="0"><br>')
    performance = models.IntegerField(initial=0, blank=False)
    mistakes = models.IntegerField(initial=0, blank=False)
    waktu = models.IntegerField(widget=widgets.RadioSelect, label='Waktu', choices=[[30,'30 Menit'],[45,'45 Menit'],[60,'60 Menit']])
    total_omset = models.FloatField(initial=0, blank=False)
    total_biaya = models.FloatField(initial=0, blank=False)
    omset_input = models.FloatField(initial=0, blank=False)
    total_payoff = models.FloatField(initial=0, blank=False)