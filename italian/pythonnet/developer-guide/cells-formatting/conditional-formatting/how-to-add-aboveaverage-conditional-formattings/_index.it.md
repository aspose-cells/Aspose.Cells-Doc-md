---
title: Come Aggiungere la Formattazione Condizionale sopra la Media
description: Come usare la libreria Aspose.Cells for Python via .NET per applicare la formattazione condizionale sopra la media. Regolando questi criteri, hai più controllo su come le celle appaiono e si visualizzano.
keywords: Aspose.Cells, Formattazione Condizionale sopra la Media, Python, Condizionale, Formattazione
type: docs
weight: 70
url: /it/python-net/how-to-add-above-average-conditional-formatting/
---

## **Possibili Scenari di Utilizzo**
Usare la formattazione condizionale sopra la media in strumenti come Microsoft Excel o Google Sheets è un modo rapido e visivo per evidenziare dati che si distinguono—specificamente, valori più alti della media in un intervallo. Ecco perché potresti usarlo:
1. Rilevare Tendenze Velocemente: Ti aiuta a identificare istantaneamente valori ad alte prestazioni senza calcolare manualmente le medie o scansionare i numeri.
1. Semplificare l'Analisi dei Dati: Non è necessario calcolare o inserire formule—è un modo automatico di applicare una formattazione basata sulla logica, risparmiando tempo.
1. Migliorare l'Attrattiva Visiva: La codifica tramite colori aiuta a rendere il foglio di calcolo più facile da leggere e più coinvolgente visualmente, specialmente durante le presentazioni.
1. Supporta le Decisioni: Riconoscere rapidamente valori sopra la media può guidare azioni, come premiare i più performanti o investigare perché alcuni prodotti superano gli altri.

## **Come aggiungere la formattazione condizionale sopra la media usando Excel**
Per aggiungere la formattazione condizionale sopra la media in Excel, ecco come fare passo dopo passo:

1. Seleziona l'intervallo di celle a cui vuoi applicare la formattazione. Ad esempio: A1:A20.
1. Vai alla scheda Home sulla barra multifunzione.
1. Clicca su Formattazione condizionale nel gruppo Stili.
1. Passa sopra Regole Top/Bottom.
1. Clicca su Sopra la Media...
1. Nella finestra di dialogo che appare: Rileverà automaticamente "Formatta le celle che sono SOPRA la media." Puoi cambiare lo stile di formattazione cliccando sulla freccia accanto a con (ad esempio, scegliere un riempimento di colore o una formattazione personalizzata).
1. Clicca su OK. Tutte le celle nel tuo intervallo selezionato che sono sopra la media di quell'intervallo saranno evidenziate.


## **Come Aggiungere la Formattazione Condizionale sopra la Media Usando Aspose.Cells per Python via .NET**

Aspose.Cells for Python via .NET supporta pienamente la formattazione condizionale fornita da Microsoft Excel 2007 e versioni successive in formato XLSX sui celle in tempo reale. Questo esempio mostra un esercizio di formattazione condizionale sopra la media con set di attributi diversi.

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
