---
title: Supporto per Locale Tedesco nelle formule dei Nomi con Python.NET
linktitle: Supporto per la localizzazione in tedesco nelle formule dei nomi
type: docs
weight: 60
url: /it/python-net/support-for-german-locale-in-named-range-formulae/
description: Impara come gestire le impostazioni locali tedesche per le formule di intervallo denominato in Excel usando Aspose.Cells for Python via .NET.
---

Le formule in inglese sono scritte nelle regioni nominate. Questo file Excel può essere aperto in un ambiente in cui il sistema è configurato per il locale tedesco, e la formula inglese sarà tradotta in lingua tedesca. Questo esempio richiede Excel installato con impostazioni di lingua tedesca e locale di sistema configurato in tedesco.

Il file di esempio per testare questa funzionalità può essere scaricato da:  
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
