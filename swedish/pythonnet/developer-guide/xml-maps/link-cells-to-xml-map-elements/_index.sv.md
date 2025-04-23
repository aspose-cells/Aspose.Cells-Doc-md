---
title: Länka celler till XML kartelement
type: docs
weight: 50
url: /sv/python-net/link-cells-to-xml-map-elements/
---

## **Möjliga användningsscenario**

Du kan länka celler till XML-kartans element med Aspose.Cells för Python via .NET. Använd [**Cells.link_to_xml_map()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/link_to_xml_map) metod för detta syfte.

## **Länka celler till Xml-kartelement**

Följande exempelkod laddar den [käll-excel-filen](5115471.xlsx) som innehåller XML-karta och länkar sedan celler A1, B2, C3, D4, E5 och F6 till XML-kartelementen FIELD1, FIELD2, FIELD4, FIELD5 och FIELD7 respektive och sparar sedan arbetsboken som [utdata-excelfil](5115467.xlsx).

Om du öppnar [utdata excel-filen](5115467.xlsx) och klickar på Developer > Source-knappen, kommer du att se att cellerna är länkade med XML-kartelement och de kommer också att markeras av Microsoft Excel som visas på bilden.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "XmlMaps-LinkCellsToXmlMapElements.py" >}}

