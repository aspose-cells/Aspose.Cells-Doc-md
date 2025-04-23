---
title: Python.NETを使った日付の日本式変換
linktitle: 日本の日付への変換
type: docs
weight: 350
url: /ja/python-net/convert-dates-to-japanese-dates/
description: Aspose.Cells for Pythonを使用して、エクセルファイルのグレゴリオ暦の日付を日本の元号日付に変換する方法について学びます。via .NET。
---

{{% alert color="primary" %}} 

日本の元号では、新しい天皇の即位により新しい元号が始まります。2019年5月1日、新しい天皇が即位し、平成時代が終了し、令和時代が始まりました。

{{% /alert %}} 

Aspose.Cellsは、西暦の日付を元号の変化を考慮して日本の元号日付に変換する方法を提供します。以下のコードスニペットは、西暦の日付を含むExcelファイルを日本の元号日付に変換し、PDFに出力する例です。

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

**Python.NET変換:**


注意：正確な元号変換のためには、お使いの環境で日本語サポートを有効にしてください。[Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/) クラスと [PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/) はこの変換に必要な機能を提供します。
