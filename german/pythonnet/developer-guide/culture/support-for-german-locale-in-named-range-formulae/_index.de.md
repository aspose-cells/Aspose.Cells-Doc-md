---
title: Unterstützung für deutsche Lokale in benannten Bereich Formeln mit Python.NET
linktitle: Unterstützung für das deutsche Gebietsschema in benannten Bereichsformeln
type: docs
weight: 60
url: /de/python-net/support-for-german-locale-in-named-range-formulae/
description: Erfahren Sie, wie man deutsche Gebietseinstellungen für benannte Bereichsformeln in Excel mit Aspose.Cells für Python via .NET handhabt.
---

Englische Formeln werden in benannten Bereichen geschrieben. Diese Excel-Datei kann in einer Umgebung geöffnet werden, in der die Systemeinstellung auf Deutsch konfiguriert ist, und die englische Formel wird ins Deutsche übersetzt. Dieses Beispiel erfordert, dass Excel mit deutschen Spracheinstellungen installiert ist und das System auf Deutsch eingestellt ist.

Beispiel-Datei zum Testen dieser Funktion kann heruntergeladen werden von:  
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
