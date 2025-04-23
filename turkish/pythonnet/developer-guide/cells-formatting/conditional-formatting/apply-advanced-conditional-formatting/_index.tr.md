---
title: Python.NET kullanarak Gelişmiş Koşullu Biçimlendirme Uygula
linktitle: Gelişmiş Koşullu Biçimlendirme Uygulama
type: docs
weight: 70
url: /tr/python-net/apply-advanced-conditional-formatting/
description: Aspose.Cells for Python via .NET kullanarak veri çubukları, renk ölçekleri ve simge setleri gibi gelişmiş koşullu biçimlendirme özelliklerini nasıl uygulayacağınızı öğrenin.
keywords: Python Excel biçimlendirme, Koşullu biçimlendirme Python, Veri çubukları Python, Renk ölçekleri Python, Simge setleri Python, Aspose.Cells Python
---

{{% alert color="primary" %}} 

Microsoft Excel 2007 ve sonraki sürümler (2010/2013/2016) gelişmiş koşullu biçimlendirme özellikleri sağlar; hücre gölgeleme, kenarlıklar, renkli simgeler, oklar, rozetler ve yazı tipi biçimlendirmeyi içerir.

{{% /alert %}} 

## **Excel Dosyalarında Gelişmiş Koşullu Biçimlendirmeyi Uygula**
Aspose.Cells for Python via .NET tüm gelişmiş koşullu biçimlendirme özelliklerini destekler;

- Sayısal değerleri görselleştirmek için Veri Çubukları
- Renk geçişli hücre gölgelemesi için Renk skalaları
- Grafiksel göstergeler için Sembol kümeleri
- Üst/alt kuralları
- Zaman dilimi tabanlı biçimlendirme

