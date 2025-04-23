---
title: Alle Arbeitsblattsäulen auf eine einzelne PDF Seite passen
type: docs
weight: 160
url: /de/net/fit-all-worksheet-columns-on-single-pdf-page/
---

{{% alert color="primary" %}}

Manchmal möchten Sie eine PDF-Datei generieren, die alle Spalten eines Arbeitsblatts auf einer Seite passt. Die [**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)-Eigenschaft bietet diese Funktion auf sehr benutzerfreundliche Weise. Komplexe Berechnungen wie die Höhe und Breite der Ausgabe-PDF werden intern behandelt und basieren auf den Daten im Arbeitsblatt.

{{% /alert %}}

## **Arbeitsblattsäulen auf eine einzelne PDF-Seite anpassen**

[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) stellt sicher, dass alle Spalten in einem Arbeitsblatt auf eine einzige PDF-Seite gerendert werden, obwohl Zeilen je nach Daten im Arbeitsblatt auf mehrere Seiten erweitert werden können.

Der folgende Beispielcode zeigt, wie die [**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)-Eigenschaft verwendet wird, um ein großes Arbeitsblatt mit 100 Spalten zu rendern.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FitAllWorksheetColumns-1.cs" >}}

{{% alert color="primary" %}}

Wenn ein bestimmtes Arbeitsblatt viele Spalten hat, kann die gerenderte PDF-Datei den Inhalt in sehr kleiner Größe anzeigen. Es ist immer noch lesbar, wenn es in einer Anzeige-Anwendung wie Acrobat Reader skaliert wird.

{{% /alert %}} {{% alert color="primary" %}}

Wenn Ihre Tabelle Formeln enthält, ist es am besten, [**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) kurz vor dem Rendern der Tabelle im PDF-Format aufzurufen. Auf diese Weise wird sichergestellt, dass die von Formeln abhängigen Werte neu berechnet und die richtigen Werte im PDF gerendert werden.

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
