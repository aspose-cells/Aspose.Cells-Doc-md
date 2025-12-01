---
title: Insert a Linked Picture from Web Address
type: docs
weight: 450
url: /python-net/insert-a-linked-picture-from-web-address/
ai_search_scope: cells_pythonnet
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

{{% alert color="primary" %}}

Sometimes you need to insert a picture from the web (http://) into a worksheet. To do so, specify the picture’s URL and the picture will be downloaded every time the spreadsheet is opened in Microsoft Excel. The image is not physically embedded into the Excel document, but points to a web resource.

{{% /alert %}}

## **Using Microsoft Excel**

In Microsoft Excel (for example 2007):

1. Click the **Insert** menu and select **Picture**.
1. Specify the web address for the picture in the Insert Picture dialog.

## **Using Aspose.Cells for Python via .NET**

Aspose.Cells for Python via .NET supports adding a linked image using the [**ShapeCollection.add_linked_picture(int upper_left_row, int upper_left_column, int height_pixels, int width_pixels, str source_full_name)**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapecollection/add_linked_picture). The method returns a [**Picture**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/picture) object.

The following example shows how to add linked picture from web address to a worksheet.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-Pictures-InsertLinkedPicture-1.py" >}}
{{< app/cells/assistant language="python-net" >}}
