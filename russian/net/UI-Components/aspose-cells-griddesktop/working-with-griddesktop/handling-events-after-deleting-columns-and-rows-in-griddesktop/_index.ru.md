---
title: Обработка событий после удаления столбцов и строк в GridDesktop
type: docs
weight: 80
url: /ru/net/aspose-cells-griddesktop/handle-events-after-delete-columns-and-rows-in-griddesktop/
keywords: GridDesktop,события,удаление строки,удаление столбца
description: В этой статье представлены события после удаления строки/столбца в GridDesktop.
---

## **Возможные сценарии использования**
Aspose.Cells для GridDesktop добавил два новых события: AfterDeleteColumns и AfterDeleteRows, как показано на следующем скриншоте. Эти события возникают при удалении столбцов и строк соответственно.

![todo:image_alt_text](handling-events-after-deleting-columns-and-rows-in-griddesktop_1.png)
## **Обработка событий после удаления столбцов и строк в GridDesktop**
Приведенный ниже образец кода объясняет, как использовать события AfterDeleteColumns и AfterDeleteRows. Когда удаляются некоторые столбцы или строки, вызывается данная функция и отображается диалоговое окно, отображающее индекс удаленного столбца или строки.
## **Образец кода**
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
