---
title: Get Paper Width and Height of Page Setup of Worksheet with Golang via C++
linktitle: Get Paper Width and Height of Page Setup
type: docs
weight: 50
url: /go-cpp/get-paper-width-and-height-of-page-setup-of-worksheet/
description: Learn how to get the Excel Worksheet Page Setup paper width and paper height using C++ code programmatically with Aspose.Cells for Go via Go API.
keywords: excel page setup paper width c++, excel page setup paper height c++
---

## **Possible Usage Scenarios**

Sometimes, you need to know the width and height of a paper size as set in the page setup of the worksheet. Please use the [**GetPaperWidth()**](https://reference.aspose.com/cells/go-cpp/pagesetup/getpaperwidth/) and [**GetPaperHeight()**](https://reference.aspose.com/cells/go-cpp/pagesetup/getpaperheight/) methods for this purpose.

## **Get Paper Width and Height of Page Setup of Worksheet**

The following sample code demonstrates the usage of [**GetPaperWidth()**](https://reference.aspose.com/cells/go-cpp/pagesetup/getpaperwidth/) and [**GetPaperHeight()**](https://reference.aspose.com/cells/go-cpp/pagesetup/getpaperheight/) methods. It first changes the paper size to *A2* and prints the width and height of the paper, then changes it to *A3*, *A4*, and *Letter*, printing the corresponding dimensions each time.

### **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetPaperWidthAndHeightOfPageSetupOfWorksheet.go" >}}

### **Console Output**

Here is the console output of the above sample code.

{{< highlight go >}}
PaperA2: 16.54x23.39
PaperA3: 11.69x16.54
PaperA4: 8.27x11.69
PaperLetter: 8.5x11
{{< /highlight >}}
