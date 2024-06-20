---
title: Fehler ignorieren beim Umsetzen von Excel in PDF
type: docs
weight: 80
url: /de/python-net/ignore-errors-while-rendering-excel-to-pdf/
description: Erfahren Sie, wie Sie Fehler beim Rendering von Excel zu PDF mit Aspose.Cells für Python via .NET API ignorieren können.
keywords: Python Ignorieren Sie Fehler beim Rendering von Excel zu PDF, Ignorieren Sie Fehler beim Speichern von Excel zu PDF mit Python, Python Ignorieren Sie Fehler bei der Umwandlung von Excel in PDF, Ignorieren Sie Fehler für Excel zu PDF in Python
---

## **Mögliche Verwendungsszenarien**

Manchmal treten beim Umsetzen Ihrer Excel-Datei in PDF Fehler oder Ausnahmen auf und der Umsetzungsprozess wird abgebrochen. Sie können während des Umsetzungsprozesses alle solchen Fehler ignorieren, indem Sie die [**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)-Eigenschaft verwenden. Auf diese Weise wird der Umsetzungsprozess reibungslos abgeschlossen, ohne dass ein Fehler oder eine Ausnahme auftritt, aber ein Datenverlust kann auftreten. Verwenden Sie diese Eigenschaft daher nur, wenn der Datenverlust für Sie nicht kritisch ist.

## **Ignorieren Sie Fehler beim Rendern von Excel in PDF**

Der folgende Code lädt die [Beispiel-Excel-Datei](55541778.xlsx), aber die Beispiel-Excel-Datei ist fehlerhaft und wirft in 17.11 während der [Umsetzung in PDF](55541779.pdf) einen Fehler. Da wir jedoch die [**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)-Eigenschaft verwenden, wirft er keinen Fehler. Allerdings geht eine *gerundete rote Pfeilform* wie in diesem Screenshot verloren.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-IgnoreErrorsWhileRenderingExcelToPdf.py" >}}
