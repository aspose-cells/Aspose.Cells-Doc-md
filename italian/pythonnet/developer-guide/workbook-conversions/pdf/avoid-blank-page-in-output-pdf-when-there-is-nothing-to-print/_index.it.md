---
title: Evita la pagina vuota nell'output PDF quando non c'è nulla da stampare
type: docs
weight: 30
url: /it/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Scopri come evitare pagine vuote nell'output PDF quando non c'è nulla da stampare con Aspose.Cells for Python via .NET API.
keywords: Python Avoid Blank Page in Output PDF when there is Nothing to Print
---
##  **Possibili scenari di utilizzo**

Quando il file Excel è vuoto e l'utente lo salva in PDF utilizzando Aspose.Cells for Python via .NET, viene visualizzata una pagina vuota nell'output PDF. A volte, questo comportamento predefinito non è desiderabile. Aspose.Cells for Python via .NET fornisce il[**PdfSaveOptions.output_blank_page_when_niente_da_stampare**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)proprietà per affrontare questo problema. Se lo imposterai come *false**, allora[**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)si verificherà ogni volta che non c'è nulla da stampare nell'output PDF.

##  **Evita la pagina vuota nell'output PDF quando non c'è nulla da stampare**

Il codice di esempio seguente crea una cartella di lavoro vuota e quindi la salva come PDF dopo aver impostato il valore[**PdfSaveOptions.output_blank_page_when_niente_da_stampare**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)proprietà come *false**. Poiché non c'è nulla da stampare nell'output PDF, il file[**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)si verifica come mostrato di seguito.

##  **Codice d'esempio**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.py" >}}

##  **Eccezione**

{{< highlight "java" >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
