---
title: Calcolo delle funzioni MINIFS e MAXIFS di Excel 2016 con Python.NET
linktitle: Calcolo delle funzioni MINIFS e MAXIFS di Excel 2016
type: docs
weight: 300
url: /it/python-net/calculation-of-excel-2016-minifs-and-maxifs-functions/
description: Impara come calcolare le funzioni MINIFS e MAXIFS di Excel 2016 usando l API Aspose.Cells per Python via .NET con esempi di codice.
keywords: python excel, minifs maxifs, calcolo formula, aspose.cells
---

## **Possibili Scenari di Utilizzo**
Microsoft Excel 2016 supporta le funzioni MINIFS e MAXIFS. Queste funzioni non sono supportate in Excel 2013 o versioni precedenti. Aspose.Cells supporta anche il calcolo di queste funzioni. La schermata seguente illustra l'uso di queste funzioni. Leggi i commenti rossi all'interno della schermata per capire come funzionano queste funzioni.

![todo:image_alt_text](calculation-of-excel-2016-minifs-and-maxifs-functions_1.png)

## **Calcolo delle funzioni MINIFS e MAXIFS di Excel 2016**
Il seguente esempio di codice carica il [file excel di esempio](5115149.xlsx) e chiama il metodo [workbook.calculate_formula()](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/) per eseguire il calcolo delle formule tramite Aspose.Cells, quindi salva i risultati in un [PDF di output](5115154.pdf).


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
