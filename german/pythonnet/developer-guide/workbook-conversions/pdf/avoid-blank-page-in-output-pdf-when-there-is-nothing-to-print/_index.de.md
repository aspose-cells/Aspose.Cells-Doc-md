---
title: Vermeiden Sie leere Seiten in der Ausgabe PDF, wenn nichts zum Drucken vorhanden ist
type: docs
weight: 30
url: /de/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/
description: Erfahren Sie, wie Sie leere Seiten in der Ausgabe PDF vermeiden, wenn mit Aspose.Cells for Python via .NET API nichts zu drucken ist.
keywords: Python Avoid Blank Page in Output PDF when there is Nothing to Print
---
##  **Mögliche Nutzungsszenarien**

Wenn die Excel-Datei leer ist und der Benutzer sie mit Aspose.Cells for Python via .NET unter PDF speichert, wird in der Ausgabe PDF eine leere Seite gerendert. Manchmal ist dieses Standardverhalten unerwünscht. Aspose.Cells for Python via .NET bietet die[**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)Eigentum, um dieses Problem zu lösen. Wenn Sie es auf *false** setzen, dann[**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)tritt immer dann auf, wenn in der Ausgabe PDF nichts zum Drucken vorhanden ist.

##  **Vermeiden Sie leere Seiten in der Ausgabe PDF, wenn nichts zum Drucken vorhanden ist**

Der folgende Beispielcode erstellt eine leere Arbeitsmappe und speichert sie nach dem Festlegen als PDF[**PdfSaveOptions.output_blank_page_when_nothing_to_print**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/output_blank_page_when_nothing_to_print/)Eigenschaft als *falsch**. Da in der Ausgabe PDF nichts zum Drucken vorhanden ist, wird die[**CellsException**](https://reference.aspose.com/cells/python-net/aspose.cells/cellsexception/)geschieht wie unten gezeigt.

##  **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AvoidBlankPageInOutputPdfWhenThereIsNothingToPrint.py" >}}

##  **Ausnahme**

{{< highlight "java" >}}

 Aspose.Cells.CellsException was unhandled

  HResult=-2146232832

  Message=There is nothing to output/print.

  Source=Aspose.Cells

  StackTrace:

       at Aspose.Cells.Workbook.Save(String fileName, SaveOptions saveOptions)

{{< /highlight >}}
