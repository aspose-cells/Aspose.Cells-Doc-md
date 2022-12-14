---
title: Vermeiden Sie leere Seiten im Ausgabe-PDF, wenn es nichts zu drucken gibt
type: docs
weight: 30
url: /de/java/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---
## **Mögliche Nutzungsszenarien**

Wenn die Excel-Datei leer ist und der Benutzer sie mit Aspose.Cells als PDF speichert, wird im Ausgabe-PDF eine leere Seite gerendert. Manchmal ist dieses Standardverhalten unerwünscht. Aspose.Cells bietet die[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) Eigenschaft, mit diesem Problem umzugehen. Wenn Sie es so einstellen**FALSCH**, dann[**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException)tritt immer dann auf, wenn in der Ausgabe-PDF nichts zu drucken ist.

## **Vermeiden Sie leere Seiten im Ausgabe-PDF, wenn es nichts zu drucken gibt**

Der folgende Beispielcode erstellt eine leere Arbeitsmappe und speichert sie nach dem Festlegen von als Ausgabe-PDF[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OutputBlankPageWhenNothingToPrint) Eigentum als**FALSCH**. Da in der Ausgabe-PDF nichts zu drucken ist, wird die[**CellsException**](https://reference.aspose.com/cells/java/com.aspose.cells/CellsException)geschieht wie unten gezeigt.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.java" >}}

## **Ausnahme**

{{< highlight "java" >}}

 Exception in thread "main" com.aspose.cells.CellsException: There is nothing to output/print.

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.zcab.a(Unknown Source)

	at com.aspose.cells.Workbook.a(Unknown Source)

	at com.aspose.cells.Workbook.save(Unknown Source)

{{< /highlight >}}
