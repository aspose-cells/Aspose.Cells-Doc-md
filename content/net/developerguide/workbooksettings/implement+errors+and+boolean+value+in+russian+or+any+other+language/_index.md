---
title : "Implement Errors and Boolean Value in Russian or Any Other Language" 
description : "" 
weight : 12135 
toc : false
type: docs
url: /net/developerguide/workbooksettings/implement+errors+and+boolean+value+in+russian+or+any+other+language/
---

# Aspose.Cells for .NET : Implement Errors and Boolean Value in Russian or Any Other Language


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Implement Errors and Boolean Value in Russian or Any Other Language](#implement-errors-and-boolean-value-in-russian-or-any-other-language)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

## Possible Usage Scenarios

If you are using Microsoft Excel in Russian Locale or Language or any other Locale or Language, it will display Errors and Boolean values according to that Locale or Language. You can achieve a similar behavior using Aspose.Cells by using the [Workbook.Settings.GlobalizationSettings](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/globalizationsettings) property. You will have to override the following methods of [GlobalizationSettings](https://apireference.aspose.com/net/cells/aspose.cells/globalizationsettings) class.

*   [GlobalizationSettings.GetErrorValueString()](https://apireference.aspose.com/net/cells/aspose.cells/globalizationsettings/methods/geterrorvaluestring)
*   [GlobalizationSettings.GetBooleanValueString()](https://apireference.aspose.com/net/cells/aspose.cells/globalizationsettings/methods/getbooleanvaluestring)

## Implement Errors and Boolean Value in Russian or Any Other Language

The following sample code illustrates how to implement Errors and Boolean Value in Russian or Any Other Language. Please check the [Sample Excel File](https://docs2.aspose.com/cells/net/attachments/48136575/73990159.xlsx) used in this code and its [Output PDF](https://docs2.aspose.com/cells/net/attachments/48136575/73990160.pdf). The screenshot shows the difference between Sample Excel File and the Output PDF for a reference.

![image](https://docs2.aspose.com/cells/net/attachments/48136575/73990161.png)

## Sample Code

