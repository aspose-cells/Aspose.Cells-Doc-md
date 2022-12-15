---
title: 将 Cells 链接到 XML 映射元素
type: docs
weight: 50
url: /zh/java/link-cells-to-xml-map-elements/
---
## **可能的使用场景**

您可以使用 Aspose.Cells 将您的单元格链接到 XML 地图元素。请使用[**Cells.LinkToXmlMap()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#linkToXmlMap(java.lang.String,%20int,%20int,%20java.lang.String)) 方法用于此目的。

## **将 Cells 链接到 XML 映射元素**

下面的示例代码加载[源文件](5472518.xlsx)其中包含 XML 映射，然后将单元格 A1、B2、C3、D4、E5 和 F6 分别链接到 XML 映射元素 FIELD1、FIELD2、FIELD4、FIELD5、FIELD7 和 FIELD8，然后将工作簿保存在[输出excel文件](5472517.xlsx).

如果你打开[输出excel文件](5472517.xlsx)然后点击*开发人员 > 来源*按钮，您将看到单元格与 XML 映射元素链接，它们也将由 Microsoft Excel 突出显示，如此图所示。

![待办事项：图像_替代_文本](link-cells-to-xml-map-elements_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LinkCellstoXmlMapElements-LinkCellstoXmlMapElements.java" >}}
