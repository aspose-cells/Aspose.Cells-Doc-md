---
title: Convert Text Numeric Data to Number
type: docs
weight: 90
url: /net/convert-text-numeric-data-to-number/
description: Learn how to convert numbers stored as text in Excel to numbers by using the Aspose.Cells for .NET API.
keywords: excel convert text to number, excel convert text to number c#, excel convert text numeric data to number, excel convert text numeric data to number c#, excel convert numeric text to number, excel convert numeric text to number c#, excel convert numeric text to number with c#, convert numeric text to number in excel with c#, convert numeric text to number in excel with c#, convert numeric string to number in excel with c#, excel convert text numeric data to number c#, excel convert numeric string to number c#
---

{{% alert color="primary" %}}

Sometimes, you want to convert numeric data entered as text to numbers. You can enter numbers as text in Microsoft Excel by putting an apostrophe before a number, for example **'12345**. Excel then treats the number as a string. Aspose.Cells allows you to convert strings to numbers.

{{% /alert %}}

Aspose.Cells provides the [**Cells.ConvertStringToNumericValue()**](https://apireference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue) method which can be used to convert all string or text numeric data into numbers.

The following screenshot shows string numbers in cells **A1:A17**. String numbers are aligned to the left.

|**Input file: numbers entered as text strings**|
| :- |
|![todo:image_alt_text](convert-text-numeric-data-to-number_1.png)|

These string numbers have been converted to numbers using [**Cells.ConvertStringToNumericValue()**](https://apireference.aspose.com/cells/net/aspose.cells/cells/methods/convertstringtonumericvalue) in the following screenshot. As you can see, they are now right-aligned.

|**Output file: the strings have been converted to numbers**|
| :- |
|![todo:image_alt_text](convert-text-numeric-data-to-number_2.png)|

## C# code to convert string numeric data to actual numbers

The following sample code illustrates how to convert all string numeric data to actual numbers in all worksheets.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-StylingAndDataFormatting-ConvertStringToNumericValue-ConvertTextNumericDatatoNumber.cs" >}}
