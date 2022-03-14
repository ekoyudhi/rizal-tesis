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


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    email = models.StringField(blank=False)
    consent = models.BooleanField(choices=[[True, 'Ya'], [False, 'Tidak']])
