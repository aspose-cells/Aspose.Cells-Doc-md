---
title: Evitare pagine vuote nell'output PDF quando non c'è niente da stampare
type: docs
weight: 30
url: /it/java/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---
## **Possibili scenari di utilizzo**

Quando il file Excel è vuoto e l'utente lo salva in PDF utilizzando Aspose.Cells, esegue il rendering di una pagina vuota nell'output PDF. A volte, questo comportamento predefinito è indesiderato. Aspose.Cells fornisce il[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) proprietà per affrontare questo problema. Se lo imposterai come**falso**, poi[**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException)si verificherà ogni volta che non c'è niente da stampare nell'output PDF.

## **Evitare pagine vuote nell'output PDF quando non c'è niente da stampare**

Il seguente codice di esempio crea una cartella di lavoro vuota e quindi la salva come output PDF dopo aver impostato il[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) proprietà come**falso**. Poiché non c'è nulla da stampare nell'output PDF, il[**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException)avviene come mostrato di seguito.

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.java" >}}

## **Eccezione**

{{< highlight "java" >}}

 Exception in thread "main" com.aspose.cells.CellsException: There is nothing to output/print.

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.Workbook.a(Unknown Source)

	at com.aspose.cells.Workbook.save(Unknown Source)

{{< /highlight >}}
