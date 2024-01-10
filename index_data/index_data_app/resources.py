from .models import Nifty50, NiftyMidcap150, NiftyNext50, NiftyMidcap50, NiftySmallcap50
from import_export import resources, fields
from import_export.widgets import DateWidget, IntegerWidget, FloatWidget


class Nifty50Resource(resources.ModelResource):
    date = fields.Field(attribute='date', column_name='Date', widget=DateWidget(format='%d-%b-%Y'))
    open_ = fields.Field(attribute='open', column_name='Open', widget=FloatWidget())
    high = fields.Field(attribute='high', column_name='High', widget=FloatWidget())
    low = fields.Field(attribute='low', column_name='Low', widget=FloatWidget())
    close = fields.Field(attribute='close', column_name='Close', widget=FloatWidget())
    shares_traded = fields.Field(attribute='shares_traded', column_name='Shares Traded', widget=IntegerWidget())
    turnover = fields.Field(attribute='turnover', column_name='Turnover (₹ Cr)', widget=FloatWidget())

    class Meta:
        model = Nifty50
        import_id_fields = []
        fields = ("date", 'open_', "high", "low", 'close', "shares_traded", "turnover")


class NiftyMidcap150Resource(resources.ModelResource):
    date = fields.Field(attribute='date', column_name='Date', widget=DateWidget(format='%d-%b-%Y'))
    open_ = fields.Field(attribute='open', column_name='Open', widget=FloatWidget())
    high = fields.Field(attribute='high', column_name='High', widget=FloatWidget())
    low = fields.Field(attribute='low', column_name='Low', widget=FloatWidget())
    close = fields.Field(attribute='close', column_name='Close', widget=FloatWidget())
    shares_traded = fields.Field(attribute='shares_traded', column_name='Shares Traded', widget=IntegerWidget())
    turnover = fields.Field(attribute='turnover', column_name='Turnover (₹ Cr)', widget=FloatWidget())

    class Meta:
        model = NiftyMidcap150
        import_id_fields = []
        fields = ("date", 'open_', "high", "low", 'close', "shares_traded", "turnover")


class NiftyNext50Resource(resources.ModelResource):
    date = fields.Field(attribute='date', column_name='Date', widget=DateWidget(format='%d-%b-%Y'))
    open_ = fields.Field(attribute='open', column_name='Open', widget=FloatWidget())
    high = fields.Field(attribute='high', column_name='High', widget=FloatWidget())
    low = fields.Field(attribute='low', column_name='Low', widget=FloatWidget())
    close = fields.Field(attribute='close', column_name='Close', widget=FloatWidget())
    shares_traded = fields.Field(attribute='shares_traded', column_name='Shares Traded', widget=IntegerWidget())
    turnover = fields.Field(attribute='turnover', column_name='Turnover (₹ Cr)', widget=FloatWidget())

    class Meta:
        model = NiftyNext50
        import_id_fields = []
        fields = ("date", 'open_', "high", "low", 'close', "shares_traded", "turnover")


class NiftyMidcap50Resource(resources.ModelResource):
    date = fields.Field(attribute='date', column_name='Date', widget=DateWidget(format='%d-%b-%Y'))
    open_ = fields.Field(attribute='open', column_name='Open', widget=FloatWidget())
    high = fields.Field(attribute='high', column_name='High', widget=FloatWidget())
    low = fields.Field(attribute='low', column_name='Low', widget=FloatWidget())
    close = fields.Field(attribute='close', column_name='Close', widget=FloatWidget())
    shares_traded = fields.Field(attribute='shares_traded', column_name='Shares Traded', widget=IntegerWidget())
    turnover = fields.Field(attribute='turnover', column_name='Turnover (₹ Cr)', widget=FloatWidget())

    class Meta:
        model = NiftyMidcap50
        import_id_fields = []
        fields = ("date", 'open_', "high", "low", 'close', "shares_traded", "turnover")


class NiftySmallcap50Resource(resources.ModelResource):
    date = fields.Field(attribute='date', column_name='Date', widget=DateWidget(format='%d-%b-%Y'))
    open_ = fields.Field(attribute='open', column_name='Open', widget=FloatWidget())
    high = fields.Field(attribute='high', column_name='High', widget=FloatWidget())
    low = fields.Field(attribute='low', column_name='Low', widget=FloatWidget())
    close = fields.Field(attribute='close', column_name='Close', widget=FloatWidget())
    shares_traded = fields.Field(attribute='shares_traded', column_name='Shares Traded', widget=IntegerWidget())
    turnover = fields.Field(attribute='turnover', column_name='Turnover (₹ Cr)', widget=FloatWidget())

    class Meta:
        model = NiftySmallcap50
        import_id_fields = []
        fields = ("date", 'open_', "high", "low", 'close', "shares_traded", "turnover")
