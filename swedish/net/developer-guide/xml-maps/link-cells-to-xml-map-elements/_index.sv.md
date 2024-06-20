---
title: Länka celler till XML kartelement
type: docs
weight: 50
url: /sv/net/link-cells-to-xml-map-elements/
---

## **Möjliga användningsscenario**

Du kan länka dina celler till XML-kartelement med Aspose.Cells. Använd [**Cells.LinkToXmlMap()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/linktoxmlmap) metoden för detta ändamål.

## **Länka celler till Xml-kartelement**

Följande exempelkod laddar den [käll-excel-filen](5115471.xlsx) som innehåller XML-karta och länkar sedan celler A1, B2, C3, D4, E5 och F6 till XML-kartelementen FIELD1, FIELD2, FIELD4, FIELD5 och FIELD7 respektive och sparar sedan arbetsboken som [utdata-excelfil](5115467.xlsx).

Om du öppnar [utdata excel-filen](5115467.xlsx) och klickar på Developer > Source-knappen, kommer du att se att cellerna är länkade med XML-kartelement och de kommer också att markeras av Microsoft Excel som visas på bilden.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LinkCellsToXmlMapElements-LinkCellsToXmlMapElements.cs" >}}
