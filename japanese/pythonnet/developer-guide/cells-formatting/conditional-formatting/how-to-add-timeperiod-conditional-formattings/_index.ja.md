---
title: 時間範囲の条件付き書式の追加方法
description: Aspose.Cells for Python via .NETを使用してタイム期間条件付き書式を適用する方法。これらの基準を調整することで、セルの外観と表示をより制御できます。
keywords: Aspose.Cells、タイム期間条件付き書式、Python、条件付き書式、フォーマット
type: docs
weight: 70
url: /ja/python-net/how-to-add-time-periods-conditional-formatting/
---

## **可能な使用シナリオ**
Excelで時間範囲の条件付き書式を使用すると、日付を扱う際に非常に便利です。視覚的に時間に基づくデータを追跡し管理できます。
1. 時間に基づくデータの即時把握：今日のタスク、先月の販売、締切、来週の予定などを素早くハイライトします。
1. より良い時間管理：期限、イベント、期限切れ間近のアイテムを把握できます。プロジェクトのタイムライン、請求書、予定表に最適です。
1. 自動更新：動的に更新されます。今日の日付が変わると、Excelが書式を自動的に更新します。

1. 視覚的な明確さ：時間に敏感な情報を色や太字のスタイルで目立たせ、見逃さないようにします。

## **Excelで時間範囲の条件付き書式を追加する方法**
Excelで期間条件付き書式を追加する方法はこちらです — 今日、先週、来月などの日付をハイライト表示するのに非常に役立ちます。

期間条件付き書式の追加手順：
1. 書式設定したい日付セルの範囲を選択します。例：A2:A50。
1. リボンのホームタブに移動します。
1. スタイルグループの条件付き書式をクリックします。
1. ハイライトセルルールにカーソルを合わせます。
1. A Date Occurring...をクリックします。
1. 表示されるダイアログボックスで：ドロップダウンを使用して期間（今日、昨日、明日、過去7日間、先週、来月など）を選択します。
1. 書式（デフォルトは薄い赤の塗りつぶしと濃い赤のテキスト、またはカスタムフォーマットをクリックして自分のスタイルを選んでください）を選択します。
1. OKをクリックします。


## **Aspose.Cells for Python via .NETを使用してタイム期間条件付き書式を追加する方法**

Aspose.Cells for Python via .NETは、XLSX形式のセルに対してMicrosoft Excel 2007以降のバージョンによる条件付き書式をフルサポートします。この例では、異なる属性セットを用いたタイム期間条件付き書式の演習を示します。

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
