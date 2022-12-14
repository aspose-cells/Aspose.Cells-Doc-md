---
title: Rendern Sie eine PDF-Seite pro Excel-Arbeitsblatt - Konvertierung von Excel in PDF
type: docs
weight: 40
url: /de/java/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

Wenn Sie mit großen Microsoft Excel-Dateien arbeiten (z. B. eine Arbeitsmappe mit vielen Blättern mit jeweils 50 Spalten und 300 oder mehr Datenzeilen), möchten Sie möglicherweise, dass die PDF-Ausgabe unabhängig von der Größe des Arbeitsblatts eine Seite pro Arbeitsblatt anzeigt . Dies würde bedeuten, dass jede Seite wahrscheinlich eine radikal andere Seitengröße hat. Dies kann erreicht werden, indem Sie Aspose.Cells for Java verwenden.

{{% /alert %}}

Bitte sehen Sie sich den folgenden Beispielcode an, der eine Excel-Datei mit mehreren Arbeitsblättern in PDF konvertiert.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-ExceltoPDF-ExceltoPDF.java" >}}

{{% alert color="primary" %}}

 Wenn die[**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#OnePagePerSheet) Option eingestellt ist**Stimmt** , wird der gesamte Blattinhalt auf einer PDF-Seite gerendert. Das eingestellte Papierformat[**Seiteneinrichtung**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup) ist ungültig, aber die anderen Einstellungen mit gesetzt[**Seiteneinrichtung**](https://reference.aspose.com/cells/java/com.aspose.cells/PageSetup)noch wirksam.

{{% /alert %}} {{% alert color="primary" %}}

Wenn Ihre Tabellenkalkulation Formeln enthält, rufen Sie am besten die auf[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula())-Methode direkt vor dem Rendern der Tabelle in PDF. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet und die korrekten Werte im PDF wiedergegeben werden.

{{% /alert %}}
