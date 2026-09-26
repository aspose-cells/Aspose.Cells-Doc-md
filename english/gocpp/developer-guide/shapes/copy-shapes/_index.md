---
title: Copy Shapes between Worksheets with Golang via C++
linktitle: Copy Shapes
type: docs
weight: 200
url: /go-cpp/copy-shapes-between-worksheets/
description: Learn how to copy shapes, charts, and other drawing objects between worksheets using Aspose.Cells with Golang via C++.
---

{{% alert color="primary" %}}

Sometimes, you need to copy elements on a worksheet, for example, pictures, charts, and other drawing objects, between worksheets. Aspose.Cells supports this feature. Charts, images, and other objects can be copied with the highest degree of precision.

This article gives you a detailed understanding of how to copy shapes between worksheets.

{{% /alert %}}

## **Copying a Picture from One Worksheet to Another**

To copy a picture from one worksheet to another, use the [**Worksheet.Pictures.Add**](https://reference.aspose.com/cells/go-cpp/picturecollection/add_int_int_int_int_stream/) method as shown in the sample code below.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyShapes.go" >}}

## **Copy a Chart from One Worksheet to Another**

The following code demonstrates the use of [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/go-cpp/shapecollection/addcopy_shape_int_int_int_int/) method to copy a chart from one worksheet to another.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyShapes-1.go" >}}

## **Copy Controls and Other Drawing Objects from One Worksheet to Another**

To copy controls and other drawing objects, use the [**Worksheet.Shapes.AddCopy**](https://reference.aspose.com/cells/go-cpp/shapecollection/addcopy_shape_int_int_int_int/) method as shown in the example below.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CopyShapes-2.go" >}}
{{< app/cells/assistant language="go" >}}
