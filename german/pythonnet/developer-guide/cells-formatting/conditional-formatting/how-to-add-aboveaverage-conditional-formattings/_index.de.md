---
title: So fügen Sie bedingte Formatierung für den Durchschnitt hinzu
description: So verwenden Sie die Aspose.Cells for Python via .NET Bibliothek, um die bedingte Formatierung AboveAverage anzuwenden. Durch Anpassen dieser Kriterien haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells, AboveAverage Bedingte Formatierung, Python, Bedingung, Formatierung
type: docs
weight: 70
url: /de/python-net/how-to-add-above-average-conditional-formatting/
---

## **Mögliche Verwendungsszenarien**
Die Verwendung der bedingten Formatierung „Über Durchschnitt“ in Tools wie Microsoft Excel oder Google Sheets ist eine schnelle und visuelle Methode, um herausragende Daten hervorzuheben—insbesondere Werte, die höher als der Durchschnitt in einem Bereich sind. Hier erfahren Sie warum:
1. Trends schnell erkennen: Es hilft Ihnen, leistungsstarke Werte sofort zu identifizieren, ohne Durchschnittswerte manuell zu berechnen oder Zahlen zu scannen.
1. Datenanalyse vereinfachen: Sie müssen keine Formeln berechnen oder eingeben—es ist eine automatische Methode, um logikbasierte Formatierung anzuwenden, Zeit zu sparen.
1. Visuelle Attraktivität erhöhen: Farbige Markierungen machen Ihre Tabelle leichter lesbar und optisch ansprechender, insbesondere bei Präsentationen.
1. Unterstützt Entscheidungsfindung: Das schnelle Erkennen von Werten über dem Durchschnitt kann Aktionen vorantreiben, wie das Belohnen leistungsstarker Mitarbeiter oder das Untersuchen von Gründen, warum bestimmte Produkte andere übertreffen.

## **So fügen Sie die bedingte Formatierung „Über Durchschnitt“ in Excel hinzu**
So fügen Sie in Excel die bedingte Formatierung „Über Durchschnitt“ Schritt für Schritt hinzu:

1. Wählen Sie den Zellbereich aus, auf den Sie die Formatierung anwenden möchten. Zum Beispiel: A1:A20.
1. Gehen Sie auf die Registerkarte Start im Menüband.
1. Klicken Sie auf Bedingte Formatierung im Bereich styles.
1. Bewegen Sie den Mauszeiger über Top/Bottom-Regeln.
1. Klicken Sie auf Über Durchschnitt...
1. Im erscheinenden Dialogfeld erkennt es automatisch "Zellen formatieren, die ÜBER dem Durchschnitt liegen." Sie können den Formatierungsstil ändern, indem Sie die Dropdown-Liste neben (z. B. eine Farbfüllung oder benutzerdefiniertes Format) verwenden.
1. Klicken Sie auf OK. Alle Zellen in Ihrem ausgewählten Bereich, die über dem Durchschnitt dieses Bereichs liegen, werden hervorgehoben.


## **So fügen Sie die Above Average Bedingte Formatierung mit Aspose.Cells for Python via .NET hinzu**

Aspose.Cells for Python via .NET unterstützt die von Microsoft Excel 2007 und neueren Versionen in XLSX-Format bereitgestellte bedingte Formatierung vollständig zur Laufzeit auf Zellen. Dieses Beispiel zeigt eine Übung für die Above Average-Bedingte Formatierung mit verschiedenen Attributsets.

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
