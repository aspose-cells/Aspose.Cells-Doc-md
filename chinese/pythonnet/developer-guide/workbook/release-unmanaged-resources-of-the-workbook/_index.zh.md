---
title: 用Python via .NET释放工作簿的未管理资源
linktitle: 释放未管理资源
type: docs
weight: 310
url: /zh/python-net/release-unmanaged-resources-of-the-workbook/
description: 学习在使用Aspose.Cells for Python via .NET处理Excel工作簿时如何正确释放未管理资源。
---

{{% alert color="primary" %}}

Aspose.Cells提供了[**workbook.close()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/close/)方法来释放[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)对象的未管理资源。这种模式对于处理如文件句柄、流或未由Python垃圾回收自动管理的内存分配等未管理资源至关重要。

{{% /alert %}}

[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类实现了Python的上下文管理器协议，用于资源管理。您可以显式调用[**close()**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/close/)方法，或使用Python的`with`语句确保正确清理。

```python
from aspose.cells import Workbook

# Create workbook object
    with aspose.cells.Workbook() as wb:
         wb.save("dispose.xlsx")
         pass
```
{{< app/cells/assistant language="python-net" >}}
