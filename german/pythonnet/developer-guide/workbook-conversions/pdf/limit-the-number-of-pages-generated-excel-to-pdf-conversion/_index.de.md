---
title: Begrenzen der Anzahl der generierten Seiten  Umsetzung von Excel in PDF
type: docs
weight: 180
url: /de/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Erfahren Sie, wie Sie die Anzahl der generierten Seiten beim Rendering von Excel zu PDF mit Aspose.Cells für Python via .NET API begrenzen können.
keywords: Python Begrenzen Sie die Anzahl der generierten Seiten beim Rendering von Excel zu PDF, Begrenzen Sie die Anzahl der generierten Seiten beim Speichern von Excel zu PDF mit Python, Legen Sie die Anzahl der generierten Seiten beim Konvertieren von Excel zu PDF fest, Kontrollieren Sie die Anzahl der generierten Seiten für Excel zu PDF in Python
---

{{% alert color="primary" %}}

Manchmal möchten Sie einen Bereich von Seiten in eine Ausgabe-PDF-Datei drucken. Aspose.Cells for Python via .NET hat die Möglichkeit, die Anzahl der generierten Seiten beim Konvertieren einer Excel-Tabelle in das PDF-Dateiformat zu begrenzen.

{{% /alert %}}

## **Begrenzen der Anzahl der generierten Seiten**

Das folgende Beispiel zeigt, wie ein Bereich von Seiten (3 und 4) in einer Microsoft Excel-Datei in PDF umgesetzt wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-LimitNumberOfPagesGenerated-1.py" >}}

{{% alert color="primary" %}}

Wenn die Tabelle Formeln enthält, ist es am besten, die Methode [Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) unmittelbar vor dem Rendern in PDF aufzurufen. Dadurch werden formelabhängige Werte neu berechnet und die korrekten Werte in der Ausgabedatei gerendert.

{{% /alert %}}
