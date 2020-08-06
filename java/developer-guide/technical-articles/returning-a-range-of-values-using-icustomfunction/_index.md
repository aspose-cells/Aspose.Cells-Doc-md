---
title: Returning a Range of Values using ICustomFunction
type: docs
weight: 270
url: /java/returning-a-range-of-values-using-icustomfunction/
---

{{% alert color="primary" %}} 

Aspose.Cells provides [ICustomFunction](https://apireference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) interface which is used to implement user-defined or custom functions that are not supported by Microsoft Excel as built-in functions.

Mostly when you implement the [ICustomFunction](https://apireference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) interface method, you need to return a single cell value. But sometimes, you need to return a range of values. This article will explain how to return the range of values from [ICustomFunction](https://apireference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{% /alert %}} 
#### **Returning a Range of Values using ICustomFunction**
The following code implements [ICustomFunction](https://apireference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) and returns the range of values via its method. Please check the [output excel file](attachments/5276466/5472922.xlsx) and [pdf](attachments/5276466/5472925.pdf) generated with the code for your reference.

Create a class with a function *CalculateCustomFunction*. This class implements [ICustomFunction](https://apireference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

{{< gist "aspose-com-gists" "439a68a5e4305388c50ca306ef238de5" "Examples-src-AsposeCellsExamples-TechnicalArticles-CustomFunctionStaticValue-CustomFunctionStaticValue.java" >}}

Now use the above function into your program.

{{< gist "aspose-com-gists" "a20e8fa273e7cfa37d032b8211fcf8bf" "Examples-src-main-java-com-aspose-cells-examples-articles-ReturningRangeOfValues-ReturningRangeOfValues.java" >}}
