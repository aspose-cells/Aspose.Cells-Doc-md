---
title: Konvertera datum till japanska datum med Python.NET
linktitle: Konvertera datum till japanska datum
type: docs
weight: 350
url: /sv/python-net/convert-dates-to-japanese-dates/
description: Lär dig hur man konverterar gregorianska datum till japanska datum i Excel filer med Aspose.Cells för Python via .NET.
---

{{% alert color="primary" %}} 

I det japanska kalendern börjar en ny era med en ny kejsares regeringstid. Den 1 maj 2019 trädde en ny kejsare till makten, vilket avslutade Heisei-eran och började Reiwa-eran.

{{% /alert %}} 

Aspose.Cells erbjuder ett sätt att konvertera gregorianska datum till japanska datum med hänsyn till erasbyten. Följande kodexempel visar hur man konverterar en källexcelfil med gregorianska datum till en PDF-utgång med japanska datum:

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)

```python
import os
from aspose.cells import Workbook, LoadOptions, LoadFormat, SaveFormat, CountryCode

# Source directory
current_dir = os.path.dirname(os.path.abspath(__file__))
source_dir = os.path.join(current_dir, "data")
output_dir = os.path.join(current_dir, "output")

# Create output directory if not exists
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

**Python.NET-konvertering:**


Obs: Se till att stödet för japanskt språk är aktiverat i din miljö för korrekt erasbyten. Klassen [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) och [PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) tillhandahåller nödvändig funktionalitet för denna konvertering.
{{< app/cells/assistant language="python-net" >}}
