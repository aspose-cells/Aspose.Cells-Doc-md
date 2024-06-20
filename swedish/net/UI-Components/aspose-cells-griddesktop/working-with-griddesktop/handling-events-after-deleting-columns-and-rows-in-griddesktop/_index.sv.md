---
title: Hantera händelser efter att kolumner och rader har tagits bort i GridDesktop
type: docs
weight: 80
url: /sv/net/aspose-cells-griddesktop/handle-events-after-delete-columns-and-rows-in-griddesktop/
keywords: GridDesktop,händelser,ta bort rad,ta bort kolumn
description: Den här artikeln introducerar händelserna efter att ha tagit bort rad/kolumn i GridDesktop.
---

## **Möjliga användningsscenario**
Aspose.Cells för GridDesktop har lagt till två nya händelser dvs. AfterDeleteColumns och AfterDeleteRows som visas i följande skärmbild. Dessa händelser utlöses när du tar bort kolumner och rader respektive.

![todo:image_alt_text](handling-events-after-deleting-columns-and-rows-in-griddesktop_1.png)
## **Hantera händelser efter att ha tagit bort kolumner och rader i GridDesktop**
Den följande exempelkoden förklarar hur man använder händelserna AfterDeleteColumns och AfterDeleteRows. När du tar bort vissa kolumner eller rader kommer den angivna funktionen att kallas och visa en informationsruta som visar indexet för den borttagna kolumnen eller raden.
## **Exempelkod**
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
