---
title: Filtrera typen av data när arbetsboken laddas från mallfilen
type: docs
weight: 400
url: /sv/net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---
{{% alert color="primary" %}}

 Ibland vill du ange vilken typ av data som ska laddas när du bygger arbetsboken från mallfilen. Filtrering av laddade data kan förbättra prestandan för ditt speciella ändamål, särskilt när du använder[LightCells API:er](/cells/sv/net/using-lightcells-api/) . Vänligen använd[**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter) egendom för detta ändamål.

{{% /alert %}}

Följande exempelkod läser bara in formobjekt när arbetsboken läses in från[mallfil](5115552.xlsx) som du kan ladda ner från den angivna länken. Följande skärmdump visar[mallfil](5115552.xlsx) innehållet och förklarar också att data i röd färg och gul bakgrund inte kommer att laddas pga[**LoadOptions.LoadFilter**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/loadfilter)egenskapen har ställts in på[**LoadDataFilterOptions.Shape**](https://reference.aspose.com/cells/net/aspose.cells/loaddatafilteroptions)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

 Följande skärmdump visar[mata ut PDF](5115555.pdf) som du kan ladda ner från den angivna länken. Här kan du se, data i röd färg och gul bakgrund är inte närvarande men alla former finns där.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-FilterDataWhileLoadingWorkbook-1.cs" >}}
