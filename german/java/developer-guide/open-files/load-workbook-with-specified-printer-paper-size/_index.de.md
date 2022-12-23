---
title: Laden Sie die Arbeitsmappe mit dem angegebenen Druckerpapierformat
type: docs
weight: 790
url: /de/java/load-workbook-with-specified-printer-paper-size/
---
{{% alert color="primary" %}} 

 Sie können das Druckerpapierformat Ihrer Wahl angeben, während Sie Ihre Arbeitsmappe mit verwenden[LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)) Methode. Bitte beachten Sie, dass beim Erstellen einer neuen Datei in MS Excel das Papierformat mit der Einstellung des Standarddruckers in Ihrem Gerät übereinstimmt.

{{% /alert %}} 
## **Laden Sie die Arbeitsmappe mit dem angegebenen Druckerpapierformat**
 Der folgende Beispielcode veranschaulicht die Verwendung von[LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\) Methode. Es erstellt zuerst eine Arbeitsmappe und speichert sie dann im Byte-Array-Stream im Format XLSX. Dann lädt es es mit A5-Papierformat und speichert es im Format PDF. Dann lädt er es erneut mit A3-Papierformat und speichert es erneut im Format PDF. Wenn Sie die Ausgabe-PDFs öffnen und ihre Papiergröße überprüfen, werden Sie feststellen, dass sie unterschiedlich sind. Einer ist A5 und der andere ist A3. Bitte laden Sie die herunter[A5-Ausgabe PDF](5473435.pdf) und[A3-Ausgabe PDF](5473436.pdf) generiert durch den Code für Ihre Referenz.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
