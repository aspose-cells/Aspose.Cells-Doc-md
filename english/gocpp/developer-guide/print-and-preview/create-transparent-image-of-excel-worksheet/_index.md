--- 
title: Create Transparent Image of Excel Worksheet with Golang via C++ 
linktitle: Create Transparent Image of Excel Worksheet 
type: docs 
weight: 170 
url: /go-cpp/create-transparent-image-of-excel-worksheet/ 
description: Generate transparent images of Excel worksheets using Aspose.Cells with Golang via C++. 
--- 

{{% alert color="primary" %}} 

Sometimes, you need to generate an image of your worksheet as a transparent image. You want to apply transparency to all cells that have no fill colors. Aspose.Cells provides the [**ImageOrPrintOptions.GetTransparent()**](https://reference.aspose.com/cells/go-cpp/imageorprintoptions/gettransparent/) property to apply transparency to the worksheet image. When this property is **false**, cells with no fill colors are drawn in white, and when it is **true**, cells with no fill colors are drawn as transparent. 

{{% /alert %}} 

In the following worksheet image, transparency has not been applied. The cells with no fill colors are drawn in white.

|**Output without transparency: the cell background is white**| 
| :- | 
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)| 

While in the following worksheet image, transparency has been applied. The cells with no fill colors are transparent.

|**Output with transparency enabled**| 
| :- | 
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)| 

The following sample code generates a transparent image from an Excel worksheet.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CreateTransparentImageOfExcelWorksheet.go" >}}
{{< app/cells/assistant language="go" >}}
