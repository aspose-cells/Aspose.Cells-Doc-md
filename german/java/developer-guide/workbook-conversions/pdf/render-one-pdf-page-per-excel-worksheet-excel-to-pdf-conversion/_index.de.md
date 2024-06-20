---
title: Ein PDF Seite pro Excel Arbeitsblatt rendern  Konvertierung von Excel in PDF
type: docs
weight: 40
url: /de/java/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

Bei der Arbeit mit großen Microsoft Excel-Dateien (zum Beispiel einem Arbeitsbuch mit vielen Arbeitsblättern, jedes mit 50 Spalten und 300 oder mehr Zeilen Daten) möchten Sie möglicherweise, dass die PDF-Ausgabe pro Arbeitsblatt eine Seite anzeigt, unabhängig von der Größe des Arbeitsblatts. Dies bedeutet, dass jede Seite wahrscheinlich eine radikal unterschiedliche Seitengröße haben wird. Dies kann mit Hilfe von Aspose.Cells for Java erreicht werden.

{{% /alert %}}

Bitte sehen Sie sich den folgenden Beispielcode an, der eine Excel-Datei mit mehreren Arbeitsblättern in PDF konvertiert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExceltoPDF-ExceltoPDF.java" >}}

{{% alert color="primary" %}}

Wenn die [**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OnePagePerSheet)-Option auf **true** gesetzt ist, wird der gesamte Inhalt des Arbeitsblatts auf einer PDF-Seite gerendert. Die Papiergröße, die mit [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) festgelegt ist, ist ungültig, aber die anderen Einstellungen, die mit [**PageSetup**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) festgelegt wurden, sind weiterhin wirksam.

{{% /alert %}} {{% alert color="primary" %}}

Wenn Ihr Arbeitsblatt Formeln enthält, ist es am besten, die Methode [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) kurz vor dem Rendern des Arbeitsblatts in PDF aufzurufen. Dies stellt sicher, dass die formelabhängigen Werte neu berechnet und die korrekten Werte im PDF dargestellt werden.

{{% /alert %}}
