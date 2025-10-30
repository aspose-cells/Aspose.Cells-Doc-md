---
title: データ棒条件付き書式の追加方法
description: Aspose.Cells for Python via .NETライブラリを使用してデータバー条件付き書式を適用する方法。これらの基準を調整することで、セルの外観と表示をより細かく制御できます。
keywords: Aspose.Cells、データバー条件付き書式、Python、条件付き書式、フォーマット
type: docs
weight: 70
url: /ja/python-net/how-to-add-databars-conditional-formatting/
---

## **可能な使用シナリオ**
条件付き書式でデータ棒を使用することは、データを一目で理解するための効果的（そして視覚的！）な方法です。

1. 値のビジュアル比較：データ棒は数字を横棒に変え、値を並べて比較しやすくします — セル内のミニバーグラフのように！
1. 即時パターン認識：高値、低値、外れ値を並べ替えや数値のスキャンなしで瞬時に把握できます。
1. 読みやすさ向上：特に長い表で役立つ — 認知負荷を軽減し、主要な傾向を素早く理解できます。
1. 動的かつリアルタイム：数値が変わるとバーも自動で更新されます — リアルタイムのメトリクス、進捗やKPIの追跡に最適です。
1. プロフェッショナルなダッシュボード：レポートやダッシュボードに清潔感のあるモダンな仕上がりを追加します。

## **Excelでデータ棒条件付き書式を追加する方法**
Excelにデータ棒条件付き書式を追加するには、次の手順で行います：

1. データ範囲を選択します。例：C2:C20 — 販売、スコア、進捗値など。
1. リボンのホームタブに移動します。
1. スタイルグループの条件付き書式をクリックします。
1. データ棒にカーソルを合わせます。
1. スタイルを選択します：グラデーション塗りつぶし（棒が左から右に徐々にフェード）とソリッド塗りつぶし（棒に単色）。
1. 好みのスタイルをクリックして終了です！

## **Aspose.Cells for Python via .NETを使用してデータバーの条件付き書式を追加する方法**

Aspose.Cells for Python via .NETは、XLSX形式のセルに対してMicrosoft Excel 2007以降のバージョンによる条件付き書式をフルサポートします。この例では、異なる属性セットを用いたデータバー条件付き書式の演習を示します。

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
