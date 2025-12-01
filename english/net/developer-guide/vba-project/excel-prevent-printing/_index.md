---
title: How to Prevent Users from Printing Excel File
type: docs
weight: 600
url: /net/how-to-prevent-printing-excel/
description: Learn how to How to prevent users from printing excel through the Aspose.Cells for .NET API.
keywords: excel printing, prevent printing excel, how to prevent users from printing excel, excel prevent printing, prevent printing workbook, Prevent users from printing the whole workbook with VBA. 
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
In our daily work, there may be some important information in the excel file, in order to protect the internal data outspread, the company will not allow us to print them. This document will tell you how to prevent others from printing Excel files.

## **How to Prevent Users from Printing File in MS-Excel**
You can apply the following VBA code to protect your specific file to be printed.
1. Open your workbook which you don’t allow others to print.
1. Select "Developer" tab tab in the Excel ribbon and Click on the "View Code" button in the "Controls" section. Alternatively, you can hold down the ALT + F11 keys to open the Microsoft Visual Basic for Applications window.
<br>
<img src="1.png" width=70% />
1. And then in the left Project Explorer, double click ThisWorkbook to open the module, and add some vba codes.
<br>
<img src="2.png" width=70% />
1. Then save and close this code, and go to back the workbook, and now when you print the sample file, they will not allowed to be printed and you will get the following warning box:
<br>
<img src="3.png" width=70% />

## **How to Prevent Users from Printing Excel File using Aspose.Cells for .NET**

The following sample code illustrates how to prevent users from printing excel file:

1. Load the [sample file](sample.xlsx).
1. Get the VbaModuleCollection object from VbaProject property of Workbook.
1. Get VbaModule object via "ThisWorkbook" name.
1. Set the codes property of VbaModule.
1. Save the sample file to [xlsm format](out.xlsm).

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "VBA-Prevent-printing-excel.cs" >}}
{{< app/cells/assistant language="csharp" >}}
