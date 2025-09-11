---
title: How to Add Time Periods Conditional Formatting
description: How to use the Aspose.Cells for Python via .NET library to apply TimePeriods conditional formatting. By adjusting these criteria, you have more control over how cells look and appear.
keywords: Aspose.Cells, TimePeriods Conditional Formatting, Python, Conditional, Formatting
type: docs
weight: 70
url: /python-net/how-to-add-time-periods-conditional-formatting/
---

## **Possible Usage Scenarios**
Using Time Periods conditional formatting in Excel is super useful when working with dates—it helps you visually track and manage time-based data quickly.
1. Instant Insights on Time-Based Data: Quickly highlight things like Today’s tasks, Last month’s sales, Upcoming deadlines, Next week’s appointments.
1. Better Time Management: Helps you stay on top of due dates, events, or expiring items. Great for project timelines, invoices, or schedules.
1. Automatic Updates: It updates dynamically. If today’s date changes, Excel will update the formatting without you lifting a finger.

1. Visual Clarity: Makes time-sensitive information stand out using colors or bold styles — so it doesn’t get missed.

## **How to Add Time Periods Conditional Formatting Using Excel**
Here's how you can add Time Periods conditional formatting in Excel — super useful for highlighting dates like today, last week, next month, etc.

Steps to Add Time Periods Conditional Formatting:
1. Select the range of date cells you want to format. Example: A2:A50.
1. Go to the Home tab on the ribbon.
1. Click on Conditional Formatting in the Styles group.
1. Hover over Highlight Cells Rules.
1. Click on A Date Occurring...
1. In the dialog box that appears: Use the drop-down to select a time period(Today, Yesterday, Tomorrow, Last 7 days, Last week, Next month, etc.).
1. Choose the format (default is light red fill with dark red text, or click Custom Format to choose your own).
1. Click OK.


## **How to Add Time Periods Conditional Formatting Using Aspose.Cells for Python via .NET**

Aspose.Cells for Python via .NET fully supports the conditional formatting provided by Microsoft Excel 2007 and later versions in XLSX format on cells at runtime. This example demonstrates an exercise for Time Periods conditional formatting with different sets of attributes.

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