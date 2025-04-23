---
title: Evitare Pagina Vuota nel PDF di Output quando non c è Nulla da Stampare
type: docs
weight: 30
url: /it/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---

## **Possibili Scenari di Utilizzo**

Quando il file Excel è vuoto e l'utente lo salva in PDF utilizzando Aspose.Cells, viene visualizzata una pagina vuota nel PDF di output. A volte, questo comportamento predefinito non è desiderato. Aspose.Cells fornisce la proprietà [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) per gestire questo problema. Se la si imposta su **false**, allora si verificherà [**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception) quando non c'è nulla da stampare nel PDF di output.

## **Evitare Pagina Vuota nel PDF di Output quando non c'è Nulla da Stampare**

Il codice di esempio seguente crea un foglio di lavoro vuoto e lo salva come PDF dopo aver impostato la proprietà [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) su **false**. Poiché non c'è nulla da stampare nel PDF di output, si verifica [**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception) come mostrato di seguito.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.cs" >}}

## **Eccezione**

{{< highlight java >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
