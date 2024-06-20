---
title: Behandlung von Ereignissen nach dem Löschen von Spalten und Zeilen in GridDesktop
type: docs
weight: 80
url: /de/net/aspose-cells-griddesktop/handle-events-after-delete-columns-and-rows-in-griddesktop/
keywords: GridDesktop, Ereignisse, Zeile löschen, Spalte löschen
description: Dieser Artikel führt die Ereignisse nach dem Löschen von Zeile/Spalte in GridDesktop ein.
---

## **Mögliche Verwendungsszenarien**
Aspose.Cells für GridDesktop hat zwei neue Ereignisse hinzugefügt, nämlich AfterDeleteColumns und AfterDeleteRows, wie im folgenden Screenshot gezeigt. Diese Ereignisse werden ausgelöst, wenn Sie Spalten bzw. Zeilen löschen.

![todo:image_alt_text](handling-events-after-deleting-columns-and-rows-in-griddesktop_1.png)
## **Behandlung von Ereignissen nach dem Löschen von Spalten und Zeilen in GridDesktop**
Der folgende Beispielcode erläutert, wie die Ereignisse AfterDeleteColumns und AfterDeleteRows genutzt werden können. Immer wenn Sie einige Spalten oder Zeilen löschen, wird die angegebene Funktion aufgerufen und zeigt ein Meldungsfenster, das den Index der gelöschten Spalte oder Zeile anzeigt.
## **Beispielcode**
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
