---
title: Fråga Cell Områden mappade till XML Map Path med metoden Worksheet.XmlMapQuery
type: docs
weight: 60
url: /sv/net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---
## **Möjliga användningsscenarier**

Du kan fråga cellområden som är mappade till XML-kartans sökväg med Aspose.Cells med hjälp av[**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery)metod. Om sökvägen finns kommer den att returnera listan över cellområden som är relaterade till den sökvägen i XML-kartan. Den första parametern i[**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery)metod anger XML-elementets sökväg och den andra parametern anger en XML-karta som du vill fråga.

## **Fråga Cell Områden mappade till XML Map Path med metoden Worksheet.XmlMapQuery**

 Följande skärmdump visar Microsoft Excel som visar XML-karta inuti[exempel på Excel-fil](55541790.xlsx) används i koden. Koden frågar XML-kartan två gånger och skriver ut listan över cellområden som returneras av[**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery)metod på konsolen som visas nedan.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-QueryCellAreasMappedToXmlMapPath.cs" >}}

### **Konsolutgång**

{{< highlight "java" >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]Aspose.Cells.CellArea(B1:B8)[0,1,7,1]Aspose.Cells.CellArea(C1:C8)[0,2,7,2]Aspose.Cells.CellArea(D1:D8)[0,3,7,3]Aspose.Cells.CellArea(E1:E8)[0,4,7,4]Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]{{< /highlight >}}

## **Hämta XML-sökväg från listobjekt/tabell**

XML-data kan importeras till kalkylblad. Ibland krävs XML-sökväg från ListObjects i kalkylbladet. Den här funktionen är tillgänglig i Excel genom att använda ett uttryck som Sheet1.ListObjects(1).XmlMap.DataBinding. Samma funktion är tillgänglig på Aspose.Cells genom att ringa[**ListObject.XmlMap.DataBinding.Url**](https://reference.aspose.com/cells/net/aspose.cells/xmldatabinding/properties/url). Följande exempel visar denna funktion. Mallfil och andra källfiler kan laddas ner från följande länkar:

1. [XML Data.xlsx](72417285.xlsx)
1. [Country List.xml](72417287.xml)
1. [Food List.xml](72417286.xml)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-GetXMLPathFromListObject.cs" >}}
