---
title: Hantera händelser efter borttagning av kolumner och rader i GridDesktop
type: docs
weight: 80
url: /sv/net/handling-events-after-deleting-columns-and-rows-in-griddesktop/
---
## **Möjliga användningsscenarier**
Aspose.Cells för GridDesktop har lagt till två nya händelser, dvs AfterDeleteColumns och AfterDeleteRows som visas i följande skärmdump. Dessa händelser aktiveras när du tar bort kolumner respektive rader.

![todo:image_alt_text](handling-events-after-deleting-columns-and-rows-in-griddesktop_1.png)
## **Hantera händelser efter borttagning av kolumner och rader i GridDesktop**
Följande exempelkod förklarar hur du använder AfterDeleteColumns och AfterDeleteRows-händelser. När du tar bort några kolumner eller rader kommer den givna funktionen att anropas och visa en meddelanderuta som visar indexet för den raderade kolumnen eller raden.
## **Exempelkod**
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
