---
title: Evitare pagine vuote nell'output PDF quando non c'è niente da stampare
type: docs
weight: 30
url: /it/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---
## **Possibili scenari di utilizzo**

Quando il file Excel è vuoto e l'utente lo salva in PDF utilizzando Aspose.Cells, esegue il rendering di una pagina vuota nell'output PDF. A volte, questo comportamento predefinito è indesiderato. Aspose.Cells fornisce il[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) proprietà per affrontare questo problema. Se lo imposterai come**falso**, poi[**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)si verificherà ogni volta che non c'è niente da stampare nell'output PDF.

## **Evitare pagine vuote nell'output PDF quando non c'è niente da stampare**

Il codice di esempio seguente crea una cartella di lavoro vuota e quindi la salva come PDF dopo aver impostato il[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) proprietà come**falso**. Poiché non c'è nulla da stampare nell'output PDF, il[**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)avviene come mostrato di seguito.

## **Codice d'esempio**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.cs" >}}

## **Eccezione**

{{< highlight "java" >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
