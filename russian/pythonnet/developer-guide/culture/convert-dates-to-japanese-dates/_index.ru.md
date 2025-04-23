---
title: Преобразование дат в японские даты с помощью Python.NET
linktitle: Преобразование дат в японские даты
type: docs
weight: 350
url: /ru/python-net/convert-dates-to-japanese-dates/
description: Узнайте, как преобразовать григорианские даты в японские в файлах Excel с помощью Aspose.Cells для Python via .NET.
---

{{% alert color="primary" %}} 

В Японском календаре новая эра начинается с правления нового императора. 1 мая 2019 года во власти появился новый император, с этого момента закончилась эра Хэйсэй и началась эпоха Рэйва.

{{% /alert %}} 

Aspose.Cells предоставляет способ преобразования григорианских дат в японские с учетом изменений эпох. Следующий пример показывает преобразование исходного файла Excel, содержащего григорианские даты, в PDF с японскими датами:

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

**Преобразование с помощью Python.NET:**


Примечание: убедитесь, что в вашей среде включена поддержка японского языка для точных преобразований эры. Класс [Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) и [PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) обеспечивают необходимый функционал для этого преобразования.
