---
title: How to Add Top10 Conditional Formatting
description: How to use the Aspose.Cells for Python via .NET library to apply Top10 conditional formatting. By adjusting these criteria, you have more control over how cells look and appear.
keywords: Aspose.Cells, Top10 Conditional Formatting, Python, Conditional, Formatting
type: docs
weight: 70
url: /python-net/how-to-add-top10-conditional-formatting/
---

## **Possible Usage Scenarios**
Using Top 10 conditional formatting in Excel helps quickly highlight the highest-performing values in a dataset — not just the literal top 10 values, but often the top N values or top N% (you can choose!).

1. Spot Trends and Outliers: Instantly identify the top performers (e.g., top 10 sales reps, best grades, highest revenue months).Makes it easy to analyze without sorting data.
1. Data Visualization: Adds color cues that make important data points stand out visually.Helps viewers of the spreadsheet understand the key values at a glance.
1. Quick Comparisons: Useful in dashboards and reports where you want to highlight excellence or peaks.
1. Dynamic Updates: If your data changes, the conditional formatting updates automatically to reflect the new top values.

## **How to Add Top10 Conditional Formatting Using Excel**
Here’s how you can add Top10 conditional formatting in Excel, step by step:

1. Select the range of cells you want to analyze. For example: Select B2:B100, if you're working with scores or sales numbers.
1. Go to the Home tab on the Excel ribbon.
1. Click on Conditional Formatting in the Styles group.
1. Hover over Top/Bottom Rules in the dropdown.
1. Click on Top 10 Items...
1. A dialog box will pop up: It will say: Format cells that rank in the top 10. You can change the number (e.g., Top 5, Top 3, etc.). Choose a format (like a light red fill, bold text, or click Custom Format for more options).
1. Click OK


## **How to Add Top10 Conditional Formatting Using Aspose.Cells for Python via .NET**

Aspose.Cells for Python via .NET fully supports the conditional formatting provided by Microsoft Excel 2007 and later versions in XLSX format on cells at runtime. This example demonstrates an exercise for Top 10 conditional formatting with different sets of attributes.

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