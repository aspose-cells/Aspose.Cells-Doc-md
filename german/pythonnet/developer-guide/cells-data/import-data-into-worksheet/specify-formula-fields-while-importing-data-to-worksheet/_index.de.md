---
title: Feldformeln beim Importieren von Daten in ein Arbeitsblatt mit Python angeben via .NET
linktitle: Formelfelder beim Importieren von Daten in das Arbeitsblatt angeben
type: docs
weight: 300
url: /de/python-net/specify-formula-fields-while-importing-data-to-worksheet/
description: Erfahren Sie, wie Sie beim Importieren von Daten in Arbeitsblätter mit Aspose.Cells für Python via .NET Feldformeln angeben.
keywords: Python Feldformeln beim Datenimport angeben, Python Formelspalten beim Importieren von Daten festlegen, Aspose.Cells Python Formelimport
---

## **Mögliche Verwendungsszenarien**

Sie können Formelfeldfelder beim Importieren von Daten in Ihr Arbeitsblatt mithilfe der [**ImportTableOptions.is_formulas**](https://reference.aspose.com/cells/python-net/aspose.cells/importtableoptions/is_formulas/)-Eigenschaft angeben. Diese Eigenschaft erwartet eine boolesche Liste, wobei der Wert **True** angibt, dass das Feld eine Formel ist. Wenn beispielsweise das dritte Feld ein Formelfeld ist, ist das dritte Element in der Liste **True**.

## **Formelfeld beim Datenimport angeben**

Das folgende Beispiel zeigt, wie man Formelfelder beim Datenimport angibt. Siehe die generierte [Ausgabedatei Excel](61767838.xlsx) und den Screenshot, der die Ergebnisse zeigt.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Beispielcode**

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
{{< app/cells/assistant language="python-net" >}}
