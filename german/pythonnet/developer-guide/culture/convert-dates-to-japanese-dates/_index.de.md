---
title: Datum in japanisches Datum mit Python.NET umwandeln
linktitle: Datumsangaben in japanische Datumsangaben konvertieren
type: docs
weight: 350
url: /de/python-net/convert-dates-to-japanese-dates/
description: Erfahren Sie, wie man Gregorianische Daten in japanische Daten in Excel Dateien mit Aspose.Cells für Python via .NET umwandelt.
---

{{% alert color="primary" %}} 

Im japanischen Kalender beginnt eine neue Ära mit der Herrschaft eines neuen Kaisers. Am 1. Mai 2019 kam ein neuer Kaiser an die Macht, mit dem die Heisei-Ära endete und die Reiwa-Ära begann.

{{% /alert %}} 

Aspose.Cells bietet eine Möglichkeit, gregorianische Daten in japanische Daten unter Berücksichtigung von Ärawechseln umzuwandeln. Das folgende Codesnippet zeigt, wie eine Quelldatei im Excel-Format mit gregorianischen Daten in eine PDF-Datei mit japanischen Daten konvertiert wird:

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

**Python.NET-Konvertierung:**


Hinweis: Stellen Sie sicher, dass die japanische Sprachunterstützung in Ihrer Umgebung aktiviert ist, um eine genaue Ära-Konvertierung zu gewährleisten. Die Klassen [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) und [PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) bieten die notwendige Funktionalität für diese Konvertierung.
{{< app/cells/assistant language="python-net" >}}
