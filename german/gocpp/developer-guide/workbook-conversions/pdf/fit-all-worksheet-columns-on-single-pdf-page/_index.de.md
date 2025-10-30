---
title: Alle Spalten des Arbeitsblatts auf eine einzige PDF Seite anpassen mit Golang via C++
linktitle: Alle Arbeitsblattsäulen auf eine einzelne PDF Seite passen
type: docs
weight: 160
url: /de/go-cpp/fit-all-worksheet-columns-on-single-pdf-page/
description: Erstellen Sie eine PDF, die alle Spalten eines Arbeitsblatts auf eine Seite passt, mit Aspose.Cells unter Golang via C++.
---

{{% alert color="primary" %}}

Manchmal möchten Sie eine PDF-Datei erstellen, die alle Spalten eines Arbeitsblatts auf eine Seite passt. Die Eigenschaft [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) bietet diese Funktion sehr einfach. Komplexe Berechnungen wie die Höhe und Breite des Ausgabepdfs werden intern gehandhabt und basieren auf den Daten im Arbeitsblatt.

{{% /alert %}}

## **Arbeitsblattsäulen auf eine einzelne PDF-Seite anpassen**

[**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) stellt sicher, dass alle Spalten eines Arbeitsblatts auf eine einzelne PDF-Seite gerendert werden, obwohl die Zeilen je nach Daten im Arbeitsblatt auf mehrere Seiten erweitert werden können.

Das folgende Beispiel zeigt, wie die Eigenschaft [**PdfSaveOptions.PaginatedSaveOptions(PaginatedSaveOptions_Impl* impl)**](https://reference.aspose.com/cells/go-cpp/paginatedsaveoptions/~paginatedsaveoptions/) verwendet wird, um ein großes Arbeitsblatt mit 100 Spalten zu rendern.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FitAllWorksheetColumnsOnSinglePdfPage.go" >}}
{{% alert color="primary" %}}

Wenn ein bestimmtes Arbeitsblatt viele Spalten hat, kann die gerenderte PDF-Datei den Inhalt in sehr kleiner Größe anzeigen. Es ist immer noch lesbar, wenn es in einer Anzeige-Anwendung wie Acrobat Reader skaliert wird.

{{% /alert %}} {{% alert color="primary" %}}

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/go-cpp/workbook/calculateformula/) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Auf diese Weise wird sichergestellt, dass die von Formeln abhängigen Werte neu berechnet und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
