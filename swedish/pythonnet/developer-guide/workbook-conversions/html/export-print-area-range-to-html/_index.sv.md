---
title: Exportera utskriftsområde till HTML
type: docs
weight: 60
url: /sv/python-net/export-print-area-range-to/
---

## **Möjliga användningsscenario**

Detta är ett vanligt scenario där vi behöver exportera endast utskriftsområdet, dvs. det valda cellområdet istället för hela bladet till HTML. Denna funktion finns redan tillgänglig för PDF-rendering, men nu kan du utföra denna uppgift för HTML också. Ange först utskriftsområdet i sidinställningsobjektet för arbetsbladet. Använd sedan [**HtmlSaveOptions.export_print_area_only**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/export_print_area_only)-flaggan för att exportera endast det valda området.

## Exempelkod

Följande exempelkod laddar en arbetsbok och exporterar sedan utskriftsområdet till HTML. Exempelfilen för att testa denna funktion kan laddas ned från följande länk:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-ExportPrintAreaToHtml-1.py" >}}
