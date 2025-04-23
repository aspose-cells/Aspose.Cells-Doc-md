---
title: Fehler ignorieren beim Umsetzen von Excel in PDF
type: docs
weight: 70
url: /de/java/ignore-errors-while-rendering-excel-to-pdf/
---

## **Mögliche Verwendungsszenarien**

Manchmal treten beim Konvertieren Ihrer Excel-Datei in PDF Fehler oder Ausnahmen auf, und der Konvertierungsprozess wird beendet. Sie können alle solchen Fehler während des Konvertierungsprozesses mithilfe der Eigenschaft [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError) ignorieren. Auf diese Weise wird der Konvertierungsprozess reibungslos abgeschlossen, ohne Fehler oder Ausnahmen zu werfen, jedoch kann ein Datenverlust auftreten. Verwenden Sie diese Eigenschaft daher bitte nur, wenn der Datenverlust nicht kritisch für Sie ist.

## **Ignorieren Sie Fehler beim Rendern von Excel in PDF**

Der folgende Code lädt die [Beispiel-Excel-Datei](55541813.xlsx), aber die Beispiel-Excel-Datei ist fehlerhaft und wirft bei der [Konvertierung in PDF](55541814.pdf) in 17.11 einen Fehler, aber da wir die Eigenschaft [**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError) verwenden, wirft es keinen Fehler. Allerdings geht eine gerundete rote pfeilartige Form wie in diesem Screenshot verloren.

![todo:image_alt_text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.java" >}}
{{< app/cells/assistant language="java" >}}
