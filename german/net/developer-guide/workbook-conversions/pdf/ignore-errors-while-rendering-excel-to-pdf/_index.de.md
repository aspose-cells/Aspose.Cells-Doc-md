---
title: Fehler ignorieren beim Umsetzen von Excel in PDF
type: docs
weight: 80
url: /de/net/ignore-errors-while-rendering-excel-to-pdf/
---

## **Mögliche Verwendungsszenarien**

Manchmal treten beim Umsetzen Ihrer Excel-Datei in PDF Fehler oder Ausnahmen auf und der Umsetzungsprozess wird abgebrochen. Sie können während des Umsetzungsprozesses alle solchen Fehler ignorieren, indem Sie die [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)-Eigenschaft verwenden. Auf diese Weise wird der Umsetzungsprozess reibungslos abgeschlossen, ohne dass ein Fehler oder eine Ausnahme auftritt, aber ein Datenverlust kann auftreten. Verwenden Sie diese Eigenschaft daher nur, wenn der Datenverlust für Sie nicht kritisch ist.

## **Ignorieren Sie Fehler beim Rendern von Excel in PDF**

Der folgende Code lädt die [Beispiel-Excel-Datei](55541778.xlsx), aber die Beispiel-Excel-Datei ist fehlerhaft und wirft in 17.11 während der [Umsetzung in PDF](55541779.pdf) einen Fehler. Da wir jedoch die [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)-Eigenschaft verwenden, wirft er keinen Fehler. Allerdings geht eine *gerundete rote Pfeilform* wie in diesem Screenshot verloren.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.cs" >}}
