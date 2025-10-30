---
title: Hur man skapar Sunburst diagram med Golang via C++
description: Lär dig hur man skapar ett sunburst diagram i Aspose.Cells for C++, ett diagram som visar data i en cirkel. Vår guide hjälper dig att ställa in olika egenskaper och formatering av ditt diagram, inklusive datamärkning, legend, färger och mer.
keywords: Aspose.Cells for C++, sunburst diagram, skapa, ställ in egenskaper, datamärkning, legend, format, färg, cirkel, data rendering.
type: docs
weight: 162
url: /sv/go-cpp/creating-sunburst-chart/
---

## **Möjliga användningsscenario**
Treemaps-diagram är bra för att jämföra proportioner inom hierarkin, men treemaps är inte optimala för att visa hierarkiska nivåer mellan de största kategorierna och varje datapunkt. En sunburst-diagram är mycket bättre för att visa detta. Sunburst-diagram är idealiskt för att visa hierarkiska data. Varje nivå i hierarkin representeras av en ring eller cirkel, där den innersta ringen är toppen av hierarkin. Ett sunburst-diagram utan hierarkiska data (en nivå av kategorier) ser ut som en donut. Men ett sunburst-diagram med flera nivåer av kategorier visar hur de yttre ringarna är relaterade till de inre ringarna. Sunburst-diagram är mest effektiva för att visa hur en ring är uppdelad i dess bidragande delar, medan en annan typ av hierarkiskt diagram, treemaps-diagram, är ideal för att jämföra relativa storlekar.

![todo:image_alt_text](sample.png)
## **Solfjäderdiagram**
Efter att ha kört koden nedan kommer du att se solfjäderdiagrammet som visas nedan.

![todo:image_alt_text](result.png)
## **Exempelkod**
Följande exempelkod läser in [provkalkylbladet](sunburst.xlsx) och genererar [utmatningskalkylbladet](out.xlsx).

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreatingSunburstChart.go" >}}
