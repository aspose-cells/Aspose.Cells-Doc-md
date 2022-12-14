---
title: Обработка событий после удаления столбцов и строк в GridDesktop
type: docs
weight: 80
url: /ru/net/handling-events-after-deleting-columns-and-rows-in-griddesktop/
---
## **Возможные сценарии использования**
Aspose.Cells для GridDesktop добавлено два новых события, т. е. AfterDeleteColumns и AfterDeleteRows, как показано на следующем снимке экрана. Эти события запускаются, когда вы удаляете столбцы и строки соответственно.

![дело:изображение_альтернативный_текст](handling-events-after-deleting-columns-and-rows-in-griddesktop_1.png)
## **Обработка событий после удаления столбцов и строк в GridDesktop**
В следующем примере кода объясняется, как использовать события AfterDeleteColumns и AfterDeleteRows. Всякий раз, когда вы удаляете некоторые столбцы или строки, данная функция будет вызываться и отображать окно сообщения, в котором отображается индекс удаленного столбца или строки.
## **Образец кода**
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
