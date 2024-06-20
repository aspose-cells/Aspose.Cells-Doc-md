---
title: Begrenzen der Anzahl der generierten Seiten  Umsetzung von Excel in PDF
type: docs
weight: 180
url: /de/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---

{{% alert color="primary" %}}

Manchmal möchten Sie einen Bereich von Seiten in eine Ausgabe-PDF-Datei drucken. Aspose.Cells hat die Möglichkeit, eine Begrenzung festzulegen, wie viele Seiten generiert werden, wenn eine Excel-Tabelle in die PDF-Dateiformat umgesetzt wird.

{{% /alert %}}

## **Begrenzen der Anzahl der generierten Seiten**

Das folgende Beispiel zeigt, wie ein Bereich von Seiten (3 und 4) in einer Microsoft Excel-Datei in PDF umgesetzt wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LimitNumberOfPagesGenerated-1.cs" >}}

{{% alert color="primary" %}}

Wenn in der Tabelle Formeln enthalten sind, ist es am besten, [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) kurz vor der Umsetzung in PDF aufzurufen. Dadurch werden formelabhängige Werte neu berechnet und die korrekten Werte in der Ausgabedatei dargestellt.

{{% /alert %}}
