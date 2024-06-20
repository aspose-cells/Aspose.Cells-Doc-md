---
title: Gestione degli eventi dopo la cancellazione di colonne e righe in GridDesktop
type: docs
weight: 80
url: /it/net/aspose-cells-griddesktop/handle-events-after-delete-columns-and-rows-in-griddesktop/
keywords: GridDesktop, eventi, cancella riga, cancella colonna
description: Questo articolo presenta gli eventi dopo la cancellazione di righe/colonne in GridDesktop.
---

## **Possibili Scenari di Utilizzo**
Aspose.Cells for GridDesktop ha aggiunto due nuovi eventi, ovvero AfterDeleteColumns e AfterDeleteRows come mostrato nella seguente schermata. Questi eventi vengono attivati quando si eliminano rispettivamente colonne e righe.

![todo:image_alt_text](handling-events-after-deleting-columns-and-rows-in-griddesktop_1.png)
## **Gestione degli eventi dopo la cancellazione di colonne e righe in GridDesktop**
Il seguente codice di esempio spiega come utilizzare gli eventi AfterDeleteColumns e AfterDeleteRows. Ogni volta che vengono eliminate alcune colonne o righe, verrà chiamata la funzione data e verrà visualizzata una finestra di dialogo che mostra l'indice della colonna o riga eliminata.
## **Codice di Esempio**
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
