---
title: Använda FormelText funktionen i Aspose.Cells med Python.NET
linktitle: Använda FormelText funktionen
type: docs
weight: 60
url: /sv/python-net/using-formulatext-function-in-aspose-cells/
description: Lär dig hur man arbetar med Excels FORMULATEXT funktion med Aspose.Cells för Python via .NET. Hämta och sätt cellformler programmatiskt samtidigt som du bevarar kalkylbladets integritet.
keywords: Aspose.Cells, Python, Excel, FORMULATEXT, formelhantering, kalkylbladsautomation
---

{{% alert color="primary" %}} 

FORMULATEXT är en Excel 2013 och senare funktion. Den stöds inte av tidigare versioner som Excel 2010 eller 2007 etc. Som namnet antyder visar den formeltexten som finns i en specificerad cell. Den här artikeln visar hur man använder denna funktion med Aspose.Cells för Python via .NET.

{{% /alert %}} 

Följande kodexempel demonstrerar användningen av FORMULATEXT med Aspose.Cells. Koden skriver först en formel i cell A1 och visar sedan formeltexten med FORMULATEXT i cell A2.

```python
from aspose.cells import Workbook

# Create a workbook object
workbook = Workbook()

# Access first worksheet
worksheet = workbook.worksheets[0]

# Put some formula in cell A1
cell_a1 = worksheet.cells.get("A1")
cell_a1.formula = "=Sum(B1:B10)"

# Get the text of the formula in cell A2 using FORMULATEXT function
cell_a2 = worksheet.cells.get("A2")
cell_a2.formula = "=FormulaText(A1)"

# Calculate the workbook
workbook.calculate_formula()

# Print the results of A2, It will now print the text of the formula inside cell A1
print(cell_a2.string_value)
```

## **Konsoloutput**
Här är konsolutmatningen för ovanstående exempel:

{{< highlight python >}}
=SUM(B1:B10)
{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
