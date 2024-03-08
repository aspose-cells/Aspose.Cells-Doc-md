---
title: X-axel vs. Kategori Axel
description: Lär dig hur du skiljer mellan X-axeln och Kategoriaxeln i Aspose.Cells for Java. Vår guide hjälper dig att förstå skillnaderna i deras användning och egenskaper, och hur du konfigurerar dem efter dina behov.
keywords: Aspose.Cells for Java, X axis, Category axis, difference, usage, properties, configuration.
type: docs
weight: 180
url: /sv/java/x-axis-vs-category-axis/
---
##  **Möjliga användningsscenarier**
Det finns olika typer av X-axlar. Medan Y-axeln är en värdetypsaxel, kan X-axeln vara en kategoritypaxel eller en värdetypaxel. Med hjälp av en värdeaxel behandlas data som kontinuerligt varierande numeriska data, och markören placeras vid en punkt längs axeln som varierar enligt dess numeriska värde. Med hjälp av en kategoriaxel behandlas data som en sekvens av icke-numeriska textetiketter, och markören placeras vid en punkt längs axeln enligt dess position i sekvensen. Exemplet nedan illustrerar skillnaden mellan värde- och kategoriaxlar.
 Våra exempeldata visas i[exempel på tabellfil](sample.png) Nedan. Den första kolumnen innehåller våra X-axeldata, som kan behandlas som kategorier eller som värden. Observera att siffrorna inte är jämnt fördelade, och de visas inte ens i numerisk ordning.

![todo:image_alt_text](sample.png)
##  **Hantera X och kategoriaxel som Microsoft Excel**
Vi kommer att visa dessa data på två typer av diagram, det första diagrammet är XY (Scatter) diagram X som värdeaxel, det andra diagrammet är linjediagram X som Kategoriaxel.

![todo:image_alt_text](compare.png)

 Följande exempelkod genererar[utdata Excel-fil](XAxis.xlsx).

##  **Exempelkod**
{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "X-axis-vs-category-axis.java" >}}
