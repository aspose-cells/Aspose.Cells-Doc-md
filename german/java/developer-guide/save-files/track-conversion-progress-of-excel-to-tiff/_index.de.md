---
title: Verfolgen Sie den Konvertierungsfortschritt von Excel in TIFF
type: docs
weight: 140
url: /de/java/track-conversion-progress-of-excel-to-tiff/
---
## **Mögliche Nutzungsszenarien**

Manchmal kann das Konvertieren großer Excel-Dateien einige Zeit dauern. Während dieser Zeit möchten Sie möglicherweise den Fortschritt der Dokumentkonvertierung statt nur eines Ladebildschirms anzeigen, um die Benutzerfreundlichkeit Ihrer Anwendung zu verbessern. Aspose.Cells unterstützt die Verfolgung des Dokumentenkonvertierungsprozesses durch Bereitstellung der**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**Schnittstelle. Das**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**Schnittstelle bietet**[PageStartSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving(com.aspose.cells.PageStartSavingArgs))**und**[PageEndSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving(com.aspose.cells.PageEndSavingArgs))** Methoden, die Sie in Ihrer benutzerdefinierten Klasse implementieren können. Sie können auch steuern, welche Seiten gerendert werden, wie in gezeigt*TestTiffPageSavingCallback*benutzerdefinierte Klasse.

## **Verfolgen Sie den Konvertierungsfortschritt von Excel in TIFF**

Das folgende Codebeispiel lädt die[Excel-Quelldatei](sampleUseWorkbookRenderForImageConversion.xlsx)und druckt seinen Konvertierungsfortschritt in der Konsole mithilfe von*TestTiffPageSavingCallback*benutzerdefinierte Klasse, die die implementiert**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**Schnittstelle. Die generierte Ausgabedatei ist als Referenz beigefügt.

[Ausgabedatei](DocumentConversionProgressForTiff_out.tiff)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.java" >}}

Das Folgende ist der Code für die*TestTiffPageSavingCallback*benutzerdefinierte Klasse.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.java" >}}

## **Konsolenausgabe**

Beginnen Sie mit dem Speichern des Seitenindex 0 der Seiten 10</br>
Beenden Sie das Speichern des Seitenindex 0 der Seiten 10</br>
Beginnen Sie mit dem Speichern von Seitenindex 1 von Seite 10</br>
Beenden Sie das Speichern des Seitenindex 1 der Seite 10</br>
Beginnen Sie mit dem Speichern von Seitenindex 2 von Seite 10</br>
Beenden Sie das Speichern des Seitenindex 2 der Seite 10</br>
Beginnen Sie mit dem Speichern von Seitenindex 3 von Seite 10</br>
Beenden Sie das Speichern des Seitenindex 3 der Seite 10</br>
Beginnen Sie mit dem Speichern von Seitenindex 4 von Seite 10</br>
Beenden Sie das Speichern von Seitenindex 4 von Seite 10</br>
Beginnen Sie mit dem Speichern von Seitenindex 5 der Seiten 10</br>
Beenden Sie das Speichern des Seitenindex 5 der Seite 10</br>
Beginnen Sie mit dem Speichern von Seitenindex 6 von Seite 10</br>
Beenden Sie das Speichern des Seitenindex 6 der Seite 10</br>
Beginnen Sie mit dem Speichern von Seitenindex 7 von Seiten 10</br>
Beenden Sie das Speichern des Seitenindex 7 von Seite 10</br>
Beginnen Sie mit dem Speichern von Seitenindex 8 von Seiten 10</br>
Beenden Sie das Speichern des Seitenindex 8 von Seite 10
