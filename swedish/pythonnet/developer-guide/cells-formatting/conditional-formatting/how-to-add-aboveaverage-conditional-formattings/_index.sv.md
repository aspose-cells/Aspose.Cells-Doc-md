---
title: Hur man lägger till Villkorlig formatering för över medelvärde
description: Hur man använder Aspose.Cells för Python via .NET biblioteket för att tillämpa Ovanså Intensiv villkorlig formatering. Genom att justera dessa kriterier, får du mer kontroll över hur celler ser ut och visas.
keywords: Aspose.Cells, Över Genomsnittlig Villkorlig Formatering, Python, Villkorlig, Formatering
type: docs
weight: 70
url: /sv/python-net/how-to-add-above-average-conditional-formatting/
---

## **Möjliga användningsscenario**
Att använda Villkorlig formatering för över medelvärde i verktyg som Microsoft Excel eller Google Sheets är ett snabbt och visuellt sätt att markera utstickande data—specifikt värden som är högre än medelvärdet i ett område. Här är varför du kanske vill använda det:
1. Snabbt upptäcka trender: Det hjälper dig att omedelbart identifiera högpresterande värden utan att manuellt beräkna medelvärden eller skanna igenom siffror.
1. Förenkla dataanalysen: Du behöver inte beräkna eller mata in några formler—det är ett automatisk sätt att tillämpa logikbaserad formatering, vilket sparar tid.
1. Förbättra visuell tilltalande: Färgkodning hjälper till att göra ditt kalkylblad lättare att läsa och mer visuellt engagerande, särskilt under presentationer.
1. Understödja beslutsfattande: Att snabbt identifiera värden över medelvärdet kan driva åtgärder, som att belöna högpresterare eller undersöka varför vissa produkter presterar bättre än andra.

## **Hur man lägger till Villkorlig formatering för över medelvärde i Excel**
För att lägga till Villkorlig formatering för över medelvärde i Excel, gör så här steg för steg:

1. Markera det cellområde du vill tillämpa formateringen på. Till exempel: A1:A20.
1. Gå till fliken Hem i menyfliksområdet.
1. Klicka på Villkorsstyrd formatering i Stilar-gruppen.
1. Hovra över Top/Bottom Rules.
1. Klicka på Över medelvärde...
1. I dialogrutan som visas: Den upptäcker automatiskt "Format a celler som är OVAN medelvärdet." Du kan ändra formateringsstilen genom att klicka på rullgardinsmenyn bredvid (t.ex. välja en färgfyllning eller anpassad formatering).
1. Klicka på OK. Alla celler i ditt valda område som är över medelvärdet för det området kommer att markeras.


## **Hur man lägger till Över-Genomsnittlig Villkorlig Formatering med Aspose.Cells för Python via .NET**

Aspose.Cells för Python via .NET stöder fullt ut den villkorliga formateringen som tillhandahålls av Microsoft Excel 2007 och senare versioner i XLSX-format på celler i realtid. Det här exemplet visar ett övningsexempel för Över-Genomsnittlig villkorlig formatering med olika uppsättningar av attribut.

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
