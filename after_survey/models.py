from hashlib import sha3_384
from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)


doc = """
After Survey
"""


class Constants(BaseConstants):
    name_in_url = 'after_survey'
    players_per_group = None
    num_rounds = 1


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    s1 = models.StringField(label="Nomor HP OVO/GOPAY")
    s2 = models.IntegerField(label="Umur")
    s3 = models.IntegerField(choices=[[1,'Laki-laki'],[2,'Perempuan']], label='Jenis Kelamin')
    s4 = models.StringField(label="Pekerjaan")
    s5 = models.StringField(label="Fakultas")
    s6 = models.IntegerField(choices=[[1,'Di bawah 1 juta'],[2,'1 juta s.d 2,5 juta'],[3,'2,5 jt s.d 5 jt'],[4,'di atas 5 jt']], label='Range Biaya Hidup/Uang Saku per bulan')
    s7 = models.IntegerField(choices=[[1,'Belum punya'],[2,'Sudah punya']], label='Apakah Sudah punya NPWP')
    s8 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6],widget=widgets.RadioSelectHorizontal,label="Jika belum, seberapa ingin Anda memiliki NPWP? Sama sekali tidak berminat <--------------> Ya, saya sangat ingin")
    s9 = models.IntegerField(choices=[[1,'Belum pernah'],[2,'Sudah pernah']], label='Jika sudah punya, apakah pernah Lapor SPT')
    s10 = models.IntegerField(choices=[[1,'10%'],[2,'20%'],[3,'30%'],[4,'40%'],[5,'50%'],[6,'60%'],[7,'70%']], label='Menurut Anda, berapa besar probabilitas dari kemungkinan diperiksa yang Anda rasakan dalam game ini?')
    s11 = models.IntegerField(choices=[1, 2, 3, 4, 5, 6],widget=widgets.RadioSelectHorizontal,label="Seberapa adilkah penghitungan pajak dalam penelitian ini. Sangat tidak adil <---------------> Sangat adil")
    angka_random = models.IntegerField(min=11, max=99, label="2 digit angka")
    periode_terpilih = models.IntegerField(initial=0, blank=False)
    payoff_real = models.FloatField(initial=0, blank=False)

