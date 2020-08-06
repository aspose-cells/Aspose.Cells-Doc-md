---
title : "Handling Events after Deleting Columns and Rows in GridDesktop" 
description : "" 
weight : 16603 
toc : false
type: docs
url: /net/developerguide/griddesktop/griddesktop/handling+events+after+deleting+columns+and+rows+in+griddesktop/
---

# Aspose.Cells for .NET : Handling Events after Deleting Columns and Rows in GridDesktop


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Handling Events after Deleting Columns and Rows in GridDesktop](#handling-events-after-deleting-columns-and-rows-in-griddesktop)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

## Possible Usage Scenarios

`Aspose.Cells for GridDesktop` has added two new events i.e. `AfterDeleteColumns` and `AfterDeleteRows` as shown in the following screenshot. These events are fired when you delete columns and rows respectively.

![image](61767759.png)

## Handling Events after Deleting Columns and Rows in GridDesktop

The following sample code explains how to make use of `AfterDeleteColumns` and `AfterDeleteRows` events. Whenever you delete some columns or rows, the given function will be called and show a message box that displays the index of the deleted column or row.

## Sample Code

{{< code lang="cs" >}}
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
{{< /code >}}

