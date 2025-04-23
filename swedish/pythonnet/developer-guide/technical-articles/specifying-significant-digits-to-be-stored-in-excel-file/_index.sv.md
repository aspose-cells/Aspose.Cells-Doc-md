---
title: Att specificera viktiga siffror som ska lagras i Excel fil med Python.NET
linktitle: Angivande av signifikanta siffror
type: docs
weight: 30
url: /sv/python-net/specifying-significant-digits-to-be-stored-in-excel-file/
description: Läs hur du kan kontrollera viktiga siffror som lagras i Excel filer med Aspose.Cells för Python via .NET API.
---

## **Möjliga användningsscenario**

Som standard lagrar Aspose.Cells 17 viktiga siffror av dubbla värden inuti Excel-filen, till skillnad från MS-Excel som bara lagrar 15 viktiga siffror. Du kan ändra detta beteende från 17 till 15 viktiga siffror med hjälp av [**CellsHelper.significant_digits**](https://reference.aspose.com/cells/python-net/aspose.cells/cellshelper/significant_digits/)-egenskapen.

## **Ange signifikanta siffror som ska lagras i Excel-fil**

Följande exempelkravforce Aspose.Cells att använda 15 viktiga siffror när dubbla värden lagras. Kontrollera gärna [utdataexcel-fil](22774105.xlsx) (ändra förlängning till .zip för att inspektera lagrade värden). Nedan visas hur denna inställning påverkar lagrade värden.

![todo:image_alt_text](specifying-significant-digits-to-be-stored-in-excel-file_1.png)

## **Exempelkod**

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
