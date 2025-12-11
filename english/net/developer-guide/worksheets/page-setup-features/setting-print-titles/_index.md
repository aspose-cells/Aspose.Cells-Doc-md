---
title: How to Set Print Titles
type: docs
weight: 200
url: /net/how-to-set-print-titles/
description: This article provides code demonstrating how to set print titles using the Aspose.Cells library.
keywords: Print rows and columns repeatedly, C# How to Set Print Titles, Set and Clear Print Titles using C#, How to Clear Print Titles in C#, How to Add Print Titles using C#, How to Remove Print Titles using C#, How to Set Print Titles in Excel, How to Clear Print Titles in Excel.
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**

Setting print titles in Excel ensures that specific rows or columns are repeated on every printed page, which is especially useful for large spreadsheets that span multiple pages. Here are some reasons why you might set print titles:

1. **Enhanced Readability:** Print titles help readers understand the data by keeping headers visible on all pages, making it easier to interpret the information on each page without having to refer back to the first page.

2. **Professional Presentation:** Consistently displaying headers or labels on each page creates a more polished and professional appearance for printed documents.

3. **Improved Navigation:** For documents with extensive data, repeating the headers on each page allows for quicker navigation and reference, reducing the need to flip back and forth between pages.

4. **Reduced Errors:** When headers are present on every page, it minimizes the chances of misinterpretation or data entry errors, as users can easily see the context of the data.

5. **Consistency:** Ensuring that important information, such as column headers or row labels, is always visible maintains consistency and clarity throughout the document.

## **How to Set Print Titles in Excel**

To set print titles in Excel, follow these steps:

1. **Open the Page Layout Tab:** Click on the “Page Layout” tab in the ribbon at the top of the Excel window.  
2. **Access Print Titles:** In the “Page Setup” group, click on “Print Titles”.  
3. **Set Rows to Repeat:** In the “Page Setup” dialog box, go to the “Sheet” tab. In the “Print titles” section, specify the rows to repeat at the top by clicking the box next to “Rows to repeat at top” and selecting the row(s) you want to repeat.  
4. **Set Columns to Repeat (if needed):** Similarly, you can specify the columns to repeat at the left by clicking the box next to “Columns to repeat at left” and selecting the column(s) you want to repeat.  
   <br>
   <img src="3.png" width=60% />
5. **Confirm and Print:** Click “OK” to apply the settings. When you print the worksheet, the specified rows or columns will appear on every printed page.

## **How to Clear Print Titles in Excel**

To clear print titles in Excel, you need to remove the rows or columns that are set to repeat on every printed page. Here’s how to do it:

1. **Open the Page Layout Tab:** Click on the “Page Layout” tab in the ribbon at the top of the Excel window.  
2. **Access Print Titles:** In the “Page Setup” group, click on “Print Titles”.  
3. **Clear Print Titles:** In the “Page Setup” dialog box, go to the “Sheet” tab. Clear the text boxes for “Rows to repeat at top” and “Columns to repeat at left” by deleting any content inside them.  
   <br>
   <img src="4.png" width=60% />
4. **Confirm and Close:** Click “OK” to apply the changes.

## **How to Set Print Titles Using Aspose.Cells**

To set print titles in a specified worksheet, first load the [sample file](input.xlsx), then modify the **Worksheet.PageSetup.PrintTitleRows** and **Worksheet.PageSetup.PrintTitleColumns** properties of the **PageSetup** object for the desired worksheet. Setting these properties to a range string will set the print titles.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-set-print-titles.cs" >}}

The output result:  
<br>
<img src="1.png" width=60% />

## **How to Clear Print Titles Using Aspose.Cells**

To clear the print titles in a specified worksheet, first load the [sample file](input.xlsx), then modify the **Worksheet.PageSetup.PrintTitleRows** and **Worksheet.PageSetup.PrintTitleColumns** properties of the **PageSetup** object for the desired worksheet. Setting these properties to an empty string will clear the print titles.

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Worksheets-PageSetup-clear-print-titles.cs" >}}

The output result:  
<br>
<img src="2.png" width=60% />
{{< app/cells/assistant language="csharp" >}}
