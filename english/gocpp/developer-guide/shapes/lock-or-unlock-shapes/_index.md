---  
title: Lock or unlock shapes  
linktitle: Lock or unlock shapes  
type: docs  
weight: 200  
url: /go-cpp/lock-or-unlock-shapes/  
---  

{{% alert color="primary" %}}

Sometimes, you need to protect all shapes in certain worksheets to prevent them from being destroyed by unwanted situations. In this case, you need to lock all shapes in the specified worksheet.

Sometimes, you need to be able to modify certain shapes in certain protected worksheets, in which case you need to unlock these shapes.

This article will describe in detail how to lock and unlock specified shapes.

{{% /alert %}}

## **Protect all shapes in a specified worksheet**

To protect all shapes in a specified worksheet, use the [Worksheet.Protect(ProtectionType)](https://reference.aspose.com/cells/go-cpp/worksheet/protect_protectiontype/) method, as shown in the following sample code.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LockOrUnlockShapes.go" >}}

## **Unlock specified shapes in a protected worksheet**

To unlock a specified shape in a protected worksheet, use [shape.IsLocked](https://reference.aspose.com/cells/go-cpp/shape/islocked/) and [shape.SetIsLocked](https://reference.aspose.com/cells/go-cpp/shape/setislocked/), as shown in the following sample code.

Note: [shape.IsLocked](https://reference.aspose.com/cells/go-cpp/shape/islocked/) and [shape.SetIsLocked](https://reference.aspose.com/cells/go-cpp/shape/setislocked/) are meaningful only when the worksheet is protected.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LockOrUnlockShapes-1.go" >}}

{{< app/cells/assistant language="go" >}}
