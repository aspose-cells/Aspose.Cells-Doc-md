---
title: Filtrera VBA projekt vid inläsning av en arbetsbok
type: docs
weight: 140
url: /sv/net/filter-vba-project-while-loading-a-workbook/
---

## **Filtrera VBA-projekt vid inläsning av en Excel-arbetsbok i C#**

Vissa .xlsm/.xslb-filer har en extremt stor mängd makron (eller mycket, mycket långa makron). Aspose.Cells kommer ovillkorligen att ladda denna (meta)data när sådana arbetsböcker öppnas. Du kan behöva kontrollera detta via [**LoadDataFilterOptions**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions) när du verkligen bara behöver extrahera kalkylbladsnamn för ett stort antal arbetsböcker och därmed hoppa över sådana onödiga innehåll. Denna filtrering tillhandahålls genom att införa ett nytt alternativ, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions).

## **Exempelkod**

Följande exempelkod laddar en arbetsbok så att endast VBA filtreras. En testfil för att testa denna funktion kan hämtas från följande länk:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterVBAMacrosWhileLoadingWorkbook-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
