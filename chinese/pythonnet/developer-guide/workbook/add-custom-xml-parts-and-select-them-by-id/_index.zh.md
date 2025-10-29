---
title: 添加自定义XML部件并按ID选择
type: docs
weight: 70
url: /zh/python-net/add-custom-xml-parts-and-select-them-by-id/
---

## **可能的使用场景**

自定义XML部分是存储在Microsoft Excel文档中的XML数据，由处理它们的应用程序使用。目前没有直接通过Microsoft Excel界面添加它们的方法。但是，您可以通过多种程序方式添加，例如使用VSTO、使用Aspose.Cells等。如果要使用Aspose.Cells for Python via .NET API添加自定义XML部分，请使用[**Workbook.custom_xml_parts.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes)方法。您也可以使用[**CustomXmlPart.id**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id)属性设置其ID。同样，如果要按ID选择自定义XML部分，可以使用[**Workbook.custom_xml_parts.select_by_id()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str)方法。

## **添加自定义XML部件并按ID选择**

以下示例代码首先使用 [**Workbook.custom_xml_parts.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes) 方法添加了四个自定义 XML 部件。然后使用 [**CustomXmlPart.id**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id) 属性设置它们的 ID。最后，使用 [**Workbook.custom_xml_parts.select_by_id()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str) 方法找到或选择了其中一个添加的自定义 XML 部件。还请参考下面给出的代码的控制台输出。

## **示例代码**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-AddCustomXMLPartsAndSelectThemByID.py" >}}

## **控制台输出**

{{< highlight java >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}

{{< app/cells/assistant language="python-net" >}}
