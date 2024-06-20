---
title: Fortschritt der Dokumentkonvertierung verfolgen
type: docs
weight: 970
url: /de/net/track-document-conversion-progress/
---

## **Mögliche Verwendungsszenarien**

Manchmal kann die Konvertierung großer Excel-Dateien einige Zeit in Anspruch nehmen. In dieser Zeit möchten Sie möglicherweise den Dokumentkonvertierungsfortschritt anzeigen, anstatt nur einen Ladefortschrittsbildschirm, um die Benutzerfreundlichkeit Ihrer Anwendung zu verbessern. Aspose.Cells unterstützt die Verfolgung des Dokumentkonvertierungsprozesses durch Bereitstellung des [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)-Interfaces. Das [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)-Interface bietet die [**PageStartSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving)- und [**PageEndSaving**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving)-Methoden, die Sie in Ihrer eigenen Klasse implementieren können. Sie können auch steuern, welche Seiten gerendert werden, wie im benutzerdefinierten TestPageSavingCallback-Klasse demonstriert.

## **Fortschritt der Dokumentkonvertierung nachverfolgen**

Der folgende Codeausschnitt lädt die [Quell-Excel-Datei](94896151.xlsx) und druckt ihren Konvertierungsfortschritt in der Konsole mithilfe der benutzerdefinierten Klasse *TestPageSavingCallback*, die das [**IPageSavingCallback**](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)-Interface implementiert.

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.cs" >}}

Der folgende Code ist für die benutzerdefinierte Klasse *TestPageSavingCallback*.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.cs" >}}

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
