---
title: Begrenzen Sie die Anzahl der generierten Seiten – Konvertierung von Excel in PDF
type: docs
weight: 60
url: /de/java/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

Manchmal möchten Sie eine Reihe von Seiten in eine PDF-Ausgabedatei drucken. Aspose.Cells hat die Möglichkeit, ein Limit festzulegen, wie viele Seiten beim Konvertieren einer Excel-Tabelle in PDF generiert werden.

{{% /alert %}}

## **Begrenzung der Anzahl der generierten Seiten**

Das folgende Beispiel zeigt, wie eine Reihe von Seiten (3 und 4) in einer Microsoft Excel-Datei in PDF gerendert wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LimitNumberofPagesGenerated-LimitNumberofPagesGenerated.java" >}}

{{% alert color="primary" %}}

 Wenn die Tabelle Formeln enthält, rufen Sie am besten an[**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula()) kurz vor dem Rendern in das PDF-Format. Dadurch wird sichergestellt, dass formelabhängige Werte neu berechnet und die richtigen Werte in der Ausgabedatei gerendert werden.

{{% /alert %}}
