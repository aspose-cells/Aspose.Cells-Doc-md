---
title: Filtrera VBA projekt vid inläsning av en arbetsbok med Golang via C++
linktitle: Filtrera VBA projekt vid inläsning av en arbetsbok
type: docs
weight: 140
url: /sv/go-cpp/filter-vba-project-while-loading-a-workbook/
description: Lär dig hur man filtrerar VBA projekt vid inläsning av en Excel arbetsbok med Aspose.Cells med Golang via C++.
---

## **Filtrera VBA-projekt vid inläsning av en Excel-arbetsbok i C++**

Vissa .xlsm/.xslb filer har ett extremt stort antal makron (eller mycket, mycket långa makron). Aspose.Cells laddar ostört denna (meta)data när du öppnar sådana arbetsböcker. Du kan dock kontrollera detta med [**LoadDataFilterOptions**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions) när du verkligen behöver enbart extrahera bladnamn för ett stort antal arbetsböcker och därigenom hoppa över sådant onödigt innehåll. Denna filterfunktion introduceras genom ett nytt alternativ, [**LoadDataFilterOptions.VBA**](https://reference.aspose.com/cells/go-cpp/loaddatafilteroptions).

## **Exempelkod**

Följande exempelkod laddar en arbetsbok så att endast VBA filtreras. En testfil för att testa denna funktion kan hämtas från följande länk:

[sampleMacroEnabledWorkbook.xlsm](79527938.xlsm)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilterVbaProjectWhileLoadingAWorkbook.go" >}}
