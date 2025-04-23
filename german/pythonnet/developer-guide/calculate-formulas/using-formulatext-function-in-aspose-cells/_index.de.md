---
title: Verwendung der FormulaText Funktion in Aspose.Cells mit Python.NET
linktitle: Verwendung der FormulaText Funktion
type: docs
weight: 60
url: /de/python-net/using-formulatext-function-in-aspose-cells/
description: Erfahren Sie, wie Sie mit Aspose.Cells für Python via .NET die Excel Funktion FORMULATEXT verwenden. Holen Sie sich und setzen Sie Zellformeln programmatisch, während Sie die Tabellenkalkulation integrieren.
keywords: Aspose.Cells, Python, Excel, FORMULATEXT, Formelhandschlag, Tabellenkalkulationsautomatisierung
---

{{% alert color="primary" %}} 

FORMULATEXT ist eine Funktion ab Excel 2013. Wird von älteren Versionen wie Excel 2010 oder 2007 nicht unterstützt. Wie der Name schon sagt, zeigt sie den Formeltext einer angegebenen Zelle an. Dieser Artikel zeigt, wie man diese Funktion mit Aspose.Cells für Python via .NET verwendet.

{{% /alert %}} 

Das folgende Beispiel zeigt die Verwendung von FORMULATEXT mit Aspose.Cells. Der Code schreibt zuerst eine Formel in Zelle A1 und zeigt dann den Formelttexteintrag mit FORMULATEXT in Zelle A2 an.

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

## **Konsolenausgabe**
Hier ist die Konsolenausgabe des obigen Beispielcodes:

{{< highlight python >}}
=SUM(B1:B10)
{{< /highlight >}}
