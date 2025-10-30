---
title: Ortalamanın Üzerinde Koşullu Biçimlendirme Nasıl Eklenir
description: Aspose.Cells for Python via .NET kütüphanesini kullanarak Yüksek Ortalama koşullu biçimlendirmeyi nasıl uygulayacağınız. Bu kriterleri ayarlayarak, hücrelerin görünümünü ve nasıl görüneceğini daha fazla kontrol edebilirsiniz.
keywords: Aspose.Cells, Yüksek Ortalama Koşullu Biçimlendirme, Python, Koşullu, Biçimlendirme
type: docs
weight: 70
url: /tr/python-net/how-to-add-above-average-conditional-formatting/
---

## **Olası Kullanım Senaryoları**
Microsoft Excel veya Google Sheets gibi araçlarda Ortalamanın Üzerinde Koşullu Biçimlendirme kullanmak, öne çıkan verileri hızlı ve görsel olarak vurgulamanın kolay bir yoludur—özellikle bir aralıktaki ortalamanın üzerinde olan değerler için. İşte neden kullanılır:
1. Hızlı Trendleri Tespit Edin: Bu, ortalamaları manuel olarak hesaplamadan veya sayıları taramadan yüksek performans gösteren değerleri anında belirlemenize yardımcı olur.
1. Veri Analizini Basitleştirin: Formül hesaplamanıza veya girmenize gerek yok—otomatik olarak mantık tabanlı biçimlendirme uygular, zaman kazandırır.
1. Görsel Çekiciliği Artırın: Renk kodlama, çalışma sayfanızın okunmasını kolaylaştırmaya ve görsel olarak daha ilgi çekici hale getirmeye yardımcı olur, özellikle sunumlar sırasında.
1. Karar Verme Sürecini Destekler: Ortalamanın üzerinde olan değerleri hızlıca belirlemek, yüksek performans gösterenleri ödüllendirmek veya belirli ürünlerin neden diğerlerinden üstün olduğunu araştırmak gibi eylemleri yönlendirebilir.

## **Excel Kullanarak Ortalamanın Üzerinde Koşullu Biçimlendirme Nasıl Eklenir**
Excel'de Ortalamanın Üzerinde koşullu biçimlendirme eklemek için adım adım şu şekilde yapabilirsiniz:

1. Biçimlendirmeyi uygulamak istediğiniz hücre aralığını seçin. Örneğin: A1:A20.
1. Şeritteki Giriş sekmesine gidin.
1. Stiller grubunda Koşullu Biçimlendirme'ye tıklayın.
1. En üstteki/Azalt Rule'ler üzerine gelin.
1. Ortalamanın Üzerinde… seçeneğine tıklayın.
1. Karşınıza çıkan iletişim kutusunda: "ORTALAMANIN ÜZERİNDE olan hücreleri biçimlendir" otomatik tespit edilecektir. Biçimlendirme stilinizi değiştirmek için, yanındaki açılır menüden (ör. bir renk doldurma veya özel format seçin).
1. Tamam'a tıklayın. Seçilen aralıktaki ortalamanın üzerinde olan tüm hücreler vurgulanacaktır.


## **Aspose.Cells for Python via .NET kullanarak Yüksek Ortalama Koşullu Biçimlendirme Nasıl Eklenir**

Aspose.Cells for Python via .NET, Microsoft Excel 2007 ve sonraki sürümler tarafından sağlanan koşullu biçimlendirmeyi çalışma zamanında XLSX formatında tamamen destekler. Bu örnek, farklı özellik setleriyle Yüksek Ortalama koşullu biçimlendirme alıştırmasıdır.

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

        self.add_above_average()
        self.add_above_average2()
        self.add_above_average3()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "Testoutput.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)



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

    def add_above_average(self):
        conds = self.get_format_condition("A11:C12", Color.tomato)
        idx = conds.add_condition(FormatConditionType.ABOVE_AVERAGE)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID

    def add_above_average2(self):
        conds = self.get_format_condition("A13:C14", Color.empty)
        idx = conds.add_condition(FormatConditionType.ABOVE_AVERAGE)
        cond = conds[idx]
        cond.above_average.is_above_average = False
        cond.above_average.is_equal_average = True
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID

    def add_above_average3(self):
        conds = self.get_format_condition("A15:C16", Color.empty)
        idx = conds.add_condition(FormatConditionType.ABOVE_AVERAGE)
        cond = conds[idx]
        cond.above_average.is_above_average = False
        cond.above_average.is_equal_average = True
        cond.above_average.std_dev = 3
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID

```
{{< app/cells/assistant language="python-net" >}}
