---
title: Filtrera vilken typ av data som ska laddas från mallfilen när arbetsboken laddas
type: docs
weight: 400
url: /sv/python-net/filtering-the-kind-of-data-while-loading-the-workbook-from-template-file/
---

{{% alert color="primary" %}}

Ibland vill du ange vilken sorts data som ska laddas när du bygger arbetsboken från mallen. Filtrering av laddad data kan förbättra prestandan för ditt speciella ändamål. Använd egenskapen [**LoadOptions.load_filter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) för detta ändamål.

{{% /alert %}}

Följande exempelkod laddar endast formobjekt när arbetsboken laddas från [mallfilen](5115552.xlsx) som du kan ladda ned från länken. Följande skärmbild visar innehållet i [mallfilen](5115552.xlsx) och förklarar också att datan i rött och med gul bakgrund inte kommer att laddas eftersom egenskapen [**LoadOptions.load_filter**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/load_filter) har ställts in till [**LoadDataFilterOptions.SHAPE**](https://reference.aspose.com/cells/python-net/aspose.cells/loaddatafilteroptions/)

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_1.png)

Följande skärmbild visar [utdata PDF](5115555.pdf) som du kan ladda ned från länken. Här kan du se att datan i rött och gul bakgrund inte finns men alla former är där.

![todo:image_alt_text](filtering-the-kind-of-data-while-loading-the-workbook-from-template-file_2.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Open-files-FilterDataWhileLoadingWorkbook-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
