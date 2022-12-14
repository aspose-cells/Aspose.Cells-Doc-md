---
title: 添加自定义 XML 部件并按 ID 选择它们
type: docs
weight: 70
url: /zh/net/add-custom-xml-parts-and-select-them-by-id/
---
## **可能的使用场景**

自定义 XML 部件是存储在 Microsoft Excel 文档中并由处理它们的应用程序使用的 XML 数据。目前没有使用 Microsoft Excel UI 直接添加它们的方法。但是，您可以通过各种方式以编程方式添加它们，例如使用 VSTO、使用 Aspose.Cells 等。请使用[**工作簿.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add)方法，如果你想使用 Aspose.Cells API 添加自定义 XML 部件。你也可以设置它的 ID，使用[**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id)财产。同样，如果你想通过 ID 选择 Custom XML Part，你可以使用[**工作簿.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)方法。

## **添加自定义 XML 部件并按 ID 选择它们**

以下示例代码首先添加四个自定义 XML 部件，使用[**工作簿.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add)方法。然后它使用设置他们的ID[**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id)财产。最后，它使用以下方法查找或选择添加的自定义 XML 部件之一[**工作簿.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)方法。另请参阅下面给出的代码的控制台输出以供参考。

## **示例代码**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-AddCustomXMLPartsAndSelectThemByID.cs" >}}

## **控制台输出**

{{< highlight "java" >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}
