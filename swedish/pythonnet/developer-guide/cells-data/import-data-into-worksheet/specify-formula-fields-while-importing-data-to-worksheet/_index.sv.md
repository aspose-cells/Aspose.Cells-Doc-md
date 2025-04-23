---
title: Ange formelfält vid import av data till kalkylblad med Python via .NET
linktitle: Ange formelfält vid import av data till kalkylbladet
type: docs
weight: 300
url: /sv/python-net/specify-formula-fields-while-importing-data-to-worksheet/
description: Lär dig hur man anger formelfält vid import av data till kalkylblad med Aspose.Cells för Python via .NET API.
keywords: Python specificerar formelfält under datainmatning, Python ställer in formelkolumner när data importeras, Aspose.Cells Python formelimport
---

## **Möjliga användningsscenario**

Du kan specificera formelfält när du importerar data till ditt kalkylblad med egenskapen [**ImportTableOptions.is_formulas**](https://reference.aspose.com/cells/python-net/aspose.cells/importtableoptions/is_formulas/). Denna egenskap tar en boolesk lista där värdet **True** indikerar att fältet är en formel. Till exempel, om det tredje fältet är ett formelfält, kommer det tredje elementet i listan att vara **True**.

## **Specificera formelfält vid datainmatning**

Följande exempel visar hur man specificerar formelfält vid import av data. Se den genererade [utdata Excel-filen](61767838.xlsx) och skärmdump som visar resultaten.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Exempelkod**

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
