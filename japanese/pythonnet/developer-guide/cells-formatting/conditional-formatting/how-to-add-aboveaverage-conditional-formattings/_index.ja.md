---
title: 上位平均条件付き書式の追加方法
description: Aspose.Cells for Python via .NETライブラリを使用してAboveAverage条件付き書式を適用する方法。これらの基準を調整することで、セルの見た目や表示をより細かく制御できます。
keywords: Aspose.Cells、AboveAverage条件付き書式、Python、条件付き書式
type: docs
weight: 70
url: /ja/python-net/how-to-add-above-average-conditional-formatting/
---

## **可能な使用シナリオ**
Microsoft ExcelやGoogle Sheetsのようなツールで、上位平均条件付き書式を使用すると、特定の範囲内で平均より高い値を持つデータを素早くハイライトでき、視覚的に目立たせることができます。使用理由は次のとおりです：
1. トレンドを素早く把握：平均や数値を手動で計算せずに、高パフォーマンスの値を瞬時に見つけることができます。
1. データ分析の簡素化：数式の計算や入力は不要で、論理に基づく書式設定を自動的に適用でき、時間を節約します。
1. 視覚的魅力の向上：色分けにより、表を見やすくし、プレゼンテーション時に特に効果的です。
1. 意思決定を支援：平均以上の値を素早く識別することで、ハイパフォーマーへの報酬やなぜ特定の製品が他より優れているのか調査するなどの行動を促進できます。

## **Excelで平均以上の条件付き書式を追加する方法**
Excelに平均以上の条件付き書式を追加するには、次の手順で行います：

1. 書式を適用したいセル範囲を選択します。例：A1:A20。
1. リボンのホームタブに移動します。
1. スタイルグループの条件付き書式をクリックします。
1. 上/下ルールにカーソルを合わせます。
1. 平均以上をクリックします...
1. 表示されるダイアログボックスで：自動的に「平均より上のセルをフォーマット」と検出されます。書式スタイルは、ドロップダウンの横をクリックして変更できます（例：色の塗りつぶしやカスタムフォーマット）。
1. OKをクリックします。選択範囲内で平均以上のセルがハイライトされます。


## **Aspose.Cells for Python via .NET を用いたAbove Average条件付き書式の追加方法**

Aspose.Cells for Python via .NET は、Excel 2007以降のMicrosoft Excelの条件付き書式をランタイムのセル上で完全にサポートします。この例では、異なる設定の集合を使ったAbove Average条件付き書式の演習を示します。

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
