---
title : "Returning a Range of Values using ICustomFunction" 
description : "" 
weight : 12493 
toc : false
type: docs
url: /java/developerguide/technicalarticles/returning+a+range+of+values+using+icustomfunction/
---

# Aspose.Cells for Java : Returning a Range of Values using ICustomFunction


Aspose.Cells provides [ICustomFunction](https://apireference.aspose.com/cells/java/com.aspose.cells/ICustomFunction) interface which is used to implement user-defined or custom functions that are not supported by Microsoft Excel as built-in functions.

Mostly when you implement the [ICustomFunction](https://apireference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)interface method, you need to return a single cell value. But sometimes, you need to return a range of values. This article will explain how to return the range of values from [ICustomFunction](https://apireference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

#### Returning a Range of Values using ICustomFunction

The following code implements [ICustomFunction](https://apireference.aspose.com/cells/java/com.aspose.cells/ICustomFunction)and returns the range of values via its method. Please check the [output excel file](https://docs2.aspose.com/cells/java/attachments/5276466/5472922.xlsx) and [pdf](https://docs2.aspose.com/cells/java/attachments/5276466/5472925.pdf) generated with the code for your reference.

Create a class with a function *CalculateCustomFunction*. This class implements [ICustomFunction](https://apireference.aspose.com/cells/java/com.aspose.cells/ICustomFunction).

Now use the above function into your program.

