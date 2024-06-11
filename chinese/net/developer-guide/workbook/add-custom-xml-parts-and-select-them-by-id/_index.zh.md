---
title: 添加自定义XML部件并按ID选择
type: docs
weight: 70
url: /zh/net/add-custom-xml-parts-and-select-them-by-id/
---

## **可能的使用场景**

自定义 XML 部件是存储在 Microsoft Excel 文档内部的 XML 数据，并由处理这些数据的应用程序使用。目前还没有直接的方法可以使用 Microsoft Excel UI 添加它们。但是，您可以以各种方式以编程方式添加它们，例如使用 VSTO、使用 Aspose.Cells 等。如果要使用 Aspose.Cells API 添加自定义 XML 部件，请使用 [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add) 方法。您还可以使用 [**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id) 属性设置它的 ID。同样，如果要根据 ID 选择自定义 XML 部件，可以使用 [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid) 方法。

## **添加自定义XML部件并按ID选择**

以下示例代码首先使用 [**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add) 方法添加了四个自定义 XML 部件。然后使用 [**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id) 属性设置它们的 ID。最后，使用 [**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid) 方法找到或选择了其中一个添加的自定义 XML 部件。还请参考下面给出的代码的控制台输出。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-AddCustomXMLPartsAndSelectThemByID.cs" >}}

## **控制台输出**

{{< highlight java >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}
