---
title: Exportera utskriftsområde till HTML
type: docs
weight: 60
url: /sv/java/export-print-area-range-to-html/
---
## Möjliga användningsscenarier

Detta är ett mycket vanligt scenario att vi endast behöver exportera utskriftsområdet, dvs. valt cellområde istället för hela arket till HTML. Denna funktion är redan tillgänglig för PDF-rendering, men nu kan du utföra denna uppgift för HTML också. Ställ först in utskriftsområdet i sidinställningarna i kalkylbladet. Senare användning[**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportPrintAreaOnly)egenskap för att endast exportera valt intervall.

## Java-kod för att exportera utskriftsområdesintervall till HTML

Följande exempelkod läser in en arbetsbok och exporterar sedan utskriftsområdet till HTML. Exempelfilen för att testa den här funktionen kan laddas ner från följande länk:

[sampleInlineCharts.xlsx](79527960.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

