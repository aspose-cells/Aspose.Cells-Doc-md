---
title: 将单元格链接到 XML 地图元素
type: docs
weight: 50
url: /zh/python-net/link-cells-to-xml-map-elements/
---

## **可能的使用场景**

你可以使用 Aspose.Cells for Python via .NET 将单元格连接到 XML 映射元素。请使用 [**Cells.link_to_xml_map()**](https://reference.aspose.com/cells/python-net/aspose.cells/cells/link_to_xml_map) 方法实现此目的。

## **将单元格链接到 XML 地图元素**

以下示例代码加载了包含 XML 地图的 [源 Excel 文件](5115471.xlsx)，然后将单元格 A1、B2、C3、D4、E5 和 F6 链接到 XML 地图元素 FIELD1、FIELD2、FIELD4、FIELD5、FIELD7 和 FIELD8，然后将工作簿保存在 [输出 Excel 文件](5115467.xlsx) 中。

如果您打开 [输出 Excel 文件](5115467.xlsx) 并单击“开发人员 > 源”按钮，您将看到单元格已链接到 XML 地图元素，并且它们也将被 Microsoft Excel 标记，如下图所示。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "XmlMaps-LinkCellsToXmlMapElements.py" >}}

{{< app/cells/assistant language="python-net" >}}
