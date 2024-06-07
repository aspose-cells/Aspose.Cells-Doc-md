---
title: 在 GridDesktop 中删除列和行后处理事件
type: docs
weight: 80
url: /zh/net/aspose-cells-griddesktop/handle-events-after-delete-columns-and-rows-in-griddesktop/
keywords: GridDesktop,事件,删除行,删除列
description: 本文介绍了在 GridDesktop 中删除行/列后的事件。
---

## **可能的使用场景**
Aspose.Cells for GridDesktop 添加了两个新事件，即 AfterDeleteColumns 和 AfterDeleteRows，如下截图所示。在删除列和行时触发这些事件。

![todo:image_alt_text](handling-events-after-deleting-columns-and-rows-in-griddesktop_1.png)
## **在 GridDesktop 中删除列和行后处理事件**
以下示例代码解释了如何利用 AfterDeleteColumns 和 AfterDeleteRows 事件。每当删除一些列或行时，将调用给定函数，并显示一个消息框，其中显示已删除列或行的索引。
## **示例代码**
{{< highlight java >}}

 private void gridDesktop1_AfterDeleteColumnsAndRows(object sender, Aspose.Cells.GridDesktop.WorksheetEventArgs args)

{

    if(args.SheetEvents == Aspose.Cells.GridDesktop.WorksheetEvents.ColumnDeleted)

    {

        MessageBox.Show("Deleted Column Index: " + args.Index);

    }

    if (args.SheetEvents == Aspose.Cells.GridDesktop.WorksheetEvents.RowDeleted)

    {

        MessageBox.Show("Deleted Row Index: " + args.Index);

    }

}

{{< /highlight >}}
