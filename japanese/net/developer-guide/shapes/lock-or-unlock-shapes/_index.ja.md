---
title: 形状のロックまたはロック解除
linktitle: 形状のロックまたはロック解除
type: docs
weight: 200
url: /ja/net/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

場合によっては、特定のワークシート内のすべての形状を保護して、望ましくない状況によって破壊されるのを防ぐ必要があります。その場合は、指定されたワークシート内のすべての形状をロックする必要があります。

場合によっては、特定の保護されたワークシート内の特定の形状を変更する必要がある場合があります。その場合は、これらの形状をロック解除する必要があります。

この記事では、指定された形状をロックおよびロック解除する方法について詳しく説明します。

{{% /alert %}}

## **指定されたワークシート内のすべての形状を保護**

指定されたワークシート内のすべての形状を保護するには、[Worksheet.Protect( ProtectionType.Objects)](https://reference.aspose.com/cells/net/aspose.cells/worksheet/protect/#protect)メソッドを使用します。以下のサンプルコード例に示すように。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-1.cs" >}}

## **保護されたワークシート内の指定された形状のロック解除**

保護されたワークシート内の指定された形状をアンロックするには、[shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/)を使用します。以下のサンプルコード例に示すように。

注: [shape.IsLocked](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/islocked/)は、ワークシートが保護されている場合にのみ意味があります。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Lock-Or-Unlock-Shapes-2.cs" >}}

