---
title: 使用 Worksheet.XmlMapQuery 方法查询映射到 XML Map 路径的单元格区域
type: docs
weight: 60
url: /zh/java/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **可能的使用场景**

您可以使用 Aspose.Cells 中的 [**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) 方法查询映射到 XML 地图路径的单元区域。 如果路径存在，它将返回与 XML 地图中的该路径相关的单元区域的列表。 [**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap) 方法的第一个参数指定 XML 元素路径，第二个参数指定要查询的 XML 地图。

## **使用 Worksheet.XmlMapQuery 方法查询映射到 XML Map 路径的单元格区域**

下面的屏幕截图显示了 Microsoft Excel 在代码中使用的[sample Excel file](55541818.xlsx)中显示的 XML 地图。 代码两次查询 XML 地图，并在控制台上打印由 [**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) 方法返回的单元格区域列表。

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

## **从列表对象/表格中获取 XML 路径**

XML 数据可以导入到工作表中。 有时需要从工作表的 ListObjects 中获取 XML 路径。 在 Excel 中，可以使用类似于 Sheet1.ListObjects(1).XmlMap.DataBinding 的表达式。 在 Aspose.Cells 中可以通过调用 [**ListObject.getXmlMap().getDataBinding().getUrl()**](https://reference.aspose.com/cells/java/com.aspose.cells/xmldatabinding#Url) 来使用。 下面的示例演示了此功能。 模板文件和其他源文件可以从以下链接下载：

1. [XMLData.xlsx](XMLData.xlsx)
1. [CountryList.xml](CountryList.xml)
1. [FoodList.xml](FoodList.xml)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-GetXMLPathFromListObject.java" >}}
