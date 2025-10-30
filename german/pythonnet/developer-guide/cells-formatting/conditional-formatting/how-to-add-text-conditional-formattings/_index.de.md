---
title: Wie man Text Bedingte Formatierung hinzufügt
description: Wie man die Aspose.Cells für Python via .NET Bibliothek verwendet, um Text bedingte Formatierung anzuwenden. Durch Anpassen dieser Kriterien haben Sie mehr Kontrolle darüber, wie Zellen aussehen und erscheinen.
keywords: Aspose.Cells, Text Bedingte Formatierung, Python, Bedingung, Formatierung
type: docs
weight: 70
url: /de/python-net/how-to-add-text-conditional-formatting/
---

## **Mögliche Verwendungsszenarien**
Die textbasierte bedingte Formatierung in Tabellenkalkulationen ist nützlich, um Zellen hervorzuheben, die bestimmte textuelle Kriterien erfüllen. Dies kann die Datenanalyse verbessern und es erleichtern, wichtige Informationen in einem großen Datensatz zu finden. Hier sind einige Gründe für die Verwendung von Text-Bedingter Formatierung:

1. Spezifischen Text hervorheben: Sie können Formatierungen basierend auf bestimmten Wörtern, Phrasen oder Zeichen anwenden. Zum Beispiel möchten Sie alle Zellen hervorheben, die das Wort "Urgent" oder "Completed" enthalten, um Aufgaben in einem Projekt leicht zu unterscheiden.
1. Muster oder Trends erkennen: Wenn Sie mit Kategorien oder Status arbeiten (wie "Hoch", "Mittel", "Niedrig"), kann die textbasierte bedingte Formatierung diese visuell unterscheiden, was die Fortschrittsverfolgung oder Priorisierung erleichtert.
1. Fehler- oder Dateneingabenwarnungen: Textformatierungen können inkonsistente oder fehlerhafte Eingaben kennzeichnen, wie falsch geschriebene Wörter, unvollständiger Text oder falsche Werte. Dies ist besonders in Datensätzen mit viel Texteingaben nützlich.
1. Verbesserte Lesbarkeit: Farbcodierung von Text oder Änderung seines Stils (fett, kursiv usw.) hilft, wichtige Informationen hervorzuheben und verbessert die Gesamtlesbarkeit Ihres Blattes.
1. Dynamisches Feedback: Sie können Regeln einrichten, die die Formatierung automatisch anpassen, wenn Text bestimmte Bedingungen erfüllt. Das bedeutet, dass Sie die Formatierung nicht manuell aktualisieren müssen, wenn sich die Daten ändern.

Kurz gesagt, hilft Ihnen die bedingte Textformatierung schnell relevante Informationen, Fehler und Trends zu erkennen und ist ein leistungsstarkes Werkzeug für das Management und die Interpretation von Textdaten.

## **Wie man Text-Bedingte Formatierung mit Excel hinzufügt**
Um die textbasierte bedingte Formatierung in Excel hinzuzufügen, folgen Sie diesen Schritten:

1. Zellenbereich auswählen: Markieren Sie die Zellen, auf die Sie die bedingte Formatierung anwenden möchten.
1. Öffnen Sie das Menü für bedingte Formatierung: Gehen Sie zum Start-Tab im Excel-Ribbons. Klicken Sie auf „Bedingte Formatierung“ in der Gruppe „Stile“.
1. Wählen Sie „Neue Regel“: Wählen Sie im Dropdown-Menü „Neue Regel“.
1. Wählen Sie „Nur Zellen formatieren, die enthalten“: Im Dialogfeld für Neue Formatierungsregel wählen Sie „Nur Zellen formatieren, die enthalten“ unter dem Abschnitt „Regeltyp auswählen“.
1. Legen Sie die Regelkriterien fest: Im Abschnitt "Formatieren Sie Zellen mit" wählen Sie aus dem Dropdown "Bestimmter Text". Wählen Sie entweder "enthalten", "beginnen mit" oder "enden mit", je nach Bedingung, die Sie anwenden möchten. Geben Sie den Text ein, den Sie formatieren möchten (z.B. ein bestimmtes Wort wie "Dringend" oder "Abgeschlossen").
1. Format auswählen: Klicken Sie auf die Schaltfläche Format. Im Dialogfeld Zellen formatieren können Sie die Schriftfarbe, Füllfarbe oder andere Formatierungsoptionen nach Wunsch auswählen.
1. Regel anwenden: Sobald Sie das gewünschte Format eingestellt haben, klicken Sie auf OK, um die Regel anzuwenden. Klicken Sie erneut auf OK im Dialogfeld Neue Formatierungsregel, um es zu schließen.
1. Ergebnisse anzeigen: Die Zellen, die den angegebenen Text enthalten, werden jetzt entsprechend formatiert, was das Erkennen relevanter Informationen erleichtert.


## **Wie man Text bedingte Formatierung mit Aspose.Cells für Python via .NET hinzufügt**

Aspose.Cells für Python via .NET unterstützt die von Microsoft Excel 2007 und neueren Versionen in XLSX-Format bereitgestellte bedingte Formatierung vollständig zur Laufzeit auf Zellen. Diese Beispiele demonstrieren eine Übung für fortgeschrittene Arten der bedingten Formatierung, einschließlich BeginsWith, ContainsBlank, ContainsText und so weiter.

