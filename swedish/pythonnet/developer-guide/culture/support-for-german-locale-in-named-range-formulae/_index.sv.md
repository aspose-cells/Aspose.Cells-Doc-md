---
title: Stöd för tyskt lokalt språk i namngivna cellområden med Python.NET
linktitle: Stöd för tysk lokal i namnformler
type: docs
weight: 60
url: /sv/python-net/support-for-german-locale-in-named-range-formulae/
description: Lär dig hur man hanterar tyskägda inställningar för namngivna området i Excel med Aspose.Cells för Python via .NET.
---

Engelska formler skrivs i namngivna regioner. Denna Excel-fil kan öppnas i en miljö där systemet är konfigurerat för tyskt språk, och den engelska formeln ska översättas till tyska. Detta exempel kräver att Excel är installerat med tyskt språk och systemets lokal är konfigurerad till tyskt.

Testfil för att prova denna funktion kan laddas ner från:  
[sampleNamedRangeTest.xlsm](73990165.xlsm)

```python
import os
from aspose.cells import Workbook

source_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "source")
output_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), "output")

name = "HasFormula"
value = "=GET.CELL(48, INDIRECT(\"ZS\",FALSE))"

wb_source = Workbook(os.path.join(source_dir, "sampleNamedRangeTest.xlsm"))
ws_col = wb_source.worksheets

name_index = ws_col.names.add(name)
named_range = ws_col.names[name_index]
named_range.refers_to = value

if not os.path.exists(output_dir):
    os.makedirs(output_dir)

wb_source.save(os.path.join(output_dir, "sampleOutputNamedRangeTest.xlsm"))
```
{{< app/cells/assistant language="python-net" >}}
