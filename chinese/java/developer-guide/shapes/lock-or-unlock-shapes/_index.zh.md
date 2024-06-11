---
title: 锁定或解锁形状
linktitle: 锁定或解锁形状
type: docs
weight: 200
url: /zh/java/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

有时，您需要保护工作表中的所有形状，以防止它们被不需要的情况破坏。在这种情况下，您需要锁定指定工作表中的所有形状。

有时，您需要能够修改受保护工作表中的特定形状，在这种情况下，您需要解锁这些形状。

本文将详细介绍如何锁定和解锁指定的形状。

{{% /alert %}}

## **保护指定工作表中的所有形状**

要保护指定工作表中的所有形状，请使用 [Worksheet.protect(int type)](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet/#protect-int-) 方法，如下面的示例代码所示。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Lock-Or-Unlock-Shapes-1.java" >}}

## **解锁受保护工作表中的指定形状**

要解除对受保护工作表中的指定形状的锁定状态，请使用 [shape.IsLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#isLocked--) 和 [shape.setLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#setLocked-boolean-)，如下面的示例代码所示。

注意：只有在工作表受保护时，[shape.IsLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#isLocked--) 和 [shape.setLocked](https://reference.aspose.com/cells/java/com.aspose.cells/shape/#setLocked-boolean-) 才有意义。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Lock-Or-Unlock-Shapes-2.java" >}}

