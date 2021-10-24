from django.db import models
from jalali_date import datetime2jalali, date2jalali

class Product(models.Model):

    Name = models.CharField(max_length=100)

    def __str__(self) -> str:
        return super().__str__()


class ProductSell(models.Model):

    Product = models.ForeignKey(to=Product, on_delete=models.PROTECT, verbose_name='کالا')
    Count= models.IntegerField()
    SellDateTime = models.DateTimeField()

    monthdict = {

        'فروردین':'Farvardin',
        'اردیبهشت':'Ordibehesht',
        'خرداد':'Khordad',
        'تیر':'Tir',
        'مرداد':'Mordad',
        'شهریور':'Shahrivar',
        'مهر':'Mehr',
        'آبان':'Aban',
        'آذر':'Azar',
        'دی':'Dey',
        'بهمن':'Bahman',
        'اسفند':'Esfand',
    }

    def __str__(self) -> str:
        return super().__str__()


    def get_month_jalali(self):
        monthName = datetime2jalali(self.SellDateTime).strftime('%B')

        for key, value in self.monthdict.items:
            if value == monthName:
                return key



    def get_report(self):

        products = Product.objects.all()
        result = {}

        for k in self.monthdict.keys():
            plist = []
            for i in range(0, products.count()):
                plist.append(0)
            result.update({k:plist})

 
        counter = 0
        for product in products:
            productsells = ProductSell.objects.filter(Product_id=product.id)

            for ps in productsells:
                month = ps.get_month_jalali()
                count = ps.Count

                result[month][counter]=result[month][counter]+count


            counter += 1

        return result     



