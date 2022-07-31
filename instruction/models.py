from tokenize import blank_re
from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)

doc = """
Instruction
"""


class Constants(BaseConstants):
    players_per_group = None
    num_rounds = 3
    name_in_url = 'Instruction'

    letters_per_word = 1

    use_timeout = True
    seconds_per_period = 60
    tarif_pajak = 0.1

    header = "Kontak Peneliti (Rizal) <a href='http://wa.me/628569041762' target='_blank'>http://wa.me/628569041762</a>"

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
    q1 = models.IntegerField(choices=[[1,'Nusa Jaya'],[2,'Nusa Makmur']], label='1) Anda adalah warga negara?')
    q2 = models.IntegerField(choices=[[1,'Mencatat dan membayar pajak'],[2,'Membayar dan melaporkan pajak'],[3,'Mencatat dan membayar pajak'],[4,'Mencatat, membayar, dan melaporkan pajak']], label='2)	Kewajiban setiap warga negara Nusa Makmur yang memiliki usaha adalah?')
    q3 = models.IntegerField(choices=[[1,'15 Periode'],[2,'12 Periode']], label='3) Anda harus melaporkan pajak dalam berapa periode?')
    q4 = models.IntegerField(choices=[[1,'Laba (Rugi)'],[2,'Omset']], label='4)	Nilai pajak dihitung dari?(Dasar pengenaan Pajak)')
    q5 = models.IntegerField(choices=[[1,'Tidak ada'],[2,'Ada, dari 20% ke 10% dari Laba'],[3,'Ada, dari 10% ke 5% dari Laba'],[4,'Ada, dari 20% ke 10% dari Omset']], label='5) Apakah ada penurunan tarif, berapa nilainya?')
    q6 = models.IntegerField(choices=[[1,'a'],[2,'b'],[3,'c'],[4,'d']], label='6) Pilih penghitungan pajak dan pendapatan bersih yang paling tepat (Anda dapat menggunakan kalkulator)<br><img src="https://i.ibb.co/Kh4QQq1/tb1.jpg" alt="2022-02-21-195502" border="0" width="600" height="200"><br>Pilih jawaban di bawah')
    q7 = models.IntegerField(choices=[[1,'Tidak diketahui'],[2,'20% s.d 40% dari total seluruh wajib pajak Nusa Makmur'],[3,'20% s.d 40% dari total seluruh periode pelaporan pajak'],[4,'20% s.d. 40% untuk masing-masing subjek pada setiap pelaporan pajaknya']], label='7) Berapa probabilitas pemeriksaan yang dilakukan oleh Nusa Makmur?')
    q8 = models.IntegerField(choices=[[1,'sebesar 100% dari selisih pajak yang kurang dibayar'],[2,'sebesar 200% dari selisih pajak yang kurang dibayar'],[3,'sebesar 300% dari selisih pajak yang kurang dibayar']], label='8) Besar total denda jika terdapat pajak yang masing kurang dibayar?')
    q9 = models.IntegerField(choices=[[1,'a'],[2,'b'],[3,'c']], label='9)	Jika Anda menjadi petugas pemeriksa pajak, pilih hitungan denda yang tepat (Anda dapat menggunakan kalkulator)<br><img src="https://i.ibb.co/Sm21jsh/tb2.jpg" alt="2022-02-21-195538" border="0" width="600" height="400"><br>Pilih jawaban di bawah')
    performance = models.IntegerField(initial=0, blank=False)
    waktu = models.IntegerField(widget=widgets.RadioSelect, label='Waktu', choices=[[30,'30 detik'],[45,'45 detik'],[60,'60 detik']])
    total_omset = models.FloatField(initial=0, blank=False)
    total_biaya = models.FloatField(initial=0, blank=False)
    omset_input = models.FloatField(initial=0, blank=False)
    total_payoff = models.FloatField(initial=0, blank=False)