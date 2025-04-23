---
title: Arbeitsbuch mit spezifischer Druckerpapiergröße laden
type: docs
weight: 790
url: /de/java/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}} 

Sie können die Papiergröße Ihres Druckers beim Laden Ihrer Arbeitsmappe mit der [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize-int-) Methode festlegen. Bitte beachten Sie, dass, wenn Sie eine neue Datei in MS Excel erstellen, die Papiergröße der Standardeinstellung Ihres Druckers entspricht.

{{% /alert %}} 
## **Arbeitsmappe mit angegebener Druckerpapiergröße laden**
Der folgende Beispielcode zeigt die Verwendung der [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize-int-) Methode. Er erstellt zunächst eine Arbeitsmappe, speichert sie in einem Byte-Array-Stream im XLSX-Format, lädt sie mit A5-Papiergröße und speichert sie im PDF-Format. Dann lädt er sie erneut mit A3-Papiergröße und speichert sie wieder im PDF-Format. Wenn Sie die Ausgabedateien im PDF-Format öffnen und deren Papiergröße prüfen, werden Sie sehen, dass sie unterschiedlich sind. Ein PDF ist A5 und das andere A3. Laden Sie die [A5-Ausgabe-PDF](5473435.pdf) und das [A3-Ausgabe-PDF](5473436.pdf), die durch den Code erzeugt wurden.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
