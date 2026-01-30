---
title: Implement Custom Paper Size of Worksheet for Rendering with Go
linktitle: Implement Custom Paper Size of Worksheet for Rendering
type: docs
weight: 70
url: /gocpp/implement-custom-paper-size-of-worksheet-for-rendering/
description: This article explains how to use the Go API to set custom paper size of your desired worksheets when rendering Excel file to PDF file format programmatically.
keywords: set custom paper size while rendering excel to pdf go
ai_search_scope: cells_cpp
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

There is no direct option available to create custom paper sizes in MS Excel; however, you can set a custom paper size for your desired worksheets when rendering Excel files to the PDF format. This document explains how to set a custom paper size of a worksheet using Aspose.Cells APIs.

## **Implement Custom Paper Size of Worksheet for Rendering**

Aspose.Cells allows you to set your desired paper size for the worksheet. You may use the [**CustomPaperSize**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/custompapersize/) method of the [**PageSetup**](https://reference.aspose.com/cells/cpp/aspose.cells/pagesetup/) class to specify a custom page size. The following sample code illustrates how to specify a custom paper size for the first worksheet in the workbook. Please also see the [output PDF](45056028.pdf) generated with the following code for reference.

## **Screenshot**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ImplementCustomPaperSizeOfWorksheetForRendering.go" >}}