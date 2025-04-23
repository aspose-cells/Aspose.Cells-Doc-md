---
title: 复制Excel的范围
linktitle: 复制范围
type: docs
weight: 105
url: /zh/net/copy-ranges-of-Excel/
---

## **介绍**

在Excel中，您可以选择一个范围，复制该范围，然后以特定选项粘贴到同一工作表、其他工作表或其他文件。

## **使用Aspose.Cells复制范围**

Aspose.Cells提供了一些重载[Range.Copy](https://reference.aspose.com/cells/net/aspose.cells/range/copy/#copy)方法来复制范围。
还有[Range.CopyStyle](https://reference.aspose.com/cells/net/aspose.cells/range/copystyle/)只复制范围的样式；[Range.CopyData](https://reference.aspose.com/cells/net/aspose.cells/range/copydata/)只复制范围的值。

## **复制范围**

创建两个范围：源范围、目标范围，然后使用Range.Copy方法将源范围复制到目标范围。

查看以下代码：

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range.cs" >}}

## **使用选项粘贴范围**

Aspose.Cells支持使用特定类型粘贴范围。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Paste-Range.cs" >}}

## **仅复制数据的范围**
还可以使用Range.CopyData方法来复制数据，示例如下：

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range-Data.cs" >}}

## **高级主题**
- [将源范围的行高复制到目标范围](/cells/zh/net/copy-row-heights-of-source-range-to-destination-range/)


{{< app/cells/assistant language="csharp" >}}
