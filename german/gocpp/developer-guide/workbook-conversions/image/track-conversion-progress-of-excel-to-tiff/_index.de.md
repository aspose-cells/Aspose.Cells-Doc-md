---
title: Fortschrittsverfolgung bei der Konvertierung von Excel in TIFF mit Golang über C++
linktitle: Konvertierungsvorgang von Excel nach TIFF verfolgen
type: docs
weight: 190
url: /de/go-cpp/track-conversion-progress-of-excel-to-tiff/
description: Lernen Sie, wie Sie den Fortschritt bei der Umwandlung von Excel Dateien in TIFF mit Aspose.Cells for C++ verfolgen können.
---

## **Mögliche Verwendungsszenarien**

 Das Konvertieren großer Excel-Dateien kann manchmal einige Zeit in Anspruch nehmen. Während dieser Zeit möchten Sie vielleicht den Fortschritt der Dokumenten-Konvertierung anzeigen, anstatt nur einen Ladebildschirm, um die Benutzerfreundlichkeit Ihrer Anwendung zu verbessern. Aspose.Cells unterstützt die Verfolgung des Fortschritts bei der Dokumenten-Konvertierung durch die Bereitstellung der [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/)-Schnittstelle. Die [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/)-Schnittstelle bietet [**PageStartSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pagestartsaving/) und [**PageEndSaving**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/pageendsaving/)-Methoden, die Sie in Ihrer eigenen Klasse implementieren können. Außerdem können Sie steuern, welche Seiten gerendert werden, wie im benutzerdefinierten *TestPageSavingCallback*-Klasse demonstriert.

## **Konvertierungsvorgang von Excel nach TIFF verfolgen**

Das folgende Codebeispiel lädt die [Quelle Excel-Datei](95584311.xlsx) und zeigt den Fortschritt der Konvertierung in der Konsole durch die Verwendung der benutzerdefinierten Klasse *TestPageSavingCallback*, die das [**IPageSavingCallback**](https://reference.aspose.com/cells/go-cpp/ipagesavingcallback/)-Schnittstelle implementiert. Die generierte Ausgabedatei ist zu Ihrer Referenz angehängt.

[Output File](95584312.tiff)

## **Beispielcode**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackConversionProgressOfExcelToTiff.go" >}}
Der folgende Code zeigt die *TestTiffPageSavingCallback*-benutzerdefinierte Klasse.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-TrackConversionProgressOfExcelToTiff-1.go" >}}
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
End saving page index 8 of pages 10</br>

{{< /highlight >}}
