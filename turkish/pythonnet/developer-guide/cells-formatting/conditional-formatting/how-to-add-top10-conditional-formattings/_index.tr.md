---
title: En İyi 10 Koşullu Biçimlendirmeyi Nasıl Eklerim
description: Aspose.Cells for Python via .NET kullanarak En Yüksek10 koşullu biçimlendirme nasıl uygulanır. Bu kriterleri ayarlayarak hücrelerin görünümünü ve görünüşünü daha fazla kontrol edebilirsiniz.
keywords: Aspose.Cells, En Yüksek10 Koşullu Biçimlendirme, Python, Koşullu, Biçimlendirme
type: docs
weight: 70
url: /tr/python-net/how-to-add-top10-conditional-formatting/
---

## **Olası Kullanım Senaryoları**
Excel'de Top 10 koşullu biçimlendirmeyi kullanmak, bir veri kümesinde en yüksek performans gösteren değerleri hızlıca vurgulamaya yardımcı olur — sadece en yüksek 10 değeri değil, aynı zamanda genellikle en yüksek N değerleri veya N%'lik (seçebilirsiniz!) gösterir.

1. Trendleri ve Aykırı Değerleri Belirle: En yüksek performans gösterenleri (örneğin, en iyi 10 satış temsilcisi, en iyi notlar, en yüksek gelirli aylar) anında tanımlayın. Veri sıralamadan analiz yapmayı kolaylaştırır.
1. Veri Görselleştirme: Önemli veri noktalarını görsel olarak öne çıkaran renk göstergeleri ekler. Elektronik tabloyu okuyan kişinin ana değerleri anlamasına yardımcı olur.
1. Hızlı Karşılaştırmalar: Mükemmelliği veya zirveyi vurgulamak istediğiniz panolar ve raporlarda kullanışlıdır.
1. Dinamik Güncellemeler: Verileriniz değiştiğinde, koşullu biçimlendirme otomatik olarak yeni en yüksek değerleri yansıtacak şekilde güncellenir.

## **Excel'de Top10 Koşullu Biçimlendirme Nasıl Eklenir**
İşte adım adım Excel'de Top10 koşullu biçimlendirmeyi nasıl ekleyeceğiniz:

1. Analiz etmek istediğiniz hücre aralığını seçin. Örneğin: Puanlar veya satış sayılarıyla çalışıyorsanız B2:B100 aralığını seçin.
1. Excel şeridinde Giriş sekmesine gidin.
1. Stiller grubunda Koşullu Biçimlendirme'ye tıklayın.
1. Aşağı açılır menüde Top/Alt Kuralları üzerinde durun.
1. En Üst 10 Öğeleri...'ne tıklayın.
1. Bir iletişim kutusu açılır: Üst 10'de sıralanan hücreleri biçimlendir. Sayıyı değiştirebilirsiniz (örn. En Üst 5, En Üst 3 vb.). Bir biçim seçin (örneğin, açık kırmızı doldurma, kalın metin veya daha fazla seçenek için Özel Biçim'e tıklayın).
1. Tamam'a tıklayın.


## **Aspose.Cells for Python via .NET kullanarak En Yüksek10 Koşullu Biçimlendirmeyi nasıl eklerim**

Aspose.Cells for Python via .NET, XLSX formatında hücrelerde Microsoft Excel 2007 ve sonrası sürümler tarafından sağlanan koşullu biçimlendirmeyi tam destekler. Bu örnek, En Yüksek 10 koşullu biçimlendirme için farklı özellik setleriyle bir egzersiz gösterir.

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

        self.add_top10_1()
        self.add_top10_2()
        self.add_top10_3()
        self.add_top10_4()

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

    def add_top10_1(self):
        conds = self.get_format_condition("A17:C20", Color.gray)
        idx = conds.add_condition(FormatConditionType.TOP10)
        cond = conds[idx]
        cond.style.background_color = Color.yellow
        cond.style.pattern = BackgroundType.SOLID

    def add_top10_2(self):
        conds = self.get_format_condition("A21:C24", Color.green)
        idx = conds.add_condition(FormatConditionType.TOP10)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.top10.is_bottom = True

    def add_top10_3(self):
        conds = self.get_format_condition("A25:C28", Color.orange)
        idx = conds.add_condition(FormatConditionType.TOP10)
        cond = conds[idx]
        cond.style.background_color = Color.blue
        cond.style.pattern = BackgroundType.SOLID
        cond.top10.is_percent = True

    def add_top10_4(self):
        conds = self.get_format_condition("A29:C32", Color.gold)
        idx = conds.add_condition(FormatConditionType.TOP10)
        cond = conds[idx]
        cond.style.background_color = Color.green
        cond.style.pattern = BackgroundType.SOLID
        cond.top10.rank = 3
```

{{< app/cells/assistant language="csharp" >}}
{{< app/cells/assistant language="python-net" >}}
