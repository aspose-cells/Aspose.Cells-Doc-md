---
title: 形状のロックまたはロック解除
linktitle: 形状のロックまたはロック解除
type: docs
weight: 200
url: /ja/python-java/lock-or-unlock-shapes/
---

{{% alert color="primary" %}}

場合によっては、特定のワークシート内のすべての形状を保護して、望ましくない状況によって破壊されるのを防ぐ必要があります。その場合は、指定されたワークシート内のすべての形状をロックする必要があります。

場合によっては、特定の保護されたワークシート内の特定の形状を変更する必要がある場合があります。その場合は、これらの形状をロック解除する必要があります。

この記事では、指定された形状をロックおよびロック解除する方法について詳しく説明します。

{{% /alert %}}

## **指定されたワークシート内のすべての形状を保護**

特定のワークシートのすべての図形を保護するには、[Worksheet.Protect(type)](https://reference.aspose.com/cells/python-java/asposecells.api/worksheet#protect(int)) メソッドを使用します。次のサンプルコードに示すように、保護されたワークシート内の指定された図形をロック解除するには、[shape.IsLocked](https://reference.aspose.com/cells/python-java/asposecells.api/shape#IsLocked) を使用します。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Lock-Or-Unlock-Shapes-1.py" >}}

## **保護されたワークシート内の指定された形状のロック解除**

保護されたワークシート内の指定された図形をロック解除するには、次のサンプルコードに示すように [shape.IsLocked](https://reference.aspose.com/cells/python-java/asposecells.api/shape#IsLocked) を使用します。

注：[shape.IsLocked](https://reference.aspose.com/cells/python-java/asposecells.api/shape#IsLocked) はワークシートが保護されている場合にのみ意味を持ちます。

{{< gist "aspose-cells-gists" "32e50c6aabc547111966569f3fd39694" "Lock-Or-Unlock-Shapes-2.py" >}}