Bu örnek Python.NET ile çeşitli gelişmiş koşullu biçimlendirme türlerini gösterir:

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

        self.add_default_icon_set()
        self.add_icon_set2()
        self.add_icon_set3()
        self.add_icon_set4()
        self.add_icon_set5()
        self.add_icon_set6()
        self.add_icon_set7()
        self.add_icon_set8()
        self.add_icon_set9()
        self.add_icon_set10()
        self.add_icon_set11()
        self.add_icon_set12()
        self.add_icon_set13()
        self.add_icon_set14()
        self.add_icon_set15()
        self.add_icon_set16()
        self.add_icon_set17()
        self.add_icon_set18()
        self.add_default_color_scale()
        self.add_3_color_scale()
        self.add_2_color_scale()
        self.add_above_average()
        self.add_above_average2()
        self.add_above_average3()
        self.add_top10_1()
        self.add_top10_2()
        self.add_top10_3()
        self.add_top10_4()
        self.add_data_bar1()
        self.add_data_bar2()
        self.add_contains_text()
        self.add_not_contains_text()
        self.add_contains_blank()
        self.add_not_contains_blank()
        self.add_begin_with()
        self.add_end_with()
        self.add_contains_error()
        self.add_not_contains_error()
        self.add_duplicate()
        self.add_unique()
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

    def add_icon_set2(self):
        conds = self.get_format_condition("M1:O2", Color.alice_blue)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.ARROWS3
        self._sheet.cells.get("M1").put_value("Arrows3")

    def add_icon_set3(self):
        conds = self.get_format_condition("M3:O4", Color.antique_white)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.ARROWS4
        self._sheet.cells.get("M3").put_value("Arrows4")

    def add_icon_set4(self):
        conds = self.get_format_condition("M5:O6", Color.aqua)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.ARROWS5
        self._sheet.cells.get("M5").put_value("Arrows5")

    def add_icon_set5(self):
        conds = self.get_format_condition("M7:O8", Color.aquamarine)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.ARROWS_GRAY3
        self._sheet.cells.get("M7").put_value("ArrowsGray3")

    def add_icon_set6(self):
        conds = self.get_format_condition("M9:O10", Color.azure)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.ARROWS_GRAY4
        self._sheet.cells.get("M9").put_value("ArrowsGray4")

    def add_icon_set7(self):
        conds = self.get_format_condition("M11:O12", Color.beige)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.ARROWS_GRAY5
        self._sheet.cells.get("M11").put_value("ArrowsGray5")

    def add_icon_set8(self):
        conds = self.get_format_condition("M13:O14", Color.bisque)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.FLAGS3
        self._sheet.cells.get("M13").put_value("Flags3")

    def add_icon_set9(self):
        conds = self.get_format_condition("M15:O16", Color.blanched_almond)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.QUARTERS5
        self._sheet.cells.get("M15").put_value("Quarters5")

    def add_icon_set10(self):
        conds = self.get_format_condition("M17:O18", Color.blue)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.RATING4
        self._sheet.cells.get("M17").put_value("Rating4")

    def add_icon_set11(self):
        conds = self.get_format_condition("M19:O20", Color.blue_violet)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.RATING5
        self._sheet.cells.get("M19").put_value("Rating5")

    def add_icon_set12(self):
        conds = self.get_format_condition("M21:O22", Color.brown)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.RED_TO_BLACK4
        self._sheet.cells.get("M21").put_value("RedToBlack4")

    def add_icon_set13(self):
        conds = self.get_format_condition("M23:O24", Color.burly_wood)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.SIGNS3
        self._sheet.cells.get("M23").put_value("Signs3")

    def add_icon_set14(self):
        conds = self.get_format_condition("M25:O26", Color.cadet_blue)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.SYMBOLS3
        self._sheet.cells.get("M25").put_value("Symbols3")

    def add_icon_set15(self):
        conds = self.get_format_condition("M27:O28", Color.chartreuse)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.SYMBOLS32
        self._sheet.cells.get("M27").put_value("Symbols32")

    def add_icon_set16(self):
        conds = self.get_format_condition("M29:O30", Color.chocolate)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.TRAFFIC_LIGHTS31
        self._sheet.cells.get("M29").put_value("TrafficLights31")

    def add_icon_set17(self):
        conds = self.get_format_condition("M31:O32", Color.coral)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.TRAFFIC_LIGHTS32
        self._sheet.cells.get("M31").put_value("TrafficLights32")

    def add_icon_set18(self):
        conds = self.get_format_condition("M33:O35", Color.cornflower_blue)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.TRAFFIC_LIGHTS4
        self._sheet.cells.get("M33").put_value("TrafficLights4")

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

    def add_duplicate(self):
        conds = self.get_format_condition("E23:G24", Color.light_slate_gray)
        idx = conds.add_condition(FormatConditionType.DUPLICATE_VALUES)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E23").put_value("bb")
        self._sheet.cells.get("G24").put_value("bb")

    def add_unique(self):
        conds = self.get_format_condition("E21:G22", Color.light_salmon)
        idx = conds.add_condition(FormatConditionType.UNIQUE_VALUES)
        cond = conds[idx]
        cond.style.background_color = Color.yellow
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E21").put_value("aa")
        self._sheet.cells.get("G22").put_value("aa")

    def add_not_contains_error(self):
        conds = self.get_format_condition("E19:G20", Color.light_sea_green)
        idx = conds.add_condition(FormatConditionType.NOT_CONTAINS_ERRORS)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E19").put_value("  ")
        self._sheet.cells.get("G20").put_value("  ")

    def add_contains_error(self):
        conds = self.get_format_condition("E17:G18", Color.light_sky_blue)
        idx = conds.add_condition(FormatConditionType.CONTAINS_ERRORS)
        cond = conds[idx]
        cond.style.background_color = Color.yellow
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E17").put_value("  ")
        self._sheet.cells.get("G18").put_value("  ")

    def add_begin_with(self):
        conds = self.get_format_condition("E15:G16", Color.light_goldenrod_yellow)
        idx = conds.add_condition(FormatConditionType.BEGINS_WITH)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.text = "ab"
        self._sheet.cells.get("E15").put_value("abc")
        self._sheet.cells.get("G16").put_value("babx")

    def add_end_with(self):
        conds = self.get_format_condition("E13:G14", Color.light_gray)
        idx = conds.add_condition(FormatConditionType.ENDS_WITH)
        cond = conds[idx]
        cond.style.background_color = Color.yellow
        cond.style.pattern = BackgroundType.SOLID
        cond.text = "ab"
        self._sheet.cells.get("E13").put_value("nnnab")
        self._sheet.cells.get("G14").put_value("mmmabc")

    def add_not_contains_blank(self):
        conds = self.get_format_condition("E11:G12", Color.light_coral)
        idx = conds.add_condition(FormatConditionType.NOT_CONTAINS_BLANKS)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E11").put_value("abc")
        self._sheet.cells.get("G12").put_value("  ")

    def add_contains_blank(self):
        conds = self.get_format_condition("E9:G10", Color.light_blue)
        idx = conds.add_condition(FormatConditionType.CONTAINS_BLANKS)
        cond = conds[idx]
        cond.style.background_color = Color.yellow
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E9").put_value("  ")
        self._sheet.cells.get("G10").put_value("  ")

    def add_not_contains_text(self):
        conds = self.get_format_condition("E7:G8", Color.light_coral)
        idx = conds.add_condition(FormatConditionType.NOT_CONTAINS_TEXT)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.text = "3"

    def add_contains_text(self):
        conds = self.get_format_condition("E5:G6", Color.light_blue)
        idx = conds.add_condition(FormatConditionType.CONTAINS_TEXT)
        cond = conds[idx]
        cond.style.background_color = Color.yellow
        cond.style.pattern = BackgroundType.SOLID
        cond.text = "1"

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

    def add_default_icon_set(self):
        self.get_format_condition("A1:C2", Color.yellow)

    def add_default_color_scale(self):
        conds = self.get_format_condition("A5:C6", Color.pink)
        idx = conds.add_condition(FormatConditionType.COLOR_SCALE)
        cond = conds[idx]

    def add_3_color_scale(self):
        conds = self.get_format_condition("A7:C8", Color.green)
        idx = conds.add_condition(FormatConditionType.COLOR_SCALE)
        cond = conds[idx]
        cond.color_scale.min_cfvo.type = FormatConditionValueType.NUMBER
        cond.color_scale.min_cfvo.value = 9
        cond.color_scale.min_color = Color.purple

    def add_2_color_scale(self):
        conds = self.get_format_condition("A9:C10", Color.white)
        idx = conds.add_condition(FormatConditionType.COLOR_SCALE)
        cond = conds[idx]
        cond.color_scale.min_color = Color.gold
        cond.color_scale.max_color = Color.sky_blue

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

### **Excel'in Renk Seçimi ile Renk Skalası Biçimlendirilmesi Hesapla**
Bu kod, Excel'in Renk Skalası koşullu biçimlendirme kuralları için seçtiği rengi belirlemeye nasıl kullanılır gösterir:

```python
import os
from aspose.cells import Workbook
from aspose.pydrawing import Color

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-Python
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Instantiate a workbook object and open the template file
workbook = Workbook(os.path.join(data_dir, "Book1.xlsx"))
# Get the first worksheet
worksheet = workbook.worksheets[0]
# Get the A1 cell
a1 = worksheet.cells.get("A1")

# Get the conditional formatting resultant object
cfr1 = a1.get_conditional_formatting_result()
# Get the ColorScale resultant color object
c = cfr1.color_scale_result

# Read and print the color values
print(c.to_argb())
print(c.name)
```
