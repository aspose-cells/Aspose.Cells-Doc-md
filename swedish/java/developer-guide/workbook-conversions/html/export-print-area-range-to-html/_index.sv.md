---
title: Exportera utskriftsområde till HTML
type: docs
weight: 60
url: /sv/java/export-print-area-range-to-html/
---

## Möjliga användningsfall

Detta är ett mycket vanligt scenario att vi behöver exportera endast utskriftsområde dvs. valt cellområde istället för hela bladet till HTML. Denna funktion är redan tillgänglig för PDF-rendering, men nu kan du utföra denna uppgift också för HTML. Först ställ in utskriftsområdet i sidlayoutobjektet för arbetsbladet. Använd sedan [**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ExportPrintAreaOnly) egenskapen för att exportera endast valt område.

## Java-kod för att exportera utskriftsområde till HTML

Följande provkod laddar en arbetsbok och exporterar sedan utskriftsområdet till HTML. Filen för att testa denna funktion kan laddas ner från följande länk:

[sampleInlineCharts.xlsx](79527960.xlsx)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HTML-ExportPrintAreaToHtml-1.java" >}}

{{< app/cells/assistant language="java" >}}
