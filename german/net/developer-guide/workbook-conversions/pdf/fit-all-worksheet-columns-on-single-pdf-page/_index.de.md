---
title: Alle Arbeitsblattspalten auf einer einzigen PDF-Seite einpassen
type: docs
weight: 160
url: /de/net/fit-all-worksheet-columns-on-single-pdf-page/
---
{{% alert color="primary" %}}

Manchmal möchten Sie eine PDF-Datei generieren, die alle Spalten eines Arbeitsblatts auf eine Seite passt. Das[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet) property bietet diese Funktion auf sehr benutzerfreundliche Weise. Komplexe Berechnungen wie Höhe und Breite der Ausgabe-PDF werden intern verarbeitet und basieren auf den Daten im Arbeitsblatt.

{{% /alert %}}

## **Arbeitsblattspalten auf einzelne PDF-Seite einpassen**

[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)stellt sicher, dass alle Spalten in einem Arbeitsblatt auf einer einzigen PDF-Seite gerendert werden, obwohl Zeilen je nach Daten im Arbeitsblatt auf mehrere Seiten erweitert werden können.

Der Beispielcode unten zeigt die Verwendung[**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/allcolumnsinonepagepersheet)-Eigenschaft, um ein großes Arbeitsblatt mit 100 Spalten zu rendern.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FitAllWorksheetColumns-1.cs" >}}

{{% alert color="primary" %}}

Wenn ein bestimmtes Arbeitsblatt viele Spalten hat, zeigt die gerenderte PDF-Datei den Inhalt möglicherweise in einer sehr kleinen Größe an. Es ist immer noch lesbar, wenn es in einer Anzeigeanwendung wie Acrobat Reader vergrößert wird.

{{% /alert %}} {{% alert color="primary" %}}

 Wenn Ihre Tabellenkalkulation Formeln enthält, rufen Sie am besten an[**Workbook.CalculateFormula()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula) unmittelbar vor dem Rendern der Tabelle in das PDF-Format. Dadurch wird sichergestellt, dass die formelabhängigen Werte neu berechnet und die richtigen Werte im PDF wiedergegeben werden.

{{% /alert %}}
