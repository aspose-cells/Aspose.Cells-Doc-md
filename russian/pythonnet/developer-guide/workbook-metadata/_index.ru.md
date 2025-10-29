---
title: Использование WorkbookMetadata с Python.NET
linktitle: Метаданные книги
type: docs
weight: 320
url: /ru/python-net/using-workbookmetadata/
description: Узнайте, как эффективно управлять метаданными рабочей книги с помощью API Aspose.Cells для Python via .NET.
---

{{% alert color="primary" %}}

Aspose.Cells позволяет загружать легковесную версию книги в память для редактирования информации о метаданных. Используйте класс [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata) для загрузки книги.

{{% /alert %}}

Приведенный ниже образец кода использует класс [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata) для редактирования пользовательских свойств документа книги. После открытия книги с помощью класса [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), вы сможете читать свойства документа. Вот пример кода, использующий класс [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata).

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
