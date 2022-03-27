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

from os import environ

doc = """
Main Game
"""


class Constants(BaseConstants):
    name_in_url = 'Game'
    players_per_group = None
    num_rounds = 15
    num_audit = 3
    num_audit_max = 6

    letters_per_word = 1

    use_timeout = True
    seconds_per_period = 60
    tarif_pajak = 0.1
    header = "Kontak Peneliti (Rizal) <a href='http://wa.me/628569041762' target='_blank'>http://wa.me/628569041762</a>"

class Subsession(BaseSubsession):
    pass

class Group(BaseGroup):
    pass


class Player(BasePlayer):
    prefill_persen = models.FloatField(initial=0, blank=False)
    performance = models.IntegerField(initial=0, blank=False)
    waktu = models.IntegerField(widget=widgets.RadioSelect, label='Waktu', choices=[[30,'30 detik'],[45,'45 detik'],[60,'60 detik']])
    total_omset = models.FloatField(initial=0, blank=False)
    total_biaya = models.FloatField(initial=0, blank=False)
    omset_input = models.FloatField(initial=0, blank=False)
    payoff_awal = models.FloatField(initial=0, blank=False)
    audit = models.StringField(blank=True)
    denda = models.FloatField(initial=0, blank=True)
    restitusi = models.FloatField(initial=0, blank=True)
    total_payoff = models.FloatField(initial=0, blank=False)
