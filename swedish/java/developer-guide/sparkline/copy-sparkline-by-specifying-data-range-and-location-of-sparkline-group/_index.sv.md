---
title: Kopiera Sparkline genom att ange dataintervall och plats för Sparkline Group
type: docs
weight: 120
url: /sv/java/copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group/
---
Kopiera Sparkline genom att ange dataintervall och plats för Sparkline Group i MS Excel

Microsoft Excel låter dig kopiera en Sparkline genom att ange dataintervall och plats för Sparkline Group. Följ dessa steg för att kopiera din Sparkline till andra celler.

- Välj cellen som innehåller din Sparkline.
-  Välj**Redigera data** från**Sparkline** avsnitt inuti**Design** flik
-  Välja**Redigera gruppplats och data...**
- Ange dataområde och plats och klicka på OK.

## Exempel

 Aspose.Cells tillhandahåller[**SparklineCollection.add(dataRange, rad, kolumn)**](https://reference.aspose.com/cells/java/com.aspose.cells/SparklineCollection) metod för att specificera dataintervall och plats för Sparkline Group.

### Skärmdumpar av käll- och utdatafiler

Följande skärmdump visar källfilen för Excel som används i koden. Det rödmarkerade området visar "**Redigera gruppplats och data...**" alternativ för att specificera dataintervallet och placeringen av sparklinegruppen. Cellen P4 visar sparkline som kommer att kopieras till de andra fyra cellerna fyllda med gul färg med Aspose.Cells.

![todo:image_alt_text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_1.png)

Följande skärmdump visar den utgående Excel-filen som genereras av exempelkoden. Som du kan se har gnistan i cell P4 kopierats till nästa fyra celler i kolumn P var och en med olika dataintervall.

![todo:image_alt_text](copy-sparkline-by-specifying-data-range-and-location-of-sparkline-group_2.png)

### Java-kod för att kopiera sparkline genom att ange dataintervall och plats för sparkline-gruppen

Följande exempelkod laddar källfilen för Excel som visas i skärmdumpen ovan, kommer sedan åt den första sparkline-gruppen och lägger till dataintervall och platser i sparkline-gruppen. Slutligen skriver den utdata Excel-filen på disken som också visas i skärmdumpen ovan.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-CopySparkline-CopySparkline.java" >}}
