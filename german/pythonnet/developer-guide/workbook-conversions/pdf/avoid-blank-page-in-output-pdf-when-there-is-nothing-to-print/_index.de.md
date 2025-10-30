---
title: Leere Seite im Ausgabe PDF vermeiden, wenn nichts gedruckt werden soll
type: docs
weight: 30
url: /de/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Lernen Sie, wie Sie leere Seiten im Ausgabepdf vermeiden, wenn nichts gedruckt werden soll, mit Aspose.Cells für Python via .NET API
keywords: Python vermeiden Sie leere Seite im Ausgabepdf, wenn nichts gedruckt werden soll
---

## **Mögliche Verwendungsszenarien**

Wenn die Excel-Datei leer ist und der Benutzer sie mit Aspose.Cells für Python via .NET in PDF speichert, wird eine leere Seite im Ausgabepdf gerendert. Manchmal ist dieses Standardverhalten unerwünscht. Aspose.Cells für Python via .NET bietet die [**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)-Eigenschaft, um dieses Problem zu behandeln. Wenn Sie es auf **false** setzen, tritt [**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/) auf, wenn im Ausgabepdf nichts zu drucken ist.

## **Leere Seite im Ausgabe-PDF vermeiden, wenn nichts gedruckt werden soll**

Der folgende Beispielcode erstellt eine leere Arbeitsmappe und speichert sie dann als PDF, nachdem die Eigenschaft [**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/) auf **false** gesetzt wurde. Da in der Ausgabedatei PDF nichts gedruckt werden soll, tritt die [**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/) wie unten gezeigt auf.

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.py" >}}

## **Ausnahme**

{{< highlight java >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
{{< app/cells/assistant language="python-net" >}}
