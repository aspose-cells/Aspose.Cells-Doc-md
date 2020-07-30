---
title : "Implement Errors and Boolean Value in Russian or Any Other Language" 
description : "" 
weight : 12117 
toc : false
type: docs
url: /java/developerguide/workbooksettings/implement+errors+and+boolean+value+in+russian+or+any+other+language/
---

# Aspose.Cells for Java : Implement Errors and Boolean Value in Russian or Any Other Language


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Implement Errors and Boolean Value in Russian or Any Other Language](#implement-errors-and-boolean-value-in-russian-or-any-other-language)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

## Possible Usage Scenarios

If you are using Microsoft Excel in Russian Locale or Language or any other Locale or Language, it will display Errors and Boolean values according to that Locale or Language. You can achieve similar behavior by using Aspose.Cells [Workbook.getSettings().setGlobalizationSettings()](https://apireference.aspose.com/java/cells/com.aspose.cells/workbooksettings#GlobalizationSettings) method or property. You will have to override the following methods of [GlobalizationSettings](https://apireference.aspose.com/java/cells/com.aspose.cells/GlobalizationSettings) class.

*   [GlobalizationSettings.getErrorValueString()](https://apireference.aspose.com/java/cells/com.aspose.cells/globalizationsettings#getErrorValueString(java.lang.String))
*   [GlobalizationSettings.getBooleanValueString()](https://apireference.aspose.com/java/cells/com.aspose.cells/globalizationsettings#getBooleanValueString(boolean))

## Implement Errors and Boolean Value in Russian or Any Other Language

The following sample code illustrates how to implement Errors and Boolean Value in Russian or Any Other Language. Please check the Sample Excel File used in this code and its Output PDF. The screenshot shows the difference between [Sample Excel File](https://docs2.aspose.com/cells/java/attachments/48136897/48496697.xlsx) and the [Output PDF](https://docs2.aspose.com/cells/java/attachments/48136897/48496696.pdf) for a reference.

![](https://docs2.aspose.com/cells/java/attachments/48136897/48496698.png)

## Sample Code

## Attachments:

![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [outputRussianGlobalization.pdf](https://docs2.aspose.com/cells/java/attachments/48136897/48496696.pdf) (application/pdf)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [sampleRussianGlobalization.xlsx](https://docs2.aspose.com/cells/java/attachments/48136897/48496697.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/java/images/icons/bullet_blue.gif) [Implement-Errors-and-Boolean-Value-in-Russian-or-Any-Other-Language.png](https://docs2.aspose.com/cells/java/attachments/48136897/48496698.png) (image/png)  

