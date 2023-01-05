---
title: Fehler beim Rendern von Excel auf PDF ignorieren
type: docs
weight: 70
url: /de/java/ignore-errors-while-rendering-excel-to-pdf/
---
## **Mögliche Nutzungsszenarien**

Wenn Sie Ihre Excel-Datei in PDF konvertieren, treten manchmal Fehler oder Ausnahmen auf und der Konvertierungsprozess wird beendet. Sie können alle diese Fehler während des Konvertierungsprozesses ignorieren, indem Sie die verwenden[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError)Eigentum. Auf diese Weise wird der Konvertierungsprozess reibungslos abgeschlossen, ohne dass Fehler oder Ausnahmen ausgelöst werden, es kann jedoch zu Datenverlusten kommen. Nutzen Sie diese Eigenschaft daher bitte nur, wenn der Datenverlust für Sie unkritisch ist.

## **Fehler beim Rendern von Excel auf PDF ignorieren**

Der folgende Code lädt die[Beispiel-Excel-Datei](55541813.xlsx)aber die Beispiel-Excel-Datei ist fehlerhaft und löst einen Fehler aus[Umstellung auf PDF](55541814.pdf)in 17.11 aber da verwenden wir[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#IgnoreError)-Eigenschaft, wird kein Fehler ausgegeben. Eine abgerundete rote pfeilähnliche Form, wie in diesem Screenshot gezeigt, geht jedoch verloren.

![todo: Bild_alt_Text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.java" >}}
