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
Consent
"""


class Constants(BaseConstants):
    name_in_url = 'Consent'
    players_per_group = None
    num_rounds = 1

    header = "Kontak Peneliti (Rizal) <a href='http://wa.me/628569041762' target='_blank'>http://wa.me/628569041762</a>"


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    #email = models.StringField(blank=False)
    consent = models.BooleanField(choices=[[True, 'Ya'], [False, 'Tidak']])
