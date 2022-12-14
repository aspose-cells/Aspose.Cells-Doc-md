---
title: Behandlung von Ereignissen nach dem Löschen von Spalten und Zeilen in GridDesktop
type: docs
weight: 80
url: /de/net/handling-events-after-deleting-columns-and-rows-in-griddesktop/
---
## **Mögliche Nutzungsszenarien**
Aspose.Cells für GridDesktop hat zwei neue Ereignisse hinzugefügt, nämlich AfterDeleteColumns und AfterDeleteRows, wie im folgenden Screenshot gezeigt. Diese Ereignisse werden ausgelöst, wenn Sie Spalten bzw. Zeilen löschen.

![todo: Bild_alt_Text](handling-events-after-deleting-columns-and-rows-in-griddesktop_1.png)
## **Behandlung von Ereignissen nach dem Löschen von Spalten und Zeilen in GridDesktop**
Der folgende Beispielcode erläutert, wie AfterDeleteColumns- und AfterDeleteRows-Ereignisse verwendet werden. Immer wenn Sie einige Spalten oder Zeilen löschen, wird die angegebene Funktion aufgerufen und zeigt ein Meldungsfeld an, das den Index der gelöschten Spalte oder Zeile anzeigt.
## **Beispielcode**
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
