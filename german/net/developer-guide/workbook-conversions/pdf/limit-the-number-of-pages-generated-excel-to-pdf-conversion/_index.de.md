---
title: Begrenzen Sie die Anzahl der generierten Seiten – Konvertierung von Excel in PDF
type: docs
weight: 180
url: /de/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
---
{{% alert color="primary" %}}

Manchmal möchten Sie eine Reihe von Seiten in eine PDF-Ausgabedatei drucken. Aspose.Cells hat die Möglichkeit, die Anzahl der generierten Seiten beim Konvertieren einer Excel-Tabelle in das PDF-Dateiformat zu begrenzen.

{{% /alert %}}

## **Begrenzung der Anzahl der generierten Seiten**

Das folgende Beispiel zeigt, wie eine Reihe von Seiten (3 und 4) in einer Microsoft Excel-Datei in PDF gerendert wird.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LimitNumberOfPagesGenerated-1.cs" >}}

{{% alert color="primary" %}}

 Wenn die Tabelle Formeln enthält, rufen Sie am besten an[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) kurz vor dem Rendern in PDF. Dadurch wird sichergestellt, dass formelabhängige Werte neu berechnet und die richtigen Werte in der Ausgabedatei gerendert werden.

{{% /alert %}}
