---
title: Fehler beim Rendern von Excel auf PDF ignorieren
type: docs
weight: 80
url: /de/net/ignore-errors-while-rendering-excel-to-pdf/
---
## **Mögliche Nutzungsszenarien**

 Wenn Sie Ihre Excel-Datei in PDF konvertieren, treten manchmal Fehler oder Ausnahmen auf und der Konvertierungsprozess wird beendet. Sie können alle diese Fehler während des Konvertierungsprozesses ignorieren, indem Sie die verwenden[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)Eigentum. Auf diese Weise wird der Konvertierungsprozess reibungslos abgeschlossen, ohne dass Fehler oder Ausnahmen ausgelöst werden, es kann jedoch zu Datenverlusten kommen. Nutzen Sie diese Eigenschaft daher bitte nur, wenn der Datenverlust für Sie unkritisch ist.

## **Fehler beim Rendern von Excel auf PDF ignorieren**

 Der folgende Code lädt die[Beispiel-Excel-Datei](55541778.xlsx) aber die Beispiel-Excel-Datei ist fehlerhaft und gibt währenddessen einen Fehler aus[Umstellung auf PDF](55541779.pdf) in 17.11 aber da verwenden wir[**PdfSaveOptions.IgnoreError**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/ignoreerror)-Eigenschaft, wird kein Fehler ausgegeben. Allerdings eins*abgerundete rote pfeilähnliche Form*wie in diesem Screenshot gezeigt, geht verloren.

![todo: Bild_alt_Text](ignore-errors-while-rendering-excel-to-pdf_1.png)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Rendering-IgnoreErrorsWhileRenderingExcelToPdf.cs" >}}
