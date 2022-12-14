---
title: Fråga Cell Områden mappade till XML Map Path med metoden Worksheet.XmlMapQuery
type: docs
weight: 60
url: /sv/java/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---
## **Möjliga användningsscenarier**

Du kan fråga cellområden som är mappade till XML-kartans sökväg med Aspose.Cells med hjälp av[**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) metod. Om sökvägen finns kommer den att returnera listan över cellområden som är relaterade till den sökvägen inuti XML-kartan. Den första parametern av[**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap))-metoden anger XML-elementets sökväg och den andra parametern anger en XML-karta som du vill fråga.

## **Fråga Cell Områden mappade till XML Map Path med metoden Worksheet.XmlMapQuery**

Följande skärmdump visar Microsoft Excel som visar XML-karta inuti[exempel på Excel-fil](55541818.xlsx)används i koden. Koden frågar XML-kartan två gånger och skriver ut listan över cellområden som returneras av[**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) metoden på konsolen som visas nedan.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-QueryCellAreasMappedToXmlMapPath.java" >}}

## **Konsolutgång**

{{< highlight "java" >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]Aspose.Cells.CellArea(B1:B8)[0,1,7,1]Aspose.Cells.CellArea(C1:C8)[0,2,7,2]Aspose.Cells.CellArea(D1:D8)[0,3,7,3]Aspose.Cells.CellArea(E1:E8)[0,4,7,4]Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]{{< /highlight >}}

## **Hämta XML-sökväg från listobjekt/tabell**

XML-data kan importeras till kalkylblad. Ibland krävs XML-sökväg från ListObjects i kalkylbladet. Den här funktionen är tillgänglig i Excel genom att använda ett uttryck som Sheet1.ListObjects(1).XmlMap.DataBinding. Samma funktion är tillgänglig på Aspose.Cells genom att ringa[**ListObject.getXmlMap().getDataBinding().getUrl()**](https://reference.aspose.com/cells/java/com.aspose.cells/xmldatabinding#Url). Följande exempel visar denna funktion. Mallfil och andra källfiler kan laddas ner från följande länkar:

1. [XMLData.xlsx](XMLData.xlsx)
1. [CountryList.xml](CountryList.xml)
1. [FoodList.xml](FoodList.xml)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-GetXMLPathFromListObject.java" >}}
