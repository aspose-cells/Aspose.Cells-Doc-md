---
title: Druckbereichsbereich nach HTML exportieren
type: docs
weight: 60
url: /de/net/export-print-area-range-to/
---
## **Mögliche Nutzungsszenarien**

 Dies ist ein häufiges Szenario, bei dem wir nur den Druckbereich, dh den ausgewählten Zellbereich, anstelle des gesamten Blatts in HTML exportieren müssen. Diese Funktion ist bereits für die PDF-Wiedergabe verfügbar, jetzt können Sie diese Aufgabe jedoch auch für HTML ausführen. Legen Sie zuerst den Druckbereich im Seiteneinrichtungsobjekt des Arbeitsblatts fest. Später verwenden[**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportprintareaonly) Flag, um nur den ausgewählten Bereich zu exportieren.

## Beispielcode

Der folgende Beispielcode lädt eine Arbeitsmappe und exportiert dann den Druckbereich in HTML. Beispieldatei zum Testen dieser Funktion kann unter folgendem Link heruntergeladen werden:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportPrintAreaToHtml-1.cs" >}}
