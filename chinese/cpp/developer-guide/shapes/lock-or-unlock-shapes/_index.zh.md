---
title: 锁定或解锁形状
linktitle: 锁定或解锁形状
type: docs
weight: 200
url: /zh/cpp/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

有时，您需要保护特定工作表中的所有形状，以防止它们被意外情况摧毁。在这种情况下，您需要锁定指定工作表中的所有形状。

有时，您需要能够在某些受保护的工作表中修改特定形状，这种情况下，您需要解锁这些形状。

本文章将详细介绍如何锁定和解锁指定的形状。

{{% /alert %}}

## **保护特定工作表中的所有形状**

要在指定工作表中保护所有形状，使用[Worksheet.Protect(ProtectionType)](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/)方法，示例如下所示。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Lock-Or-Unlock-Shapes-1.cpp" >}}

## **解锁受保护工作表中的指定形状**

要在受保护的工作表中解锁指定的形状，使用[shape.IsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/islocked/)和[shape.SetIsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setislocked/)，示例如下所示。

注意：[shape.IsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/islocked/)和[shape.SetIsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setislocked/)仅在工作表受保护时才有意义。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Lock-Or-Unlock-Shapes-2.cpp" >}}

