---
title: Release Unmanaged Resources of the Workbook with Python via .NET
linktitle: Release Unmanaged Resources
type: docs
weight: 310
url: /python-net/release-unmanaged-resources-of-the-workbook/
description: Learn how to properly release unmanaged resources when working with Excel workbooks using Aspose.Cells for Python via .NET.
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Aspose.Cells provides the [**workbook.close()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/close/) method to release unmanaged resources of the [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) object. This pattern is crucial for handling unmanaged resources like file handles, streams, or memory allocations that aren't automatically managed by Python's garbage collector.

{{% /alert %}}

The [**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook) class implements Python's context manager protocol for resource management. You can either explicitly call the [**close()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/close/) method or use Python's `with` statement to ensure proper cleanup.

```python
from aspose.cells import Workbook

# Create a workbook object
with Workbook() as wb:
    wb.save("dispose.xlsx")
```

{{< app/cells/assistant language="python-net" >}}
