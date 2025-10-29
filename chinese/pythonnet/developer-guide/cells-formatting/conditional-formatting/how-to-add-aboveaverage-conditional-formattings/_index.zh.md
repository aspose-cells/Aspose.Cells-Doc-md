---
title: 如何添加上方平均值条件格式
description: 如何使用 Aspose.Cells for Python via .NET 库应用 AboveAverage 条件格式。通过调整这些条件，您可以更好地控制单元格的外观和显示方式。
keywords: Aspose.Cells、AboveAverage 条件格式、Python、条件、格式化
type: docs
weight: 70
url: /zh/python-net/how-to-add-above-average-conditional-formatting/
---

## **可能的使用场景**
在Microsoft Excel或Google Sheets等工具中使用上方平均值条件格式，是一种快速且直观的突出显示数据的方式，特别是突出高于平均值的范围内的值。以下是原因：
1. 快速识别趋势：帮助你瞬间找到表现出色的值，无需手动计算平均值或扫描数字。
1. 简化数据分析：无需计算或输入公式，这是应用逻辑条件格式的自动方式，节省时间。
1. 增强视觉效果：色彩编码帮助使你的电子表格更易阅读，也更具视觉吸引力，尤其在演示时。
1. 支持决策：快速识别高于平均值的数值可以推动行动，例如奖励表现优异的员工或调查为何某些产品表现优越。

## **如何使用Excel添加高于平均值的条件格式**
以下是分步骤在Excel中添加高于平均值的条件格式的方法：

1. 选择要应用格式的单元格区域。例如：A1:A20。
1. 转到功能区的首页标签。
1. 在样式组中点击“条件格式”。
1. 浮动到“顶部/底部规则”。
1. 选择“高于平均值...”
1. 出现的对话框会自动检测“格式化高于平均值的单元格”。你可以通过点击“与...”旁边的下拉菜单来更改格式样式（例如选择填充颜色或自定义格式）。
1. 点击“确定”。你选择的区域中高于该区域平均值的所有单元格将被高亮显示。


## **如何使用 Aspose.Cells for Python via .NET 添加 Above Average 条件格式**

Aspose.Cells for Python via .NET 完全支持在 XLSX 格式中，运行时对 Microsoft Excel 2007 及更高版本提供的条件格式支持。此示例演示了使用不同属性集进行 Above Average 条件格式的操作。

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
