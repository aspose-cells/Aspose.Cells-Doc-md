---
title : "Returning a Range of Values using ICustomFunction" 
description : "" 
weight : 20543 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/calculationengine/returning+a+range+of+values+using+icustomfunction/
---

# Aspose.Cells for .NET : Returning a Range of Values using ICustomFunction


Aspose.Cells provides `ICustomFunction` interface which is used to implement user defined or custom functions that are not supported by Microsoft Excel as built-in functions.

Mostly when you implement `ICustomFunction` interface method, you need to return a single cell value. But sometimes, you need to return a range of values. This article will explain how to return range of values from `ICustomFunction`.

The following code implements `ICustomFunction` and returns the range of values via its method. Please check the [output excel file](https://docs2.aspose.com/cells/net/attachments/5017295/5112352.xlsx) and [pdf](https://docs2.aspose.com/cells/net/attachments/5017295/5112353.pdf) generated with the code for your reference.

Create a class with function `CalculateCustomFunction`. This class implements `ICustomFunction`

  
Now use above function into your program

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [output.pdf](https://docs2.aspose.com/cells/net/attachments/5017295/5112353.pdf) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [output.xlsx](https://docs2.aspose.com/cells/net/attachments/5017295/5112352.xlsx) (image/png)  

