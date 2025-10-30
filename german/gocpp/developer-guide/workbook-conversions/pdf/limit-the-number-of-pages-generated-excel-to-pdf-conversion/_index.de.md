---
title: Beschränkung der Erzeugten Seitenzahl  Excel in PDF Konvertierung mit Golang via C++
linktitle: Begrenzung der generierten Seitenzahl
type: docs
weight: 180
url: /de/go-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Lernen Sie, wie Sie die Anzahl der erzeugten Seiten beim Konvertieren von Excel in PDF mit Aspose.Cells in Golang via C++ begrenzen.
---

{{% alert color="primary" %}}

Manchmal möchten Sie einen Bereich von Seiten in eine Ausgabe-PDF-Datei drucken. Aspose.Cells hat die Möglichkeit, eine Begrenzung festzulegen, wie viele Seiten generiert werden, wenn eine Excel-Tabelle in die PDF-Dateiformat umgesetzt wird.

{{% /alert %}}

## **Begrenzen der Anzahl der generierten Seiten**

Das folgende Beispiel zeigt, wie ein Bereich von Seiten (3 und 4) in einer Microsoft Excel-Datei in PDF umgesetzt wird.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LimitTheNumberOfPagesGeneratedExcelToPdfConversion.go" >}}
{{% alert color="primary" %}}

Wenn in der Tabelle Formeln enthalten sind, ist es am besten, [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) kurz vor der Umsetzung in PDF aufzurufen. Dadurch werden formelabhängige Werte neu berechnet und die korrekten Werte in der Ausgabedatei dargestellt.

{{% /alert %}}
