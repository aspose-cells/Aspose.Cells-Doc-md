---
title: Generate Conditional Formatting DataBars Images with Golang via C++
linktitle: Generate Conditional Formatting DataBars Images
description: Aspose.Cells is a C++ library for working with spreadsheet files. It supports the generation of conditionally formatted data bars and images, allowing users to customize the display of the spreadsheet based on the value of the cells. This article will introduce how to use the Aspose.Cells library to generate conditionally formatted data bars and images.
keywords: Aspose.Cells, Conditional Formatting, Data Bars, Images, Spreadsheets
type: docs
weight: 40
url: /go-cpp/generate-conditional-formatting-databars-images/
---

{{% alert color="primary" %}}

Sometimes, you need to generate images of Conditional Formatting DataBars. You can use Aspose.Cells [**DataBar.ToImage()**](https://reference.aspose.com/cells/go-cpp/databar/toimage/) method to generate these images. This article shows how to generate a DataBar image using Aspose.Cells.

{{% /alert %}}

The following sample code generates the DataBar image for cell C1. First, it accesses the format condition object of the cell, and then, from that object, accesses the [**DataBar**](https://reference.aspose.com/cells/go-cpp/databar/) object and uses its [**ToImage()**](https://reference.aspose.com/cells/go-cpp/databar/toimage/) method to generate the image of the cell. Finally, it saves the image to disk.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GenerateConditionalFormattingDatabarsImages.go" >}}