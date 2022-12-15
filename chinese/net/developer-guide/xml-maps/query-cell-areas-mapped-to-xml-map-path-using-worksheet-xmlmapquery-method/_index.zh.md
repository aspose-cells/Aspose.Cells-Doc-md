---
title: 使用 Worksheet.XmlMapQuery 方法查询映射到 XML 地图路径的区域 Cell
type: docs
weight: 60
url: /zh/net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---
## **可能的使用场景**

您可以使用 Aspose.Cells 查询映射到 XML 映射路径的单元格区域[**工作表.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery)方法。如果路径存在，它将返回 XML 映射中与该路径相关的单元格区域列表。的第一个参数[**工作表.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery)方法指定 XML 元素路径，第二个参数指定要查询的 XML 映射。

## **使用 Worksheet.XmlMapQuery 方法查询映射到 XML 地图路径的区域 Cell**

以下屏幕截图显示了 Microsoft Excel 在[示例 Excel 文件](55541790.xlsx)在代码中使用。该代码查询 XML 映射两次并打印返回的单元格区域列表[**工作表.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery)控制台上的方法如下所示。

![待办事项：图像_替代_文本](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-QueryCellAreasMappedToXmlMapPath.cs" >}}

### **控制台输出**

{{< highlight "java" >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]Aspose.Cells.CellArea(B1:B8)[0,1,7,1]Aspose.Cells.CellArea(C1:C8)[0,2,7,2]Aspose.Cells.CellArea(D1:D8)[0,3,7,3]Aspose.Cells.CellArea(E1:E8)[0,4,7,4]Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]{{< /highlight >}}

## **从列表对象/表中获取 XML 路径**

可以将 XML 数据导入到工作表中。有时工作表的 ListObjects 需要 XML 路径。通过使用像 Sheet1.ListObjects(1).XmlMap.DataBinding 这样的表达式，可以在 Excel 中使用此功能。通过调用 Aspose.Cells 可获得相同的功能[**ListObject.XmlMap.DataBinding.Url**](https://reference.aspose.com/cells/net/aspose.cells/xmldatabinding/properties/url).以下示例演示了此功能。模板文件和其他源文件可以从以下链接下载：

1. [XML 数据.xlsx](72417285.xlsx)
1. [国家列表.xml](72417287.xml)
1. [食物清单.xml](72417286.xml)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-GetXMLPathFromListObject.cs" >}}
