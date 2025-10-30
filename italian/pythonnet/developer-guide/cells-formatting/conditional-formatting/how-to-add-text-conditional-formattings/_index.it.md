---
title: Come aggiungere la formattazione condizionale del testo
description: Come usare la libreria Aspose.Cells per Python via .NET per applicare la formattazione condizionale Text. Modificando questi criteri, puoi avere un maggiore controllo sull aspetto e sulle apparenze delle celle.
keywords: Aspose.Cells, Formattazione Condizionale Text, Python, Condizionale, Formattazione
type: docs
weight: 70
url: /it/python-net/how-to-add-text-conditional-formatting/
---

## **Possibili Scenari di Utilizzo**
Usare la formattazione condizionale basata su testo nei fogli di calcolo è utile per evidenziare le celle che soddisfano criteri testuali specifici. Questo può migliorare l'analisi dei dati e rendere più facile trovare informazioni chiave in un grande set di dati. Ecco alcune ragioni per usare la formattazione condizionale del testo:

1. Evidenziare testo specifico: Puoi applicare formattazione basata su parole, frasi o caratteri specifici. Per esempio, potresti voler evidenziare tutte le celle che contengono la parola "Urgente" o "Completato" per differenziare facilmente i compiti in un progetto.
1. Identificare schemi o tendenze: Se lavori con categorie o stati (come "Alto", "Medio", "Basso"), la formattazione condizionale del testo può distinguere visivamente tra di loro, facilitando il monitoraggio dei progressi o la prioritizzazione dei compiti.
1. Avvisi di errore o inserimento dati: La formattazione del testo può segnalare inserimenti incoerenti o errati, come parole mal scritte, testo incompleto o valori incorretti. Questo è particolarmente utile in set di dati con molto input testuale.
1. Maggiore leggibilità: Codificare a colori il testo o cambiarne lo stile (grassetto, corsivo, ecc.) aiuta a far risaltare le informazioni importanti, migliorando la leggibilità complessiva del foglio.
1. Feedback dinamico: Puoi impostare regole che regolano automaticamente la formattazione quando il testo corrisponde a determinate condizioni. Ciò significa che non devi aggiornare manualmente la formattazione man mano che i dati cambiano.

In sostanza, la formattazione condizionale del testo ti aiuta a individuare rapidamente informazioni rilevanti, errori e tendenze, rendendola uno strumento potente per gestire e interpretare dati testuali.

## **Come aggiungere la formattazione condizionale del testo usando Excel**
Per aggiungere una formattazione condizionale basata su testo in Excel, segui questi passaggi:

1. Seleziona l’intervallo di celle: Evidenzia le celle su cui vuoi applicare la formattazione condizionale.
1. Apri il menu di formattazione condizionale: Vai alla scheda Home nella barra di Excel. Clicca su Formattazione condizionale nel gruppo "Stili".
1. Scegli “Nuova regola”: Dal menu a discesa, seleziona Nuova regola.
1. Seleziona “Formatta solo le celle che contengono”: Nella finestra di dialogo Nuova regola di formattazione, scegli Formatta solo le celle che contengono sotto la sezione "Seleziona un tipo di regola".
1. Imposta i criteri della regola: Nella sezione "Formatta celle con", scegli Testo specifico dal menu a discesa. Seleziona contiene, inizia con o termina con, a seconda della condizione che vuoi applicare. Inserisci il testo che desideri formattare (ad esempio, una parola specifica come "Urgente" o "Completato").
1. Scegli la formattazione: Clicca sul pulsante Formatta. Nella finestra di dialogo Formato celle, puoi selezionare il colore carattere, il colore riempimento o altre opzioni di formattazione preferite.
1. Applica la regola: Una volta impostato il formato desiderato, clicca su OK per applicare la regola. Clicca nuovamente OK nella finestra di dialogo della Nuova regola di formattazione per chiuderla.
1. Visualizza i risultati: Le celle contenenti il testo specificato avranno ora la formattazione applicata, facilitando l’individuazione delle informazioni rilevanti.


## **Come aggiungere la formattazione condizionale Text usando Aspose.Cells per Python via .NET**

Aspose.Cells per Python via .NET supporta pienamente la formattazione condizionale fornita da Microsoft Excel 2007 e versioni successive in formato XLSX sulle celle in fase di esecuzione. Questo esempio dimostra un esercizio di formattazione condizionale avanzata tra cui BeginsWith, ContainsBlank, ContainsText e altri.

### **Formatta la cella quando il valore inizia con il testo specificato**

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
### **Formatta la cella quando il valore contiene uno spazio vuoto**

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

### **Formatta la cella quando il valore contiene errori**

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

### **Formatta la cella quando il valore contiene testo specificato**

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

### **Formatta cella quando il valore contiene valori duplicati**

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

### **Formatta cella quando il valore termina con testo specificato**

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

### **Formatta cella quando il valore non contiene vuoto**

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

### **Formatta cella quando il valore non contiene errori**

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

### **Formatta cella quando il valore non contiene testo specificato**

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

### **Formatta cella quando il valore contiene valori unici**

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
