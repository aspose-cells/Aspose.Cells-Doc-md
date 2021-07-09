---
title: Query Cell Areas Mapped to XML Map Path using Worksheet.XmlMapQuery method
type: docs
weight: 60
url: /net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **Possible Usage Scenarios**

You can query cell areas mapped to the XML map path with Aspose.Cells using the [**Worksheet.XmlMapQuery()**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) method. If the path exists, it will return the list of cell areas related to that path inside XML map. The first parameter of the [**Worksheet.XmlMapQuery()**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) method specifies the XML element path and the second parameter specifies an XML map you want to query.

## **Query Cell Areas Mapped to XML Map Path using Worksheet.XmlMapQuery method**

The following screenshot shows the Microsoft Excel displaying XML Map inside the [sample Excel file](attachments/54690143/55541790.xlsx) used in the code. The code queries the XML map two times and prints the list of cell areas returned by the [**Worksheet.XmlMapQuery()**](https://apireference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) method on the console as shown below.

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-XmlMaps-QueryCellAreasMappedToXmlMapPath.cs" >}}

### **Console Output**

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

## **Get XML path from List Object/Table**

XML data can be imported to worksheets. Sometimes XML path is required from the ListObjects of the worksheet. This feature is available in Excel by using an expression like Sheet1.ListObjects(1).XmlMap.DataBinding. The same feature is available in Aspose.Cells by calling [**ListObject.XmlMap.DataBinding.Url**](https://apireference.aspose.com/cells/net/aspose.cells/xmldatabinding/properties/url).  The following example demonstrates this feature. Template file and other source files can be downloaded from the following links:

1. [XML Data.xlsx](72417285.xlsx)
1. [Country List.xml](72417287.xml)
1. [Food List.xml](72417286.xml)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-XmlMaps-GetXMLPathFromListObject.cs" >}}
