---
title: Arbeitsbuch mit spezifischer Druckerpapiergröße laden
type: docs
weight: 790
url: /de/java/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}} 

Sie können die Druckerpapiergröße Ihrer Wahl beim Laden Ihrer Arbeitsmappe mithilfe der Methode [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)) festlegen. Bitte beachten Sie, dass Sie beim Erstellen einer neuen Datei in MS Excel feststellen werden, dass die Papiergröße dieselbe ist wie die Einstellung des Standarddruckers auf Ihrem Computer.

{{% /alert %}} 
## **Arbeitsmappe mit angegebener Druckerpapiergröße laden**
Der folgende Beispielcode veranschaulicht die Verwendung der Methode [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)). Es erstellt zunächst eine Arbeitsmappe, speichert sie dann in einem Byte-Array-Stream im XLSX-Format. Dann lädt es sie mit A5-Papiergröße und speichert sie im PDF-Format. Dann lädt es sie erneut mit A3-Papiergröße und speichert sie erneut im PDF-Format. Wenn Sie die Ausgabe-PDFs öffnen und deren Papiergröße überprüfen, werden Sie feststellen, dass sie unterschiedlich sind. Eine ist A5 und die andere ist A3. Bitte laden Sie die [A5-Ausgabe-PDFs](5473435.pdf) und [A3-Ausgabe-PDFs](5473436.pdf) herunter, die vom Code generiert wurden, um sich zu informieren.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
