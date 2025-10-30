---
title: Hur man lägger till villkorsstyrd formattering med datastavar
description: Hur man använder Aspose.Cells för Python via .NET biblioteket för att tillämpa Datastaplar villkorlig formatering. Genom att justera dessa kriterier får du mer kontroll över hur cellerna ser ut och framstår.
keywords: Aspose.Cells, Datastaplar Villkorlig Formatering, Python, Villkorlig, Formatering
type: docs
weight: 70
url: /sv/python-net/how-to-add-databars-conditional-formatting/
---

## **Möjliga användningsscenario**
Att använda datastavar i villkorsstyrd formatering är ett kraftfullt (och visuellt!) sätt att snabbt förstå dina data.

1. Visuell jämförelse av värden: Datastavar förvandlar siffror till horisontella staplar, vilket gör det extremt enkelt att jämföra värden sida vid sida — som ett mini-stapeldiagram inuti cellerna!
1. Omedelbar mönsterigenkänning: Du kan direkt se toppar, dalar och avvikelser utan att sortera eller skanna siffror.
1. Bättre läsbarhet: Särskilt användbart i långa tabeller — det minskar den kognitiva belastningen och hjälper dig att snabbt förstå nyckeltrender.
1. Dynamiskt och i realtid: När värdena ändras uppdateras staplarna automatiskt — perfekt för att spåra live-mått, framsteg eller KPI:er.
1. Professionella instrumentpaneler: Ger en ren, modern och polerad look till rapporter eller instrumentpaneler.

## **Hur man lägger till villkorsstyrd formatering med datastavar med Excel**
För att lägga till villkorsstyrd formatering med datastavar i Excel, gör så här steg för steg:

1. Välj ditt dataområde, till exempel: C2:C20 — detta kan vara försäljningssiffror, poäng eller framstegs värden.
1. Gå till fliken Hem i menyfliksområdet.
1. Klicka på Villkorsstyrd formatering i gruppen Stilar.
1. Håll muspekaren över Datastavar.
1. Välj en stil: Gradientfyllning (staplar tonar från vänster till höger) och Solid Fill (staplar har en solid färg).
1. Klicka på den stil du gillar — och du är klar!

## **Hur man lägger till Datastaplar villkorlig formatering med Aspose.Cells för Python via .NET**

Aspose.Cells för Python via .NET stöder fullt ut den villkorsbaserade formateringen som erbjuds av Microsoft Excel 2007 och senare versioner i XLSX-format på celler i realtid. Detta exempel visar ett övningsexempel för Datastaplar villkorsformatering med olika uppsättningar av attribut.

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
