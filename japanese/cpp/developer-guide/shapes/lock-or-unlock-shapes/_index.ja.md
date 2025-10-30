---
title: 形状のロックまたはロック解除
linktitle: 形状のロックまたはロック解除
type: docs
weight: 200
url: /ja/cpp/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

場合によっては、特定のワークシート内のすべての形状を保護して、望ましくない状況によって破壊されるのを防ぐ必要があります。その場合は、指定されたワークシート内のすべての形状をロックする必要があります。

場合によっては、特定の保護されたワークシート内の特定の形状を変更する必要がある場合があります。その場合は、これらの形状をロック解除する必要があります。

この記事では、指定された形状をロックおよびロック解除する方法について詳しく説明します。

{{% /alert %}}

## **指定されたワークシート内のすべての形状を保護**

指定されたワークシート内のすべての形状を保護するには、[Worksheet.Protect(ProtectionType)](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/protect/)メソッドを使用します。次のサンプルコードに示すように。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Lock-Or-Unlock-Shapes-1.cpp" >}}

## **保護されたワークシート内の指定された形状のロック解除**

保護されたワークシート内の指定された形状をロック解除するには、[shape.IsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/islocked/)および[shape.SetIsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setislocked/)を使用します。次のサンプルコードに示すように。

注：[shape.IsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/islocked/)および[shape.SetIsLocked](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/setislocked/)は、ワークシートが保護された場合のみ意味を持ちます。

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "Lock-Or-Unlock-Shapes-2.cpp" >}}

{{< app/cells/assistant language="cpp" >}}
