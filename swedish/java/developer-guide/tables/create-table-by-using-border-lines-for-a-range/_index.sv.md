---
title: Skapa en tabell genom att använda kantlinjer för en mängd.
type: docs
weight: 50
url: /sv/java/create-table-by-using-border-lines-for-a-range/
description: Hur man skapar en tabell med mängd genom att använda kantlinjer. Aspose.Cells for Java erbjuder ett enkelt att använda API som kan användas för att lägga till kanter för en mängd.
keywords: skapa tabell, mängd till tabell, mängd till tabell excel, excel mängd till tabell, mängd till tabell med kanter, hur man skapar tabell från mängd, konvertera mängd till tabell, excel konvertera mängd till tabell, excel skapa tabell, mängd till tabell java 
---

{{% alert color="primary" %}}

Ibland vill du skapa en tabell genom att lägga till kantlinjer för en **Mängd**/**CellOmråde** baserad på adressen för de celler du har. Du kan använda metoden [**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean)) för att skapa en mängd celler. Metoden [**Cells.createRange**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#createRange(int,%20int,%20boolean)) returnerar ett [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range)-objekt. Du kan skapa ett [**Style**](https://reference.aspose.com/cells/java/com.aspose.cells/Style)-objekt och ange kante...liner (topp, vänster, botten, höger) alternativ därefter. Senare kan du få cellerna från [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) och tillämpa önskad formatering på cellerna.

{{% /alert %}}

Följande exempel visar hur man skapar en [**Range**](https://reference.aspose.com/cells/java/com.aspose.cells/Range) och anger kantlinjerna för områdscellerna.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CreateTableforRange-CreateTableforRange.java" >}}

Efter att ovanstående kod har körts kan vi ha den genererade Excel-filen som innehåller den formaterade tabellen; här är skärmdumpen på filen.

![todo:image_alt_text](create-table-by-using-border-lines-for-a-range_1.png)
