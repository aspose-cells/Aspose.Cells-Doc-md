---
title: Fortschritt der Dokumentkonvertierung verfolgen
type: docs
weight: 120
url: /de/java/track-document-conversion-progress/
---

## **Mögliche Verwendungsszenarien**

Manchmal kann die Konvertierung großer Excel-Dateien einige Zeit in Anspruch nehmen. Während dieser Zeit möchten Sie möglicherweise den Dokumentkonvertierungsfortschritt anzeigen, anstatt nur einen Ladebildschirm anzuzeigen, um die Benutzerfreundlichkeit Ihrer Anwendung zu verbessern. Aspose.Cells unterstützt die Verfolgung des Dokumentkonvertierungsprozesses durch Bereitstellung der [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)-Schnittstelle. Die [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)-Schnittstelle bietet [**PageStartSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving-com.aspose.cells.PageStartSavingArgs-) und [**PageEndSaving**](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving-com.aspose.cells.PageEndSavingArgs-) Methoden, die Sie in Ihrer eigenen Klasse implementieren können. Sie können auch steuern, welche Seiten dargestellt werden, wie in der benutzerdefinierten Klasse *TestPageSavingCallback* dargestellt.

## **Fortschritt der Dokumentkonvertierung nachverfolgen**

Der folgende Codeausschnitt lädt die [Quelle-Excel-Datei](PagesBook1.xlsx) und gibt ihren Konvertierungsfortschritt in der Konsole aus, indem die benutzerdefinierte Klasse *TestPageSavingCallback* implementiert wird, die die [**IPageSavingCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)-Schnittstelle implementiert.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.java" >}}

Der folgende Code ist für die benutzerdefinierte Klasse *TestPageSavingCallback*.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.java" >}}

## **Konsolenausgabe**

{{< highlight java >}}

Start saving page index 0 of pages 11</br>
End saving page index 0 of pages 11</br>
Start saving page index 1 of pages 11</br>
End saving page index 1 of pages 11</br>
Start saving page index 2 of pages 11</br>
End saving page index 2 of pages 11</br>
Start saving page index 3 of pages 11</br>
End saving page index 3 of pages 11</br>
Start saving page index 4 of pages 11</br>
End saving page index 4 of pages 11</br>
Start saving page index 5 of pages 11</br>
End saving page index 5 of pages 11</br>
Start saving page index 6 of pages 11</br>
End saving page index 6 of pages 11</br>
Start saving page index 7 of pages 11</br>
End saving page index 7 of pages 11</br>
Start saving page index 8 of pages 11</br>
End saving page index 8 of pages 11

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
