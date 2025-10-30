---
title: Angabe von signifikanten Ziffern zum Speichern in Excel Dateien mit Python.NET
linktitle: Festlegung der signifikanten Ziffern
type: docs
weight: 30
url: /de/python-net/specifying-significant-digits-to-be-stored-in-excel-file/
description: Erfahren Sie, wie Sie mithilfe der Aspose.Cells für Python via .NET API steuern können, wie viele signifikante Ziffern in Excel Dateien gespeichert werden.
---

## **Mögliche Verwendungsszenarien**

Standardmäßig speichert Aspose.Cells für Python via .NET 17 signifikante Ziffern von Double-Werten in der Excel-Datei, im Gegensatz zu MS-Excel, das nur 15 signifikante Ziffern speichert. Sie können dieses Verhalten von 17 auf 15 signifikante Ziffern ändern mit dem Attribut [**CellsHelper.significant_digits**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/significant_digits/).

## **Angabe von signifikanten Ziffern, die in der Excel-Datei gespeichert werden sollen**

Der folgende Beispielcode erzwingt, dass Aspose.Cells 15 signifikante Ziffern verwendet, wenn Double-Werte gespeichert werden. Überprüfen Sie die [Ausgabedatei Excel](22774105.xlsx) (ändern Sie die Erweiterung in .zip, um die gespeicherten Werte zu inspizieren). Das folgende Bild zeigt, wie diese Einstellung die gespeicherten Werte beeinflusst:

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Beispielcode**

```python
from aspose.cells import Workbook, CellsHelper
import aspose.cells
import os
import pytest

# Set significant digits to 15
CellsHelper.set_significant_digits(15)

# Create new workbook
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Set value with extended precision
cell = worksheet.cells.get("A1")
cell.put_value(1234567890123456.001234567890123456)

# Save modified workbook
workbook.save("output.xlsx")
```

```python
import os
from aspose.cells import Workbook, CellsHelper

# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Set significant digits to 15 like MS-Excel
CellsHelper.set_significant_digits(15)

# Create workbook
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Access cell A1
c = worksheet.cells.get("A1")

# Put double value with 15 significant digits
c.put_value(1234567890.123451711)

# Save the workbook
output_dir = os.path.join(current_dir, "output")
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

workbook.save(os.path.join(output_dir, "out_SignificantDigits.xlsx"))
```
{{< app/cells/assistant language="python-net" >}}
