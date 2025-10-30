---
title: So fügen Sie eine Top10 Bedingte Formatierung hinzu
description: So verwenden Sie die Aspose.Cells für Python via .NET Bibliothek, um Top10 Bedingungformatierung anzuwenden. Durch die Anpassung dieser Kriterien haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells, Top10 Bedingte Formatierung, Python, Bedingt, Formatierung
type: docs
weight: 70
url: /de/python-net/how-to-add-top10-conditional-formatting/
---

## **Mögliche Verwendungsszenarien**
Die Verwendung der Top 10-Bedingten Formatierung in Excel hilft, die leistungsstärksten Werte in einem Datensatz schnell hervorzuheben — nicht nur die tatsächlichen Top 10-Werte, sondern oft die Top N-Werte oder Top N% (Sie können wählen!).

1. Trends und Ausreißer erkennen: Identifizieren Sie sofort die besten Performer (z.B. Top 10 Verkäufer, beste Noten, umsatzstärkste Monate). Erleichtert die Analyse ohne Daten zu sortieren.
1. Datenvisualisierung: Fügt Farbcodierungen hinzu, die wichtige Datenpunkte visuell hervorheben. Hilft den Betrachtern des Tabellenblatts, die Schlüsselwerte auf einen Blick zu verstehen.
1. Schnelle Vergleiche: Nützlich in Dashboards und Berichten, bei denen Sie Exzellenz oder Spitzen hervorheben möchten.
1. Dynamische Aktualisierungen: Wenn sich Ihre Daten ändern, passt sich die bedingte Formatierung automatisch an, um die neuen Top-Werte widerzuspiegeln.

## **So fügen Sie Top10-Bedingte Formatierung mit Excel hinzu**
Hier erfahren Sie Schritt für Schritt, wie Sie Top10-Bedingte Formatierung in Excel hinzufügen:

1. Wählen Sie den Zellbereich aus, den Sie analysieren möchten. Zum Beispiel: Wählen Sie B2:B100, wenn Sie mit Punktzahlen oder Verkaufszahlen arbeiten.
1. Gehen Sie zur Registerkarte Start im Excel-Band.
1. Klicken Sie auf Bedingte Formatierung im Bereich styles.
1. Bewegen Sie den Mauszeiger über Top/Bottom-Regeln im Dropdown.
1. Klicken Sie auf Top 10 Elemente...
1. Es erscheint ein Dialogfeld: Es sagt: Zellen formatieren, die zu den Top 10 gehören. Sie können die Zahl ändern (z.B. Top 5, Top 3, etc.). Wählen Sie ein Format (z.B. hellroter Hintergrund, fetter Text oder klicken Sie auf Benutzerdefiniertes Format für mehr Optionen).
1. Klicken Sie auf OK


## **So fügen Sie Top10-Bedingte Formatierung mit Aspose.Cells für Python via .NET hinzu**

Aspose.Cells für Python via .NET unterstützt vollumfänglich die bedingte Formatierung, die von Microsoft Excel 2007 und späteren Versionen im XLSX-Format auf Zellen zur Laufzeit bereitgestellt wird. Dieses Beispiel demonstriert eine Übung für Top 10-Bedingungen mit unterschiedlichen Attributsätzen.

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
