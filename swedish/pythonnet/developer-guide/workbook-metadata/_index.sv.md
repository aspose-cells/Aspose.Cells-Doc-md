---
title: Använda WorkbookMetadata med Python.NET
linktitle: Arbetsboksmetadata 
type: docs
weight: 320
url: /sv/python-net/using-workbookmetadata/
description: Lär dig hur du hanterar arbetsboksmetadata effektivt med Aspose.Cells för Python via .NET API.
---

{{% alert color="primary" %}}

Aspose.Cells tillåter dig att ladda en lättviktsversion av arbetsbok i minnet för att redigera dess metadatainformation. Använd [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata) klassen för att ladda arbetsboken.

{{% /alert %}}

Följande kodexempel använder [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata) klassen för att redigera anpassade dokumentegenskaper i en arbetsbok. När du öppnar arbetsboken med [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) klassen, kommer du att kunna läsa dokumentegenskaper. Här är ett kodexempel som använder [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata) klassen.

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
