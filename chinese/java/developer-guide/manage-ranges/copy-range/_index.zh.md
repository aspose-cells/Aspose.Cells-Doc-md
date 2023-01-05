---
title: 复制Excel的范围
linktitle: 复制范围
type: docs
weight: 30
url: /zh/java/copy-ranges-of-Excel/
---
## **介绍**

在 Excel 中，您可以选择一个范围，复制该范围，然后将其与特定选项一起粘贴到同一工作表、其他工作表或其他文件中。

## **使用 Aspose.Cells 复制范围**

Aspose.Cells 提供一些过载[范围.复制](https://reference.aspose.com/cells/java/com.aspose.cells/range)复制范围的方法。
## **复制范围**

创建两个范围：源范围、目标范围，然后使用 Range.Copy 方法将源范围复制到目标范围。

请参见以下代码：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Copy-Range.java" >}}

## **粘贴带选项的范围**

Aspose.Cells 支持粘贴特定类型的范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Paste-Range.java" >}}

## **仅复制范围内的数据。**
您也可以使用 Range.CopyData 方法复制数据，如下代码所示：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Copy-Range-Data.java" >}}


