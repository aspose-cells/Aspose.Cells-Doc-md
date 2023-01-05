---
title: Gestione degli eventi dopo l'eliminazione di colonne e righe in GridDesktop
type: docs
weight: 80
url: /it/net/handling-events-after-deleting-columns-and-rows-in-griddesktop/
---
## **Possibili scenari di utilizzo**
Aspose.Cells per GridDesktop ha aggiunto due nuovi eventi, ovvero AfterDeleteColumns e AfterDeleteRows, come mostrato nello screenshot seguente. Questi eventi vengono attivati quando elimini rispettivamente colonne e righe.

![cose da fare:immagine_alt_testo](handling-events-after-deleting-columns-and-rows-in-griddesktop_1.png)
## **Gestione degli eventi dopo l'eliminazione di colonne e righe in GridDesktop**
Il seguente codice di esempio spiega come utilizzare gli eventi AfterDeleteColumns e AfterDeleteRows. Ogni volta che elimini alcune colonne o righe, la funzione data verrà chiamata e mostrerà una finestra di messaggio che mostra l'indice della colonna o riga eliminata.
## **Codice d'esempio**
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
