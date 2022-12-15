---
title: 在 GridDesktop 中删除列和行后处理事件
type: docs
weight: 80
url: /zh/net/handling-events-after-deleting-columns-and-rows-in-griddesktop/
---
## **可能的使用场景**
GridDesktop 的 Aspose.Cells 添加了两个新事件，即 AfterDeleteColumns 和 AfterDeleteRows，如以下屏幕截图所示。当您分别删除列和行时会触发这些事件。

![待办事项：图像_替代_文本](handling-events-after-deleting-columns-and-rows-in-griddesktop_1.png)
## **在 GridDesktop 中删除列和行后处理事件**
以下示例代码说明了如何使用 AfterDeleteColumns 和 AfterDeleteRows 事件。每当您删除某些列或行时，将调用给定函数并显示一个消息框，其中显示已删除列或行的索引。
## **示例代码**
{{< highlight "java" >}}

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
