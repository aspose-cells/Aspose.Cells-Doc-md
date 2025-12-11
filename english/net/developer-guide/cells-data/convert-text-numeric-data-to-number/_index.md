---
title: Convert Text Numeric Data to Number
type: docs
weight: 900
url: /net/convert-text-numeric-data-to-number/
description: Learn how to convert numbers stored as text in Excel to numbers by using the Aspose.Cells for .NET API.
keywords: excel convert text to number, excel convert text to number c#, excel convert text numeric data to number, excel convert text numeric data to number c#, excel convert numeric text to number, excel convert numeric text to number c#, excel convert numeric text to number with c#, convert numeric text to number in excel with c#, convert numeric text to number in excel with c#, convert numeric string to number in excel with c#, excel convert text numeric data to number c#, excel convert numeric string to number c#
ai_search_scope: cells_net
ai_search_endpoint: "https://docsearch.api.aspose.cloud/ask"
---

## **Possible Usage Scenarios**
Sometimes, you want to convert numeric data entered as text to numbers. You can enter numbers as text in Microsoft Excel by putting an apostrophe before a number, for example **'12345**. Excel then treats the number as a string. Aspose.Cells allows you to convert strings to numbers.

## How to Convert numbers stored as text to numbers in Excel
You can convert numbers stored as text to numbers by following a few simple steps.

1. Select any single cell or range of cells that has an error indicator in the upper‑left corner.  
2. Next to the selected cell or range of cells, click the error button that appears. On the menu, click **Convert to Number**.  
3. If the error button is not available, select a column with this problem. If you don't want to convert the whole column, you can select one or more cells instead. Just be sure the cells you select are in the same column; otherwise, this process won't work. The **Text to Columns** button is typically used for splitting a column, but it can also be used to convert a single column of text to numbers. On the **Data** tab, click **Text to Columns**.  
4. Click the **Finish** button in the pop‑up box.  
5. The numbers stored as text are transformed into numbers.

<br>
<img src="4.png" width=70% />
<br>
<img src="1.png" width=70% />
<br>
<img src="2.png" width=70% />
<br>
<img src="3.png" width=70% />

## How to Convert numbers stored as text to numbers using Aspose.Cells for .NET
Aspose.Cells provides the [**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue) method, which can be used to convert all string or text numeric data into numbers.

The following screenshot shows string numbers in cells **A1:A17**. String numbers are aligned to the left.  
<br>
<img src="5.png" width=70% />

These string numbers have been converted to numbers using [**Cells.ConvertStringToNumericValue()**](https://reference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue) in the following screenshot. As you can see, they are now right‑aligned.  
<br>
<img src="6.png" width=70% />

## C# code to convert string numeric data to actual numbers

The following sample code illustrates how to convert all string numeric data to actual numbers in all worksheets.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.cs" >}}
{{< app/cells/assistant language="csharp" >}}
