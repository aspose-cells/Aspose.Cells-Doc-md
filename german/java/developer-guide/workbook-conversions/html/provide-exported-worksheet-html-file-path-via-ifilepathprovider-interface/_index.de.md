---
title: Exportierten Arbeitsblatt HTML Dateipfad über das IFilePathProvider Interface bereitstellen
type: docs
weight: 870
url: /de/java/provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface/
---

## **Mögliche Verwendungsszenarien**
Angenommen, Sie haben eine Excel-Datei mit mehreren Blättern und möchten jedes Blatt in eine separate HTML-Datei exportieren. Wenn eines Ihrer Blätter Verknüpfungen zu anderen Blättern enthält, werden diese Verknüpfungen in der exportierten HTML-Datei unterbrochen. Um dieses Problem zu lösen, stellt Aspose.Cells das [IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)-Interface zur Verfügung, das Sie implementieren können, um die unterbrochenen Verknüpfungen zu beheben.
## **Exportierten Arbeitsblatt-HTML-Dateipfad über das IFilePathProvider-Interface bereitstellen**
Bitte laden Sie die [Beispiel-Excel-Datei](5473417.zip) herunter, die im folgenden Code verwendet wird, und ihre exportierten HTML-Dateien. Alle diese Dateien befinden sich im *Temp*-Verzeichnis. Sie sollten es auf dem Laufwerk *C:* extrahieren. Dann wird es zum Verzeichnis *C:\Temp*. Dann öffnen Sie die Datei *Sheet1.html* im Browser und klicken Sie auf die beiden Links darin. Diese Links verweisen auf die beiden exportierten HTML-Arbeitsblätter, die sich im Verzeichnis *C:\Temp\OtherSheets* befinden.

{{< highlight java >}}

 file:///C:/Temp/OtherSheets/Sheet2.html#RANGE!A1

file:///C:/Temp/OtherSheets/Sheet3.html#RANGE!A1

{{< /highlight >}}

Der folgende Screenshot zeigt, wie die *C:\Temp\Sheet1.html* und ihre Links aussehen.

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_1.png)

Der folgende Screenshot zeigt den HTML-Quellcode. Wie Sie sehen können, verweisen die Links nun auf das Verzeichnis *C:\Temp\OtherSheets*. Dies wurde mithilfe der [IFilePathProvider](https://reference.aspose.com/cells/java/com.aspose.cells/IFilePathProvider)-Schnittstelle erreicht.

![todo:image_alt_text](provide-exported-worksheet-html-file-path-via-ifilepathprovider-interface_2.png)
## **Beispielcode**
Bitte beachten Sie, dass das Verzeichnis *C:\Temp* nur zu Illustrationszwecken dient. Sie können jedes beliebige Verzeichnis Ihrer Wahl verwenden und [Beispiel-Excel-Datei](5473414.xlsx) dorthin platzieren und den bereitgestellten Beispielcode ausführen. Es wird dann ein *OtherSheets*-Unterverzeichnis in Ihrem Verzeichnis erstellen und HTMLs der zweiten und dritten Arbeitsblätter darin exportieren. Ändern Sie bitte die *dirPath*-Variable im bereitgestellten Code und verweisen Sie sie vor der Ausführung auf das Verzeichnis Ihrer Wahl.

{{% alert color="primary" %}} 

Der Beispielcode funktioniert nur, wenn Sie die Aspose.Cells-Lizenz setzen. Wenn Sie den Code ohne Lizenzierung ausführen, wird er in eine Endlosschleife geraten. Daher haben wir eine Überprüfung hinzugefügt, um eine Meldung auszugeben und die Ausführung zu stoppen, wenn die Lizenz nicht gesetzt ist. Sie können entweder eine Lizenz erwerben oder beim Aspose.Purchase-Team eine 30-tägige temporäre Lizenz anfordern.

{{% /alert %}} 

Bitte beachten Sie, dass das Kommentieren dieser Zeilen im Code die Links in *Sheet1.html* unterbrechen wird und *Sheet2.html* oder *Sheet3.html* nicht geöffnet werden, wenn ihre Links innerhalb von *Sheet1.html* angeklickt werden.



{{< highlight java >}}

 //If you will comment this line, then hyperlinks will be broken

options.setFilePathProvider(new FilePathProvider());

{{< /highlight >}}



Hier ist der vollständige Beispielcode, den Sie mit der bereitgestellten [Beispiel-Excel-Datei](5473414.xlsx) ausführen können.



{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-files-handling-OpeningFilesThroughPath-1.java" >}}

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-FilePathProvider-FilePathProvider.java" >}}
{{< app/cells/assistant language="java" >}}
