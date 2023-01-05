---
title: 使用 Worksheet.XmlMapQuery 方法查询映射到 XML 地图路径的区域 Cell
type: docs
weight: 60
url: /zh/java/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---
## **可能的使用场景**

您可以使用 Aspose.Cells 查询映射到 XML 映射路径的单元格区域[**工作表.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)） 方法。如果路径存在，它将返回 XML 映射中与该路径相关的单元格区域列表。的第一个参数[**工作表.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)方法指定 XML 元素路径，第二个参数指定要查询的 XML 映射。

## **使用 Worksheet.XmlMapQuery 方法查询映射到 XML 地图路径的区域 Cell**

以下屏幕截图显示了 Microsoft Excel 在[示例 Excel 文件](55541818.xlsx)在代码中使用。该代码查询 XML 映射两次并打印返回的单元格区域列表[**工作表.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)方法在控制台上，如下所示。

![待办事项：图片_替代_文本](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-QueryCellAreasMappedToXmlMapPath.java" >}}

## **控制台输出**

{{< highlight "java" >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]Aspose.Cells.CellArea(B1:B8)[0,1,7,1]Aspose.Cells.CellArea(C1:C8)[0,2,7,2]Aspose.Cells.CellArea(D1:D8)[0,3,7,3]Aspose.Cells.CellArea(E1:E8)[0,4,7,4]Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]{{< /highlight >}}

## **从列表对象/表中获取 XML 路径**

可以将 XML 数据导入到工作表中。有时工作表的 ListObjects 需要 XML 路径。通过使用像 Sheet1.ListObjects(1).XmlMap.DataBinding 这样的表达式，可以在 Excel 中使用此功能。通过调用 Aspose.Cells 可获得相同的功能[**ListObject.getXmlMap().getDataBinding().getUrl()**](https://reference.aspose.com/cells/java/com.aspose.cells/xmldatabinding#Url).以下示例演示了此功能。模板文件和其他源文件可以从以下链接下载：

1. [XML数据.xlsx](XMLData.xlsx)
1. [国家列表.xml](CountryList.xml)
1. [食品清单.xml](FoodList.xml)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-GetXMLPathFromListObject.java" >}}
