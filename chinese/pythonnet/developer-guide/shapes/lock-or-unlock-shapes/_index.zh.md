---
title: 锁定或解锁形状
linktitle: 锁定或解锁形状
type: docs
weight: 200
url: /zh/python-net/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

有时，您需要保护工作表中的所有形状，以防止它们被不需要的情况破坏。在这种情况下，您需要锁定指定工作表中的所有形状。

有时，您需要能够修改受保护工作表中的特定形状，在这种情况下，您需要解锁这些形状。

本文将详细介绍如何锁定和解锁指定的形状。

{{% /alert %}}

## **保护指定工作表中的所有形状**

要保护指定工作表中的所有形状，请使用[Worksheet.Protect(type)](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protect/#aspose.cells.ProtectionType)方法，如以下示例代码所示。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Lock-Or-Unlock-Shapes-1.py" >}}

## **解锁受保护工作表中的指定形状**

要在受保护的工作表中解锁指定的形状，请使用[shape.is_locked](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/is_locked/)，如以下示例代码所示。

注意：当工作表受到保护时，[shape.is_locked](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/is_locked/)只有意义。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Lock-Or-Unlock-Shapes-2.py" >}}

{{< app/cells/assistant language="python-net" >}}
