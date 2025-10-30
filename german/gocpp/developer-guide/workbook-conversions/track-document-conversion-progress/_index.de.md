---
title: Verfolgen Sie den Fortschritt der Dokumentkonvertierung mit Golang via C++
linktitle: Fortschritt der Dokumentkonvertierung verfolgen
type: docs
weight: 970
url: /de/go-cpp/track-document-conversion-progress/
description: Erfahren Sie, wie Sie den Fortschritt der Dokumentkonvertierung in C++ mit Aspose.Cells verfolgen, um die Benutzerfreundlichkeit der Anwendung zu verbessern.
---

## **Mögliche Verwendungsszenarien**

Das Konvertieren großer Excel-Dateien kann manchmal einige Zeit in Anspruch nehmen. Während dieser Zeit möchten Sie vielleicht den Fortschritt der Dokumentkonvertierung anzeigen, anstatt nur einen Ladebildschirm, um die Benutzererfahrung Ihrer Anwendung zu verbessern. Aspose.Cells unterstützt die Verfolgung des Fortschritts durch die Bereitstellung der [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/)-Schnittstelle. Die [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/)-Schnittstelle bietet [**PageStartSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pagestartsaving/) and [**PageEndSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pageendsaving/)-Methoden, die Sie in Ihrer benutzerdefinierten Klasse implementieren können. Sie können auch steuern, welche Seiten gerendert werden, wie in der benutzerdefinierten Klasse `TestPageSavingCallback` demonstriert.

## **Fortschritt der Dokumentkonvertierung nachverfolgen**

Der nachstehende Code lädt die [Quell-Excel-Datei](94896151.xlsx) und zeigt den Fortschritt der Konvertierung in der Konsole an, indem die benutzerdefinierte Klasse `TestPageSavingCallback` die [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/)-Schnittstelle implementiert.

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackDocumentConversionProgress.go" >}}
Der folgende Code ist für die benutzerdefinierte Klasse `TestPageSavingCallback`.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackDocumentConversionProgress-1.go" >}}
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
