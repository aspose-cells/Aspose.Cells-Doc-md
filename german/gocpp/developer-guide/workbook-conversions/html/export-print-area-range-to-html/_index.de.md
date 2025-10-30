---
title: Exportiere Druckbereichsbereich nach HTML mit Golang via C++
linktitle: Exportiere Druckbereichsbereich nach HTML
type: docs
weight: 60
url: /de/go-cpp/export-print-area-range-to/
description: Erfahren Sie, wie Sie den Druckbereichsbereich mit Aspose.Cells for C++ nach HTML exportieren.
---

## **Mögliche Verwendungsszenarien**

Dies ist ein häufiges Szenario, bei dem nur der Druckbereich, also ein ausgewählter Zellbereich, anstelle des gesamten Blatts nach HTML exportiert werden soll. Diese Funktion ist bereits für die PDF-Renderung verfügbar; jetzt können Sie diese Aufgabe auch für HTML ausführen. Zunächst setzen Sie den Druckbereich im Seiten-Setup-Objekt des Arbeitsblatts. Später verwenden Sie das [**HtmlSaveOptions.GetExportPrintAreaOnly()**](https://reference.aspose.com/cells/go-cpp/htmlsaveoptions/getexportprintareaonly/)-Flag, um nur den ausgewählten Bereich zu exportieren.

## **Beispielcode**

Der folgende Beispielcode lädt eine Arbeitsmappe und exportiert dann den Druckbereich nach HTML. Die Testdatei für diese Funktion kann von folgendem Link heruntergeladen werden:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExportPrintAreaRangeToHtml.go" >}}
