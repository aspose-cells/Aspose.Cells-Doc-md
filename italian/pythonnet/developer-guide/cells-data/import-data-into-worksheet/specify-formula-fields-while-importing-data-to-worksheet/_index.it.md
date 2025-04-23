---
title: Specificare i campi Formula durante l importazione dei dati nel foglio di lavoro con Python via .NET
linktitle: Specificare i campi della formula durante l importazione dei dati nel foglio di lavoro
type: docs
weight: 300
url: /it/python-net/specify-formula-fields-while-importing-data-to-worksheet/
description: Scopri come specificare i campi formula durante l importazione dei dati nei fogli di lavoro usando Aspose.Cells per Python via .NET API.
keywords: Python specifica i campi formula durante l importazione dei dati, Python imposta le colonne delle formule durante l importazione dei dati, Aspose.Cells Python import delle formule
---

## **Possibili Scenari di Utilizzo**

Puoi specificare i campi formula durante l'importazione dei dati nel tuo foglio di lavoro usando la proprietà [**ImportTableOptions.is_formulas**](https://reference.aspose.com/cells/python-net/aspose.cells/importtableoptions/is_formulas/). Questa proprietà accetta una lista booleana in cui il valore **True** indica che il campo è una formula. Ad esempio, se il terzo campo è un campo formula, il terzo elemento della lista sarà **True**.

## **Specifica i campi formula durante l'importazione dei dati**

Il seguente esempio mostra come specificare i campi formula durante l'importazione dei dati. Guarda il file Excel di output generato ([output.xlsx](61767838.xlsx)) e lo screenshot che mostra i risultati.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Codice di Esempio**

```python
import os
from dataclasses import dataclass
from aspose.cells import Workbook, ImportTableOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

@dataclass
class DataItems:
    number1: int
    number2: int
    formula1: str
    formula2: str

def run():
    output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")
    os.makedirs(output_dir, exist_ok=True)

    dis = []
    dis.append(DataItems(2002, 3502, "=SUM(A2,B2)", "=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")"))
    dis.append(DataItems(2003, 3503, "=SUM(A3,B3)", "=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")"))
    dis.append(DataItems(2004, 3504, "=SUM(A4,B4)", "=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")"))
    dis.append(DataItems(2005, 3505, "=SUM(A5,B5)", "=HYPERLINK(\"https://www.aspose.com\",\"Aspose Website\")"))

    wb = Workbook()
    ws = wb.worksheets[0]

    opts = ImportTableOptions()
    opts.is_formulas = [False, False, True, True]

    ws.cells.import_custom_objects(dis, 0, 0, opts)

    wb.calculate_formula()
    ws.auto_fit_columns()

    output_path = os.path.join(output_dir, "outputSpecifyFormulaFieldsWhileImportingDataToWorksheet.xlsx")
    wb.save(output_path)

    print("SpecifyFormulaFieldsWhileImportingDataToWorksheet executed successfully.")

if __name__ == "__main__":
    run()
```
