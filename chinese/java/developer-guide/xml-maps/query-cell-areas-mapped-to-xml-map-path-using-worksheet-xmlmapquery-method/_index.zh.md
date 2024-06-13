---
title: 通过 Worksheet.XmlMapQuery 方法查询映射到 XML 地图路径的单元格区域
type: docs
weight: 60
url: /zh/java/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **可能的使用场景**

您可以使用Aspose.Cells的[**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap))方法查询映射到XML映射路径的单元格区域。如果路径存在，它将返回与XML映射内部该路径相关的单元格区域的列表。[**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap))方法的第一个参数指定XML元素路径，第二个参数指定您要查询的XML映射。

## **通过 Worksheet.XmlMapQuery 方法查询映射到 XML 地图路径的单元格区域**

下面的屏幕截图显示了Microsoft Excel显示内含在代码中使用的[sample Excel文件](55541818.xlsx)中的XML映射。代码两次查询XML映射并以控制台上的[**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap))方法返回的单元格区域列表显示如下。

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-QueryCellAreasMappedToXmlMapPath.java" >}}

## **控制台输出**

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

## **从列表对象/表格获取 XML 路径**

XML 数据可以导入工作表。有时需要从工作表的 ListObjects 获取 XML 路径。在 Excel 中，可以通过类似 Sheet1.ListObjects(1).XmlMap.DataBinding 的表达式来实现这一特性。在 Aspose.Cells 中，可以通过调用 [**ListObject.getXmlMap().getDataBinding().getUrl()**](https://reference.aspose.com/cells/java/com.aspose.cells/xmldatabinding#Url) 实现相同的功能。以下示例演示了这一功能。模板文件和其他源文件可以从以下链接下载：

1. [XMLData.xlsx](XMLData.xlsx)
1. [CountryList.xml](CountryList.xml)
1. [FoodList.xml](FoodList.xml)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-GetXMLPathFromListObject.java" >}}
