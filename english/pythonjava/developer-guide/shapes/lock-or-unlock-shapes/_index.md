---
title: Lock or unlock shapes
linktitle: Lock or unlock shapes
type: docs
weight: 200
url: /python-java/lock-or-unlock-shapes/
ai_search_scope: cells_pythonjava
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes, you need to protect all shapes in certain worksheets to prevent them from being destroyed by unwanted situations. In this case, you need to lock all shapes in the specified worksheet.

Sometimes, you need to be able to modify certain shapes in certain protected worksheets, in which case, you need to unlock these shapes.

This article will introduce in detail how to lock and unlock specified shapes.

{{% /alert %}}

## **Protect all shapes in a specified worksheet**

To protect all shapes in a specified worksheet, use the [Worksheet.Protect(type)](https://reference.aspose.com/cells/python-java/asposecells.api/worksheet#protect(int)) method, as shown in the following sample code.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Lock-Or-Unlock-Shapes-1.py" >}}

## **Unlock specified shapes in a protected worksheet**

To unlock a specified shape in a protected worksheet, use [shape.IsLocked](https://reference.aspose.com/cells/python-java/asposecells.api/shape#IsLocked), as shown in the following sample code.

Note: [shape.IsLocked](https://reference.aspose.com/cells/python-java/asposecells.api/shape#IsLocked) is meaningful only when the worksheet is protected.

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Lock-Or-Unlock-Shapes-2.py" >}}

