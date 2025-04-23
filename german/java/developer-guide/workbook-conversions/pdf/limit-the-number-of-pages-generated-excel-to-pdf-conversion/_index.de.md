---
title: Begrenzen der Anzahl der generierten Seiten  Umsetzung von Excel in PDF
type: docs
weight: 60
url: /de/java/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

Manchmal möchten Sie einen Bereich von Seiten in eine Ausgabedatei im PDF-Format drucken. Aspose.Cells bietet die Möglichkeit, eine Begrenzung festzulegen, wie viele Seiten generiert werden, wenn ein Excel-Arbeitsblatt in PDF konvertiert wird.

{{% /alert %}}

## **Begrenzen der Anzahl der generierten Seiten**

Das folgende Beispiel zeigt, wie ein Bereich von Seiten (3 und 4) in einer Microsoft Excel-Datei in PDF umgesetzt wird.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LimitNumberofPagesGenerated-LimitNumberofPagesGenerated.java" >}}

{{% alert color="primary" %}}

Enthält das Arbeitsblatt Formeln, ist es am besten, [**Workbook.calculateFormula**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula--) kurz vor der Umwandlung in das PDF-Format aufzurufen. Dadurch werden formelabhängige Werte neu berechnet und die korrekten Werte in der Ausgabedatei gerendert.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
