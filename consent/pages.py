from otree.api import Currency as c, currency_range
from ._builtin import Page, WaitPage
from .models import Constants


class Consent(Page):
    form_model = 'player'
    form_fields = ['consent']
    def error_message(player, values):
        solution = dict(
          consent=True
                  )
        error_messages = dict()
        for field_name in solution:
                if values [field_name] != solution[field_name]:
                    error_messages[field_name] = 'Anda tidak dapat melanjutkan karena pilihan anda Tidak. Silahkan keluar dari website ini jika tidak ingin berpartisipasi.'
        return error_messages

page_sequence = [Consent]
