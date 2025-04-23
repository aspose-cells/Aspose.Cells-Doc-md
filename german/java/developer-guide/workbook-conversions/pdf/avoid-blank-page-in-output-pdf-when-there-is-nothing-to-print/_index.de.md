---
title: Leere Seite im Ausgabe PDF vermeiden, wenn nichts gedruckt werden soll
type: docs
weight: 30
url: /de/java/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---

## **Mögliche Verwendungsszenarien**

Wenn die Excel-Datei leer ist und der Benutzer sie in PDF mit Aspose.Cells speichert, wird im Ausgabe-PDF eine leere Seite gerendert. Manchmal ist dieses Standardverhalten unerwünscht. Aspose.Cells stellt die [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint)-Eigenschaft bereit, um dieses Problem zu behandeln. Wenn Sie es auf **false** setzen, dann tritt [**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException) auf, wenn nichts im Ausgabe-PDF gedruckt werden soll.

## **Leere Seite im Ausgabe-PDF vermeiden, wenn nichts gedruckt werden soll**

Der folgende Beispielcode erstellt eine leere Arbeitsmappe und speichert sie dann als Ausgabe-PDF, nachdem die [**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint)-Eigenschaft auf **false** gesetzt wurde. Da im Ausgabe-PDF nichts gedruckt werden soll, tritt [**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException) wie unten gezeigt auf.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.java" >}}

## **Ausnahme**

{{< highlight java >}}

 Exception in thread "main" com.aspose.cells.CellsException: There is nothing to output/print.

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.Workbook.a(Unknown Source)

	at com.aspose.cells.Workbook.save(Unknown Source)

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
