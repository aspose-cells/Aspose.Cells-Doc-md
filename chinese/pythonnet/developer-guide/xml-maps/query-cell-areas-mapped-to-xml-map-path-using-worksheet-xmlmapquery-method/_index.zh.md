---
title: 通过 Worksheet.XmlMapQuery 方法查询映射到 XML 地图路径的单元格区域
type: docs
weight: 60
url: /zh/python-net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **可能的使用场景**

你可以用 Aspose.Cells for Python via .NET 查询映射到 XML 映射路径的单元区域，使用 [**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query) 方法。如果路径存在，返回与该路径相关的单元区域列表。[**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query) 方法的第一个参数指定 XML 元素路径，第二个参数指定要查询的 XML 映射。

## **通过 Worksheet.XmlMapQuery 方法查询映射到 XML 地图路径的单元格区域**

以下屏幕截图显示了 Microsoft Excel 在代码中使用的 [示例 Excel 文件](55541790.xlsx) 内显示 XML 地图。代码查询 XML 地图两次，并将 [**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query) 方法返回的单元区域列表打印到控制台上，如下所示。

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "XmlMaps-QueryCellAreasMappedToXmlMapPath.py" >}}

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

## **从列表对象/表格获取 XML 路径**

XML 数据可以导入到工作表中。有时需要从工作表的 ListObjects 获取 XML 路径。Excel 中可通过表达式如 Sheet1.ListObjects(1).XmlMap.DataBinding 来实现。Aspose.Cells for Python via .NET 通过调用 [**ListObject.xml_map.data_binding.url**](https://reference.aspose.com/cells/python-net/aspose.cells/xmldatabinding/url) 提供此功能。以下示例演示了此功能。模板文件和其他源文件可从以下链接下载：

1. [XML Data.xlsx](72417285.xlsx)
1. [Country List.xml](72417287.xml)
1. [Food List.xml](72417286.xml)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "XmlMaps-GetXMLPathFromListObject.py" >}}

{{< app/cells/assistant language="python-net" >}}
