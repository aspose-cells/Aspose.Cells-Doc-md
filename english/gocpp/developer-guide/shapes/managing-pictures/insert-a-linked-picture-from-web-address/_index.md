---
title: Insert a Linked Picture from Web Address with Golang via C++
linktitle: Insert a Linked Picture from Web Address
type: docs
weight: 450
url: /go-cpp/insert-a-linked-picture-from-web-address/
description: Learn how to insert a linked picture from a web address into a worksheet using Aspose.Cells for C++.
---

{{% alert color="primary" %}}

Sometimes you need to insert a picture from the web (http://) into a worksheet. To do so, specify the picture’s URL, and the picture will be downloaded each time the spreadsheet is opened in Microsoft Excel. The image is not physically embedded in the Excel document, but points to a web resource.

{{% /alert %}}

## **Using Microsoft Excel**

In Microsoft Excel (for example, 2007):

1. Click the **Insert** menu and select **Picture**.
2. Specify the web address for the picture in the Insert Picture dialog.

## **Using Aspose.Cells for C++**

Aspose.Cells for C++ supports adding a linked image using the [**ShapeCollection::AddLinkedPicture(int upperLeftRow, int upperLeftColumn, int heightPixels, int widthPixels, System::String sourceFullName)**](https://reference.aspose.com/cells/go-cpp/shapecollection/addlinkedpicture/) method. The method returns a [**Picture**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/picture/) object.

The following example shows how to add a linked picture from a web address to a worksheet.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-InsertALinkedPictureFromWebAddress.go" >}}