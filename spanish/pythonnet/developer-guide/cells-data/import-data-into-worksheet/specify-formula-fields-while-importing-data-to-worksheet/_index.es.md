---
title: Especificar campos de fórmula al importar datos a una hoja de trabajo con Python via .NET
linktitle: Especificar Campos de Fórmula al Importar Datos a la Hoja de Cálculo
type: docs
weight: 300
url: /es/python-net/specify-formula-fields-while-importing-data-to-worksheet/
description: Aprende cómo especificar campos de fórmula al importar datos a hojas de trabajo usando Aspose.Cells para Python via .NET API.
keywords: Especificar campos de fórmula durante la importación de datos en Python, configurar columnas de fórmula al importar datos, Aspose.Cells Python importación de fórmulas
---

## **Escenarios de uso posibles**

Puedes especificar campos de fórmula al importar datos en tu hoja de trabajo usando la propiedad [**ImportTableOptions.is_formulas**](https://reference.aspose.com/cells/python-net/aspose.cells/importtableoptions/is_formulas/). Esta propiedad acepta una lista booleana donde el valor **True** indica que el campo es una fórmula. Por ejemplo, si el tercer campo es un campo de fórmula, el tercer elemento de la lista será **True**.

## **Especificar campos de fórmula durante la importación de datos**

El siguiente ejemplo demuestra cómo especificar campos de fórmula al importar datos. Vea el archivo de Excel de salida generado ([archivo de ejemplo](61767838.xlsx)) y la captura de pantalla que muestra los resultados.

![todo:image_alt_text](specify-formula-fields-while-importing-data-to-worksheet_1.png)

## **Código de muestra**

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
