---
title: Geben Sie den Dateipfad des exportierten Arbeitsblatts HTML über die IFilePathProvider-Schnittstelle an
type: docs
weight: 870
url: /de/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---
## **Mögliche Nutzungsszenarien**
 Angenommen, Sie haben eine Excel-Datei mit mehreren Blättern und möchten jedes Blatt in eine einzelne HTML-Datei exportieren. Wenn eines Ihrer Blätter Links zu anderen Blättern enthält, werden diese Links im exportierten HTML unterbrochen. Um dieses Problem zu lösen, bietet Aspose.Cells[IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)Schnittstelle, die Sie implementieren können, um die defekten Links zu reparieren.
## **Geben Sie den Dateipfad des exportierten Arbeitsblatts HTML über die IFilePathProvider-Schnittstelle an**
 Bitte laden Sie die herunter[Excel-Beispieldatei](5473417.zip) wird im folgenden Code und seinen exportierten HTML-Dateien verwendet. Alle diese Dateien befinden sich in der*Temp* Verzeichnis. Sie sollten es extrahieren*C:* Fahrt. Dann wird es*C:\Temp* Verzeichnis. Dann öffnen Sie die*Blatt1.html* Datei im Browser und klicken Sie auf die beiden darin enthaltenen Links. Diese Links verweisen auf diese beiden exportierten HTML-Arbeitsblätter, die sich in der*C:\Temp\OtherSheets*Verzeichnis.

{{< highlight "java" >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

Der folgende Screenshot zeigt, wie die*C:\Temp\Tabelle1.html*und seine Links aussehen

![todo: Bild_alt_Text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

 Der folgende Screenshot zeigt die Quelle HTML. Wie Sie sehen können, beziehen sich die Links jetzt darauf*C:\Temp\OtherSheets* Verzeichnis. Dies wurde mit Hilfe von erreicht[IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)Schnittstelle.

![todo: Bild_alt_Text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Beispielcode**
 bitte beachten Sie*C:\Temp* Verzeichnis dient nur der Veranschaulichung. Sie können ein beliebiges Verzeichnis Ihrer Wahl und Ihres Ortes verwenden[Excel-Beispieldatei](5473414.xlsx) darin und führen Sie den bereitgestellten Beispielcode aus. Es wird dann erstellt*AndereBlätter* Unterverzeichnis in Ihrem Verzeichnis und exportieren Sie das zweite und dritte Arbeitsblatt HTML darin. Bitte ändern Sie die*dirPfad*-Variable innerhalb des bereitgestellten Codes und verweisen Sie sie vor der Ausführung auf das Verzeichnis Ihrer Wahl.

{{% alert color="primary" %}} 

Der Beispielcode funktioniert nur, wenn Sie die Lizenz Aspose.Cells festlegen. Wenn Sie versuchen, den Code auszuführen, ohne die Lizenz festzulegen, wird er in eine Endlosschleife versetzt. Daher haben wir ein Häkchen hinzugefügt, um eine Nachricht zu drucken und die Ausführung zu stoppen, wenn die Lizenz nicht festgelegt ist. Sie können entweder eine Lizenz erwerben oder eine temporäre 30-Tage-Lizenz beim Team Aspose.Purchase anfordern.

{{% /alert %}} 

 Bitte beachten Sie, dass das Kommentieren dieser Zeilen im Code die Links unterbricht*Blatt1.html* und*Sheet2.html* oder*Sheet3.html*öffnet sich nicht, wenn auf ihre Links geklickt wird*Blatt1.html*



{{< highlight "java" >}}

 //If you will comment this line, then hyperlinks will be broken

options.setFilePathProvider(new FilePathProvider());

{{< /highlight >}}



 Hier ist der vollständige Beispielcode, den Sie mit dem bereitgestellten ausführen können[Excel-Beispieldatei](5473414.xlsx).



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-handling-OpeningFilesThroughPath-1.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilePathProvider-FilePathProvider.java" >}}
