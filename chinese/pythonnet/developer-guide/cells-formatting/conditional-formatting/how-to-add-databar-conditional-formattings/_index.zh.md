---
title: 如何添加数据条条件格式
description: 如何使用 Aspose.Cells for Python via .NET 库应用 Data Bars 条件格式。通过调整这些条件，您可以更好地控制单元格的外观和显示方式。
keywords: Aspose.Cells、Data Bars 条件格式、Python、条件、格式化
type: docs
weight: 70
url: /zh/python-net/how-to-add-databars-conditional-formatting/
---

## **可能的使用场景**
在条件格式中使用数据条是一种强大且直观的方式，可以快速理解你的数据。

1. 数值的直观比较：数据条将数字转换成水平条形，使得比较数值变得非常容易——就像在单元格中的迷你条形图！
1. 即时模式识别：你可以立即看到最高值、最低值和异常值，无需排序或扫描数值。
1. 更好的可读性：特别适用于长表格——它减少认知负荷，帮助你快速掌握关键趋势。
1. 动态实时：随着数值的变化，条形会自动更新——非常适合追踪实时指标、进度或关键绩效指标（KPI）。
1. 专业外观的仪表板：为报告或仪表板增添干净、现代、精致的外观。

## **如何使用Excel添加数据条条件格式**
以下是逐步在Excel中添加数据条条件格式的方法：

1. 选择你的数据区域，例如：C2:C20——这可以是销售额、得分或进度值。
1. 转到功能区的首页标签。
1. 点击“样式”组中的“条件格式”。
1. 浮动到“数据条”。
1. 选择样式：渐变填充（条从左到右逐渐变淡）和纯色填充（条具有单色）。
1. 点击你喜欢的风格——完成！

## **如何使用 Aspose.Cells for Python via .NET 添加 Data Bars 条件格式**

Aspose.Cells for Python via .NET 完全支持在 XLSX 格式中，运行时对 Microsoft Excel 2007 及更高版本提供的条件格式支持。此示例演示了使用不同属性集进行 DataBars 条件格式的操作。

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
