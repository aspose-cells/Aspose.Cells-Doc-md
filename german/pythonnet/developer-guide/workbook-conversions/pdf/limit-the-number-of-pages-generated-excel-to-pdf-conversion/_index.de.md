---
title: Begrenzen Sie die Anzahl der generierten Seiten – Excel auf PDF Konvertierung
type: docs
weight: 180
url: /de/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/
description: Erfahren Sie, wie Sie die Anzahl der beim Rendern von Excel generierten Seiten auf PDF mit Aspose.Cells for Python via .NET API begrenzen.
keywords: Python Limit the Number of Pages Generated while Rendering Excel to PDF, Limit the Number of Pages Generated while saving Excel to PDF using Python, Python Set the Number of Pages Generated while converting Excel to PDF, Control the Number of Pages Generated for Excel to PDF in python
---
{{% alert color="primary" %}}

Manchmal möchten Sie einen Seitenbereich in einer Ausgabedatei PDF drucken. Aspose.Cells for Python via .NET bietet die Möglichkeit, eine Grenze für die Anzahl der generierten Seiten festzulegen, wenn eine Excel-Tabelle in das Dateiformat PDF konvertiert wird.

{{% /alert %}}

##  **Begrenzung der Anzahl der generierten Seiten**

Das folgende Beispiel zeigt, wie ein Seitenbereich (3 und 4) in einer Excel-Datei Microsoft in PDF gerendert wird.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-LimitNumberOfPagesGenerated-1.py" >}}

{{% alert color="primary" %}}

 Wenn die Tabelle Formeln enthält, rufen Sie am besten an[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#) Methode direkt vor dem Rendern in PDF. Dadurch wird sichergestellt, dass formelabhängige Werte neu berechnet werden und die richtigen Werte in der Ausgabedatei gerendert werden.

{{% /alert %}}
