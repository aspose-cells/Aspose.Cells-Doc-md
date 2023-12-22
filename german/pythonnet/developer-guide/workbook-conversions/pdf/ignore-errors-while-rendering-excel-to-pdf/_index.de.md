---
title: Ignorieren Sie Fehler beim Rendern von Excel auf PDF
type: docs
weight: 80
url: /de/python-net/ignore-errors-while-rendering-excel-to-pdf/
description: Erfahren Sie, wie Sie Fehler beim Rendern von Excel in PDF mit Aspose.Cells for Python via .NET API ignorieren.
keywords: Python Ignore Errors while Rendering Excel to PDF, Ignore Errors while saving Excel to PDF using Python, Python Ignore Errors while converting Excel to PDF, Ignore Errors for Excel to PDF in python
---
##  **Mögliche Nutzungsszenarien**

 Wenn Sie Ihre Excel-Datei in PDF konvertieren, treten manchmal Fehler oder Ausnahmen auf und der Konvertierungsprozess wird abgebrochen. Sie können alle derartigen Fehler während des Konvertierungsvorgangs ignorieren, indem Sie die verwenden[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)Eigentum. Auf diese Weise wird der Konvertierungsprozess reibungslos abgeschlossen, ohne dass Fehler oder Ausnahmen ausgelöst werden, es kann jedoch zu Datenverlusten kommen. Bitte nutzen Sie diese Eigenschaft daher nur, wenn der Datenverlust für Sie unkritisch ist.

##  **Ignorieren Sie Fehler beim Rendern von Excel auf PDF**

 Der folgende Code lädt die[Beispiel-Excel-Datei](55541778.xlsx) aber die Beispiel-Excel-Datei ist fehlerhaft und löst einen Fehler aus[Umstellung auf PDF](55541779.pdf) in 17.11 aber da wir verwenden[**PdfSaveOptions.ignore_error**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/ignore_error/)Eigenschaft, es wird kein Fehler ausgegeben. Allerdings eins*abgerundete rote pfeilartige Form*wie in diesem Screenshot gezeigt, geht verloren.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

##  **Beispielcode**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-IgnoreErrorsWhileRenderingExcelToPdf.py" >}}
