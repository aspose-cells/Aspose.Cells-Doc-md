---
title: Converti Date in Date Giapponesi con Python.NET
linktitle: Convertire le date in date giapponesi
type: docs
weight: 350
url: /it/python-net/convert-dates-to-japanese-dates/
description: Impara come convertire le date Gregoriane in date giapponesi nei file Excel usando Aspose.Cells for Python via .NET.
---

{{% alert color="primary" %}} 

Nel Calendario Giapponese, una nuova era inizia con il regno di un nuovo imperatore. Il 1° maggio 2019, un nuovo imperatore ha preso il potere, con cui l'era Heisei è terminata e l'era Reiwa è iniziata.

{{% /alert %}} 

Aspose.Cells fornisce un metodo per convertire le date Gregoriane in date giapponesi considerando i cambi di era. Il seguente snippet di codice dimostra come convertire un file Excel di origine contenente date Gregoriane in un output PDF con date giapponesi:

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

**Conversione Python.NET:**


Nota: assicurarsi che il supporto per la lingua giapponese sia abilitato nel proprio ambiente per conversioni accurate delle ere. La classe [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) e [PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) forniscono le funzionalità necessarie per questa conversione.
