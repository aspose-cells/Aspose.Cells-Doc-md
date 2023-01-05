---
title: Verfolgen Sie den Fortschritt der Dokumentenkonvertierung
type: docs
weight: 120
url: /de/java/track-document-conversion-progress/
---
## **Mögliche Nutzungsszenarien**

Manchmal kann das Konvertieren großer Excel-Dateien einige Zeit dauern. Während dieser Zeit möchten Sie möglicherweise den Fortschritt der Dokumentkonvertierung statt nur eines Ladebildschirms anzeigen, um die Benutzerfreundlichkeit Ihrer Anwendung zu verbessern. Aspose.Cells unterstützt die Verfolgung des Dokumentenkonvertierungsprozesses durch Bereitstellung der**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**Schnittstelle. Das**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**Schnittstelle bietet**[PageStartSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageStartSaving(com.aspose.cells.PageStartSavingArgs))**und**[PageEndSaving](https://reference.aspose.com/cells/java/com.aspose.cells/ipagesavingcallback#pageEndSaving(com.aspose.cells.PageEndSavingArgs))** Methoden, die Sie in Ihrer benutzerdefinierten Klasse implementieren können. Sie können auch steuern, welche Seiten gerendert werden, wie in gezeigt*TestPageSavingCallback*benutzerdefinierte Klasse.

## **Verfolgen Sie den Fortschritt der Dokumentenkonvertierung**

Das folgende Codebeispiel lädt die[Excel-Quelldatei](PagesBook1.xlsx)und druckt seinen Konvertierungsfortschritt in der Konsole mithilfe von*TestPageSavingCallback*benutzerdefinierte Klasse, die die implementiert**[IPageSavingCallback](https://reference.aspose.com/cells/java/com.aspose.cells/IPageSavingCallback)**Schnittstelle.

## **Beispielcode**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-1.java" >}}

Das Folgende ist der Code für die*TestPageSavingCallback*benutzerdefinierte Klasse.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-LoadingSavingConvertingAndManaging-DocumentConversionProgress-2.java" >}}

## **Konsolenausgabe**

Beginnen Sie mit dem Speichern des Seitenindex 0 der Seiten 11</br>
Beenden Sie das Speichern des Seitenindex 0 der Seiten 11</br>
Beginnen Sie mit dem Speichern von Seitenindex 1 von Seite 11</br>
Beenden Sie das Speichern des Seitenindex 1 der Seite 11</br>
Beginnen Sie mit dem Speichern von Seitenindex 2 von Seite 11</br>
Beenden Sie das Speichern des Seitenindex 2 der Seite 11</br>
Beginnen Sie mit dem Speichern von Seitenindex 3 von Seite 11</br>
Beenden Sie das Speichern des Seitenindex 3 der Seite 11</br>
Beginnen Sie mit dem Speichern von Seitenindex 4 von Seite 11</br>
Beenden Sie das Speichern von Seitenindex 4 von Seite 11</br>
Beginnen Sie mit dem Speichern von Seitenindex 5 von Seite 11</br>
Beenden Sie das Speichern des Seitenindex 5 der Seite 11</br>
Beginnen Sie mit dem Speichern von Seitenindex 6 von Seite 11</br>
Beenden Sie das Speichern des Seitenindex 6 der Seite 11</br>
Beginnen Sie mit dem Speichern von Seitenindex 7 von Seite 11</br>
Beenden Sie das Speichern des Seitenindex 7 von Seite 11</br>
Beginnen Sie mit dem Speichern von Seitenindex 8 der Seiten 11</br>
Beenden Sie das Speichern des Seitenindex 8 der Seite 11