### **Zelle formatieren, wenn der Wert mit bestimmtem Text beginnt**

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

        self.add_begin_with()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_begin_with.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)


    def add_begin_with(self):
        conds = self.get_format_condition("E15:G16", Color.light_goldenrod_yellow)
        idx = conds.add_condition(FormatConditionType.BEGINS_WITH)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.text = "ab"
        self._sheet.cells.get("E15").put_value("abc")
        self._sheet.cells.get("G16").put_value("babx")


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
### **Zelle formatieren, wenn der Wert Leer enthält**

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

        self.add_contains_blank()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_contains_blank.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)

    def add_contains_blank(self):
        conds = self.get_format_condition("E9:G10", Color.light_blue)
        idx = conds.add_condition(FormatConditionType.CONTAINS_BLANKS)
        cond = conds[idx]
        cond.style.background_color = Color.yellow
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E9").put_value("  ")
        self._sheet.cells.get("G10").put_value("  ")

```

### **Zelle formatieren, wenn der Wert Fehler enthält**

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

        self.add_contains_error()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_contains_error.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)


    def add_contains_error(self):
        conds = self.get_format_condition("E17:G18", Color.light_sky_blue)
        idx = conds.add_condition(FormatConditionType.CONTAINS_ERRORS)
        cond = conds[idx]
        cond.style.background_color = Color.yellow
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E17").put_value("  ")
        self._sheet.cells.get("G18").put_value("  ")

```

### **Zelle formatieren, wenn der Wert bestimmten Text enthält**

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

        self.add_contains_text()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_contains_text.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)

    def add_contains_text(self):
        conds = self.get_format_condition("E5:G6", Color.light_blue)
        idx = conds.add_condition(FormatConditionType.CONTAINS_TEXT)
        cond = conds[idx]
        cond.style.background_color = Color.yellow
        cond.style.pattern = BackgroundType.SOLID
        cond.text = "1"

```

### **Zelle formatieren, wenn der Wert doppelte Werte enthält**

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

        self.add_duplicate()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_duplicate.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)

    def add_duplicate(self):
        conds = self.get_format_condition("E23:G24", Color.light_slate_gray)
        idx = conds.add_condition(FormatConditionType.DUPLICATE_VALUES)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E23").put_value("bb")
        self._sheet.cells.get("G24").put_value("bb")

```

### **Zelle formatieren, wenn der Wert mit bestimmtem Text endet**

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

        self.add_end_with()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_end_with.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)


    def add_end_with(self):
        conds = self.get_format_condition("E13:G14", Color.light_gray)
        idx = conds.add_condition(FormatConditionType.ENDS_WITH)
        cond = conds[idx]
        cond.style.background_color = Color.yellow
        cond.style.pattern = BackgroundType.SOLID
        cond.text = "ab"
        self._sheet.cells.get("E13").put_value("nnnab")
        self._sheet.cells.get("G14").put_value("mmmabc")

```

### **Zelle formatieren, wenn der Wert Leer nicht enthält**

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

        self.add_not_contains_blank()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_not_contains_blank.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)

    def add_not_contains_blank(self):
        conds = self.get_format_condition("E11:G12", Color.light_coral)
        idx = conds.add_condition(FormatConditionType.NOT_CONTAINS_BLANKS)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E11").put_value("abc")
        self._sheet.cells.get("G12").put_value("  ")

```

### **Zelle formatieren, wenn der Wert Fehler nicht enthält**

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

        self.add_not_contains_error()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_not_contains_error.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)

    def add_not_contains_error(self):
        conds = self.get_format_condition("E19:G20", Color.light_sea_green)
        idx = conds.add_condition(FormatConditionType.NOT_CONTAINS_ERRORS)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E19").put_value("  ")
        self._sheet.cells.get("G20").put_value("  ")

```

### **Zelle formatieren, wenn der Wert bestimmten Text nicht enthält**

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

        self.add_not_contains_text()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_not_contains_text.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)

    def add_not_contains_text(self):
        conds = self.get_format_condition("E7:G8", Color.light_coral)
        idx = conds.add_condition(FormatConditionType.NOT_CONTAINS_TEXT)
        cond = conds[idx]
        cond.style.background_color = Color.pink
        cond.style.pattern = BackgroundType.SOLID
        cond.text = "3"
```

### **Zelle formatieren, wenn der Wert eindeutige Werte enthält**

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

        self.add_unique()        

        self._sheet.auto_fit_column(12)
        output_dir = os.path.join(data_dir, "output")
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        out_fn = os.path.join(output_dir, "add_unique.out.xlsx")
        book.save(out_fn, SaveFormat.XLSX)


    def add_unique(self):
        conds = self.get_format_condition("E21:G22", Color.light_salmon)
        idx = conds.add_condition(FormatConditionType.UNIQUE_VALUES)
        cond = conds[idx]
        cond.style.background_color = Color.yellow
        cond.style.pattern = BackgroundType.SOLID
        self._sheet.cells.get("E21").put_value("aa")
        self._sheet.cells.get("G22").put_value("aa")

```

{{< app/cells/assistant language="python-net" >}}
