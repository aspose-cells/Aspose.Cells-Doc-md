---
title: Как добавить условное форматирование выше среднего
description: Как использовать библиотеку Aspose.Cells for Python via .NET для применения условного форматирования «Выше среднего». Настраивая эти критерии, у вас появляется больше контроля над внешним видом и отображением ячеек.
keywords: Aspose.Cells, условное форматирование «Выше среднего», Python, условие, форматирование
type: docs
weight: 70
url: /ru/python-net/how-to-add-above-average-conditional-formatting/
---

## **Возможные сценарии использования**
Использование условного форматирования выше среднего в таких инструментах, как Microsoft Excel или Google Sheets, — быстрый и визуальный способ выделить выделяющиеся данные — особенно значения выше среднего в диапазоне. Вот почему вы можете использовать его:
1. Быстро выявляйте тренды: помогает мгновенно определить высокоэффективные значения без ручных расчетов среднего или поиска по числам.
1. Упростите анализ данных: вам не нужно рассчитывать или вводить формулы — это автоматический способ применения логики форматирования, что экономит время.
1. Повышайте визуальную привлекательность: цветовое кодирование помогает сделать таблицу более читаемой и визуально привлекательной, особенно во время презентаций.
1. Поддержка принятия решений: быстрое выявление значений выше среднего может стимулировать действия, такие как поощрение высокоэффективных сотрудников или расследование причин превосходства одних продуктов над другими.

## **Как добавить условное форматирование выше среднего в Excel**
Чтобы добавить условное форматирование выше среднего в Excel, выполните следующие шаги:

1. Выберите диапазон ячеек, к которому нужно применить форматирование. Например: A1:A20.
1. Перейдите на вкладку Главная на ленте.
1. Нажмите на Условное форматирование в группе Стиль.
1. Наведите на Правила верхней/нижней границы.
1. Нажмите Выше среднего...
1. В появившемся диалоговом окне: автоматически обнаружится "Форматировать ячейки, которые ВЫШЕ среднего." Вы можете изменить стиль форматирования, нажав на стрелку рядом с "с" (например, выбрать заливку цветом или пользовательский формат).
1. Нажмите ОК. Все ячейки в выбранном диапазоне, превышающие среднее значение этого диапазона, будут выделены.


## **Как добавить условное форматирование «Выше среднего» с помощью Aspose.Cells for Python via .NET**

Aspose.Cells for Python via .NET полностью поддерживает условное форматирование, предоставляемое Microsoft Excel 2007 и более поздними версиями в формате XLSX на этапе выполнения. Этот пример демонстрирует упражнение по условному форматированию «Выше среднего» с различными наборами атрибутов.

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
