---
title: Filtrera vilken typ av data som ska laddas från mallfilen när arbetsboken laddas
type: docs
weight: 400
url: /sv/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}

Ibland vill du ange vilken typ av data som ska laddas när du bygger arbetsboken från mallfilen. Filtrering av laddad data kan förbättra prestanda för ditt speciella ändamål, särskilt när du använder [LightCells APIs](/cells/sv/net/using-lightcells-api/). Använd egenskapen [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) för detta ändamål.

{{% /alert %}}

Följande exempelkod laddar endast formobjekt när arbetsboken laddas från [mallfilen](5115552.xlsx) som du kan ladda ned från länken. Följande skärmbild visar innehållet i [mallfilen](5115552.xlsx) och förklarar också att datan i rött och med gul bakgrund inte kommer att laddas eftersom egenskapen [**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) har ställts in till [**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Följande skärmbild visar [utdata PDF](5115555.pdf) som du kan ladda ned från länken. Här kan du se att datan i rött och gul bakgrund inte finns men alla former är där.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterDataWhileLoadingWorkbook-1.cs" >}}
