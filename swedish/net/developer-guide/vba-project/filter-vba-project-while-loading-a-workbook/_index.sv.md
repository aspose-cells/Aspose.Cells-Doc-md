---
title: Filtrera VBA-projekt när en arbetsbok laddas
type: docs
weight: 140
url: /sv/net/filter-vba-project-while-loading-a-workbook/
---
## **Filtrera VBA-projekt när du laddar en Excel-arbetsbok i C#**

Vissa .xlsm/.xslb-filer har en extremt stor mängd makron (eller väldigt, väldigt långa makron). Aspose.Cells kommer ovillkorligen att ladda dessa (meta)data när sådana arbetsböcker öppnas. Du kan dock behöva kontrollera detta[**LoadDataFilterOptions**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) när du egentligen bara behöver extrahera arknamn för ett stort antal arbetsböcker och därmed hoppa över sådant onödigt innehåll. Detta filter tillhandahålls genom att introducera ett nytt alternativ,[**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions).

## **Exempelkod**

Följande exempelkod läser in en arbetsbok så att endast VBA filtreras. En exempelfil för att testa den här funktionen kan laddas ner från följande länk:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterVBAMacrosWhileLoadingWorkbook-1.cs" >}}
