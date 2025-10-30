---
title: So fügen Sie Datenbalken Bedingte Formatierung hinzu
description: So verwenden Sie die Aspose.Cells for Python via .NET Bibliothek, um Data Bars bedingte Formatierung anzuwenden. Durch Anpassen dieser Kriterien haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells, Data Bars Bedingte Formatierung, Python, Bedingung, Formatierung
type: docs
weight: 70
url: /de/python-net/how-to-add-databars-conditional-formatting/
---

## **Mögliche Verwendungsszenarien**
Die Verwendung von Datenbalken in der bedingten Formatierung ist eine kraftvolle (und visuelle!) Möglichkeit, Ihre Daten auf einen Blick zu verstehen.

1. Visueller Vergleich von Werten: Datenbalken verwandeln Zahlen in horizontale Balken, was den Vergleich von Werten nebeneinander superleicht macht — wie ein kleines Balkendiagramm in Ihren Zellen!
1. Sofortige Mustererkennung: Sie können sofort Hochs, Tiefs und Ausreißer sehen, ohne Zahlen zu sortieren oder zu scannen.
1. Bessere Lesbarkeit: Besonders nützlich in langen Tabellen — es reduziert die kognitive Belastung und hilft Ihnen, wichtige Trends schnell zu erfassen.
1. Dynamisch & Echtzeit: Wenn sich Werte ändern, aktualisieren sich die Balken automatisch — perfekt zum Verfolgen von Live-Metriken, Fortschritten oder KPIs.
1. Professionell aussehende Dashboards: Verleiht Berichten oder Dashboards ein sauberes, modernes und gepflegtes Aussehen.

## **So fügen Sie Datenbalken-Bedingte Formatierung mit Excel hinzu**
Um Datenbalken-Bedingte Formatierung in Excel hinzuzufügen, gehen Sie Schritt für Schritt wie folgt vor:

1. Wählen Sie Ihren Datenbereich aus, zum Beispiel: C2:C20 — das könnten Verkaufszahlen, Punktzahlen oder Fortschrittswerte sein.
1. Gehen Sie auf die Registerkarte Start im Menüband.
1. Klicken Sie auf Bedingte Formatierung in der Gruppe Stil.
1. Bewegen Sie den Mauszeiger über Datenbalken.
1. Wählen Sie einen Stil: Farbverlauf (Balken verblassen von links nach rechts) oder Festfüllung (Balken mit einer einheitlichen Farbe).
1. Klicken Sie auf den Stil, den Sie mögen — fertig!

## **Wie man Data Bars bedingte Formatierung mit Aspose.Cells für Python via .NET hinzufügt**

Aspose.Cells für Python via .NET unterstützt die von Microsoft Excel 2007 und neueren Versionen in XLSX-Format bereitgestellte bedingte Formatierung vollständig zur Laufzeit auf Zellen. Dieses Beispiel demonstriert eine Übung für DataBars bedingte Formatierung mit verschiedenen Attributsets.

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
