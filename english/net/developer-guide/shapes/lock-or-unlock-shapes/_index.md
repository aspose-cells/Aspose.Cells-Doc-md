---
title: Lock or unlock shapes
linktitle: Lock or unlock shapes
type: docs
weight: 200
url: /net/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

Sometimes, you need to protect all shapes in certain worksheets to prevent them from being destroyed by unwanted situations. In this case, you need to lock all shapes in the specified worksheet.

Sometimes, you need to be able to modify certain shapes in certain protected worksheets, in which case, you need to unlock these shapes.

This article will introduce in detail how to lock and unlock specified shapes.

{{% /alert %}}

## **Protect all shapes in a specified worksheet**

To protect all shapes in a specified worksheet, use the [Worksheet.Protect( ProtectionType.Objects)](https://reference.aspose.com/cells/net/aspose.cells/worksheet/protect/#protect) method, as shown in the following sample code.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-1.cs" >}}

## **Unlock specified shapes in a protected worksheet**

To unlock a specified shape in a protected worksheet, use [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/), as shown in the following sample code.

Note: [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/) is meaningful only when the worksheet is protected.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-2.cs" >}}

