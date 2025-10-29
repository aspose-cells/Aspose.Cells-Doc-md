---
title: 使用C++通过Golang将单元格链接到XML映射元素
linktitle: 将单元格链接到 XML 地图元素
type: docs
weight: 50
url: /zh/go-cpp/link-cells-to-xml-map-elements/
description: 学习如何使用C++通过Golang和Aspose.Cells将单元格链接到XML映射元素
---

## **可能的使用场景**

您可以使用 Aspose.Cells 将单元格链接到 XML 地图元素。请使用此目的的 [**Cells.LinkToXmlMap()**](https://reference.aspose.com/cells/go-cpp/cells/linktoxmlmap/) 方法。

## **将单元格链接到 XML 地图元素**

以下示例代码加载了包含 XML 地图的 [源 Excel 文件](5115471.xlsx)，然后将单元格 A1、B2、C3、D4、E5 和 F6 链接到 XML 地图元素 FIELD1、FIELD2、FIELD4、FIELD5、FIELD7 和 FIELD8，然后将工作簿保存在 [输出 Excel 文件](5115467.xlsx) 中。

如果您打开 [输出 Excel 文件](5115467.xlsx) 并单击“开发人员 > 源”按钮，您将看到单元格已链接到 XML 地图元素，并且它们也将被 Microsoft Excel 标记，如下图所示。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-LinkCellsToXmlMapElements.go" >}}
