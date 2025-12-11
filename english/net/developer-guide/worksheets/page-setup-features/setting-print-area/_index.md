---
title: How to Set Print Area
type: docs
weight: 200
url: /net/how-to-set-print-area/
description: This article shows code explaining how to set the print area using the Aspose.Cells library.
keywords: Limit printing range, Set Print Range, Clear Print Range, Set and Clear Print Range using C#, C# How to Set Print Area, Set and Clear Print Area using C#, How to Clear Print Area in C#, How to Add Print Area using C#, How to Remove Print Area using C#, How to Set Print Area in Excel, How to Clear Print Area in Excel.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Setting a print area in a document, such as an Excel spreadsheet, helps control what content is included when printing. Here are some reasons to set a print area:

1. **Focus on Specific Data:** You can print only the most relevant sections, avoiding unnecessary content.  
2. **Improved Layout:** It helps in organizing and fitting the content neatly on the printed pages, avoiding splits or unwanted page breaks.  
3. **Save Resources:** By limiting the print area, you can reduce the amount of paper and ink used.  
4. **Professional Presentation:** It ensures that only the polished and final version of data is printed, which is particularly important for reports or presentations.  
5. **Consistency:** When printing the same document multiple times, having a set print area ensures consistency in the output.  

<br>
Setting a print area is especially useful in larger documents where only a portion needs to be shared or reviewed in printed form.

## **How to Set Print Area in Excel**

To set a print area in Excel, follow these steps:

1. **Select the Cells:** Click and drag to select the range of cells you want to set as the print area.  
2. **Open the Page Layout Tab:** Go to the **Page Layout** tab in the ribbon at the top of the Excel window.  
3. **Set Print Area:** In the **Page Setup** group, click **Print Area**. From the drop‑down menu, select **Set Print Area**.  
   <br>
   <img src="3.png" width=60% />
4. **Add to the Print Area:** If you want to add more cells to the existing print area, select the additional cells, go to **Print Area** in the **Page Layout** tab, and choose **Add to Print Area**.  

<br>
This action will define the selected cells as the print area. When you print the worksheet, only this defined area will be printed.

## **How to Clear Print Area in Excel**

To clear the print area in Excel, follow these steps:

1. **Open the Page Layout Tab:** Click on the **Page Layout** tab in the ribbon at the top of the Excel window.  
2. **Clear Print Area:** In the **Page Setup** group, click **Print Area**. From the drop‑down menu, select **Clear Print Area**.  
   <br>
   <img src="4.png" width=60% />

<br>
This action will remove any previously set print area, allowing the entire worksheet to be printed.

## **What Happens After Clearing the Print Area**

Clearing the print area in a spreadsheet application like Excel using Aspose.Cells will result in the entire worksheet being included when you print the document. If a print area is set, only the specified range of cells will be printed. By clearing the print area, you ensure that no specific range is defined, and the default printing behavior— which includes the entire sheet— will take effect.

1. **Default Printing Behavior:** The entire worksheet will be considered for printing. This means all cells with data or formatting will be printed.  
2. **No Print Area Limits:** Previously defined print‑area limits will be removed. If there were specific rows and columns designated for printing, they will no longer be constrained to those limits.  
3. **Full‑Content Print:** All content, including headers, footers, and any other data within the worksheet, will be included in the print job.  

## **How to Set Print Area Using Aspose.Cells**

To set the print area in a specified worksheet: first, load the [sample file](input.xlsx), and then modify the [**Worksheet.PageSetup.PrintArea**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/printarea/) property of the [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/) object for the desired worksheet. Setting this property to a range string will define the print area.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-set-print-area.cs" >}}

The resulting output:
<br>
<img src="1.png" width=60% />

## **How to Clear Print Area Using Aspose.Cells**

To clear the print area in a specified worksheet: first, load the [sample file](input.xlsx), and then modify the [**Worksheet.PageSetup.PrintArea**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/printarea/) property of the [**PageSetup**](https://reference.aspose.com/cells/net/aspose.cells/pagesetup/) object for the desired worksheet. Setting this property to an empty string will clear the print area.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-clear-print-area.cs" >}}

The resulting output:
<br>
<img src="2.png" width=60% />
{{< app/cells/assistant language="csharp" >}}
