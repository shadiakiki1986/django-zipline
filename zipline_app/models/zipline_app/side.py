BUY = 'B'
SELL = 'S'
FILL_SIDE_CHOICES = (
  (BUY, 'Buy'),
  (SELL, 'Sell')
)

# Django docs: writing validators
# https://docs.djangoproject.com/en/1.10/ref/validators/#writing-validators
from django.core.exceptions import ValidationError
from django.utils.translation import ugettext_lazy as _
from django.forms import fields
from django.db import models

def validate_nonzero(value):
    if value == 0:
        raise ValidationError(
            _('Quantity %(value)s is not allowed'),
            params={'value': value},
        )

# Inspired by django.forms.fields.py#FloatField
class PositiveFloatFieldForm(fields.FloatField):
  default_error_messages = {
    'invalid': _('Enter a positive number.'),
  }
  def validate(self, value):
    super(PositiveFloatFieldForm, self).validate(value)
    if value is None:
      return value
    if value<0:
      raise ValidationError(self.error_messages['invalid'], code='invalid')
    return value

  def widget_attrs(self, widget):
    attrs = super(PositiveFloatFieldForm, self).widget_attrs(widget)
    attrs['min']=0
    return attrs

# order type
MARKET = 'M'
LIMIT = 'L'
ORDER_TYPE_CHOICES = (
  (MARKET, 'Market'),
  (LIMIT, 'Limit')
)

class PositiveFloatFieldModel(models.FloatField):
  def formfield(self, **kwargs):
    defaults = {'form_class': PositiveFloatFieldForm}
    defaults.update(kwargs)
    return super(PositiveFloatFieldModel, self).formfield(**defaults)

# order status
# https://github.com/quantopian/zipline/blob/master/zipline/finance/order.py#L24
OPEN = 'O'
FILLED = 'F'
CANCELLED = 'C'
REJECTED = 'R'
HELD = 'H'
ORDER_STATUS_CHOICES = (
  (OPEN, 'Open'),
  (FILLED, 'Filled'),
  (CANCELLED, 'Cancelled'),
  (REJECTED, 'Rejected'),
  (HELD, 'Held'),
)

# order validity
GTC = 'C'
GTD = 'D'
DAY = '-'
ORDER_VALIDITY_CHOICES = (
  (GTC, 'GTC order'),
  (GTD, 'GTD order'),
  (DAY, 'Day order'),
)
