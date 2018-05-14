# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Analiza(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)

    numerdziewiarnia = models.CharField(db_column='NumerDziewiarnia', max_length=50)
    plany = models.FloatField(db_column='Plany', blank=True, null=True)

    dostawyzaklad = models.FloatField(db_column='DostawyZaklad', blank=True, null=True)

    dostawymagazyn9 = models.FloatField(db_column='DostawyMagazyn9', blank=True, null=True)

    wydaniamagazyn9 = models.FloatField(db_column='WydaniaMagazyn9', blank=True, null=True)

    wydaniageneruj9 = models.FloatField(db_column='WydaniaGeneruj9', blank=True, null=True)

    otwartezlecenia = models.FloatField(db_column='OtwarteZlecenia', blank=True, null=True)

    poczekalnia = models.FloatField(db_column='Poczekalnia', blank=True, null=True)

    birth = models.FloatField(db_column='Birth', blank=True, null=True)
    walk = models.FloatField(db_column='Walk', blank=True, null=True)
    span = models.FloatField(db_column='Span', blank=True, null=True)

    stock = models.FloatField(db_column='Stock', blank=True, null=True)

    data = models.DateTimeField(db_column='Data', blank=True, null=True)

    uzytkownik = models.CharField(db_column='Uzytkownik', max_length=50, blank=True, null=True)

    czas = models.DateTimeField(db_column='Czas', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Analiza'
        unique_together = (('id', 'numerdziewiarnia'),)


class Dzmagazyn(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)

    zaklad = models.CharField(db_column='Zaklad', max_length=50, blank=True, null=True)

    numerdziewiarnia = models.CharField(db_column='NumerDziewiarnia', max_length=50)
    matid = models.CharField(db_column='MatId', max_length=10)
    kolor = models.CharField(max_length=10)

    nazwa = models.CharField(db_column='Nazwa', max_length=50, blank=True, null=True)

    winnobyc = models.FloatField(db_column='WinnoByc', blank=True, null=True)
    jest = models.FloatField(db_column='Jest', blank=True, null=True)
    kw = models.IntegerField(blank=True, null=True)

    uzytkownik = models.CharField(db_column='Uzytkownik', max_length=50, blank=True, null=True)

    czas = models.DateTimeField(db_column='Czas', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Dzmagazyn'
        unique_together = (('id', 'numerdziewiarnia'),)


class Dzrolki(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)

    numerdziewiarnia = models.CharField(db_column='NumerDziewiarnia', max_length=70)

    gestrickt = models.FloatField(db_column='Gestrickt', blank=True, null=True)

    datumstrickerei = models.DateTimeField(db_column='DatumStrickerei', blank=True, null=True)

    qm = models.DecimalField(db_column='QM', max_digits=18, decimal_places=2, blank=True, null=True)

    datumwalkerei = models.DateTimeField(db_column='DatumWalkerei', blank=True, null=True)

    gewicht = models.CharField(db_column='Gewicht', max_length=50, blank=True, null=True)

    werk = models.CharField(db_column='Werk', max_length=2, blank=True, null=True)

    datumwerk = models.DateTimeField(db_column='DatumWerk', blank=True, null=True)

    walkbetrieb = models.CharField(db_column='Walkbetrieb', max_length=50, blank=True, null=True)

    ubergabedatum = models.CharField(db_column='UbergabeDatum',
                                     max_length=50, blank=True, null=True)

    shortkey = models.IntegerField(db_column='ShortKey', blank=True, null=True)
    uk = models.IntegerField(db_column='UK', blank=True, null=True)

    maszyna = models.CharField(db_column='Maszyna', max_length=50, blank=True, null=True)

    userdziewiarnia = models.CharField(
        db_column='UserDziewiarnia', max_length=50, blank=True, null=True)

    userpralnia = models.CharField(db_column='UserPralnia', max_length=50, blank=True, null=True)

    czasstrick = models.CharField(db_column='CzasStrick', max_length=50, blank=True, null=True)

    czaswalk = models.CharField(db_column='CzasWalk', max_length=50, blank=True, null=True)

    welna = models.CharField(db_column='Welna', max_length=45, blank=True, null=True)

    uzytkownik = models.CharField(db_column='Uzytkownik', max_length=50, blank=True, null=True)

    miejsce = models.CharField(db_column='Miejsce', max_length=50, blank=True, null=True)

    datamagiel = models.DateTimeField(db_column='DataMagiel', blank=True, null=True)
    kw = models.IntegerField(db_column='KW', blank=True, null=True)

    usermagiel = models.CharField(db_column='UserMagiel', max_length=50, blank=True, null=True)

    qmmagiel = models.FloatField(db_column='QMMagiel', blank=True, null=True)

    dp = models.DecimalField(db_column='DP', max_digits=15, decimal_places=3, blank=True, null=True)

    szp = models.DecimalField(db_column='SZP', max_digits=15,
                              decimal_places=3, blank=True, null=True)

    ds = models.DecimalField(db_column='DS', max_digits=15, decimal_places=3, blank=True, null=True)

    szs = models.DecimalField(db_column='SZS', max_digits=15,
                              decimal_places=3, blank=True, null=True)

    ump = models.CharField(db_column='UMP', max_length=45, blank=True, null=True)

    ums = models.CharField(db_column='UMS', max_length=45, blank=True, null=True)
    lsp = models.SmallIntegerField(db_column='LSP')
    lsw = models.SmallIntegerField(db_column='LSW')

    czas = models.DateTimeField(db_column='Czas', blank=True, null=True)

    class Meta:
        managed = True
        db_table = 'Dzrolki'
        unique_together = (('id', 'numerdziewiarnia'),)


class Dzplany(models.Model):

    id = models.AutoField(db_column='id', primary_key=True)

    numerdziewiarnia = models.CharField(
        db_column='NumerDziewiarnia', max_length=50)

    matid = models.CharField(db_column='MatId', max_length=10, blank=True, null=True)
    kolor = models.CharField(max_length=10, blank=True, null=True)

    nazwa = models.CharField(db_column='Nazwa', max_length=30, blank=True, null=True)

    ilosc = models.DecimalField(db_column='Ilosc', max_digits=15,
                                decimal_places=3, blank=True, null=True)
    kw = models.IntegerField(db_column='KW', blank=True, null=True)

    dataotrzymania = models.DateTimeField(db_column='DataOtrzymania', blank=True, null=True)

    datawyslania = models.DateTimeField(db_column='DataWyslania', blank=True, null=True)

    uwagi = models.CharField(db_column='Uwagi', max_length=255, blank=True, null=True)

    iloscprzyjeta = models.DecimalField(
        db_column='Iloscprzyjeta', max_digits=15, decimal_places=3, blank=True, null=True)

    jednostka = models.CharField(db_column='Jednostka', max_length=5, blank=True, null=True)

    zakladdocelowy = models.CharField(db_column='ZakladDocelowy',
                                      max_length=2, blank=True, null=True)

    kgstrickstofu = models.DecimalField(
        db_column='KGStrickstofu', max_digits=15, decimal_places=3, blank=True, null=True)

    vorschlagkg = models.DecimalField(
        db_column='VorschlagKg', max_digits=15, decimal_places=3, blank=True, null=True)

    gramy = models.DecimalField(db_column='Gramy', max_digits=15,
                                decimal_places=3, blank=True, null=True)

    hersteller = models.CharField(db_column='Hersteller', max_length=50, blank=True, null=True)

    strickplan = models.CharField(db_column='Strickplan', max_length=4, blank=True, null=True)

    beginwerk = models.CharField(db_column='BeginWerk', max_length=2, blank=True, null=True)

    strickplangoslar = models.CharField(
        db_column='StrickplanGoslar', max_length=50, blank=True, null=True)

    iloscprzyjeta1 = models.DecimalField(
        db_column='IloscPrzyjeta1', max_digits=15, decimal_places=3, blank=True, null=True)

    datastrickerei = models.CharField(db_column='DataStrickerei',
                                      max_length=10, blank=True, null=True)

    datawalkerei = models.CharField(db_column='DataWalkerei', max_length=10, blank=True, null=True)

    soku = models.CharField(db_column='Soku', max_length=1, blank=True, null=True)

    produktioninfo = models.CharField(db_column='ProduktionInfo',
                                      max_length=45, blank=True, null=True)

    autouwagi = models.CharField(db_column='AutoUwagi', max_length=255, blank=True, null=True)

    uzytkownik = models.CharField(db_column='Uzytkownik', max_length=50, blank=True, null=True)

    ilosclogisoft = models.DecimalField(
        db_column='IloscLogiSoft', max_digits=15, decimal_places=2, blank=True, null=True)

    zaklad = models.CharField(db_column='Zaklad', max_length=50, blank=True, null=True)
    lsz = models.SmallIntegerField(db_column='LSZ')

    datakomplet = models.DateTimeField(db_column='DataKomplet', blank=True, null=True)

    czas = models.DateTimeField(db_column='Czas', blank=True, null=True)

    dzrolki_to_dzplany = models.ForeignKey(Dzrolki, on_delete=False, default=None)

    class Meta:
        managed = True
        db_table = 'Dzplany'
        unique_together = (('id', 'numerdziewiarnia'),)
