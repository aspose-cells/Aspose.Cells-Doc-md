---
title: 使用 Worksheet.XmlMapQuery 方法查询映射到 XML Map 路径的单元格区域
type: docs
weight: 60
url: /zh/net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **可能的使用场景**

您可以使用 Aspose.Cells 的 [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) 方法查询映射到 XML Map 路径的单元格区域。如果路径存在，它将返回与 XML 映射内相关的该路径的单元格区域列表。[**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) 方法的第一个参数指定了 XML 元素路径，第二个参数指定要查询的 XML Map。

## **使用 Worksheet.XmlMapQuery 方法查询映射到 XML Map 路径的单元格区域**

以下截图显示了 Microsoft Excel 在代码中使用的 [示例 Excel 文件](55541790.xlsx) 中显示的 XML Map。代码查询 XML map 两次，并在控制台上打印 [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery) 方法返回的单元格区域列表，如下图所示。

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **示例代码**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-QueryCellAreasMappedToXmlMapPath.cs" >}}

### **控制台输出**

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

XML 数据可以导入工作表。有时需要从工作表的 ListObjects 获取 XML 路径。在 Excel 中，可以通过类似于 Sheet1.ListObjects(1).XmlMap.DataBinding 这样的表达式来实现。在 Aspose.Cells 中，通过调用 [**ListObject.XmlMap.DataBinding.Url**](https://reference.aspose.com/cells/net/aspose.cells/xmldatabinding/properties/url) 来实现相同的功能。以下示例演示了此功能。可从以下链接下载模板文件和其他源文件：

1. [XML 数据.xlsx](72417285.xlsx)
1. [国家列表.xml](72417287.xml)
1. [食物列表.xml](72417286.xml)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-GetXMLPathFromListObject.cs" >}}
