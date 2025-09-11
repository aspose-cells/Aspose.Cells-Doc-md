---
title: Lock or unlock shapes
linktitle: Lock or unlock shapes
type: docs
weight: 200
url: /python-net/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

Sometimes, you need to protect all shapes in certain worksheets to prevent them from being destroyed by unwanted situations. In this case, you need to lock all shapes in the specified worksheet.

Sometimes, you need to be able to modify certain shapes in certain protected worksheets, in which case, you need to unlock these shapes.

This article will introduce in detail how to lock and unlock specified shapes.

{{% /alert %}}

## **Protect all shapes in a specified worksheet**

To protect all shapes in a specified worksheet, use the [Worksheet.Protect(type)](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/protect/#aspose.cells.ProtectionType) method, as shown in the following sample code.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Lock-Or-Unlock-Shapes-1.py" >}}

## **Unlock specified shapes in a protected worksheet**

To unlock a specified shape in a protected worksheet, use [shape.is_locked](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/is_locked/), as shown in the following sample code.

Note: [shape.is_locked](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/is_locked/) is meaningful only when the worksheet is protected.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Lock-Or-Unlock-Shapes-2.py" >}}

{{< app/cells/assistant language="python-net" >}}