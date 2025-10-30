---
title: Filtrera VBA projekt vid inläsning av en arbetsbok
type: docs
weight: 140
url: /sv/python-net/filter-vba-project-while-loading-a-workbook/
---

## **Filtrera VBA-projekt vid laddning av en Excel-arbetsbok i Python**

Vissa .xlsm/.xslb-filer har extremt många makron (eller mycket, mycket långa makron). Aspose.Cells för Python via .NET laddar dessa (meta)data obestridligt vid öppning av sådana arbetsböcker. Du kan behöva kontrollera detta via [**LoadDataFilterOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions) när du enbart behöver extrahera bladnamn för många arbetsböcker och därigenom hoppa över onödigt innehåll. Denna filtrering tillhandahålls genom att införa ett nytt alternativ, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/).

## **Exempelkod**

Följande exempelkod laddar en arbetsbok så att endast VBA filtreras. En testfil för att testa denna funktion kan hämtas från följande länk:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "VBAProject-FilterVBAMacrosWhileLoadingWorkbook-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
