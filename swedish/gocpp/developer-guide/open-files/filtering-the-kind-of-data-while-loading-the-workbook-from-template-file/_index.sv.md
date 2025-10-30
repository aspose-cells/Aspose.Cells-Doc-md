---
title: Filtrering av den typ av data när du laddar arbetsboken från mallfil med Golang via C++
linktitle: Filtrera data vid laddning av arbetsbok
type: docs
weight: 400
url: /sv/go-cpp/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
description: Lär dig hur du filtrerar specifika datatyper vid inläsning av en arbetsbok från en mallfil med Aspose.Cells och Golang via C++.
---

{{% alert color="primary" %}}

Ibland vill du specificera vilken typ av data som ska laddas när du konstruerar arbetsboken från mallfilen. Filtrering av inläst data kan förbättra prestanda för ditt speciella syfte, särskilt när du använder [LightCells API:er](/cells/sv/cpp/using-lightcells-api/). Använd egenskapen [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) för detta ändamål.

{{% /alert %}}

Följande exempelkod laddar endast formobjekt när arbetsboken laddas från [mallfilen](5115552.xlsx) som du kan ladda ned från länken. Följande skärmbild visar innehållet i [mallfilen](5115552.xlsx) och förklarar också att datan i rött och med gul bakgrund inte kommer att laddas eftersom egenskapen [**LoadOptions.GetLoadFilter()**](https://reference.aspose.com/cells/go-cpp/loadoptions/getloadfilter/) har ställts in till [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/cpp/aspose.cells/loaddatafilteroptions/)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Följande skärmbild visar [utdata PDF](5115555.pdf) som du kan ladda ned från länken. Här kan du se att datan i rött och gul bakgrund inte finns men alla former är där.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-FilteringTheKindOfDataWhileLoadingTheWorkbookFromTemplateFile.go" >}}
