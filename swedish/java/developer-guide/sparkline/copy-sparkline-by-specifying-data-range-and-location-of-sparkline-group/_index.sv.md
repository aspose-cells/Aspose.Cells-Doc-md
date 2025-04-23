---
title: Kopiera sparkline genom att ange dataområde och plats för sparklinegrupp
type: docs
weight: 120
url: /sv/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---

Kopiera sparkline genom att ange dataområde och plats för sparklinegrupp i MS Excel

Microsoft Excel tillåter dig att kopiera en sparkline genom att ange dataområde och plats för sparklinegrupp. Följ dessa steg för att kopiera din sparkline till andra celler.

- Välj cellen som innehåller din sparkline.
- Välj **Redigera data** från avsnittet **Sparkline** inne i fliken **Design**
- Välj **Redigera gruppläge & Data...**
- Ange dataområde och plats och klicka OK.

## Exempel

Aspose.Cells tillhandahåller metoden [**SparklineCollection.add(dataRange, row, column)**](https://reference.aspose.com/cells/java/com.aspose.cells/SparklineCollection) för att ange dataområde och plats för sparklinegruppen.

### Skärmbilder av käll- och utdatafiler

Följande skärmbild visar den käll-Excel-fil som används i koden. Det röda markerade området visar alternativet "**Redigera gruppläge & Data...**" för att ange dataområdet och platsen för sparklinegruppen. Cellen P4 visar sparkline som kommer att kopieras till de andra fyra cellerna fyllda med gul färg med hjälp av Aspose.Cells.

![todo:image_alt_text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_1.png)

Följande skärmbild visar den genererade utdata-Excel-filen av kodexemplet. Som du kan se har sparkline i cellen P4 kopierats till de närmaste fyra cellerna i kolumn P, var och en med olika dataområde.

![todo:image_alt_text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_2.png)

### Java-kod för att kopiera sparkline genom att ange dataområde och plats för sparklinegrupp

Följande kodexempel laddar den angivna käll-Excel-filen enligt skärmbilden ovan, får sedan åtkomst till den första sparklinegruppen och lägger till dataområden och platser inuti sparklinegruppen. Slutligen skriver den utdata-Excel-filen på disk, vilket också visas i skärmbilden ovan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopySparkline-CopySparkline.java" >}}
{{< app/cells/assistant language="java" >}}
