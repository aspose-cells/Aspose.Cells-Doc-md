---
title: 使用WorkbookMetadata与Python.NET
linktitle: 工作簿元数据
type: docs
weight: 320
url: /zh/python-net/using-workbookmetadata/
description: 学习如何使用Aspose.Cells for Python via .NET API高效管理工作簿元数据。
---

{{% alert color="primary" %}}

Aspose.Cells允许您将工作簿的轻量级版本加载到内存中，以编辑其元数据信息。请使用[**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata)类来加载工作簿。

{{% /alert %}}

以下示例代码使用[**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata)类来编辑工作簿的自定义文档属性。一旦使用[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类打开工作簿，您将能够读取文档属性。以下是使用[**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata)类的示例代码。

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

{{< app/cells/assistant language="python-net" >}}
