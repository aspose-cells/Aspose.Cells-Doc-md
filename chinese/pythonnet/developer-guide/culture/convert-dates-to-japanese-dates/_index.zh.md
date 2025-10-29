---
title: 使用Python.NET将日期转换为日本日期
linktitle: 将日期转换为日本日期
type: docs
weight: 350
url: /zh/python-net/convert-dates-to-japanese-dates/
description: 学习如何使用Aspose.Cells for Python via .NET将公历日期转换为Excel文件中的日本日期。
---

{{% alert color="primary" %}} 

在日本日历中，新的时代随着新皇帝的即位而开始。2019年5月1日，一位新皇帝即位，平成时代结束，令和时代开始。

{{% /alert %}} 

Aspose.Cells提供一种在考虑时代变更的情况下，将公历日期转换为日本日期的方法。以下代码演示了将包含公历日期的源Excel文件转换为包含日本日期的PDF输出的过程：

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

**Python.NET 转换：**


注意：确保环境中启用了日语支持以获得准确的年代转换。[Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) 类和 [PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) 提供了此转换所需的功能。
{{< app/cells/assistant language="python-net" >}}
