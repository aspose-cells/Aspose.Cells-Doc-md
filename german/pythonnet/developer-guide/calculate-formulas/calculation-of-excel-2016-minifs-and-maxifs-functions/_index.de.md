---
title: Berechnung der Excel 2016 MINIFS und MAXIFS Funktionen mit Python.NET
linktitle: Berechnung der Excel 2016 MINIFS und MAXIFS Funktionen
type: docs
weight: 300
url: /de/python-net/calculation-of-excel-2016-minifs-and-maxifs-functions/
description: Erfahren Sie, wie man Excel 2016 MINIFS und MAXIFS Funktionen mit Aspose.Cells für Python via .NET API berechnet, inklusive Codebeispiele.
keywords: python excel, minifs maxifs, Formelbehandlung, aspose.cells
---

## **Mögliche Verwendungsszenarien**
Microsoft Excel 2016 unterstützt MINIFS- und MAXIFS-Funktionen. Diese Funktionen werden in Excel 2013 oder älteren Versionen nicht unterstützt. Aspose.Cells unterstützt ebenfalls die Berechnung dieser Funktionen. Das folgende Bildschirmfoto zeigt die Verwendung dieser Funktionen. Bitte lesen Sie die roten Kommentare im Screenshot, um zu verstehen, wie diese Funktionen funktionieren.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Berechnung der Excel 2016 MINIFS- und MAXIFS-Funktionen**
Der folgende Beispielcode lädt die [Beispieldatei](5115149.xlsx) und ruft die Methode [workbook.calculate_formula()](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) auf, um die Formelauswertung mithilfe von Aspose.Cells durchzuführen und die Ergebnisse in der [Ausgabedatei](5115154.pdf) zu speichern.


```python
import os
from aspose.cells import Workbook, PdfSaveOptions

# For complete examples and data files, please go to https://github.com/aspose-cells/Aspose.Cells-for-.NET

current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "data")
output_dir = os.path.join(current_dir, "output")

# Load your source workbook containing MINIFS and MAXIFS functions
workbook = Workbook(os.path.join(source_dir, "sampleMINIFSAndMAXIFS.xlsx"))

# Perform Aspose.Cells formula calculation
workbook.calculate_formula()

# Save the calculations result in pdf format
options = PdfSaveOptions()
options.one_page_per_sheet = True

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

workbook.save(os.path.join(output_dir, "outputMINIFSAndMAXIFS.pdf"), options)
```
{{< app/cells/assistant language="python-net" >}}
