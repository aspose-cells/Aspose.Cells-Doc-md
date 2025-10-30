---
title: Fråga cellområden kopplade till XML kartvärdering med hjälp av Worksheet.XmlMapQuery metoden
type: docs
weight: 60
url: /sv/python-net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **Möjliga användningsscenario**

Du kan fråga cellområden mappade till XML-kartans sökväg med Aspose.Cells för Python via .NET med [**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query) metod. Om sökvägen finns returneras en lista över cellområden relaterade till den sökvägen i XML-kartan. Den första parametern för [**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query) metod specificerar XML-elementets sökväg och den andra parameter anger vilken XML-karta du vill fråga.

## **Fråga cellområden kopplade till XML-kartvärdering med hjälp av Worksheet.XmlMapQuery-metoden**

Följande skärmbild visar Microsoft Excel som visar XML-karta inne i [prov Excel-filen](55541790.xlsx) som används i koden. Koden frågar XML-kartan två gånger och skriver ut listan över cellområden som returnerats av metoden [**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query) på konsolen som visas nedan.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **Exempelkod**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "XmlMaps-QueryCellAreasMappedToXmlMapPath.py" >}}

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

XML-data kan importeras till kalkylblad. Ibland krävs XML-sökväg från ListObjects i kalkylbladet. Denna funktion är tillgänglig i Excel genom att använda ett uttryck som Sheet1.ListObjects(1).XmlMap.DataBinding. Samma funktion är tillgänglig i Aspose.Cells för Python via .NET genom att anropa [**ListObject.xml_map.data_binding.url**](https://reference.aspose.com/cells/python-net/aspose.cells/xmldatabinding/url). Följande exempel illustrerar denna funktion. Mallfil och andra källfiler kan laddas ner från länkarna nedan:

1. [XML Data.xlsx](72417285.xlsx)
1. [Country List.xml](72417287.xml)
1. [Food List.xml](72417286.xml)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "XmlMaps-GetXMLPathFromListObject.py" >}}

{{< app/cells/assistant language="python-net" >}}
