---
title: Hur man lägger till textbaserad villkorsstyrd formatering
description: Hur man använder Aspose.Cells för Python via .NET för att tillämpa Text villkorlig formatering. Genom att justera dessa kriterier får du mer kontroll över hur cellerna ser ut och framstår.
keywords: Aspose.Cells, Text Villkorlig Formatering, Python, Villkorlig, Formatering
type: docs
weight: 70
url: /sv/python-net/how-to-add-text-conditional-formatting/
---

## **Möjliga användningsscenario**
Att använda textbaserad villkorsstyrd formatering i kalkylblad är användbart för att markera celler som uppfyller specifika textkrav. Detta kan förbättra dataanalys och göra det lättare att hitta nyckelinformation i en stor datamängd. Här är några anledningar till att använda textbaserad villkorsstyrd formatering:

1. Markera särskild text: Du kan tillämpa formatering baserat på specifika ord, fraser eller tecken. Till exempel kan du vilja markera alla celler som innehåller ordet "Brådskande" eller "Avslutad" för att enkelt särskilja uppgifter i ett projekt.
1. Identifiera mönster eller trender: Om du arbetar med kategorier eller statusar (som "Hög", "Medium", "Låg") kan textbaserad villkorsstyrd formatering visuellt skilja mellan dem, vilket gör det lättare att följa framsteg eller prioritera uppgifter.
1. Fel- eller dataregistreringsvarningar: Textformatering kan flagga inkonsekventa eller felaktiga inmatningar, som stavfel, ofullständig text eller felaktiga värden. Detta är särskilt användbart i dataset med mycket textinmatning.
1. Förbättrad läsbarhet: Färgmärkning av text eller ändring av stil (fet, kursiv osv.) hjälper till att framhäva viktig information, vilket förbättrar det övergripande läsbarheten.
1. Dynaisk feedback: Du kan skapa regler som automatiskt justerar formateringen när text matchar vissa villkor. Detta innebär att du inte behöver uppdatera formateringen manuellt när data ändras.

Kort sagt hjälper textbaserad villkorsstyrd formatering dig att snabbt upptäcka relevant information, fel och trender, vilket gör det till ett kraftfullt verktyg för att hantera och tolka textuell data.

## **Hur man lägger till textvillkorsstyrd formatering med Excel**
För att lägga till textbaserad villkorsstyrd formatering i Excel, följ dessa steg:

1. Markera cellområdet: Markera de celler där du vill tillämpa villkorsstyrd formatering.
1. Öppna menyn Villkorsstyrd formatering: Gå till fliken Start i Excel-rollen. Klicka på Villkorsstyrd formatering i "Stilar"-gruppen.
1. Välj "Nytt regel": Från rullgardinsmenyn, välj Ny regel.
1. Välj "Formatera endast celler som innehåller": I dialogrutan Ny formatregel, välj Formatera endast celler som innehåller under avsnittet "Välj regeltyp".
1. Ange regelkriterier: I avsnittet "Formatera celler med", välj Specifik text från rullgardinen. Välj antingen innehåller, börjar med eller slutar med, beroende på villkoret du vill tillämpa. Ange den text du vill formatera (t.ex. ett specifikt ord som "Brådskande" eller "Avslutad").
1. Välj formateringen: Klicka på knappen Formatera. I dialogrutan Formatera celler kan du välja teckensfärg, fyllnadsfärg eller andra formateringsalternativ.
1. Tillämpa regeln: När du har ställt in önskad formatering klickar du OK för att tillämpa regeln. Klicka på OK igen i dialogrutan Ny formatregel för att stänga den.
1. Visa resultaten: Cellerna som innehåller den angivna texten kommer nu att ha den tillämpliga formateringen, vilket gör det enkelt att hitta relevant information.


## **Hur man lägger till Text Villkorlig Formatering med Aspose.Cells för Python via .NET**

Aspose.Cells för Python via .NET stöder fullt ut den villkorsbaserade formateringen som erbjuds av Microsoft Excel 2007 och senare versioner i XLSX-format på celler i realtid. Dessa exempel visar en övning för avancerade typer av villkorsformatering inklusive BörjarMed, InnehållerTom, InnehållerText och så vidare.

### **Formatera cell när värdet börjar med specifik text**

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
### **Formatera cell när värdet innehåller tomt**

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

### **Formatera cell när värdet innehåller fel**

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

### **Formatera cell när värdet innehåller angiven text**

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

### **Formatera cell när värdet innehåller dubbletter**

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

### **Formatera cell när värdet slutar med specificerad text**

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

### **Formatera cell när värdet inte innehåller tomt**

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

### **Formatera cell när värdet inte innehåller fel**

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

### **Formatera cell när värdet inte innehåller specificerad text**

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

### **Formatera cell när värdet innehåller unika värden**

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
