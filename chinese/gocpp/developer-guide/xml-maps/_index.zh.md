---
title: 使用 C++ 通过 Golang 将 XML 导入到 Excel 工作簿
linktitle: XML 映射
type: docs
weight: 210
url: /zh/go-cpp/import-xml-map-inside-a-workbook-using-aspose-cells/
description: 使用 C++ 通过 Golang 将 XML 数据文件的数据导入到 Microsoft Excel 中使用 Aspose.Cells
---

{{% alert color="primary" %}}

Aspose.Cells 允许您使用 [**Workbook.ImportXml()**](https://reference.aspose.com/cells/go-cpp/workbook/importxml_string_string_int_int/) 方法导入工作簿内的XML映射。可以按照以下步骤在Microsoft Excel中导入XML映射：

- 选择 **开发者** 选项卡。
- 单击 **在 XML 部分导入** 并按照所需步骤操作。

您需要提供您的 XML 数据以完成导入。这里是一个[样本 XML 数据](5115037.txt)，您可以用于测试。

{{% /alert %}}

## **使用 Microsoft Excel 导入 XML 地图**

下面的截图显示如何使用 Microsoft Excel 导入 XML 地图。

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **使用 Aspose.Cells 导入 XML 地图**

以下示例代码显示如何使用 [**Workbook.ImportXml()**](https://reference.aspose.com/cells/go-cpp/workbook/importxml_string_string_int_int/) 方法。它生成如截图所示的 [输出 Excel 文件](5115036.xlsx)。

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-XmlMaps.go" >}}
## ** 高级主题**
- [使用XmlMapCollection.Add方法在工作簿中添加XML映射](/cells/zh/cpp/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [导出链接到工作簿中的 XML 映射的 XML 数据](/cells/zh/cpp/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [查找 XML 映射的根元素名称](/cells/zh/cpp/find-the-root-element-name-of-xml-map/)
- [将单元格链接到 XML 地图元素](/cells/zh/cpp/link-cells-to-xml-map-elements/)
