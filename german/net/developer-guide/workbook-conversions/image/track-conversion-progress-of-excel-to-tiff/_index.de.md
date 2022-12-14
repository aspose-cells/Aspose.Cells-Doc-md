---
title: Verfolgen Sie den Konvertierungsfortschritt von Excel in TIFF
type: docs
weight: 190
url: /de/net/track-conversion-progress-of-excel-to-tiff/
---
## **Mögliche Nutzungsszenarien**

 Manchmal kann das Konvertieren großer Excel-Dateien einige Zeit dauern. Während dieser Zeit möchten Sie möglicherweise den Fortschritt der Dokumentkonvertierung statt nur eines Ladebildschirms anzeigen, um die Benutzerfreundlichkeit Ihrer Anwendung zu verbessern. Aspose.Cells unterstützt die Verfolgung des Dokumentenkonvertierungsprozesses durch Bereitstellung der**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)** Schnittstelle. Das**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)**Schnittstelle bietet**[PageStartSaving](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pagestartsaving)**und**[PageEndSaving](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback/methods/pageendsaving)**Methoden, die Sie in Ihrer benutzerdefinierten Klasse implementieren können. Sie können auch steuern, welche Seiten gerendert werden, wie im T*estPageSavingCallback*benutzerdefinierte Klasse.

## **Verfolgen Sie den Konvertierungsfortschritt von Excel in TIFF**

 Das folgende Codebeispiel lädt die[Excel-Quelldatei](95584311.xlsx) und druckt seinen Konvertierungsfortschritt in der Konsole mithilfe von*TestPageSavingCallback* benutzerdefinierte Klasse, die die implementiert**[IPageSavingCallback](https://reference.aspose.com/cells/net/aspose.cells.rendering/ipagesavingcallback)**Schnittstelle. Die generierte Ausgabedatei ist als Referenz beigefügt.

[Ausgabedatei](95584312.tiff)

## **Beispielcode**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-1.cs" >}}

Das Folgende ist der Code für die*TestTiffPageSavingCallback*benutzerdefinierte Klasse.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-LoadingSavingConvertingAndManaging-DocumentConversionProgressForTiff-2.cs" >}}

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
Beenden Sie das Speichern des Seitenindex 8 von Seite 10</br>

