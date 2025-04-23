---
title: Bereich des Druckbereichs in HTML exportieren
type: docs
weight: 60
url: /de/python-net/export-print-area-range-to/
---

## **Mögliche Verwendungsszenarien**

Dies ist ein gängiges Szenario, bei dem wir nur den Druckbereich, d.h. den ausgewählten Zellenbereich, anstelle des gesamten Arbeitsblatts in HTML exportieren müssen. Diese Funktion ist bereits für PDF-Rendering verfügbar, jetzt können Sie diese Aufgabe auch für HTML ausführen. Legen Sie zunächst den Druckbereich im Seitenlayoutobjekt des Arbeitsblatts fest. Verwenden Sie später die [**HtmlSaveOptions.export_print_area_only**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_print_area_only)-Markierung, um nur den ausgewählten Bereich zu exportieren.

## Beispielcode

Der folgende Beispielscode lädt eine Arbeitsmappe und exportiert dann den Druckbereich in das HTML. Die Beispieldatei zum Testen dieser Funktion kann unter folgendem Link heruntergeladen werden:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportPrintAreaToHtml-1.py" >}}
