---
title: Come aggiungere la formattazione condizionale con barre dati
description: Come usare la libreria Aspose.Cells per Python via .NET per applicare la formattazione condizionale Data Bars. Modificando questi criteri, puoi avere un maggiore controllo sull aspetto e sulle apparenze delle celle.
keywords: Aspose.Cells, Formattazione Condizionale Data Bars, Python, Condizionale, Formattazione
type: docs
weight: 70
url: /it/python-net/how-to-add-databars-conditional-formatting/
---

## **Possibili Scenari di Utilizzo**
Usare le barre dati nella formattazione condizionale è un modo potente (e visivo!) per comprendere i tuoi dati a colpo d'occhio.

1. Confronto visivo dei valori: le barre dati trasformano i numeri in barre orizzontali, rendendo molto facile confrontare i valori fianco a fianco — come un mini grafico a barre all'interno delle tue celle!
1. Riconoscimento immediato dei pattern: puoi vedere istantaneamente massimi, minimi e outlier senza ordinare o scansionare i numeri.
1. Migliore leggibilità: particolarmente utile in tabelle lunghe — riduce il carico cognitivo e aiuta a cogliere rapidamente le tendenze chiave.
1. Dinamico & in tempo reale: man mano che i valori cambiano, le barre si aggiornano automaticamente — ottimo per monitorare metriche, progresso o KPI in tempo reale.
1. Dashboard dal look professionale: aggiunge un aspetto pulito, moderno e curato ai report o ai dashboard.

## **Come aggiungere la formattazione condizionale con barre dati usando Excel**
Per aggiungere la formattazione condizionale con barre dati in Excel, ecco come puoi farlo passo passo:

1. Seleziona l'intervallo di dati, ad esempio: C2:C20 — questo potrebbe essere vendite, punteggi o valori di progresso.
1. Vai alla scheda Home sulla barra multifunzione.
1. Clicca su Formattazione condizionale nel gruppo Stili.
1. Passa sopra le Barre Dati.
1. Scegli uno stile: Riempimento gradiente (le barre sfumano da sinistra a destra) e Riempimento solido (le barre hanno un colore solido).
1. Clicca sullo stile che preferisci — e hai finito!

## **Come aggiungere la formattazione condizionale Data Bars usando Aspose.Cells per Python via .NET**

Aspose.Cells per Python via .NET supporta pienamente la formattazione condizionale fornita da Microsoft Excel 2007 e versioni successive in formato XLSX sulle celle in fase di esecuzione. Questo esempio dimostra un esercizio di formattazione condizionale DataBars con diversi set di attributi.

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
