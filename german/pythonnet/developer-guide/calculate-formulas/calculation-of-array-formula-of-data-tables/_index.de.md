---
title: Berechnung von Array Formeln in Datentabellen mit Python.NET
linktitle: Berechnung der Array Formel von DatenTabellen
type: docs
weight: 70
url: /de/python-net/calculation-of-array-formula-of-data-tables/
description: Lernen Sie, wie man Array Formeln für Excel Datentabellen mit Aspose.Cells für Python via .NET API berechnet, um Überschriften zu modifizieren und Tabellen programmatisch zu speichern.
keywords: Python Excel Datentabellen, Python Array Formeln, Aspose.Cells Python, DatenTabellen in Python berechnen, Excel Automatisierung in Python
---

{{% alert color="primary" %}}

Sie können in Microsoft Excel eine Datentabelle erstellen, indem Sie Data > What-If-Analysis > Data Table... verwenden. Aspose.Cells für Python via .NET ermöglicht die Berechnung der Array-Formel einer Datentabelle. Bitte verwenden Sie [**workbook.calculate_formula()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) wie üblich, um beliebige Formeln zu berechnen.

{{% /alert %}}

Im folgenden Beispiel verwenden wir die [quell Excel-Datei](5115535.xlsx). Wenn Sie den Wert der Zelle B1 auf 100 ändern, aktualisieren sich die Werte der Daten-Tabelle (gelb hervorgehoben) auf 120, wie die Screenshots unten zeigen. Der Python-Code generiert diese [Ausgabedatei](5115538.pdf).

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_1.png)

![todo:image_alt_text](calculation-of-array-formula-of-data-tables_2.png)

Unten ist die Python-Implementierung, die demonstriert, wie man die [Ausgabedatei](5115538.pdf) aus der [Quell Excel-Datei](5115535.xlsx) generiert:

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

**Python-Code-Erklärung:**
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
