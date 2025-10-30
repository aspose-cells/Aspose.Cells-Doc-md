---
title: So fügen Sie Icon Sets Bedingte Formatierung hinzu
description: So verwenden Sie die Aspose.Cells for Python via .NET Bibliothek, um Icon Sets bedingte Formatierung anzuwenden. Durch Anpassen dieser Kriterien haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells, IconSets Bedingte Formatierung, Python, Bedingung, Formatierung
type: docs
weight: 70
url: /de/python-net/how-to-add-icon-sets-conditional-formatting/
---

## **Mögliche Verwendungsszenarien**
Die Verwendung von Icon Sets in der bedingten Formatierung in Excel ist eine großartige Möglichkeit, Daten-Trends oder Kategorien auf einen Blick mithilfe von Symbolen wie Pfeilen, Ampeln, Sternen, Flaggen und mehr zu visualisieren. Es verleiht Ihrer Tabelle eine zusätzliche Klarheit, ohne Diagramme oder tiefgehende Analysen zu erfordern.

1. Sofortige visuelle Einblicke: Symbole machen es superleicht, zu sehen, welche Werte hoch, mittel oder niedrig sind, ohne jede Zahl lesen zu müssen. Ideal für Dashboards, KPIs und Leistungsüberwachung.
1. Einfaches Trend-Spotting: Pfeile zeigen, ob Werte steigen, fallen oder neutral bleiben. Ampeln oder Formen helfen, Status oder Dringlichkeit anzuzeigen.
1. Professionelles Aussehen: Macht Berichte polierter und präsentationsbereit. Hilft nicht-technischen Betrachtern, Daten schnell zu verstehen.
1. Dynamisch & Automatisch: Aktualisiert sich automatisch, wenn sich Werte ändern — kein manuelles Neufomattieren notwendig.

## **So fügen Sie Icon Sets-Bedingte Formatierung mit Excel hinzu**
Um Icon Sets-Bedingte Formatierung in Excel hinzuzufügen, gehen Sie Schritt für Schritt wie folgt vor:

1. Wählen Sie Ihren Bereich mit numerischen Daten aus. Beispiel: B2:B20 (könnten Verkaufszahlen, Leistungswerte usw. sein).
1. Gehen Sie zum Start-Tab.
1. Klicken Sie auf Bedingte Formatierung im Bereich styles.
1. Bewegen Sie die Maus über Icon-Sätze.
1. Wählen Sie einen Symbolstil: Pfeile, Ampeln, Sterne usw.
1. Die Symbole erscheinen standardmäßig basierend auf der Wertverteilung: Grünes Icon = oberste 67 %, Gelbes Icon = mittlere 33–67 %, Rotes Icon = unterste 33 %.


## **So fügen Sie die Icon Sets bedingte Formatierung mit Aspose.Cells für Python via .NET hinzu**

Aspose.Cells für Python via .NET unterstützt die von Microsoft Excel 2007 und neueren Versionen in XLSX-Format bereitgestellte bedingte Formatierung vollständig zur Laufzeit auf Zellen. Dieses Beispiel zeigt eine Übung für Icon Sets bedingte Formatierung mit verschiedenen Attributsets.

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
