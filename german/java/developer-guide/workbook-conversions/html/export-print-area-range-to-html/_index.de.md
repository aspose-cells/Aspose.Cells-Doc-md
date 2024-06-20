---
title: Bereich des Druckbereichs in HTML exportieren
type: docs
weight: 60
url: /de/java/export-print-area-range-to-html/
---

## Mögliche Anwendungsszenarien

Dies ist ein sehr häufiges Szenario, bei dem wir nur den Druckbereich, d.h. einen ausgewählten Zellenbereich anstelle des gesamten Blatts, in HTML exportieren müssen. Diese Funktion ist bereits für die PDF-Erstellung verfügbar, jedoch können Sie nun diese Aufgabe auch für HTML ausführen. Legen Sie zunächst den Druckbereich im Seitenlayoutobjekt des Arbeitsblatts fest. Verwenden Sie später die [**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportPrintAreaOnly) Eigenschaft, um nur den ausgewählten Bereich zu exportieren.

## Java-Code zum Exportieren des Druckbereichs in HTML

Nachfolgender Beispielscode lädt eine Arbeitsmappe und exportiert dann den Druckbereich in das HTML. Die Beispieldatei zur Prüfung dieser Funktion kann von folgendem Link heruntergeladen werden:

[sampleInlineCharts.xlsx](79527960.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

