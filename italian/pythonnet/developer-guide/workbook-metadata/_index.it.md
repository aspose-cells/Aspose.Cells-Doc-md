---
title: Usando WorkbookMetadata con Python.NET
linktitle: Metadati del foglio di lavoro
type: docs
weight: 320
url: /it/python-net/using-workbookmetadata/
description: Impara come gestire efficacemente i metadati del workbook usando l’API Aspose.Cells for Python via .NET.
---

{{% alert color="primary" %}}

Aspose.Cells consente di caricare una versione leggera del foglio di lavoro in memoria per modificare le informazioni sui metadati. Si prega di utilizzare la classe [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata) per caricare il foglio di lavoro.

{{% /alert %}}

Il codice di esempio seguente utilizza la classe [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata) per modificare le proprietà personalizzate del documento di un foglio di lavoro. Una volta aperto il foglio di lavoro utilizzando la classe [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), sarà possibile leggere le proprietà del documento. Ecco un codice di esempio che utilizza la classe [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata).

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
