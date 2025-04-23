---
title: Filtrera vilken typ av data som ska laddas från mallfilen när arbetsboken laddas
type: docs
weight: 680
url: /sv/java/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}} 

Ibland vill du specificera vilken typ av data som ska laddas när du bygger arbetsboken från en mallfil. Att filtrera laddade data kan förbättra prestanda för ditt speciella ändamål, speciellt när du använder [LightCells APIs](/cells/sv/java/using-lightcells-api/). Använd egenskapen [LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) för detta ändamål.

{{% /alert %}} 
## **Filtrera vilken typ av data som ska laddas från mallfilen när arbetsboken laddas**
Följande kodexempel laddar endast formobjekt när arbetsboken laddas från [mallfilen](5472556.xlsx) som du kan ladda ner från den angivna länken.

Följande skärmbild visar [mallfilens](5472556.xlsx) innehåll och förklarar också att data i rött och med gul bakgrund inte kommer att laddas eftersom egenskapen [LoadOptions.getLoadFilter().setLoadDataFilterOptions](https://reference.aspose.com/cells/java/com.aspose.cells/loadfilter#LoadDataFilterOptions) har ställts in till [LoadDataFilterOptions.SHAPE](https://reference.aspose.com/cells/java/com.aspose.cells/loaddatafilteroptions#SHAPE).

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Följande skärmbild visar [utmatnings-PDF](5472554.pdf) som du kan ladda ner från den angivna länken. Här kan du se att datan i rött och med gul bakgrund inte är närvarande men alla formobjekt är där.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-TechnicalArticles-FilterDataWhileLoadingWorkbook-1.java" >}}
{{< app/cells/assistant language="java" >}}
