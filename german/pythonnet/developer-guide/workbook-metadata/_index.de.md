---
title: Verwendung von WorkbookMetadata mit Python.NET
linktitle: Metadaten der Arbeitsmappe
type: docs
weight: 320
url: /de/python-net/using-workbookmetadata/
description: Erfahren Sie, wie Sie Metadaten von Arbeitsmappen effizient mit der Aspose.Cells für Python via .NET API verwalten.
---

{{% alert color="primary" %}}

Aspose.Cells ermöglicht das Laden einer leichtgewichtigen Version der Arbeitsmappe in den Speicher, um ihre Metadateninformationen zu bearbeiten. Verwenden Sie die [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata)-Klasse, um die Arbeitsmappe zu laden.

{{% /alert %}}

Der folgende Beispielcode verwendet die [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata)-Klasse, um benutzerdefinierte Dokumenteigenschaften einer Arbeitsmappe zu bearbeiten. Sobald Sie die Arbeitsmappe mit der [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)-Klasse öffnen, können Sie die Dokumenteigenschaften lesen. Hier ist ein Beispielcode, der die [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata)-Klasse verwendet.

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

