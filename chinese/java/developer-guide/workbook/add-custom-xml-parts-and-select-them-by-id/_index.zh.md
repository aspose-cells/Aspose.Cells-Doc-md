---
title: 添加自定义XML部件并按ID选择
type: docs
weight: 10
url: /zh/java/add-custom-xml-parts-and-select-them-by-id/
---

## **可能的使用场景**

自定义XML部件是存储在Microsoft Excel文档中并由处理它们的应用程序使用的XML数据。目前，使用Microsoft Excel UI添加它们没有直接的方法。但是，您可以通过各种方式编程方式添加它们，例如使用*VSTO*、使用*Aspose.Cells*等。如果要使用Aspose.Cells API添加自定义XML部件，请使用[**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add-java.lang.Object-)方法。您还可以使用[**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID)属性设置其ID。同样，如果要通过ID选择自定义XML部件，可以使用[**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID-java.lang.String-)方法。

## **添加自定义XML部件并按ID选择**

以下示例代码首先使用[**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add-java.lang.Object-)方法添加了四个自定义XML部件。然后使用[**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID)属性设置它们的ID。最后，使用[**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID-java.lang.String-)方法找到或选择其中一个添加的自定义XML部件。请参考以下给出的代码的控制台输出以供参考。

## **示例代码**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-AddCustomXMLPartsAndSelectThemByID.java" >}}

## **控制台输出**

{{< highlight java >}}

Found: CustomXmlPart ID Sport

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
