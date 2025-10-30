---
title: Usando WorkbookMetadata con Python.NET
linktitle: Metadatos del libro de trabajo
type: docs
weight: 320
url: /es/python-net/using-workbookmetadata/
description: Aprende cómo gestionar metadatos de libros de trabajo de manera eficiente usando la API de Aspose.Cells para Python via .NET.
---

{{% alert color="primary" %}}

Aspose.Cells le permite cargar una versión liviana de un libro en la memoria para editar su información de metadatos. Utilice la clase [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata) para cargar el libro.

{{% /alert %}}

El siguiente código de ejemplo utiliza la clase [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata) para editar las propiedades de documento personalizadas de un libro. Una vez que abra el libro usando la clase [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook), podrá leer las propiedades del documento. Aquí tiene un código de ejemplo que utiliza la clase [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata).

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
