---
title: Python.NET kullanarak Tarihleri Japonca Tarihlere Dönüştürme
linktitle: Japon Tarihlerine Dönüştür
type: docs
weight: 350
url: /tr/python-net/convert-dates-to-japanese-dates/
description: Aspose.Cells for Python via .NET kullanarak Gregorian tarihlerini Japonya tarihine dönüştürmeyi öğrenin.
---

{{% alert color="primary" %}} 

Japon Takviminde yeni bir imparatorun padişahlığıyla yeni bir dönem başlar. 1 Mayıs 2019'da yeni bir imparator tahta çıktı ve Heisei dönemi sona erdi, Reiwa dönemi başladı.

{{% /alert %}} 

Aspose.Cells, Gregoryen tarihlerini dönem değişikliklerini göz önüne alarak Japon tarihlerine dönüştürme imkanı sağlar. Aşağıdaki kod parçası, Gregorian tarihleri içeren kaynak Excel dosyasını Japon tarihleriyle PDF çıktı olarak dönüştürmeyi gösterir.

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

**Python.NET Dönüşüm:**


Not: Doğru dönem dönüşümleri için Japonca dil desteğinin ortamınızda etkin olduğundan emin olun. [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) sınıfı ve [PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) bu dönüşüm için gerekli işlevleri sağlar.
{{< app/cells/assistant language="python-net" >}}
