---
title: Veri Çubukları Koşullu Biçimlendirmesi Nasıl Eklenir
description: Aspose.Cells for Python via .NET kütüphanesini kullanarak Veri Çubukları koşullu biçimlendirme nasıl uygulanır. Bu kriterleri ayarlayarak hücrelerin görünümünü ve görünüşünü daha fazla kontrol edebilirsiniz.
keywords: Aspose.Cells, Veri Çubukları Koşullu Biçimlendirme, Python, Koşullu, Biçimlendirme
type: docs
weight: 70
url: /tr/python-net/how-to-add-databars-conditional-formatting/
---

## **Olası Kullanım Senaryoları**
Koşullu biçimlendirmede Veri Çubukları kullanmak, verinizi bir bakışta anlamanın güçlü (ve görsel!) bir yoludur.

1. Değerlerin Görsel Karşılaştırması: Veri çubukları sayıları yatay çubuklara dönüştürür, böylece değerleri yan yana karşılaştırmak çok kolay — hücrelerinizde mini bir çubuk grafik gibi!
1. Hemen Desen Tanıma: Sıralama veya tarama yapmadan yüksekler, alçaklar ve aykırı değerleri anında görebilirsiniz.
1. Daha İyi Okunabilirlik: Özellikle uzun tablolar için faydalıdır — bilişsel yükü azaltır ve ana eğilimleri hızlıca kavramanıza yardımcı olur.
1. Dinamik ve Gerçek Zamanlı: Değerler değiştikçe, çubuklar otomatik olarak güncellenir — canlı metrikleri, ilerlemeleri veya KPI'ları takip etmek için harika.
1. Profesyonel Görünüm Sahibi Panolar: Raporlara veya panolara temiz, modern ve parlatılmış bir görünüm katar.

## **Excel Kullanarak Veri Çubukları Koşullu Biçimlendirme Nasıl Eklenir**
Excel'de Veri Çubukları koşullu biçimlendirmesi eklemek için şu adımları uygulayabilirsiniz:

1. Veri aralığınızı seçin, örneğin: C2:C20 — bu satış, skor veya ilerleme değerleri olabilir.
1. Şeritteki Giriş sekmesine gidin.
1. Stiller grubunda Koşullu Biçimlendirme’ye tıklayın.
1. Veri Çubukları üzerine gelin.
1. Bir stil seçin: Gradyan Doldurma (çubuklar soldan sağa solmalıdır) ve Düz Doldurma (çubuklar katı renkli olur).
1. Beğendiğiniz stil üzerine tıklayın — ve tamam!

## **Aspose.Cells for Python via .NET kullanarak Veri Çubukları Koşullu Biçimlendirmeyi nasıl eklerim**

Aspose.Cells for Python via .NET, XLSX formatında hücrelerde Microsoft Excel 2007 ve sonrası sürümler tarafından sağlanan koşullu biçimlendirmeyi çalışma zamanında tam destekler. Bu örnek, farklı özellik setleriyle Veri Çubukları koşullu biçimlendirme egzersizini gösterir.

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

        self.add_data_bar1()
        self.add_data_bar2()

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "Testoutput.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)    

    def add_data_bar2(self):
        conds = self.get_format_condition("E3:G4", Color.light_green)
        idx = conds.add_condition(FormatConditionType.DATA_BAR)
        cond = conds[idx]
        cond.data_bar.color = Color.orange
        cond.data_bar.min_cfvo.type = FormatConditionValueType.PERCENTILE
        cond.data_bar.min_cfvo.value = 30.78
        cond.data_bar.show_value = False

    def add_data_bar1(self):
        conds = self.get_format_condition("E1:G2", Color.yellow_green)
        idx = conds.add_condition(FormatConditionType.DATA_BAR)
        cond = conds[idx]

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
