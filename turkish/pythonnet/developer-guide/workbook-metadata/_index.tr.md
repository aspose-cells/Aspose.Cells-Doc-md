---
title: Python.NET ile WorkbookMetadata Kullanımı
linktitle: Çalışma Kitabı Meta Verisi
type: docs
weight: 320
url: /tr/python-net/using-workbookmetadata/
description: Aspose.Cells for Python via .NET API kullanarak çalışma kitabı meta verisini nasıl etkin bir şekilde yöneteceğinizi öğrenin.
---

{{% alert color="primary" %}}

Aspose.Cells, bir çalışma kitabının hafif bir sürümünü belleğe yükleyerek meta veri bilgilerini düzenlemenizi sağlar. Lütfen [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata) sınıfını kullanın.

{{% /alert %}}

Aşağıdaki örnek kod, bir çalışma kitabının özel belge özelliklerini düzenlemek için [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata) sınıfını kullanmaktadır. [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) sınıfını kullanarak çalışma kitabını açtığınızda, belge özelliklerini okuyabileceksiniz. İşte [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata) sınıfını kullanarak örnek bir kod.

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

