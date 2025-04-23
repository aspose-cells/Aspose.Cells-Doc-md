---
title: Ein PDF Seite pro Excel Arbeitsblatt rendern  Konvertierung von Excel in PDF
type: docs
weight: 100
url: /de/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
---

{{% alert color="primary" %}} 

Wenn Sie mit großen Microsoft Excel-Dateien arbeiten (z. B. mit einer Arbeitsmappe, die viele Blätter mit jeweils 50 Spalten und 300 oder mehr Zeilen Daten enthält), möchten Sie möglicherweise, dass die PDF-Ausgabe pro Arbeitsblatt eine Seite anzeigt, unabhängig von der Größe des Arbeitsblatts. Dies bedeutet, dass jede Seite wahrscheinlich eine radikal unterschiedliche Seitengröße hat. Dies kann mit Aspose.Cells for .NET erreicht werden.

{{% /alert %}} 

Bitte sehen Sie sich den folgenden Beispielcode an, der eine Excel-Datei mit mehreren Arbeitsblättern in PDF konvertiert.



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-RenderOnePdfPagePerExcelWorksheet-1.cs" >}}

{{% alert color="primary" %}} 

Wenn die [OnePagePerSheet](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/onepagepersheet) Option auf **true** gesetzt ist, wird der gesamte Blattinhalt auf eine PDF-Seite gerendert.

{{% /alert %}} {{% alert color="primary" %}} 

Wenn Ihre Arbeitsmappe Formeln enthält, ist es am besten, [Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) kurz vor dem Rendern der Arbeitsmappe in PDF aufzurufen. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet werden und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
