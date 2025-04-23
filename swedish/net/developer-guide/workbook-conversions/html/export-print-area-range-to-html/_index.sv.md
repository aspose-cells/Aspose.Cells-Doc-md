---
title: Exportera utskriftsområde till HTML
type: docs
weight: 60
url: /sv/net/export-print-area-range-to/
---

## **Möjliga användningsscenario**

Detta är ett vanligt scenario där vi behöver exportera endast utskriftsområdet, dvs. det valda cellområdet istället för hela bladet till HTML. Denna funktion finns redan tillgänglig för PDF-rendering, men nu kan du utföra denna uppgift för HTML också. Ange först utskriftsområdet i sidinställningsobjektet för arbetsbladet. Använd sedan [**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportprintareaonly)-flaggan för att exportera endast det valda området.

## Exempelkod

Följande exempelkod laddar en arbetsbok och exporterar sedan utskriftsområdet till HTML. Exempelfilen för att testa denna funktion kan laddas ned från följande länk:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportPrintAreaToHtml-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
