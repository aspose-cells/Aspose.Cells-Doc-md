---
title: How to Print Excel as Fitted Pages Wide and Tall
type: docs
weight: 200
url: /net/how-to-print-excel-as-fitted-pages-wide-and-tall/
description: This article shows you code explaining how to set FitToPagesWide and FitToPagesTall using the Aspose.Cells library.
keywords: C# How to Set FitToPagesWide and FitToPagesTall, How to add FitToPagesWide and FitToPagesTall in C#, How to Set FitToPagesWide and FitToPagesTall in Excel, How to Clear FitToPagesWide and FitToPagesTall in Excel, How to Print Excel as Fitted Pages Wide and Tall, How to Print Worksheet as One Page, How to Print All Columns of Worksheet in One Page.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Introduction**

The FitToPagesWide and FitToPagesTall settings are used in spreadsheet applications (like Microsoft Excel) to control how a spreadsheet is scaled when printing. These settings help ensure that your printed output fits within a specified number of pages, both horizontally and vertically. Here's a breakdown of each setting:

1. **FitToPagesWide**: This setting specifies the number of pages wide that the printed output should fit into. For example, setting FitToPagesWide to 1 means the content will be scaled to fit within a single page width, no matter how wide the spreadsheet is.  
2. **FitToPagesTall**: This setting specifies the number of pages tall that the printed output should fit into. For example, setting FitToPagesTall to 1 means the content will be scaled to fit within a single page height, regardless of the number of rows.

## **Why Use FitToPagesWide and FitToPagesTall**
Here are some reasons to set FitToPagesWide and FitToPagesTall:

1. **Control Over Printed Layout**: By specifying the number of pages wide and tall, you can ensure that your printed document is easy to read and well‑organized, without any columns or rows being split awkwardly across pages.  
2. **Consistency**: If you're printing multiple sheets or reports, using these settings helps maintain a consistent format, making it easier to compare and analyze printed documents.  
3. **Professional Presentation**: Properly scaling and fitting content to a specified number of pages can result in a more professional and polished presentation of your data.

## **How to Print File as Fitted Pages Wide and Tall in Excel**

To set the FitToPagesWide and FitToPagesTall settings in Microsoft Excel, follow these steps:

1. Open your Excel workbook and go to the sheet you want to print.  
2. Go to the **Page Layout** tab on the Ribbon.  
3. In the **Page Setup** group, click the small arrow in the bottom‑right corner to open the Page Setup dialog box.  
4. In the Page Setup dialog box, go to the **Page** tab.  
5. Under **Scaling**, select the option **Fit to** and then specify the number of pages wide and tall you want:  
   * Enter the number of pages wide you want in the first box (Fit to x pages wide).  
   * Enter the number of pages tall you want in the second box (Fit to y pages tall).  

<br>
<img src="2.png" width=60% />

6. Click **OK** to apply the settings.

## **How to Print Excel as Fitted Pages Wide and Tall Using Aspose.Cells**

To set FitToPagesWide and FitToPagesTall in a specific worksheet, first load the [sample file](input.xlsx), then modify the  
[**Worksheet.PageSetup.FitToPagesTall**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/fittopagestall/) and  
[**Worksheet.PageSetup.FitToPagesWide**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/fittopageswide/) properties of the [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/) object for the desired worksheet. Here is an example in C#:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-set-FitToPagesWide-FitToPagesTall.cs" >}}

The output:

<br>
<img src="1.png" width=60% />

## **How to Print Worksheet as One Page Using Aspose.Cells**

To print a worksheet as one page, first load the [sample file](sample.xlsx), then set the [**PdfSaveOptions.OnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/onepagepersheet/) property of the [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/) object. Here is an example in C#:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-OnePagePerSheet.cs" >}}

The output:

<br>
<img src="3.png" width=60% />

## **How to Print All Columns of Worksheet in One Page Using Aspose.Cells**

To print all columns of a worksheet on one page, first load the [sample file](sample.xlsx), then set the [**PdfSaveOptions.AllColumnsInOnePagePerSheet**](https://reference.aspose.com/cells/net/aspose.cells/paginatedsaveoptions/allcolumnsinonepagepersheet/) property of the [**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/) object. Here is an example in C#:

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-AllColumnsInOnePagePerSheet.cs" >}}

The output:

<br>
<img src="4.png" width=60% />
{{< app/cells/assistant language="csharp" >}}
