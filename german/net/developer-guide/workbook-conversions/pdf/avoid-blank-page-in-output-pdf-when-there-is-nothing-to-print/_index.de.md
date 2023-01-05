---
title: Vermeiden Sie eine leere Seite in der Ausgabe PDF, wenn nichts zu drucken ist
type: docs
weight: 30
url: /de/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
---
## **Mögliche Nutzungsszenarien**

Wenn die Excel-Datei leer ist und der Benutzer sie unter PDF mit Aspose.Cells speichert, wird in der Ausgabe PDF eine leere Seite gerendert. Manchmal ist dieses Standardverhalten unerwünscht. Aspose.Cells bietet die[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) Eigenschaft, mit diesem Problem umzugehen. Wenn Sie es so einstellen**FALSCH**, dann[**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)tritt immer dann auf, wenn in der Ausgabe PDF nichts zu drucken ist.

## **Vermeiden Sie eine leere Seite in der Ausgabe PDF, wenn nichts zu drucken ist**

Der folgende Beispielcode erstellt eine leere Arbeitsmappe und speichert sie dann als PDF nach dem Festlegen von[**PdfSaveOptions.OutputBlankPageWhenNothingToPrint**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/outputblankpagewhennothingtoprint) Eigentum als**FALSCH**. Da in der Ausgabe PDF nichts zu drucken ist, wird die[**CellsException**](https://reference.aspose.com/cells/net/aspose.cells/cellsexception)geschieht wie unten gezeigt.

## **Beispielcode**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Rendering-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.cs" >}}

## **Ausnahme**

{{< highlight "java" >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
