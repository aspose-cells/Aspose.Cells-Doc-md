---
title: Stellen Sie den HTML-Dateipfad des exportierten Arbeitsblatts über die IFilePathProvider-Schnittstelle bereit
type: docs
weight: 70
url: /de/net/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---
## **Mögliche Nutzungsszenarien**
 Angenommen, Sie haben eine Excel-Datei mit mehreren Blättern und möchten jedes Blatt in eine einzelne HTML-Datei exportieren. Wenn eines Ihrer Blätter Links zu anderen Blättern enthält, werden diese Links im exportierten HTML unterbrochen. Um dieses Problem zu lösen, bietet Aspose.Cells[IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)Schnittstelle, die Sie implementieren können, um die defekten Links zu reparieren.
## **Stellen Sie den HTML-Dateipfad des exportierten Arbeitsblatts über die IFilePathProvider-Schnittstelle bereit**
 Bitte laden Sie die herunter[Excel-Beispieldatei](5115213.zip)wird im folgenden Code und den exportierten HTML-Dateien verwendet. Alle diese Dateien befinden sich im Temp-Verzeichnis. Sie sollten es auf Laufwerk C: extrahieren. Dann wird es zum C:\Temp-Verzeichnis. Dann öffnen Sie die Datei Sheet1.html im Browser und klicken auf die beiden darin enthaltenen Links. Diese Links verweisen auf diese beiden exportierten HTML-Arbeitsblätter, die sich im Verzeichnis C:\Temp\OtherSheets befinden.

{{< highlight "java" >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

Der folgende Screenshot zeigt, wie die C:\Temp\Sheet1.html und ihre Links aussehen

![todo: Bild_alt_Text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

 Der folgende Screenshot zeigt die HTML-Quelle. Wie Sie sehen können, verweisen die Links jetzt auf das Verzeichnis C:\Temp\OtherSheets. Dies wurde mit Hilfe von erreicht[IFilePathProvider](https://reference.aspose.com/cells/net/aspose.cells/ifilepathprovider)Schnittstelle.

![todo: Bild_alt_Text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Beispielcode**
 Bitte beachten Sie, dass das Verzeichnis C:\Temp nur zu Illustrationszwecken dient. Sie können ein beliebiges Verzeichnis Ihrer Wahl und Ihres Ortes verwenden[Excel-Beispieldatei](5115211.xlsx)darin und führen Sie den bereitgestellten Beispielcode aus. Es erstellt dann das Unterverzeichnis OtherSheets in Ihrem Verzeichnis und exportiert das zweite und dritte HTML-Arbeitsblatt darin. Bitte ändern Sie die dirPath-Variable im bereitgestellten Code und verweisen Sie sie vor der Ausführung auf das Verzeichnis Ihrer Wahl.

{{% alert color="primary" %}} 

Der Beispielcode funktioniert nur, wenn Sie die Lizenz Aspose.Cells festlegen. Wenn Sie versuchen, den Code auszuführen, ohne die Lizenz festzulegen, wird er in eine Endlosschleife versetzt. Daher haben wir ein Häkchen hinzugefügt, um eine Nachricht zu drucken und die Ausführung zu stoppen, wenn die Lizenz nicht festgelegt ist. Sie können entweder eine Lizenz erwerben oder eine temporäre 30-Tage-Lizenz beim Team Aspose.Purchase anfordern.

{{% /alert %}} 

Bitte beachten Sie, dass das Kommentieren dieser Zeilen im Code die Links in Sheet1.html unterbricht und Sheet2.html oder Sheet3.html nicht geöffnet werden, wenn auf ihre Links in Sheet1.html geklickt wird



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-hyperlinks.cs" >}}



 Hier ist der vollständige Beispielcode, den Sie mit dem bereitgestellten ausführen können[Excel-Beispieldatei](5115211.xlsx).



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-WorkingWithHTMLFormat-ExportedWorkSheetViaIFilePathProvider-ExportedWorkSheetViaIFilePathProvider.cs" >}}
