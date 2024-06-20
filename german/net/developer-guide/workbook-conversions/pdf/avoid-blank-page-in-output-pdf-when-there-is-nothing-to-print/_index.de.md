---
title: Leere Seite im Ausgabe PDF vermeiden, wenn nichts gedruckt werden soll
type: docs
weight: 30
url: /de/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---

## **Mögliche Verwendungsszenarien**

Wenn die Excel-Datei leer ist und der Benutzer sie in PDF mit Aspose.Cells speichert, wird im Ausgabe-PDF eine leere Seite gerendert. Manchmal ist dieses Standardverhalten unerwünscht. Aspose.Cells stellt die [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint)-Eigenschaft bereit, um dieses Problem zu behandeln. Wenn Sie es auf **false** setzen, dann tritt [**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception) auf, wenn nichts im Ausgabe-PDF gedruckt werden soll.

## **Leere Seite im Ausgabe-PDF vermeiden, wenn nichts gedruckt werden soll**

Der folgende Beispielcode erstellt eine leere Arbeitsmappe und speichert sie dann als PDF, nachdem die Eigenschaft [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) auf **false** gesetzt wurde. Da in der Ausgabedatei PDF nichts gedruckt werden soll, tritt die [**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception) wie unten gezeigt auf.

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.cs" >}}

## **Ausnahme**

{{< highlight java >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
