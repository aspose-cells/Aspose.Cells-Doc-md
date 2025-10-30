---
title: Zaman Dönemleri Koşullu Biçimlendirmeyi Nasıl Eklerim
description: Aspose.Cells for Python via .NET kullanarak Zaman Dönemleri koşullu biçimlendirmeyi nasıl uygularım. Bu kriterleri ayarlayarak hücrelerin görünümünü ve görünüşünü daha fazla kontrol edebilirsiniz.
keywords: Aspose.Cells, Zaman Dönemleri Koşullu Biçimlendirme, Python, Koşullu, Biçimlendirme
type: docs
weight: 70
url: /tr/python-net/how-to-add-time-periods-conditional-formatting/
---

## **Olası Kullanım Senaryoları**
Excel'de Zaman Dönemleri koşullu biçimlendirmeyi kullanmak, tarihlerle çalışırken oldukça faydalıdır—zaman tabanlı verileri hızla izleme ve yönetmenize olanak sağlar.
1. Zaman Tabanlı Verilere Hızlı Bakış: Bugünün görevleri, geçen ayın satışları, yaklaşan son tarihler, gelecek hafta randevuları gibi önemli noktaları hemen vurgulama.
1. Daha İyi Zaman Yönetimi: Gerekli tarihleri, etkinlikleri veya süresi dolan öğeleri takip etmenize yardımcı olur. Proje zaman çizelgeleri, faturalar veya programlar için mükemmeldir.
1. Otomatik Güncellemeler: Dinamik olarak güncellenir. Bugünün tarihi değişirse, Excel biçimlendirmeyi sizin herhangi bir müdahaleniz olmadan günceller.

1. Görsel Netlik: Zamanla ilgili bilgileri renkler veya kalın stiller kullanarak öne çıkarır—böylece gözden kaçmaz.

## **Excel Kullanarak Zaman Dönemleri Koşullu Biçimlendirmeyi Nasıl Eklerim**
İşte Excel'de Zaman Dönemleri koşullu biçimlendirmeyi nasıl ekleyebileceğiniz—bugün, geçen hafta, gelecek ay gibi tarihleri vurgulamak için oldukça kullanışlıdır.

