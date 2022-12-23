---
title: Rendern Sie eine PDF-Seite pro Excel-Arbeitsblatt - Konvertierung von Excel in PDF
type: docs
weight: 100
url: /de/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---
{{% alert color="primary" %}} 

Wenn Sie mit großen Microsoft-Excel-Dateien arbeiten (z. B. eine Arbeitsmappe mit vielen Blättern mit jeweils 50 Spalten und 300 oder mehr Datenzeilen), möchten Sie möglicherweise, dass die PDF-Ausgabe unabhängig von der Größe des Arbeitsblatts eine Seite pro Arbeitsblatt anzeigt . Dies würde bedeuten, dass jede Seite wahrscheinlich eine radikal andere Seitengröße hat. Dies kann durch die Verwendung von Aspose.Cells for .NET erreicht werden.

{{% /alert %}} 

Bitte sehen Sie sich den folgenden Beispielcode an, der eine Excel-Datei mit mehreren Arbeitsblättern in PDF konvertiert.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderOnePdfPagePerExcelWorksheet-1.cs" >}}

{{% alert color="primary" %}} 

 Wenn die[Eine Seite pro Blatt](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/onepagepersheet) Option eingestellt ist**wahr**, wird der gesamte Blattinhalt auf einer PDF-Seite gerendert.

{{% /alert %}} {{% alert color="primary" %}} 

Wenn Ihre Tabellenkalkulation Formeln enthält, rufen Sie am besten an[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)kurz vor dem Rendern der Tabelle auf PDF. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet werden und die korrekten Werte in PDF gerendert werden.

{{% /alert %}}
