---
title: Come aggiungere la formattazione condizionale Top10
description: Come usare la libreria Aspose.Cells per Python via .NET per applicare la formattazione condizionale Top10. Modificando questi criteri, puoi avere un maggiore controllo sull aspetto e sulle apparenze delle celle.
keywords: Aspose.Cells, Formattazione Condizionale Top10, Python, Condizionale, Formattazione
type: docs
weight: 70
url: /it/python-net/how-to-add-top10-conditional-formatting/
---

## **Possibili Scenari di Utilizzo**
Usare la formattazione condizionale Top 10 in Excel aiuta a evidenziare rapidamente i valori con le prestazioni più alte in un dataset — non solo i top 10 valori letterali, ma spesso i top N valori o N% (puoi scegliere!).

1. Individua tendenze e anomalie: identifica istantaneamente i migliori (ad esempio, i 10 migliori venditori, le migliori note, i mesi con maggiori ricavi). Facilita l'analisi senza ordinare i dati.
1. Visualizzazione dei dati: aggiunge segnali visivi che rendono i punti dati importanti più visibili. Aiuta chi guarda il foglio di calcolo a comprendere i valori chiave a colpo d'occhio.
1. Confronti rapidi: Utile nei cruscotti e nei report in cui si desidera evidenziare l'eccellenza o i picchi.
1. Aggiornamenti dinamici: Se i tuoi dati cambiano, la formattazione condizionale si aggiorna automaticamente per riflettere i nuovi valori principali.

## **Come aggiungere la formattazione condizionale Top10 usando Excel**
Ecco come puoi aggiungere la formattazione condizionale Top10 in Excel, passo dopo passo:

1. Seleziona l'intervallo di celle che desideri analizzare. Ad esempio: Seleziona B2:B100, se lavori con punteggi o numeri di vendita.
1. Vai alla scheda Home sulla barra multifunzione di Excel.
1. Clicca su Formattazione condizionale nel gruppo Stili.
1. Passa sopra Regole Top/Bottone nel menu a discesa.
1. Fai clic su Elementi Top 10...
1. Apparirà una finestra di dialogo: Indicherà: Formatta le celle che si classificano tra le prime 10. Puoi modificare il numero (ad esempio Top 5, Top 3, ecc.). Scegli un formato (come riempimento rosato chiaro, testo in grassetto, o clicca su Formato personalizzato per altre opzioni).
1. Clicca OK


## **Come aggiungere la formattazione condizionale Top10 usando Aspose.Cells per Python via .NET**

Aspose.Cells per Python via .NET supporta pienamente la formattazione condizionale fornita da Microsoft Excel 2007 e versioni successive in formato XLSX sulle celle in fase di esecuzione. Questo esempio dimostra un esercizio di formattazione condizionale Top 10 con diversi set di attributi.

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
