---
title: 如何添加Top10条件格式
description: 如何使用 Aspose.Cells for Python via .NET 库应用 Top10 条件格式。通过调整这些条件，您可以更好地控制单元格的外观和显示方式。
keywords: Aspose.Cells、Top10 条件格式、Python、条件、格式化
type: docs
weight: 70
url: /zh/python-net/how-to-add-top10-conditional-formatting/
---

## **可能的使用场景**
在Excel中使用Top 10条件格式有助于快速突出显示数据集中表现最佳的值——不仅仅是字面意义上的前10名，而是通常包括前N个值或前N%的值（可选择！）。

1. 识别趋势和离群值：即刻识别表现最优的数据（例如：前10名销售代表、最佳成绩、最高收入月份）。无须排序数据，便于分析。
1. 数据可视化：添加颜色提示，使重要数据点直观突出。帮助表格查看者一目了然关键数值。
1. 快速对比：在仪表盘和报告中十分实用，可以突出表现优秀或达到顶峰的值。
1. 动态更新：如果数据发生变化，条件格式会自动更新以反映新的前N值。

## ** 如何使用Excel添加Top10条件格式**
以下是逐步在Excel中添加Top10条件格式的方法：

1. 选择你想分析的单元格范围。例如：选择B2:B100，若你在处理得分或销售额。
1. 转到Excel功能区的“开始”标签。
1. 在样式组中点击“条件格式”。
1. 将鼠标悬停在“前/后规则”中。
1. 点击“前10项...”
1. 会弹出一个对话框：内容为“设置前10名的单元格”。你可以更改数字（例如前5、前3等）。选择一种格式（如浅红色填充、加粗文本，或点击“自定义格式”获取更多选项）。
1. 点击“确定”


## **如何使用 Aspose.Cells for Python via .NET 添加 Top10 条件格式**

Aspose.Cells for Python via .NET 在运行时完全支持 Microsoft Excel 2007 及更高版本在 XLSX 格式中提供的条件格式。此示例演示带不同属性集的 Top 10 条件格式的练习。

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
