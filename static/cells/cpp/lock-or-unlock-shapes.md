##Lock or unlock shapes
Sometimes, you need to protect all shapes in certain worksheets to prevent them from being destroyed by unwanted situations. In this case, you need to lock all shapes in the specified worksheet.
Sometimes, you need to be able to modify certain shapes in certain protected worksheets, in which case, you need to unlock these shapes.
This article will introduce in detail how to lock and unlock specified shapes.
## **Protect all shapes in a specified worksheet**
To protect all shapes in a specified worksheet, use the [Worksheet.Protect(ProtectionType)](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) method, as shown in the following sample code.
## **Unlock specified shapes in a protected worksheet**
To unlock a specified shape in a protected worksheet, use [shape.IsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/islocked/) and [shape.SetIsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setislocked/), as shown in the following sample code.
Note: [shape.IsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/islocked/) and [shape.SetIsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setislocked/) are meaningful only when the worksheet is protected.