Zaman Dönemleri Koşullu Biçimlendirmeyi Eklemek İçin Adımlar:
1. Biçimlendirmek istediğiniz tarih aralığını seçin. Örnek: A2:A50.
1. Şeritteki Giriş sekmesine gidin.
1. Stiller grubunda Koşullu Biçimlendirme'ye tıklayın.
1. Hücreleri Vurgula Kuralları üzerinde durun.
1. Bir Tarih Oluşuyor... seçeneğine tıkla.
1. Açılan diyaloğun: Açılır menüden bir zaman dilimi seçin (Bugün, Dün, Yarın, Son 7 gün, Geçen hafta, Gelecek ay vb.).
1. Formatı seçin (varsayılan açık kırmızı dolgu ile koyu kırmızı metin veya kendi formatınızı belirlemek için Özel Format'ı tıklayın).
1. Tamam'a tıklayın.


## **Aspose.Cells for Python via .NET kullanarak Zaman Dönemleri Koşullu Biçimlendirmeyi nasıl eklerim**

Aspose.Cells for Python via .NET, XLSX formatında hücrelerde Microsoft Excel 2007 ve sonrası sürümler tarafından sağlanan koşullu biçimlendirmeyi tam destekler. Bu örnek, farklı özellik setleriyle Zaman Dönemleri koşullu biçimlendirme egzersizini gösterir.

```python
from aspose.cells import Workbook
from aspose.cells import Workbook, Worksheet, CellArea, FormatConditionType, IconSetType, FormatConditionValueType, BackgroundType, TimePeriodType
from aspose.pydrawing import Color
from datetime import datetime
import aspose.cells
import os
import pytest

class ConditionalFormatting:
    def __init__(self):
        self._sheet = None

    @staticmethod
    def run():
        # The path to the documents directory
        current_dir = os.path.dirname(os.path.abspath(__file__))
        data_dir = os.path.join(current_dir, "data")
        obj = ConditionalFormatting()
        obj.do_test(data_dir)

    def do_test(self, data_dir):
        book = Workbook()
        sheet1 = book.worksheets[0]
        self._sheet = sheet1

        self.add_time_period_1()
        self.add_time_period_2()
        self.add_time_period_3()
        self.add_time_period_4()
        self.add_time_period_5()
        self.add_time_period_6()
        self.add_time_period_7()
        self.add_time_period_8()
        self.add_time_period_9()
        self.add_time_period_10()

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "Testoutput.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)

    def add_time_period_10(self):
        conds = self.get_format_condition("I19:K20", Color.medium_sea_green)
        idx = conds.add_condition(FormatConditionType.TIME_PERIOD)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.time_period = TimePeriodType.YESTERDAY
        c = self._sheet.cells.get("I19")
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        c.put_value(datetime(2008, 7, 30))
        c = self._sheet.cells.get("K20")
        c.put_value(datetime(2008, 8, 3))
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        self._sheet.cells.get("I20").put_value("Yesterday")

    def add_time_period_9(self):
        conds = self.get_format_condition("I17:K18", Color.medium_purple)
        idx = conds.add_condition(FormatConditionType.TIME_PERIOD)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.time_period = TimePeriodType.TOMORROW
        c = self._sheet.cells.get("I17")
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        c.put_value(datetime(2008, 8, 1))
        c = self._sheet.cells.get("K18")
        c.put_value(datetime(2008, 8, 3))
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        self._sheet.cells.get("I18").put_value("Tomorrow")

    def add_time_period_8(self):
        conds = self.get_format_condition("I15:K16", Color.medium_orchid)
        idx = conds.add_condition(FormatConditionType.TIME_PERIOD)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.time_period = TimePeriodType.THIS_WEEK
        c = self._sheet.cells.get("I15")
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        c.put_value(datetime(2008, 7, 28))
        c = self._sheet.cells.get("K16")
        c.put_value(datetime(2008, 8, 3))
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        self._sheet.cells.get("I16").put_value("ThisWeek")

    def add_time_period_7(self):
        conds = self.get_format_condition("I13:K14", Color.medium_blue)
        idx = conds.add_condition(FormatConditionType.TIME_PERIOD)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.time_period = TimePeriodType.THIS_MONTH
        c = self._sheet.cells.get("I13")
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        c.put_value(datetime(2008, 7, 5))
        c = self._sheet.cells.get("K14")
        c.put_value(datetime(2008, 5, 30))
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        self._sheet.cells.get("I14").put_value("ThisMonth")

    def add_time_period_6(self):
        conds = self.get_format_condition("I11:K12", Color.medium_aquamarine)
        idx = conds.add_condition(FormatConditionType.TIME_PERIOD)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.time_period = TimePeriodType.NEXT_WEEK
        c = self._sheet.cells.get("I11")
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        c.put_value(datetime(2008, 8, 5))
        c = self._sheet.cells.get("K12")
        c.put_value(datetime(2008, 7, 30))
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        self._sheet.cells.get("I12").put_value("NextWeek")

    def add_time_period_5(self):
        conds = self.get_format_condition("I9:K10", Color.maroon)
        idx = conds.add_condition(FormatConditionType.TIME_PERIOD)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.time_period = TimePeriodType.NEXT_MONTH
        c = self._sheet.cells.get("I9")
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        c.put_value(datetime(2008, 8, 25))
        c = self._sheet.cells.get("K10")
        c.put_value(datetime(2008, 7, 30))
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        self._sheet.cells.get("I10").put_value("NextMonth")

    def add_time_period_4(self):
        conds = self.get_format_condition("I7:K8", Color.linen)
        idx = conds.add_condition(FormatConditionType.TIME_PERIOD)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.time_period = TimePeriodType.LAST_WEEK
        c = self._sheet.cells.get("I7")
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        c.put_value(datetime(2008, 7, 25))
        c = self._sheet.cells.get("K8")
        c.put_value(datetime(2008, 7, 30))
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        self._sheet.cells.get("I8").put_value("LastWeek")

    def add_time_period_3(self):
        conds = self.get_format_condition("I5:K6", Color.linen)
        idx = conds.add_condition(FormatConditionType.TIME_PERIOD)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.time_period = TimePeriodType.LAST_MONTH
        c = self._sheet.cells.get("I5")
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        c.put_value(datetime(2008, 6, 26))
        c = self._sheet.cells.get("K6")
        c.put_value(datetime(2008, 7, 30))
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        self._sheet.cells.get("I6").put_value("LastMonth")

    def add_time_period_2(self):
        conds = self.get_format_condition("I3:K4", Color.light_steel_blue)
        idx = conds.add_condition(FormatConditionType.TIME_PERIOD)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.time_period = TimePeriodType.LAST7DAYS
        c = self._sheet.cells.get("I3")
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        c.put_value(datetime(2008, 7, 26))
        c = self._sheet.cells.get("K4")
        c.put_value(datetime(2008, 8, 30))
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        self._sheet.cells.get("I4").put_value("Last7Days")

    def add_time_period_1(self):
        conds = self.get_format_condition("I1:K2", Color.light_slate_gray)
        idx = conds.add_condition(FormatConditionType.TIME_PERIOD)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.time_period = TimePeriodType.TODAY
        c = self._sheet.cells.get("I1")
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        c.put_value(datetime.today())
        c = self._sheet.cells.get("K2")
        c.put_value(datetime(2008, 7, 30))
        style = c.get_style()
        style.number = 30
        c.set_style(style)
        self._sheet.cells.get("I2").put_value("Today")


    def get_format_condition(self, cell_area_name, color):
        index = self._sheet.conditional_formattings.add()
        format_conditions = self._sheet.conditional_formattings[index]
        area = self.get_cell_area_by_name(cell_area_name)
        format_conditions.add_area(area)
        self.fill_cell(cell_area_name, color)
        return format_conditions

    def fill_cell(self, cell_area_name, color):
        area = self.get_cell_area_by_name(cell_area_name)
        k = 0
        for i in range(area.start_column, area.end_column + 1):
            for j in range(area.start_row, area.end_row + 1):
                c = self._sheet.cells.get(j, i)
                if color != Color.empty:
                    s = c.get_style()
                    s.foreground_color = color
                    s.pattern = BackgroundType.SOLID
                    c.set_style(s)
                value = j + i + k
                c.put_value(value)
                k += 1

    @staticmethod
    def get_cell_area_by_name(s):
        area = CellArea()
        str_cell_range = s.replace("$", "").split(':')
        start_row, start_col = CellsHelper.cell_name_to_index(str_cell_range[0])
        area.start_row = start_row
        area.start_column = start_col
        if len(str_cell_range) == 1:
            area.end_row = start_row
            area.end_column = start_col
        else:
            end_row, end_col = CellsHelper.cell_name_to_index(str_cell_range[1])
            area.end_row = end_row
            area.end_column = end_col
        return area

```
{{< app/cells/assistant language="python-net" >}}
