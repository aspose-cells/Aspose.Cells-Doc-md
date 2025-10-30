---
title: Eine PDF Seite pro Excel Arbeitsblatt rendern  Excel in PDF Konvertierung mit Golang via C++
type: docs
weight: 100
url: /de/go-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/
description: Excel Arbeitsblätter in PDF mit einer Seite pro Arbeitsblatt umwandeln, mit Aspose.Cells in Golang via C++.
---

{{% alert color="primary" %}} 

Beim Arbeiten mit großen Microsoft-Excel-Dateien (zum Beispiel Arbeitsmappen mit vielen Blättern, jeweils mit 50 Spalten und 300 oder mehr Zeilen Daten) möchten Sie möglicherweise, dass die PDF-Ausgabe auf einer Seite pro Arbeitsblatt angezeigt wird, unabhängig von der Größe des Arbeitsblatts. Dies bedeutet, dass jede Seite wahrscheinlich eine radikal unterschiedliche Seitengröße haben wird. Dies kann durch Verwendung von Aspose.Cells for C++ erreicht werden.

{{% /alert %}} 

Bitte sehen Sie sich den folgenden Beispielcode an, der eine Excel-Datei mit mehreren Arbeitsblättern in PDF konvertiert.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-RenderOnePdfPagePerExcelWorksheetExcelToPdfConversion.go" >}}
{{% alert color="primary" %}} 

Wenn die [PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) -Option auf **true** gesetzt ist, wird der gesamte Blattinhalt auf eine PDF-Seite gerendert.

{{% /alert %}} {{% alert color="primary" %}} 

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [Workbook::CalculateFormula()](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) direkt vor dem Rendern der Tabelle in PDF aufzurufen. Dadurch werden die Formelabhängigen Werte neu berechnet und die korrekten Werte im PDF angezeigt.

{{% /alert %}}
