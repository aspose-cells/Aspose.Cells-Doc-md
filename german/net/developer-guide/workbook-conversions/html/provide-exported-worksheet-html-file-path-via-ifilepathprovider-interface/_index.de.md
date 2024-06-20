---
title: Bereitstellung des exportierten Arbeitsblatt HTML Dateipfads über die IFilePathProvider Schnittstelle
type: docs
weight: 70
url: /de/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Mögliche Verwendungsszenarien**
Angenommen, Sie haben eine Excel-Datei mit mehreren Arbeitsblättern und möchten jedes Arbeitsblatt in separate HTML-Dateien exportieren. Wenn eines Ihrer Arbeitsblätter Links zu anderen Arbeitsblättern enthält, werden diese Links in der exportierten HTML-Datei unterbrochen. Um dieses Problem zu lösen, bietet Aspose.Cells die [IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)-Schnittstelle, die Sie implementieren können, um die defekten Links zu reparieren.
## **Exportierten Arbeitsblatt-HTML-Dateipfad über das IFilePathProvider-Interface bereitstellen**
Bitte laden Sie die [Beispiel-Excel-Datei](5115213.zip) herunter, die im folgenden Code verwendet wird, und ihre exportierten HTML-Dateien. Alle diese Dateien befinden sich im Temp-Verzeichnis. Sie sollten sie auf Laufwerk C: extrahieren. Dann wird daraus das Verzeichnis C:\Temp. Dann öffnen Sie die Datei Sheet1.html im Browser und klicken auf die zwei Links darin. Diese Links verweisen auf diese beiden exportierten HTML-Arbeitsblätter, die sich im Verzeichnis C:\Temp\Andere Blätter befinden.

{{< highlight java >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

Die folgende Abbildung zeigt, wie die C:\Temp\Sheet1.html und ihre Links aussehen

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

Die folgende Abbildung zeigt die HTML-Quelle. Wie Sie sehen können, verweisen die Links jetzt auf das Verzeichnis C:\Temp\Andere Blätter. Dies wurde mit Hilfe der [IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)-Schnittstelle erreicht.

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Beispielcode**
Bitte beachten Sie, dass das Verzeichnis C:\Temp nur zu Illustrationszwecken dient. Sie können ein beliebiges Verzeichnis Ihrer Wahl verwenden und die [Beispiel-Excel-Datei](5115211.xlsx) dort platzieren und den bereitgestellten Beispielcode ausführen. Es wird dann ein Unterordner namens OtherSheets in Ihrem Verzeichnis erstellt und die HTMLs der zweiten und dritten Arbeitsblätter darin exportiert. Ändern Sie bitte die dirPath-Variable im bereitgestellten Code und verweisen Sie vor der Ausführung darauf, das Verzeichnis Ihrer Wahl anzugeben.

{{% alert color="primary" %}} 

Der Beispielcode funktioniert nur, wenn Sie die Aspose.Cells-Lizenz setzen. Wenn Sie den Code ohne Lizenzierung ausführen, wird er in eine Endlosschleife geraten. Daher haben wir eine Überprüfung hinzugefügt, um eine Meldung auszugeben und die Ausführung zu stoppen, wenn die Lizenz nicht gesetzt ist. Sie können entweder eine Lizenz erwerben oder beim Aspose.Purchase-Team eine 30-tägige temporäre Lizenz anfordern.

{{% /alert %}} 

Bitte beachten Sie, dass das Kommentieren dieser Zeilen im Code die Links in Sheet1.html unterbrechen wird und Sheet2.html oder Sheet3.html nicht geöffnet werden, wenn ihre Links in der Sheet1.html angeklickt werden.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-hyperlinks.cs" >}}



Hier ist der vollständige Beispielcode, der mit der bereitgestellten [Beispiel-Excel-Datei](5115211.xlsx) ausgeführt werden kann.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-ExportedWorkSheetViaIFilePathProvider.cs" >}}
