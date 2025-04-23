---
title: Beräkning av Excel 2016 MINIFS och MAXIFS funktioner med Python.NET
linktitle: Beräkning av Excel 2016 MINIFS och MAXIFS funktioner
type: docs
weight: 300
url: /sv/python-net/calculation-of-excel-2016-minifs-and-maxifs-functions/
description: Lär dig hur du beräknar Excel 2016 MINIFS och MAXIFS funktioner med Aspose.Cells för Python via .NET API med kodexempel.
keywords: python excel, minifs maxifs, formelberäkning, aspose.cells
---

## **Möjliga användningsscenario**
Microsoft Excel 2016 stöder MINIFS och MAXIFS funktioner. Dessa funktioner stöds inte i Excel 2013 eller äldre versioner. Aspose.Cells stöder också beräkningen av dessa funktioner. Följande skärmbild illustrerar användningen av dessa funktioner. Läs de röda kommentarerna inuti skärmbilden för att förstå hur dessa funktioner fungerar.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Beräkning av Excel 2016 MINIFS och MAXIFS funktioner**
Följande kodexempel laddar [exempel-Excelfilen](5115149.xlsx) och anropar [workbook.calculate_formula()](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) för att utföra formelberäkningen via Aspose.Cells, och sparar sedan resultaten i [utdata PDF](5115154.pdf).


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
