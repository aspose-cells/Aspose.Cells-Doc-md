---
title: Fehler beim Rendern von Excel nach PDF mit Golang via C++ ignorieren
linktitle: Fehler ignorieren beim Umsetzen von Excel in PDF
type: docs
weight: 80
url: /de/go-cpp/ignore-errors-while-rendering-excel-to-pdf/
description: Erfahren Sie, wie Sie Fehler während der Excel zu PDF Konvertierung mit Aspose.Cells for C++ ignorieren.
---

## **Mögliche Verwendungsszenarien**

Manchmal treten beim Konvertieren Ihrer Excel-Datei in PDF Fehler oder Ausnahmen auf, und der Konvertierungsprozess wird beendet. Sie können alle solchen Fehler während des Konvertierungsprozesses ignorieren, indem Sie die [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) -Eigenschaft verwenden. Auf diese Weise wird der Konvertierungsprozess reibungslos abgeschlossen, ohne Fehler oder Ausnahmen zu verursachen, aber es kann zum Datenverlust kommen. Bitte verwenden Sie diese Eigenschaft nur, wenn der Datenverlust für Sie nicht kritisch ist.

## **Ignorieren Sie Fehler beim Rendern von Excel in PDF**

Der folgende Code lädt die [Beispiel-Excel-Datei](55541778.xlsx), aber die Excel-Datei ist fehlerhaft und wirft einen Fehler während der [Konvertierung in PDF](55541779.pdf) in 17.11, aber da wir die [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) -Eigenschaft verwenden, wird kein Fehler angezeigt. Ein *abgerundeter roter Pfeil ähnlicher Shape*, wie in diesem Screenshot gezeigt, geht jedoch verloren.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-IgnoreErrorsWhileRenderingExcelToPdf.go" >}}
