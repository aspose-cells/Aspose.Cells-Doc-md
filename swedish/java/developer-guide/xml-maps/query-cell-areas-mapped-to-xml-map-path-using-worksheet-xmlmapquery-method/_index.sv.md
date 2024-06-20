---
title: Fråga cellområden kopplade till XML kartvärdering med hjälp av Worksheet.XmlMapQuery metoden
type: docs
weight: 60
url: /sv/java/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **Möjliga användningsscenario**

Du kan fråga cellområden kopplade till XML-kartvärdering med Aspose.Cells med hjälp av metoden [**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)). Om sökvägen finns, returneras listan över cellområden relaterade till den sökvägen inuti XML-kartan. Första parametern i [**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap))-metoden specifierar XML-elementens sökväg och den andra parametern specifierar en XML-karta du vill fråga.

## **Fråga cellområden kopplade till XML-kartvärdering med hjälp av Worksheet.XmlMapQuery-metoden**

Följande skärmbild visar Microsoft Excel som visar XML-kartan i [exempel Excel-filen](55541818.xlsx) som används i koden. Koden frågar XML-kartan två gånger och skriver ut listan över cellområden som returneras av [**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) metoden på konsollen, som visas nedan.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

## **Exempelkod**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-QueryCellAreasMappedToXmlMapPath.java" >}}

## **Konsoloutput**

{{< highlight java >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]

Aspose.Cells.CellArea(B1:B8)[0,1,7,1]

Aspose.Cells.CellArea(C1:C8)[0,2,7,2]

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]

Aspose.Cells.CellArea(E1:E8)[0,4,7,4]

Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]

{{< /highlight >}}

## **Få XML-sökväg från listobjekt/tabell**

XML-data kan importeras till arbetsblad. Ibland krävs XML-sökväg från ListObjects i arbetsboken. Denna funktion är tillgänglig i Excel genom att använda ett uttryck som Sheet1.ListObjects(1).XmlMap.DataBinding. Samma funktion är tillgänglig i Aspose.Cells genom att anropa [**ListObject.getXmlMap().getDataBinding().getUrl()**](https://reference.aspose.com/cells/java/com.aspose.cells/xmldatabinding#Url). Följande exempel visar denna funktion. Mallfil och andra källfiler kan laddas ner från följande länkar:

1. [XMLData.xlsx](XMLData.xlsx)
1. [CountryList.xml](CountryList.xml)
1. [FoodList.xml](FoodList.xml)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-GetXMLPathFromListObject.java" >}}
