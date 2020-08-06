---
title: Convert Text Numeric Data to Number
type: docs
weight: 150
url: /java/convert-text-numeric-data-to-number/
---

{{% alert color="primary" %}} 

Sometimes, you want to convert numeric data entered as text to numbers. You can enter numbers as text in Microsoft Excel by putting an apostrophe before a number, for example **'12345**. Excel then treats the number as a string. Aspose.Cells allows you to convert strings to numbers.

{{% /alert %}} 

Aspose.Cells for Java API provides the [Cells.convertStringToNumericValue()](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#convertStringToNumericValue\(\)) method which can be used to convert all string or text numeric data into numbers.

The following screenshot shows string numbers in cells **A1:A17**. String numbers are aligned to the left.

**Input file: numbers entered as text strings** 

![todo:image_alt_text](convert-text-numeric-data-to-number_1.png)

These string numbers have been converted to numbers using [Cells.convertStringToNumericValue()](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#convertStringToNumericValue\(\)) in the following screenshot. As you can see, they are now right-aligned.

**Output file: the strings have been converted to numbers** 

![todo:image_alt_text](convert-text-numeric-data-to-number_2.png)

The following sample code illustrates how to convert all string numeric data to actual numbers in all worksheets.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-ConvertTextNumericDatatoNumber-ConvertTextNumericDatatoNumber.java" >}}
