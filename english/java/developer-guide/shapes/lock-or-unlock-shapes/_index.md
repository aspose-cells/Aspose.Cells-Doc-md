---
title: Lock or unlock shapes
linktitle: Lock or unlock shapes
type: docs
weight: 200
url: /java/lock-or-unlock-shapes/
ai_search_scope: cells_java
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you need to protect all shapes in certain worksheets to prevent them from being destroyed by unwanted situations. In this case, you need to lock all shapes in the specified worksheet.

Sometimes, you need to be able to modify certain shapes in certain protected worksheets, in which case you need to unlock these shapes.

This article will detail how to lock and unlock specified shapes.

{{% /alert %}}

## **Protect all shapes in a specified worksheet**

To protect all shapes in a specified worksheet, use the [Worksheet.protect(int type)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet/#protect-int-) method, as shown in the following sample code.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Lock-Or-Unlock-Shapes-1.java" >}}

## **Unlock specified shapes in a protected worksheet**

To unlock a specified shape in a protected worksheet, use [shape.IsLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#isLocked--) and [shape.setLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#setLocked-boolean-), as shown in the following sample code.

Note: [shape.IsLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#isLocked--) and [shape.setLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#setLocked-boolean-) are meaningful only when the worksheet is protected.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Lock-Or-Unlock-Shapes-2.java" >}}

{{< app/cells/assistant language="java" >}}
