---
title: Hur man lägger till Top10 villkorsstyrd formatering
description: Hur man använder Aspose.Cells för Python via .NET för att tillämpa Top10 villkorlig formatering. Genom att justera dessa kriterier får du mer kontroll över hur cellerna ser ut och framstår.
keywords: Aspose.Cells, Top10 Villkorlig Formatering, Python, Villkorlig, Formatering
type: docs
weight: 70
url: /sv/python-net/how-to-add-top10-conditional-formatting/
---

## **Möjliga användningsscenario**
Att använda Top 10 villkorsstyrd formatering i Excel hjälper dig att snabbt markera de värden som presterar bäst i en datamängd — inte bara de bokstavligen tio bästa, utan ofta de topp N värden eller topp N% (du kan välja!).

1. Upptäck trender och avvikare: Identifiera direkt de bästa prestaterna (t.ex. topp 10 säljare, bästa betyg, månader med högst intäkter). Gör det enkelt att analysera utan att sortera data.
1. Datavisualisering: Lägger till färgmarkeringar som gör viktiga datapunkter visuellt framhävda. Hjälper tittare av kalkylbladet att förstå nyckelvärdena i ett ögonblick.
1. Snabb jämförelse: Användbart i dashboards och rapporter där du vill lyfta fram excellens eller toppar.
1. Dynamiska uppdateringar: Om dina data ändras uppdateras den villkorsstyrda formateringen automatiskt för att återspegla de nya toppvärdena.

## **Hur man lägger till Top10 villkorsstyrd formatering med Excel**
Så här kan du steg för steg lägga till Top10 villkorsstyrd formatering i Excel:

1. Välj det cellområde du vill analysera. Till exempel: Välj B2:B100, om du arbetar med poäng eller försäljningssiffror.
1. Gå till fliken Hem i Excel-menyn.
1. Klicka på Villkorsstyrd formatering i Stilar-gruppen.
1. Håll muspekaren över Top/bottom-regler i rullgardinsmenyn.
1. Klicka på Top 10-objekt...
1. En dialogruta öppnas: Den säger: Formatera celler som rankas bland de 10 främsta. Du kan ändra numret (t.ex. Top 5, Top 3 osv.). Välj ett format (som en ljus röd fyllning, fet stil eller klicka på Anpassad formatering för fler alternativ).
1. Klicka på OK


## **Hur man lägger till Top10 villkorlig formatering med Aspose.Cells för Python via .NET**

Aspose.Cells för Python via .NET stöder fullt ut den villkorsbaserade formateringen som erbjuds av Microsoft Excel 2007 och senare versioner i XLSX-format på celler i realtid. Detta exempel visar ett övningsexempel för Top 10 villkorsformatering med olika uppsättningar av attribut.

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
