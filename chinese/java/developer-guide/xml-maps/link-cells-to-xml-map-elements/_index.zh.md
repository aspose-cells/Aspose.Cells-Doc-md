---
title: 将单元格链接到 XML 地图元素
type: docs
weight: 50
url: /zh/java/link-cells-to-xml-map-elements/
---

## **可能的使用场景**

您可以使用Aspose.Cells将单元格链接到XML映射元素。请使用[**Cells.LinkToXmlMap()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#linkToXmlMap-java.lang.String-int-int-java.lang.String-)方法来实现此目的。

## **将单元格链接到 XML 地图元素**

以下示例代码加载包含 XML 地图的源 Excel 文件(5472518.xlsx)，然后将单元格 A1、B2、C3、D4、E5 和 F6 分别链接到 XML 地图元素 FIELD1、FIELD2、FIELD4、FIELD5、FIELD7 和 FIELD8，然后将工作簿保存在输出 Excel 文件(5472517.xlsx)中。

如果您打开输出的 Excel 文件(5472517.xlsx) 并点击*Developer > Source*按钮，您将会看到这些单元格已链接到 XML 地图元素，并且它们也会被 Microsoft Excel 标记，如下图所示。

![todo:image_alt_text](link-cells-to-xml-map-elements_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LinkCellstoXmlMapElements-LinkCellstoXmlMapElements.java" >}}
{{< app/cells/assistant language="java" >}}
