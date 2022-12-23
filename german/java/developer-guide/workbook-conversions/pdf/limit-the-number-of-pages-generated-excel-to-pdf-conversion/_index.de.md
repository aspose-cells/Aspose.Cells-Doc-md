---
title: Beschränken Sie die Anzahl der generierten Seiten – Excel auf PDF Konvertierung
type: docs
weight: 60
url: /de/java/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

Manchmal möchten Sie eine Reihe von Seiten in eine PDF-Ausgabedatei drucken. Aspose.Cells hat die Möglichkeit, ein Limit festzulegen, wie viele Seiten generiert werden, wenn eine Excel-Tabelle in PDF konvertiert wird.

{{% /alert %}}

## **Begrenzung der Anzahl der generierten Seiten**

Das folgende Beispiel zeigt, wie ein Seitenbereich (3 und 4) in einer Microsoft-Excel-Datei in PDF gerendert wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LimitNumberofPagesGenerated-LimitNumberofPagesGenerated.java" >}}

{{% alert color="primary" %}}

 Wenn die Tabelle Formeln enthält, rufen Sie am besten an[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) kurz vor dem Rendern in das Format PDF. Dadurch wird sichergestellt, dass formelabhängige Werte neu berechnet und die richtigen Werte in der Ausgabedatei gerendert werden.

{{% /alert %}}
