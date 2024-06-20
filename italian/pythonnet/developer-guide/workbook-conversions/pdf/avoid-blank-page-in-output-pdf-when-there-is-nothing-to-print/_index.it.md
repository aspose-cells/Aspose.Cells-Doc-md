---
title: Evitare Pagina Vuota nel PDF di Output quando non c è Nulla da Stampare
type: docs
weight: 30
url: /it/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Scopri come evitare la pagina bianca nel PDF di output quando non c è nulla da stampare con Aspose.Cells per Python via .NET API.
keywords: Evita la Pagina Bianca nel PDF di Output quando Non c è Nulla da Stampare con Python
---

## **Possibili Scenari di Utilizzo**

Quando il file Excel è vuoto e l'utente lo salva in PDF usando Aspose.Cells per Python via .NET, viene generata una pagina bianca nel PDF di output. A volte, questo comportamento predefinito è indesiderabile. Aspose.Cells per Python via .NET fornisce la proprietà [**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/) per affrontare questo problema. Se la imposti su **false**, allora si verificherà [**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/) ogni volta che non ci sarà nulla da stampare nel PDF di output.

## **Evitare Pagina Vuota nel PDF di Output quando non c'è Nulla da Stampare**

Il codice di esempio seguente crea un foglio di lavoro vuoto e lo salva come PDF dopo aver impostato la proprietà [**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/) su **false**. Poiché non c'è nulla da stampare nel PDF di output, si verifica [**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/) come mostrato di seguito.

## **Codice di Esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.py" >}}

## **Eccezione**

{{< highlight java >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
