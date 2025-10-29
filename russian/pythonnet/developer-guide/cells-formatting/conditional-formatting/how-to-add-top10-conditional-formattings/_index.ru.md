---
title: Как добавить условное форматирование Top10
description: Как использовать библиотеку Aspose.Cells для Python via .NET для применения условного форматирования Top10. Настраивая эти критерии, у вас есть больший контроль над внешним видом и отображением ячеек.
keywords: Aspose.Cells, Условное форматирование Top10, Python, Условное, Форматирование
type: docs
weight: 70
url: /ru/python-net/how-to-add-top10-conditional-formatting/
---

## **Возможные сценарии использования**
Использование условного форматирования Top 10 в Excel помогает быстро выделить самые успешные значения в наборе данных — не только фактические топ 10 значений, но и часто топ N или топ N% (вы можете выбрать!).

1. Обнаружение трендов и выбросов: мгновенно определяйте лучших исполнителей (например, топ 10 продавцов, лучшие оценки, месяцы с наибольшим доходом). Упрощает анализ без сортировки данных.
1. Визуализация данных: добавляет цветовые подсказки, которые делают важные показатели визуально заметными. Помогает пользователям таблицы быстро понять ключевые значения.
1. Быстрые сравнения: полезно в информационных панелях и отчетах, где нужно выделить лучшие показатели или пики.
1. Динамические обновления: если ваши данные изменятся, условное форматирование автоматически обновится, чтобы отразить новые топовые значения.

## **Как добавить условное форматирование Top10 в Excel**
Вот пошаговая инструкция по добавлению условного форматирования Top10 в Excel:

1. Выделите диапазон ячеек, который хотите проанализировать. Например, выберите B2:B100, если работаете с оценками или продажами.
1. Перейдите на вкладку Главная на ленте Excel.
1. Нажмите на Условное форматирование в группе Стиль.
1. Наведите курсор на Правила для верхних/нижних значений в выпадающем списке.
1. Выберите Верхние 10 элементов...
Появится диалоговое окно: оно скажет: Форматировать ячейки, которые занимают топ 10. Вы можете изменить число (например, Верхних 5, Верхних 3 и т.д.). Выберите формат (например, светло-красное заполнение, жирный текст или нажмите Настраиваемый формат для дополнительных опций).
1. Нажмите ОК


## **Как добавить условное форматирование Top10 с помощью Aspose.Cells для Python via .NET**

Aspose.Cells для Python via .NET полностью поддерживает условное форматирование, предоставляемое Microsoft Excel 2007 и более новыми версиями в формате XLSX для ячеек во время выполнения. Этот пример демонстрирует упражнение по условному форматированию Top 10 с разными наборами атрибутов.

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
