---
title: Filtrera typen av data när arbetsboken laddas från mallfilen
type: docs
weight: 680
url: /sv/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---
{{% alert color="primary" %}} 

 Ibland vill du ange vilken typ av data som ska laddas när du bygger arbetsboken från en mallfil. Filtrering av laddade data kan förbättra prestandan för ditt speciella ändamål, särskilt när du använder[LightCells API:er](/cells/sv/java/using-lightcells-api/) . Vänligen använd[LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) egendom för detta ändamål.

{{% /alert %}} 
## **Filtrera typen av data när arbetsboken laddas från en mallfil**
Följande exempelkod läser bara in formobjekt när arbetsboken läses in från[mallfil](5472556.xlsx) som du kan ladda ner från den angivna länken.

 Följande skärmdump visar[mallfil](5472556.xlsx)innehållet och förklarar också att data i röd färg och gul bakgrund inte kommer att laddas eftersom[LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions)egenskapen har ställts in på[LoadDataFilterOptions.SHAPE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE).

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

 Följande skärmdump visar[mata ut PDF](5472554.pdf) som du kan ladda ner från den angivna länken. Här kan du se, data i röd färg och gul bakgrund är inte närvarande men alla former finns där.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterDataWhileLoadingWorkbook-1.java" >}}
