---
title: Specificare le cifre significative da memorizzare in un file Excel con Python.NET
linktitle: Specificare le cifre significative
type: docs
weight: 30
url: /it/python-net/specifying-significant-digits-to-be-stored-in-excel-file/
description: Impara come controllare le cifre significative memorizzate nei file Excel usando l’API Aspose.Cells per Python via .NET.
---

## **Possibili Scenari di Utilizzo**

Per impostazione predefinita, Aspose.Cells memorizza 17 cifre significative di valori double all’interno del file Excel, a differenza di MS-Excel che memorizza solo 15 cifre significative. Puoi cambiare questo comportamento da 17 a 15 cifre significative usando l’attributo [**CellsHelper.significant_digits**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/significant_digits/).

## **Specifica delle cifre significative da memorizzare nel file Excel**

Il seguente esempio di codice fornisce Aspose.Cells per l’uso di 15 cifre significative durante la memorizzazione di valori double. Controlla il [file excel di output](22774105.xlsx) (cambia l’estensione in .zip per ispezionare i valori memorizzati). Lo screenshot sotto mostra come questa impostazione influisce sui valori memorizzati:

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Codice di Esempio**

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
