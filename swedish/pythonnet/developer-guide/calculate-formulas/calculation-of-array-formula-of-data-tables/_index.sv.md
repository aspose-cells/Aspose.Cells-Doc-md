---
title: Beräkning av arrayformel för data tabeller med Python.NET
linktitle: Beräkning av Data Table Arrayformel
type: docs
weight: 70
url: /sv/python-net/calculation-of-array-formula-of-data-tables/
description: Lär dig hur du beräknar arrayformler för Excel data tabeller med Aspose.Cells för Python via .NET API. Modifiera och spara kalkylblad programmatiskt.
keywords: Python Excel Data Tabeller, Python Array Formler, Aspose.Cells Python, Beräkna Data Tabeller Python, Excel Automation Python
---

{{% alert color="primary" %}}

Du kan skapa Data Tabell i Microsoft Excel med Data > Analys > Vad-Om-Analys > Data Tabell.... Aspose.Cells för Python via .NET tillåter dig att beräkna arrayformeln för en data tabell. Använd [**workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) som vanligt för att beräkna vilken formel som helst.

{{% /alert %}}

I följande exempel använder vi [källfilen för Excel](5115535.xlsx). Om du ändrar värdet i cell B1 till 100 kommer värdena i Data Tabellen (markerad i gult) att uppdateras till 120 som visas i skärmbilderna nedan. Python-koden genererar detta [utdata PDF](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Nedan är Python-implementeringen som demonstrerar hur man genererar [utdata PDF](5115538.pdf) från [källfilen för Excel](5115535.xlsx):

```python
import os
from aspose.cells import Workbook

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Create workbook from source excel file
workbook = Workbook(os.path.join(data_dir, "DataTable.xlsx"))

# Access first worksheet
worksheet = workbook.worksheets[0]

# When you will put 100 in B1, then all Data Table values formatted as Yellow will become 120
worksheet.cells.get("B1").put_value(100)

# Calculate formula, now it also calculates Data Table array formula
workbook.calculate_formula()

# Save the workbook in pdf format
workbook.save(os.path.join(data_dir, "output_out.pdf"))
```

**Förklaring av Python-koden:**
```python
import aspose.cells as ac

# Load source workbook
workbook = ac.Workbook("5115535.xlsx")

# Calculate formulas using Python.NET API
workbook.calculate_formula()

# Save the workbook in PDF format
workbook.save("5115538.pdf", ac.SaveFormat.PDF)
```
{{< app/cells/assistant language="python-net" >}}
