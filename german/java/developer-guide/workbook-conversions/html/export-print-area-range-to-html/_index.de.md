---
title: Druckbereichsbereich nach HTML exportieren
type: docs
weight: 60
url: /de/java/export-print-area-range-to-html/
---
## Mögliche Nutzungsszenarien

Dies ist ein sehr häufiges Szenario, bei dem wir nur den Druckbereich, dh den ausgewählten Zellbereich, anstelle des gesamten Blatts in HTML exportieren müssen. Diese Funktion ist bereits für die PDF-Wiedergabe verfügbar, jetzt können Sie diese Aufgabe jedoch auch für HTML ausführen. Legen Sie zunächst den Druckbereich im Seiteneinrichtungsobjekt des Arbeitsblatts fest. Spätere Verwendung[**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportPrintAreaOnly)-Eigenschaft, um nur den ausgewählten Bereich zu exportieren.

## Java-Code zum Exportieren des Druckbereichsbereichs in HTML

Der folgende Beispielcode lädt eine Arbeitsmappe und exportiert dann den Druckbereich in HTML. Die Beispieldatei zum Testen dieser Funktion kann unter folgendem Link heruntergeladen werden:

[sampleInlineCharts.xlsx](79527960.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

