---
title: Как добавить условное форматирование с набором значков
description: Как использовать библиотеку Aspose.Cells для Python via .NET для применения условного форматирования Icon Sets. Настраивая эти критерии, у вас есть больший контроль над внешним видом и отображением ячеек.
keywords: Aspose.Cells, Условное форматирование IconSets, Python, Условное, Форматирование
type: docs
weight: 70
url: /ru/python-net/how-to-add-icon-sets-conditional-formatting/
---

## **Возможные сценарии использования**
Использование условного форматирования с наборами значков в Excel — отличный способ визуализировать тренды или категории данных с помощью символов, таких как стрелки, светофоры, звезды, флаги и другие. Это добавляет дополнительный уровень ясности к вашей таблице без необходимости создавать графики или глубокий анализ.

1. Мгновенные визуальные инсайты: значки позволяют легко увидеть, какие значения высокие, средние или низкие, без чтения каждого числа. Отлично для панелей управления, KPI и отслеживания эффективности.
1. Легкое определение трендов: стрелки показывают, увеличиваются или уменьшаются значения, или остаются без изменений. Светофоры или фигуры помогают показать статус или срочность.
1. Профессиональный внешний вид: делает отчеты более аккуратными и готовыми к презентациям. Помогает неспециалистам быстро понять данные.
1. Динамично и автоматически: обновляется автоматически при изменении значений — нет необходимости менять формат вручную.

## **Как добавить условное форматирование с наборами значков в Excel**
Чтобы добавить условное форматирование с наборами значков в Excel, выполните следующие шаги:

1. Выделите диапазон числовых данных. Например: B2:B20 (может быть, номера продаж, оценки эффективности и т.д.).
1. Перейдите на вкладку Главная.
1. Нажмите на Условное форматирование в группе Стиль.
1. Наведите указатель на Значки наборов.
1. Выберите стиль значка: стрелки, светофоры, звезды и т. д.
1. Значки будут отображаться по умолчанию в зависимости от распределения значений: Зеленый значок = верхние 67%, Желтый значок = средние 33–67%, Красный значок = нижние 33%.


## **Как добавить условное форматирование Icon Sets с помощью Aspose.Cells для Python via .NET**

Aspose.Cells для Python via .NET полностью поддерживает условное форматирование, предоставляемое Microsoft Excel 2007 и более новыми версиями в формате XLSX для ячеек во время выполнения. Этот пример демонстрирует упражнение по условному форматированию Icon Sets с разными наборами атрибутов.

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

        self.add_default_icon_set()
        self.add_icon_set2()
        self.add_icon_set3()
        self.add_icon_set4()
        self.add_icon_set5()
        self.add_icon_set6()
        self.add_icon_set7()
        self.add_icon_set8()
        self.add_icon_set9()
        self.add_icon_set10()
        self.add_icon_set11()
        self.add_icon_set12()
        self.add_icon_set13()
        self.add_icon_set14()
        self.add_icon_set15()
        self.add_icon_set16()
        self.add_icon_set17()
        self.add_icon_set18()

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "Testoutput.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)

    def add_icon_set2(self):
        conds = self.get_format_condition("M1:O2", Color.alice_blue)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.ARROWS3
        self._sheet.cells.get("M1").put_value("Arrows3")

    def add_icon_set3(self):
        conds = self.get_format_condition("M3:O4", Color.antique_white)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.ARROWS4
        self._sheet.cells.get("M3").put_value("Arrows4")

    def add_icon_set4(self):
        conds = self.get_format_condition("M5:O6", Color.aqua)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.ARROWS5
        self._sheet.cells.get("M5").put_value("Arrows5")

    def add_icon_set5(self):
        conds = self.get_format_condition("M7:O8", Color.aquamarine)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.ARROWS_GRAY3
        self._sheet.cells.get("M7").put_value("ArrowsGray3")

    def add_icon_set6(self):
        conds = self.get_format_condition("M9:O10", Color.azure)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.ARROWS_GRAY4
        self._sheet.cells.get("M9").put_value("ArrowsGray4")

    def add_icon_set7(self):
        conds = self.get_format_condition("M11:O12", Color.beige)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.ARROWS_GRAY5
        self._sheet.cells.get("M11").put_value("ArrowsGray5")

    def add_icon_set8(self):
        conds = self.get_format_condition("M13:O14", Color.bisque)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.FLAGS3
        self._sheet.cells.get("M13").put_value("Flags3")

    def add_icon_set9(self):
        conds = self.get_format_condition("M15:O16", Color.blanched_almond)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.QUARTERS5
        self._sheet.cells.get("M15").put_value("Quarters5")

    def add_icon_set10(self):
        conds = self.get_format_condition("M17:O18", Color.blue)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.RATING4
        self._sheet.cells.get("M17").put_value("Rating4")

    def add_icon_set11(self):
        conds = self.get_format_condition("M19:O20", Color.blue_violet)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.RATING5
        self._sheet.cells.get("M19").put_value("Rating5")

    def add_icon_set12(self):
        conds = self.get_format_condition("M21:O22", Color.brown)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.RED_TO_BLACK4
        self._sheet.cells.get("M21").put_value("RedToBlack4")

    def add_icon_set13(self):
        conds = self.get_format_condition("M23:O24", Color.burly_wood)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.SIGNS3
        self._sheet.cells.get("M23").put_value("Signs3")

    def add_icon_set14(self):
        conds = self.get_format_condition("M25:O26", Color.cadet_blue)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.SYMBOLS3
        self._sheet.cells.get("M25").put_value("Symbols3")

    def add_icon_set15(self):
        conds = self.get_format_condition("M27:O28", Color.chartreuse)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.SYMBOLS32
        self._sheet.cells.get("M27").put_value("Symbols32")

    def add_icon_set16(self):
        conds = self.get_format_condition("M29:O30", Color.chocolate)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.TRAFFIC_LIGHTS31
        self._sheet.cells.get("M29").put_value("TrafficLights31")

    def add_icon_set17(self):
        conds = self.get_format_condition("M31:O32", Color.coral)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.TRAFFIC_LIGHTS32
        self._sheet.cells.get("M31").put_value("TrafficLights32")

    def add_icon_set18(self):
        conds = self.get_format_condition("M33:O35", Color.cornflower_blue)
        idx = conds.add_condition(FormatConditionType.ICON_SET)
        cond = conds[idx]
        cond.icon_set.type = IconSetType.TRAFFIC_LIGHTS4
        self._sheet.cells.get("M33").put_value("TrafficLights4")

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

    def add_default_icon_set(self):
        self.get_format_condition("A1:C2", Color.yellow)

```
{{< app/cells/assistant language="python-net" >}}
