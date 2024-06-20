---
title: Fråga cellområden kopplade till XML kartvärdering med hjälp av Worksheet.XmlMapQuery metoden
type: docs
weight: 60
url: /sv/net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **Möjliga användningsscenario**

Du kan fråga cellområden som är karterade till XML-kartans sökväg med Aspose.Cells använder metoden [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery). Om sökvägen finns, kommer den att returnera listan över cellområden som är relaterade till den sökvägen inne i XML-kartan. Den första parametern av metoden [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) specifierar XML-elementets sökväg och den andra parametern specifierar en XML-karta du vill fråga.

## **Fråga cellområden kopplade till XML-kartvärdering med hjälp av Worksheet.XmlMapQuery-metoden**

Följande skärmbild visar Microsoft Excel som visar XML-karta inne i [prov Excel-filen](55541790.xlsx) som används i koden. Koden frågar XML-kartan två gånger och skriver ut listan över cellområden som returnerats av metoden [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) på konsolen som visas nedan.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **Exempelkod**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-QueryCellAreasMappedToXmlMapPath.cs" >}}

### **Konsoloutput**

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

XML-data kan importeras till kalkylblad. Ibland krävs XML-sökvägen från ListObjects i kalkylbladet. Denna funktion finns tillgänglig i Excel genom att använda ett uttryck som Sheet1.ListObjects(1).XmlMap.DataBinding. Samma funktion finns tillgänglig i Aspose.Cells genom att anropa [**ListObject.XmlMap.DataBinding.Url**](https://reference.aspose.com/cells/net/aspose.cells/xmldatabinding/properties/url).    Följande exempel demonstrerar denna funktion. Mallfilen och andra källfiler kan laddas ner från följande länkar:

1. [XML Data.xlsx](72417285.xlsx)
1. [Country List.xml](72417287.xml)
1. [Food List.xml](72417286.xml)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-GetXMLPathFromListObject.cs" >}}
