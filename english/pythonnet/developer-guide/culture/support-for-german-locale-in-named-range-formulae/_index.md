---
title: Support for German Locale in Named Range Formulae with Python.NET
linktitle: Support for German Locale in Named Range Formulae
type: docs
weight: 60
url: /python-net/support-for-german-locale-in-named-range-formulae/
description: Learn how to handle German locale settings for named range formulas in Excel using Aspose.Cells for Python via .NET.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

English formulae are written into named regions. This Excel file can be opened in an environment where the system is configured to German locale, and the English formula shall be translated to German language. This example requires Excel installed with German language settings and system locale configured to German.

Sample file for testing this feature can be downloaded from:  
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
