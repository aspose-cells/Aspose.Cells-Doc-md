---
title: Как добавить условное форматирование Гистограммы данных
description: Как использовать библиотеку Aspose.Cells для Python via .NET для применения условного форматирования Data Bars. Настраивая эти критерии, у вас есть больший контроль над внешним видом и отображением ячеек.
keywords: Aspose.Cells, Условное форматирование Data Bars, Python, Условное, Форматирование
type: docs
weight: 70
url: /ru/python-net/how-to-add-databars-conditional-formatting/
---

## **Возможные сценарии использования**
Использование гистограмм данных в условном форматировании — мощный (и визуальный!) способ быстро понять ваши данные.

1. Визуальное сравнение значений: гистограммы превращают числа в горизонтальные полосы, что облегчает сравнение значений — как мини-гистограмма внутри ячеек!
1. Немедленное распознавание шаблонов: вы можете мгновенно видеть пики, минимумы и выбросы без сортировки или анализа чисел.
1. Лучшая читаемость: особенно полезно в длинных таблицах — уменьшает когнитивную нагрузку и помогает быстро понять ключевые тенденции.
1. Динамично и в реальном времени: при изменении значений полосы автоматически обновляются — отлично для отслеживания живых метрик, прогресса или KPI.
1. Профессиональный внешний вид панелей: придает отчетам или панелям чистый, современный и аккуратный вид.

## **Как добавить условное форматирование с гистограммами данных в Excel**
Чтобы добавить условное форматирование с гистограммами данных в Excel, выполните следующие шаги:

1. Выделите диапазон данных, например: C2:C20 — это могут быть продажи, оценки или показатели прогресса.
1. Перейдите на вкладку Главная на ленте.
1. Нажмите условное форматирование в группе Стиль.
1. Наведите указатель на Гистограммы данных.
1. Выберите стиль: градиент заливки (полосы плавно переходят слева направо) или заливка сплошным цветом.
1. Нажмите на понравившийся стиль — и всё готово!

## **Как добавить условное форматирование Data Bars с помощью Aspose.Cells для Python via .NET**

Aspose.Cells для Python via .NET полностью поддерживает условное форматирование, предоставляемое Microsoft Excel 2007 и более новыми версиями в формате XLSX для ячеек во время выполнения. Этот пример демонстрирует упражнение по условному форматированию DataBars с разными наборами атрибутов.

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
