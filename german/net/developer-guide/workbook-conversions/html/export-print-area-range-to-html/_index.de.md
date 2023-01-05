---
title: Exportieren Sie den Druckbereichsbereich nach HTML
type: docs
weight: 60
url: /de/net/export-print-area-range-to/
---
## **Mögliche Nutzungsszenarien**

 Dies ist ein häufiges Szenario, in dem wir nur den Druckbereich exportieren müssen, dh ausgewählte Zellbereiche, anstatt das gesamte Blatt nach HTML zu exportieren. Diese Funktion ist bereits für das Rendern von PDF verfügbar, jetzt können Sie diese Aufgabe jedoch auch für HTML ausführen. Legen Sie zuerst den Druckbereich im Seiteneinrichtungsobjekt des Arbeitsblatts fest. Später verwenden[**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportprintareaonly) Flag, um nur den ausgewählten Bereich zu exportieren.

## Beispielcode

Der folgende Beispielcode lädt eine Arbeitsmappe und exportiert dann den Druckbereich in HTML. Die Beispieldatei zum Testen dieser Funktion kann über den folgenden Link heruntergeladen werden:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportPrintAreaToHtml-1.cs" >}}
