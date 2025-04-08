---
title: Using WorkbookMetadata with Python.NET
linktitle: Workbook Metadata
type: docs
weight: 320
url: /python-net/using-workbookmetadata/
description: Learn how to manage workbook metadata efficiently using Aspose.Cells for Python via .NET API.
---

{{% alert color="primary" %}}

Aspose.Cells allows you to load a light-weight version of workbook into memory to edit its metadata information. Please use the [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata) class to load the workbook.

{{% /alert %}}

The following sample code uses [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata) class to edit custom document properties of a workbook. Once you open the workbook using [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class, you will be able to read the document properties. Here is a sample code using the [**WorkbookMetadata**](https://reference.aspose.com/cells/python-net/aspose.cells.metadata/workbookmetadata) class.

```python
import os
from aspose.cells import Workbook, MetadataOptions, MetadataType, WorkbookMetadata

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
print(w.custom_document_properties["test"])

print("Press any key to continue...")
```

```python
from aspose.cells.metadata import WorkbookMetadata
from aspose.cells import Workbook
import clr

# Edit metadata using WorkbookMetadata
with WorkbookMetadata("input.xlsx") as meta:
    meta.custom_document_properties.add("test", "test")
    meta.save("output.xlsx")

# Verify the property using Workbook
with Workbook("output.xlsx") as w:
    custom_props = w.custom_document_properties
    print(custom_props["test"].value)
```