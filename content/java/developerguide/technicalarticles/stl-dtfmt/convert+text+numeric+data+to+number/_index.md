---
title : "Convert Text Numeric Data to Number" 
description : "" 
weight : 16405 
toc : false
type: docs
url: /java/developerguide/technicalarticles/stl-dtfmt/convert+text+numeric+data+to+number/
---

# Aspose.Cells for Java : Convert Text Numeric Data to Number


Sometimes, you want to convert numeric data entered as text to numbers. You can enter numbers as text in Microsoft Excel by putting an apostrophe before a number, for example **'12345**. Excel then treats the number as a string. Aspose.Cells allows you to convert strings to numbers.

Aspose.Cells for Java API provides the [Cells.convertStringToNumericValue()](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#convertStringToNumericValue()) method which can be used to convert all string or text numeric data into numbers.

The following screenshot shows string numbers in cells **A1:A17**. String numbers are aligned to the left.

**Input file: numbers entered as text strings**  
![image](5473023.png)

These string numbers have been converted to numbers using [Cells.convertStringToNumericValue()](https://apireference.aspose.com/java/cells/com.aspose.cells/cells#convertStringToNumericValue()) in the following screenshot. As you can see, they are now right-aligned.

**Output file: the strings have been converted to numbers**  
![image](5473022.png)

The following sample code illustrates how to convert all string numeric data to actual numbers in all worksheets.


