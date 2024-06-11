---
title: 复制Excel的范围
linktitle: 复制范围
type: docs
weight: 30
url: /zh/java/copy-ranges-of-Excel/
---

## **介绍**

在Excel中，您可以选择一个范围，复制该范围，然后以特定选项粘贴到同一工作表、其他工作表或其他文件。

## **使用Aspose.Cells复制范围**

Aspose.Cells提供了一些重载[Range.Copy](https://reference.aspose.com/cells/java/com.aspose.cells/range)方法来复制范围。
## **复制范围**

创建两个范围：源范围、目标范围，然后使用Range.Copy方法将源范围复制到目标范围。

查看以下代码：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Copy-Range.java" >}}

## **使用选项粘贴范围**

Aspose.Cells支持使用特定类型粘贴范围。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Paste-Range.java" >}}

## **仅复制范围的数据。**
还可以使用Range.CopyData方法来复制数据，示例如下：

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Copy-Range-Data.java" >}}


