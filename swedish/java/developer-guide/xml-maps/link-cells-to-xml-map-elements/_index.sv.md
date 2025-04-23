---
title: Länka celler till XML kartelement
type: docs
weight: 50
url: /sv/java/link-cells-to-xml-map-elements/
---

## **Möjliga användningsscenario**

Du kan länka dina celler till XML-kartelement med hjälp av Aspose.Cells. Använd gärna metoden [**Cells.LinkToXmlMap()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#linkToXmlMap-java.lang.String-int-int-java.lang.String-) för detta ändamål.

## **Länka celler till XML-kartelement**

Följande exempelkod laddar den [källa Excel-fil](5472518.xlsx) som innehåller XML-karta och sedan länkar cellerna A1, B2, C3, D4, E5 och F6 till XML-kartelementen FIELD1, FIELD2, FIELD4, FIELD5, FIELD7 och FIELD8 respektive och sparar sedan arbetsboken i [utdata Excel-fil](5472517.xlsx).

Om du öppnar den [utdata Excel-filen](5472517.xlsx) och klickar på knappen *Utvecklare > Källa*, kommer du att se att cellerna är länkade med XML-kartelement och de kommer också att markeras av Microsoft Excel, som visas i denna bild.

![todo:image_alt_text](link-cells-to-xml-map-elements_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LinkCellstoXmlMapElements-LinkCellstoXmlMapElements.java" >}}
{{< app/cells/assistant language="java" >}}
