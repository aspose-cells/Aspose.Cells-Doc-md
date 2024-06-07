---
title: 将单元格链接到 XML Map 元素
type: docs
weight: 50
url: /zh/java/link-cells-to-xml-map-elements/
---

## **可能的使用场景**

您可以使用 Aspose.Cells 将您的单元格链接到 XML 地图元素。 请使用 [**Cells.LinkToXmlMap()**](https://reference.aspose.com/cells/java/com.aspose.cells/cells#linkToXmlMap(java.lang.String,%20int,%20int,%20java.lang.String)) 方法进行此操作。

## **将单元格与XML映射元素关联**

以下示例代码加载了包含 XML 地图的[source excel file](5472518.xlsx)，然后将单元格 A1、B2、C3、D4、E5 和 F6 链接到 XML 地图元素 FIELD1、FIELD2、FIELD4、FIELD5、FIELD7 和 FIELD8，然后在[output excel file](5472517.xlsx)中保存工作簿。

如果打开[output excel file](5472517.xlsx)并单击 *Developer > Source* 按钮，您将看到单元格已经链接到 XML 地图元素，并且它们还将被 Microsoft Excel 高亮显示，如图所示。

![todo:image_alt_text](link-cells-to-xml-map-elements_1.png)

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LinkCellstoXmlMapElements-LinkCellstoXmlMapElements.java" >}}
