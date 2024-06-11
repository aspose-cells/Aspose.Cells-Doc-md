---
title: 锁定或解锁形状
linktitle: 锁定或解锁形状
type: docs
weight: 200
url: /zh/python-net/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

有时，您需要保护特定工作表中的所有形状，以防止它们被意外情况摧毁。在这种情况下，您需要锁定指定工作表中的所有形状。

有时，您需要能够在某些受保护的工作表中修改特定形状，这种情况下，您需要解锁这些形状。

本文章将详细介绍如何锁定和解锁指定的形状。

{{% /alert %}}

## **保护特定工作表中的所有形状**

要保护工作表中的所有形状，请使用[Worksheet.Protect(type)](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protect/#aspose.cells.ProtectionType) 方法，如下面的示例代码所示。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Lock-Or-Unlock-Shapes-1.py" >}}

## **解锁受保护工作表中的指定形状**

要解锁受保护工作表中的指定形状，请使用[shape.is_locked](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/is_locked/)，如下面的示例代码所示。

注意： [shape.is_locked](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/is_locked/) 仅在工作表受到保护时才有意义。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Lock-Or-Unlock-Shapes-2.py" >}}

