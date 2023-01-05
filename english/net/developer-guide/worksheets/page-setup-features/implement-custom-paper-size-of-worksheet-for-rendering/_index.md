---
title: Implement Custom Paper Size of Worksheet for Rendering
type: docs
weight: 70
url: /net/implement-custom-paper-size-of-worksheet-for-rendering/
description: This article explains how to use the C# API or .NET Library sample code to set custom paper size of your desired worksheets when rendering Excel file to PDF file format programmatically.
keywords: set custom paper size while rendering excel to pdf c#
---

## **Possible Usage Scenarios**

There is no direct option available to create custom paper sizes in MS Excel, however, you can set custom paper size of your desired worksheets when rendering Excel file to PDF file format. This document explains how to set a custom paper size of a worksheet using Aspose.Cells APIs.

## **Implement Custom Paper Size of Worksheet for Rendering**

Aspose.Cells allows you to implement your desired paper size of the worksheet. You may use the [**CustomPaperSize**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/methods/custompapersize) method of the [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) class to specify a custom page size. The following sample code illustrates how to specify a custom paper size for the first worksheet in the workbook. Please also see the [output PDF](45056028.pdf) generated with the following code for a reference.

## **Screenshot**

![todo:image_alt_text](implement-custom-paper-size-of-worksheet-for-rendering_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-Worksheets-PageSetupFeatures-ImplementCustomPaperSizeOfWorksheetForRendering.cs" >}}
