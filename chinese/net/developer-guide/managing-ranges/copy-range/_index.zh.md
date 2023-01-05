---
title: 复制Excel的范围
linktitle: 复制范围
type: docs
weight: 105
url: /zh/net/copy-ranges-of-Excel/
---
## **介绍**

在 Excel 中，您可以选择一个范围，复制该范围，然后将其与特定选项一起粘贴到同一工作表、其他工作表或其他文件中。

## **使用 Aspose.Cells 复制范围**

Aspose.Cells 提供一些过载[范围.复制](https://reference.aspose.com/cells/net/aspose.cells/range/copy/#copy)复制范围的方法。
和[范围.CopyStyle](https://reference.aspose.com/cells/net/aspose.cells/range/copystyle/)只有范围的复制样式；[范围.复制数据](https://reference.aspose.com/cells/net/aspose.cells/range/copydata/)只有范围的复制值

## **复制范围**

创建两个范围：源范围、目标范围，然后使用 Range.Copy 方法将源范围复制到目标范围。

请参见以下代码：

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range.cs" >}}

## **粘贴带选项的范围**

Aspose.Cells 支持粘贴特定类型的范围。

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Paste-Range.cs" >}}

## **仅复制范围内的数据。**
您也可以使用 Range.CopyData 方法复制数据，如下代码所示：

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Copy-Range-Data.cs" >}}

## **推进主题**
- [将源范围的行高复制到目标范围](/cells/zh/net/copy-row-heights-of-source-range-to-destination-range/)


