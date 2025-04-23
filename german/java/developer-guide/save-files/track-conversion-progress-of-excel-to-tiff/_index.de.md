---
title: Konvertierungsvorgang von Excel nach TIFF verfolgen
type: docs
weight: 140
url: /de/java/track-conversion-progress-of-excel-to-tiff/
---

## **Mögliche Verwendungsszenarien**

Manchmal kann die Konvertierung großer Excel-Dateien einige Zeit in Anspruch nehmen. Während dieser Zeit möchten Sie möglicherweise den Dokumentkonvertierungsfortschritt anzeigen, anstatt nur einen Ladebildschirm anzuzeigen, um die Benutzerfreundlichkeit Ihrer Anwendung zu verbessern. Aspose.Cells unterstützt die Verfolgung des Dokumentkonvertierungsprozesses durch Bereitstellung der [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)-Schnittstelle. Die [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)-Schnittstelle bietet [**PageStartSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving-com.aspose.cells.PageStartSavingArgs-) und [**PageEndSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving-com.aspose.cells.PageEndSavingArgs-) Methoden, die Sie in Ihrer eigenen Klasse implementieren können. Sie können auch steuern, welche Seiten dargestellt werden, wie in der benutzerdefinierten Klasse *TestTiffPageSavingCallback* dargestellt.

## **Konvertierungsvorgang von Excel nach TIFF verfolgen**

Der folgende Codeausschnitt lädt die [Quellexceldatei](sampleUseWorkbookRenderForImageConversion.xlsx) und gibt ihren Konvertierungsfortschritt in der Konsole aus, indem die benutzerdefinierte Klasse *TestTiffPageSavingCallback* implementiert wird, die die [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)-Schnittstelle implementiert. Die generierte Ausgabedatei ist für Ihre Referenz angehängt.

[Ausgabedatei](DocumentConversionProgressForTiff_out.tiff)

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.java" >}}

Der folgende Code zeigt die *TestTiffPageSavingCallback*-benutzerdefinierte Klasse.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.java" >}}

## **Konsolenausgabe**

{{< highlight java >}}
Start saving page index 0 of pages 10</br>
End saving page index 0 of pages 10</br>
Start saving page index 1 of pages 10</br>
End saving page index 1 of pages 10</br>
Start saving page index 2 of pages 10</br>
End saving page index 2 of pages 10</br>
Start saving page index 3 of pages 10</br>
End saving page index 3 of pages 10</br>
Start saving page index 4 of pages 10</br>
End saving page index 4 of pages 10</br>
Start saving page index 5 of pages 10</br>
End saving page index 5 of pages 10</br>
Start saving page index 6 of pages 10</br>
End saving page index 6 of pages 10</br>
Start saving page index 7 of pages 10</br>
End saving page index 7 of pages 10</br>
Start saving page index 8 of pages 10</br>
End saving page index 8 of pages 10

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
