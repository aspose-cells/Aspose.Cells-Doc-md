---
title: How to Add Above Average Conditional Formatting
description: How to use the Aspose.Cells for Python via .NET library to apply AboveAverage conditional formatting. By adjusting these criteria, you have more control over how cells look and appear.
keywords: Aspose.Cells, AboveAverage Conditional Formatting, Python, Conditional, Formatting
type: docs
weight: 70
url: /python-net/how-to-add-above-average-conditional-formatting/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Using Above Average Conditional Formatting in tools like Microsoft Excel or Google Sheets is a quick and visual way to highlight data that stands out—specifically, values that are higher than the average in a range. Here's why you might use it:
1. Spot Trends Quickly: It helps you instantly identify high-performing values without manually calculating averages or scanning numbers.
1. Simplify Data Analysis: You don’t need to calculate or input any formulas—it’s an automatic way to apply logic-based formatting, saving time.
1. Enhance Visual Appeal: Color-coding helps make your spreadsheet easier to read and more visually engaging, especially during presentations.
1. Supports Decision Making: Quickly identifying values above average can drive actions, such as rewarding high performers or investigating why certain products are outperforming others.

## **How to Add Above Average Conditional Formatting Using Excel**
To add Above Average conditional formatting in Excel, here's how you can do it step by step:

1. Select the range of cells you want to apply the formatting to. For example: A1:A20.
1. Go to the Home tab on the ribbon.
1. Click on Conditional Formatting in the Styles group.
1. Hover over Top/Bottom Rules.
1. Click Above Average...
1. In the dialog box that appears: It will automatically detect "Format cells that are ABOVE average." You can change the formatting style by clicking the drop-down next to with (e.g., choose a color fill or custom format).
1. Click OK. All cells in your selected range that are above the average of that range will be highlighted.


## **How to Add Above Average Conditional Formatting Using Aspose.Cells for Python via .NET**

Aspose.Cells for Python via .NET fully supports the conditional formatting provided by Microsoft Excel 2007 and later versions in XLSX format on cells at runtime. This example demonstrates an exercise for Above Average conditional formatting with different sets of attributes.

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
