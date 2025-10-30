---
title: トップ10条件付き書式の追加方法
description: Aspose.Cells for Python via .NETライブラリを使用してトップ10条件付き書式を適用する方法。これらの基準を調整することで、セルの見た目と外観をより制御できます。
keywords: Aspose.Cells、トップ10条件付き書式、Python、条件付き書式、フォーマット
type: docs
weight: 70
url: /ja/python-net/how-to-add-top10-conditional-formatting/
---

## **可能な使用シナリオ**
Excelのトップ10条件付き書式を使用すると、データセット内の最高のパフォーマンス値を素早くハイライトできます — 文字通りのトップ10値だけでなく、Top NやTop N％（選択可能）も含まれます。

1. 傾向と異常値を見つける：例えば、トップ10の営業担当者、最高得点、最も収益の高い月などを即座に識別。データの並べ替えなしで分析しやすくなります。
1. データの可視化：重要なデータポイントを視覚的に際立たせる色のヒントを追加。スプレッドシートの閲覧者が主要な値を一目で理解できるようにします。
1. クイック比較：ダッシュボードやレポートで、優れた結果やピークをハイライトしたい場合に役立ちます。
1. ダイナミックな更新：データが変更された場合、条件付き書式は自動的に更新され、新しいトップ値を反映します。

## **Excelでトップ10条件付き書式を追加する方法**
Excelでトップ10条件付き書式をステップバイステップで追加する方法：

1. 分析したいセル範囲を選択します。例：スコアや販売数字に取り組む場合はB2:B100を選択します。
1. Excelリボンのホームタブに移動します。
1. スタイルグループの条件付き書式をクリックします。
1. ドロップダウンメニューのトップ/ボトムルールにカーソルを合わせます。
1. Top 10 Items...をクリックします。
1. ポップアップのダイアログボックスが表示され、次のように表示されます：上位10にランク付けされるセルをフォーマットします。数字（例：Top 5、Top 3など）を変更可能です。フォーマット（薄い赤色の塗りつぶし、太字のテキスト、または詳細なオプションのためにカスタムフォーマットをクリック）を選択します。
1. OKをクリック


## **Aspose.Cells for Python via .NETを使用してトップ10条件付き書式を追加する方法**

Aspose.Cells for Python via .NETは、XLSX形式のセルに対してMicrosoft Excel 2007以降のバージョンによる条件付き書式をフルサポートします。この例では、異なる属性セットを用いたトップ10条件付き書式の演習を示します。

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
