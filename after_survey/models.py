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
    name_in_url = 'AfterSurvey'
    players_per_group = None
    num_rounds = 1

    header = "Kontak Peneliti (Rizal) <a href='http://wa.me/628569041762' target='_blank'>http://wa.me/628569041762</a>"

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    s1 = models.IntegerField(choices=[[1,"Ya, bekerja sebagai Wirausahawan"],[2,"Ya, bekerja sebagai Pekerja Paruh Waktu"],[3,"Ya, bekerja sebagai Pegawai Tetap"],[4,"Belum pernah bekerja"]], label="1) Apakah Anda pernah/sedang bekerja ?")
    s2 = models.IntegerField(choices=[[1,"0 – 3 tahun"],[2,"3 – 6 tahun"],[3,"Lebih dari 6 tahun"]], label="2) Berapa lama masa pengalaman kerja Anda?")
    s3 = models.IntegerField(choices=[[1,"Sudah punya"],[2,"Belum punya"]], label="3) Apakah Sudah memiliki NPWP?")
    s4 = models.IntegerField(choices=[[1,"Tidak Berminat"],[2,"Cukup Berminat"],[3,"Berminat"],[4,"Sangat Berminat"]], label="4) Jika belum, seberapa ingin Anda memiliki NPWP", blank=True)
    s5 = models.IntegerField(choices=[[1,"Belum pernah"],[2,"Sudah pernah"]], label="5) Jika sudah punya, apakah pernah Lapor SPT?", blank=True)
    s6 = models.IntegerField(choices=[[1,"Kurang dari 10%"],[2,"20%"],[3,"30%"],[4,"40%"],[5,"50%"],[6,"Lebih dari 50%"]], label="6) Menurut Anda, berapa besar probabilitas dari kemungkinan diperiksa yang Anda rasakan dalam game ini?")
    s7 = models.IntegerField(choices=[[1,"Tidak Adil"],[2,"Cukup Adil"],[3,"Adil"],[4,"Sangat Adil"]], label="7) Seberapa adilkah penghitungan pajak dalam penelitian ini? (tarif pajak dikali dengan omset, bukan dikali laba)")
    s8 = models.IntegerField(choices=[[1,"Tidak Mudah"],[2,"Cukup Mudah"],[3,"Mudah"],[4,"Sangat Mudah"]], label="8) Seberapa mudahkah penghitungan pajak dalam penelitian ini?")
    s9 = models.IntegerField(choices=[[1,"Tidak Setuju"],[2,"Cukup Setuju"],[3,"Setuju"],[4,"Sangat Setuju"]], label="9) Seberapa setuju Anda dengan penurunan tarif dari 20% ke 10% di negara Nusa Makmur?")
    s10 = models.IntegerField(choices=[[1,"Tidak Percaya"],[2,"Cukup Percaya"],[3,"Percaya"],[4,"Sangat Percaya"]], label="10) Seberapa besar kepercayaan Anda terhadap otoritas pajak Nusa Makmur terkait dengan perhitungan estimasi prefilled omset yang diterapkan dalam form pelaporan pajak?", blank=True)
    s11 = models.IntegerField(choices=[[1,"Tidak Perlu"],[2,"Cukup Perlu"],[3,"Perlu"],[4,"Sangat Perlu"]], label="11) Seberapa perlukah penerapan prefilled omset dalam form pelaporan pajak?", blank=True)

    t11 = models.IntegerField(label="1) Umur")
    t12 = models.IntegerField(choices=[[1,'Laki-laki'],[2,'Perempuan']], label='2) Jenis Kelamin')
    t13 = models.IntegerField(choices=[[1,'Diploma 3 (D3)'],[2,'Sarjana (S1/D4)'],[3,'Magister (S2)'],[4,'Doktoral (S3)']], label='3) Tingkat pendidikan yang sedang berlangsung')
    t14 = models.StringField(label="4) Fakultas")
    t15 = models.StringField(label="5) Program Studi")
    t16 = models.IntegerField(choices=[[1,'Di bawah 1 juta'],[2,'1 juta s.d 2,5 juta'],[3,'2,5 jt s.d 5 jt'],[4,'di atas 5 jt']], label='6) Range Biaya Hidup/Uang Saku per bulan')
    t17 = models.StringField(label="7) Nomor HP OVO/GOPAY")
    t18 = models.IntegerField(choices=[[1,'OVO'],[2,'Gopay']], label='8) Metode penerimaan yang diinginkan:')
    t19 = models.IntegerField(choices=[[1,"Tidak Menarik"],[2,"Cukup Menarik"],[3,"Menarik"],[4,"Sangat Menarik"]], label="9) Seberapa menariknya eksperimen ini bagi Anda?")
    
    angka_random = models.IntegerField(min=11, max=99, label="2 digit angka")
    periode_terpilih = models.IntegerField(initial=0, blank=False)
    payoff_real = models.FloatField(initial=0, blank=False)

