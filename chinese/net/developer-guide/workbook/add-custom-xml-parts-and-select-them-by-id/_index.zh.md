---
title: 添加自定义XML部件并根据ID选择它们
type: docs
weight: 70
url: /zh/net/add-custom-xml-parts-and-select-them-by-id/
---

## **可能的使用场景**

自定义XML部件是存储在Microsoft Excel文档中的XML数据，并由处理它们的应用程序使用。目前，使用Microsoft Excel UI没有直接的添加它们的方法。但是，您可以以各种方式编程方式添加它们，例如使用VSTO、使用Aspose.Cells等。如果要使用Aspose.Cells API添加自定义XML部件，请使用[**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add)方法。您还可以使用[**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id)属性设置其ID。类似地，如果要根据ID选择自定义XML部件，可以使用[**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)方法。

## **添加自定义XML部件并根据ID选择它们**

以下示例代码首先使用[**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add)方法添加四个自定义XML部件。然后使用[**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id)属性设置它们的ID。最后，使用[**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)方法找到或选择其中一个已添加自定义XML部件。还请查看下面给出的代码的控制台输出以供参考。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-AddCustomXMLPartsAndSelectThemByID.cs" >}}

## **控制台输出**

{{< highlight java >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}
