---
title : "Query Cell Areas Mapped to XML Map Path using Worksheet.XmlMapQuery method" 
description : "" 
weight : 12284 
toc : false
type: docs
url: /java/developerguide/xmlmaps/query+cell+areas+mapped+to+xml+map+path+using+worksheet.xmlmapquery+method/
---

# Aspose.Cells for Java : Query Cell Areas Mapped to XML Map Path using Worksheet.XmlMapQuery method


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Query Cell Areas Mapped to XML Map Path using Worksheet.XmlMapQuery method](#query-cell-areas-mapped-to-xml-map-path-using-worksheet.xmlmapquery-method)
*   3 [Sample Code](#sample-code)
*   4 [Console Output](#console-output)
*   5 [Get XML path from List Object/Table](#get-xml-path-from-list-object/table)
{{< /panel >}}
 

## Possible Usage Scenarios

You can query cell areas mapped to XML map path with Aspose.Cells using the [Worksheet.xmlMapQuery()](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) method. If the path exists, it will return the list of cell areas related to that path inside the XML map. The first parameter of [Worksheet.xmlMapQuery()](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) method specifies the XML element path and the second parameter specifies an XML map you want to query.

## Query Cell Areas Mapped to XML Map Path using Worksheet.XmlMapQuery method

The following screenshot shows the Microsoft Excel displaying XML Map inside the [sample Excel file](https://docs2.aspose.com/cells/java/attachments/54690375/55541818.xlsx) used in the code. The code queries the XML map two times and prints the list of cell areas returned by the [Worksheet.xmlMapQuery()](https://apireference.aspose.com/java/cells/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) method on the console as shown below.

![](https://docs2.aspose.com/cells/java/attachments/54690375/55541819.png)

## Sample Code

## Console Output

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

XML data can be imported to worksheets. Sometimes XML path is required from the ListObjects of the worksheet. This feature is available in Excel by using an expression like Sheet1.ListObjects(1).XmlMap.DataBinding. The same feature is available in Aspose.Cells by calling [ListObject.getXmlMap().getDataBinding().getUrl()](https://apireference.aspose.com/java/cells/com.aspose.cells/xmldatabinding#Url).  Following example demonstrates this feature. Template file and other source files can be downloaded from the following links:

1.  [XML Data.xlsx](https://docs.aspose.com/download/attachments/54690143/XML%20Data.xlsx?version=1&modificationDate=1537204009029&api=v2)
2.  [Country List.xml](https://docs.aspose.com/download/attachments/54690143/Country%20List.xml?version=1&modificationDate=1537204022375&api=v2)
3.  [Food List.xml](https://docs.aspose.com/download/attachments/54690143/Food%20List.xml?version=1&modificationDate=1537204018028&api=v2)

