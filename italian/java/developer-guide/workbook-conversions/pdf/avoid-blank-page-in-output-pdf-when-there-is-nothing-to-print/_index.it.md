---
title: Evitare Pagina Vuota nel PDF di Output quando non c è Nulla da Stampare
type: docs
weight: 30
url: /it/java/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---

## **Possibili Scenari di Utilizzo**

Quando il file Excel è vuoto e l'utente lo salva in PDF utilizzando Aspose.Cells, viene visualizzata una pagina vuota nel PDF di output. A volte, questo comportamento predefinito non è desiderato. Aspose.Cells fornisce la proprietà [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) per gestire questo problema. Se la si imposta su **false**, allora si verificherà [**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException) quando non c'è nulla da stampare nel PDF di output.

## **Evitare Pagina Vuota nel PDF di Output quando non c'è Nulla da Stampare**

Il seguente codice di esempio crea un foglio di calcolo vuoto e lo salva come PDF di output dopo aver impostato la proprietà [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) come **false**. Poiché non c'è nulla da stampare nel PDF di output, si verifica l'[**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException) come mostrato di seguito.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.java" >}}

## **Eccezione**

{{< highlight java >}}

 Exception in thread "main" com.aspose.cells.CellsException: There is nothing to output/print.

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.Workbook.a(Unknown Source)

	at com.aspose.cells.Workbook.save(Unknown Source)

{{< /highlight >}}
