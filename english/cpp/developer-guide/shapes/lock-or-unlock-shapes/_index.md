---
title: Lock or unlock shapes
linktitle: Lock or unlock shapes
type: docs
weight: 200
url: /cpp/lock-or-unlock-shapes/
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you need to protect all shapes in certain worksheets to prevent them from being destroyed by unwanted situations. In this case, you need to lock all shapes in the specified worksheet.

Sometimes, you need to be able to modify certain shapes in certain protected worksheets, in which case, you need to unlock these shapes.

This article will introduce in detail how to lock and unlock specified shapes.

{{% /alert %}}

## **Protect all shapes in a specified worksheet**

To protect all shapes in a specified worksheet, use the [Worksheet.Protect(ProtectionType)](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/) method, as shown in the following sample code.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Lock-Or-Unlock-Shapes-1.cpp" >}}

## **Unlock specified shapes in a protected worksheet**

To unlock a specified shape in a protected worksheet, use [shape.IsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/islocked/) and [shape.SetIsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setislocked/), as shown in the following sample code.

Note: [shape.IsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/islocked/) and [shape.SetIsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setislocked/) are meaningful only when the worksheet is protected.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Lock-Or-Unlock-Shapes-2.cpp" >}}

{{< app/cells/assistant language="cpp" >}}
