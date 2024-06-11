---
title: 锁定或解锁形状
linktitle: 锁定或解锁形状
type: docs
weight: 200
url: /zh/net/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

有时，您需要保护工作表中的所有形状，以防止它们被不需要的情况破坏。在这种情况下，您需要锁定指定工作表中的所有形状。

有时，您需要能够修改受保护工作表中的特定形状，在这种情况下，您需要解锁这些形状。

本文将详细介绍如何锁定和解锁指定的形状。

{{% /alert %}}

## **保护指定工作表中的所有形状**

要保护指定工作表中的所有形状，请使用 [Worksheet.Protect(ProtectionType.Objects)](https://reference.aspose.com/cells/net/aspose.cells/worksheet/protect/#protect) 方法。示例代码如下。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-1.cs" >}}

## **解锁受保护工作表中的指定形状**

要解锁受保护工作表中的指定形状，请使用 [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/)，示例代码如下。

注意：只有在工作表被保护时 [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) 才有意义。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-2.cs" >}}

