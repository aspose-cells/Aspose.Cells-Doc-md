---
title: Exportera utskriftsområde till HTML
type: docs
weight: 60
url: /sv/net/export-print-area-range-to/
---
## **Möjliga användningsscenarier**

 Detta är ett vanligt scenario där vi endast behöver exportera utskriftsområdet, dvs valt cellområde istället för hela arket till HTML. Den här funktionen är redan tillgänglig för PDF-rendering, men nu kan du utföra den här uppgiften även för HTML. Ställ först in utskriftsområdet i sidinställningarna i kalkylbladet. Använd senare[**HtmlSaveOptions.ExportPrintAreaOnly**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/exportprintareaonly) flagga för att endast exportera valt område.

## Exempelkod

Följande exempelkod läser in en arbetsbok och exporterar sedan utskriftsområdet till HTML. Exempelfil för att testa den här funktionen kan laddas ner från följande länk:

[sampleInlineCharts.xlsx](79527946.xlsx)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-ExportPrintAreaToHtml-1.cs" >}}
