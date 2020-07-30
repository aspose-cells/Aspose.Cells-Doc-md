---
title : "Query Cell Areas Mapped to XML Map Path using Worksheet.XmlMapQuery method" 
description : "" 
weight : 12333 
toc : false
type: docs
url: /net/developerguide/xmlmaps/query+cell+areas+mapped+to+xml+map+path+using+worksheet.xmlmapquery+method/
---

# Aspose.Cells for .NET : Query Cell Areas Mapped to XML Map Path using Worksheet.XmlMapQuery method


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Query Cell Areas Mapped to XML Map Path using Worksheet.XmlMapQuery method](#query-cell-areas-mapped-to-xml-map-path-using-worksheet.xmlmapquery-method)
    *   2.1 [Sample Code](#sample-code)
    *   2.2 [Console Output](#console-output)
*   3 [Get XML path from List Object/Table](#get-xml-path-from-list-object/table)
{{< /panel >}}
 

## Possible Usage Scenarios

You can query cell areas mapped to the XML map path with Aspose.Cells using the [Worksheet.XmlMapQuery()](https://apireference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) method. If the path exists, it will return the list of cell areas related to that path inside XML map. The first parameter of the [Worksheet.XmlMapQuery()](https://apireference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) method specifies the XML element path and the second parameter specifies an XML map you want to query.

## Query Cell Areas Mapped to XML Map Path using Worksheet.XmlMapQuery method

The following screenshot shows the Microsoft Excel displaying XML Map inside the [sample Excel file](https://docs2.aspose.com/cells/net/attachments/54690143/55541790.xlsx) used in the code. The code queries the XML map two times and prints the list of cell areas returned by the [Worksheet.XmlMapQuery()](https://apireference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) method on the console as shown below.

![](https://docs2.aspose.com/cells/net/attachments/54690143/55541791.png)

### Sample Code

### Console Output

{{< code lang="cs" >}}
Query Xml Map from Path - /MiscData
Aspose.Cells.CellArea(A1:A8)[0,0,7,0]
Aspose.Cells.CellArea(B1:B8)[0,1,7,1]
Aspose.Cells.CellArea(C1:C8)[0,2,7,2]
Aspose.Cells.CellArea(D1:D8)[0,3,7,3]
Aspose.Cells.CellArea(E1:E8)[0,4,7,4]

Query Xml Map from Path - /MiscData/row/Color
Aspose.Cells.CellArea(D1:D8)[0,3,7,3]
{{< /code >}}

## Get XML path from List Object/Table

XML data can be imported to worksheets. Sometimes XML path is required from the ListObjects of the worksheet. This feature is available in Excel by using an expression like Sheet1.ListObjects(1).XmlMap.DataBinding. The same feature is available in Aspose.Cells by calling [ListObject.XmlMap.DataBinding.Url](https://apireference.aspose.com/cells/net/aspose.cells/xmldatabinding/properties/url).  The following example demonstrates this feature. Template file and other source files can be downloaded from the following links:

1.  [XML Data.xlsx](https://docs2.aspose.com/cells/net/attachments/54690143/72417285.xlsx)
2.  [Country List.xml](https://docs2.aspose.com/cells/net/attachments/54690143/72417287.xml)
3.  [Food List.xml](https://docs2.aspose.com/cells/net/attachments/54690143/72417286.xml)

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [sampleXmlMapQuery.xlsx](https://docs2.aspose.com/cells/net/attachments/54690143/55541790.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Sample-Excel-File-For-Xml-Map-Query.png](https://docs2.aspose.com/cells/net/attachments/54690143/55541791.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [XML Data.xlsx](https://docs2.aspose.com/cells/net/attachments/54690143/72417285.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Food List.xml](https://docs2.aspose.com/cells/net/attachments/54690143/72417286.xml) (text/xml)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Country List.xml](https://docs2.aspose.com/cells/net/attachments/54690143/72417287.xml) (text/xml)  

