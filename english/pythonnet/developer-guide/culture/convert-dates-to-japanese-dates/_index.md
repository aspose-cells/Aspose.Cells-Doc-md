---
title: Convert Dates to Japanese Dates with Python.NET
linktitle: Convert Dates to Japanese Dates
type: docs
weight: 350
url: /python-net/convert-dates-to-japanese-dates/
description: Learn how to convert Gregorian dates to Japanese dates in Excel files using Aspose.Cells for Python via .NET.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}} 

In the Japanese calendar, a new era begins with the reign of a new emperor. On 1 May 2019, a new emperor came into power, ending the Heisei era and beginning the Reiwa era.

{{% /alert %}} 

Aspose.Cells provides a way to convert Gregorian dates to Japanese dates while considering era changes. The following code snippet demonstrates converting a source Excel file containing Gregorian dates to a PDF output with Japanese dates:

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)

```python
import os
from aspose.cells import Workbook, LoadOptions, LoadFormat, SaveFormat, CountryCode

# Source directory
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "data")
output_dir = os.path.join(current_dir, "output")

# Create output directory if it does not exist
if not os.path.exists(output_dir):
    os.makedirs(output_dir)

# Initialize load options with XLSX format
options = LoadOptions(LoadFormat.XLSX)
options.region = CountryCode.JAPAN

# Load workbook with Japanese regional settings
workbook = Workbook(os.path.join(source_dir, "JapaneseDates.xlsx"), options)

# Save as PDF
workbook.save(os.path.join(output_dir, "JapaneseDates.pdf"), SaveFormat.PDF)
```

**Python.NET Conversion:**


Note: Ensure Japanese language support is enabled in your environment for accurate era conversions. The [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) class and [PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) provide the necessary functionality for this conversion.
{{< app/cells/assistant language="python-net" >}}
