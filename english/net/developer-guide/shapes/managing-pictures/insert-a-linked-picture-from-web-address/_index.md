---
title: Insert a Linked Picture from Web Address
type: docs
weight: 450
url: /net/insert-a-linked-picture-from-web-address/
---

{{% alert color="primary" %}}

Sometimes you need to insert a picture from the web (http://) into a worksheet. To do so, specify the picture’s URL and the picture will be downloaded every time the spreadsheet is opened in Microsoft Excel. The image is not physically embedded into the Excel document, but points to a web resource.

{{% /alert %}}

## **Using Microsoft Excel**

In Microsoft Excel (for example 2007):

1. Click the **Insert** menu and select **Picture**.
1. Specify the web address for the picture in the Insert Picture dialog.

## **Using Aspose.Cells for .NET**

Aspose.Cells for .NET supports adding a linked image using the [**ShapeCollection.AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, string sourceFullName)**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapecollection/methods/addlinkedpicture). The method returns a [**Picture**](https://reference.aspose.com/cells/net/aspose.cells.drawing/picture) object.

The following example shows how to add linked picture from web address to a worksheet.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-InsertLinkedPicture-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}