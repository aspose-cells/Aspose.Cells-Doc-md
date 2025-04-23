---
title: Python.NETとともにWorkbookMetadataを使用する
linktitle: ワークブックメタデータ
type: docs
weight: 320
url: /ja/python-net/using-workbookmetadata/
description: Aspose.Cells for Python via .NET APIを使用してワークブックメタデータを効率的に管理する方法を学びます。
---

{{% alert color="primary" %}}

Aspose.Cellsを使用して、ワークブックの軽量バージョンをメモリに読み込んでメタデータ情報を編集できます。ワークブックを読み込むには、[**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata)クラスを使用してください。

{{% /alert %}}

次のサンプルコードは、[**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata)クラスを使用してワークブックのカスタムドキュメントプロパティを編集する方法を示しています。[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)クラスを使用してワークブックを開くと、ドキュメントプロパティを読むことができます。[**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata)クラスを使用したサンプルコードは次のとおりです。

```python
import os
from aspose.cells import Workbook
from aspose.cells.metadata import MetadataOptions, MetadataType, WorkbookMetadata

# The path to the documents directory.
current_dir = os.path.dirname(os.path.abspath(__file__))
data_dir = os.path.join(current_dir, "data")

# Open Workbook metadata
options = MetadataOptions(MetadataType.DOCUMENT_PROPERTIES)
meta = WorkbookMetadata(os.path.join(data_dir, "Sample1.xlsx"), options)

# Set some properties
meta.custom_document_properties.add("test", "test")

# Save the metadata info
meta.save(os.path.join(data_dir, "Sample2.out.xlsx"))

# Open the workbook
w = Workbook(os.path.join(data_dir, "Sample2.out.xlsx"))

# Read document property
print(w.custom_document_properties.get("test"))

print("Press any key to continue...")
```

