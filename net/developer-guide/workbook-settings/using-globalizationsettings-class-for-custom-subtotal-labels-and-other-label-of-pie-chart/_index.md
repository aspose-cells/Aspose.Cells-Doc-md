---
title: Using GlobalizationSettings Class for Custom Subtotal Labels and Other Label of Pie Chart
type: docs
weight: 70
url: /net/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
---

## **Possible Usage Scenarios**
Aspose.Cells APIs have exposed the [GlobalizationSettings](https://apireference.aspose.com/net/cells/aspose.cells/globalizationsettings) class in order to deal with the scenarios where the user wishes to use custom labels for Subtotals in a spreadsheet. Moreover, the [GlobalizationSettings](https://apireference.aspose.com/net/cells/aspose.cells/globalizationsettings) class can also be used to modify the **Other** label for the Pie chart while rendering worksheet or chart.
## **Introduction to GlobalizationSettings Class**
The [GlobalizationSettings](https://apireference.aspose.com/net/cells/aspose.cells/globalizationsettings) class currently offers the following 3 methods which can be overridden in a custom class to get desired labels for the Subtotals or to render custom text for the **Other** label of a Pie chart.

1. [GlobalizationSettings.GetTotalName](https://apireference.aspose.com/net/cells/aspose.cells/globalizationsettings/methods/gettotalname): Gets the total name of the function.
1. [GlobalizationSettings.GetGrandTotalName](https://apireference.aspose.com/net/cells/aspose.cells/globalizationsettings/methods/getgrandtotalname): Gets the grand total name of the function.
1. [GlobalizationSettings.GetOtherName](https://apireference.aspose.com/net/cells/aspose.cells/globalizationsettings/methods/getothername): Gets the name of "Other" labels for Pie charts.
### **Custom Labels for Subtotals**
The [GlobalizationSettings](https://apireference.aspose.com/net/cells/aspose.cells/globalizationsettings) class can be used to customize the Subtotal labels by overriding the [GlobalizationSettings.GetTotalName](https://apireference.aspose.com/net/cells/aspose.cells/globalizationsettings/methods/gettotalname) & [GlobalizationSettings.GetGrandTotalName](https://apireference.aspose.com/net/cells/aspose.cells/globalizationsettings/methods/getgrandtotalname) methods as demonstrated ahead.

{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-CustomLabelsSubtotals-GlobalizationSettings.cs" >}}


In order to inject custom labels, it is required to assign the [WorkbookSettings.GlobalizationSettings](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/globalizationsettings) property to an instance of the **CustomSettings** class defined above before adding the Subtotals to the worksheet.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-CustomLabelsSubtotals-UsingGlobalizationSettings.cs" >}}

{{% alert color="primary" %}} 

The [GlobalizationSettings](https://apireference.aspose.com/net/cells/aspose.cells/globalizationsettings) class only works for adding new Subtotals. If a spreadsheet already contains Subtotals, their labels cannot be modified.

{{% /alert %}} 
### **Custom Text for Other Label of Pie Chart**
The [GlobalizationSettings](https://apireference.aspose.com/net/cells/aspose.cells/globalizationsettings) class offers [GetOtherName](https://apireference.aspose.com/net/cells/aspose.cells/globalizationsettings/methods/getothername) method which is useful to give the "Other" label of Pie charts a custom value. The following snippet defines a custom class and overrides the [GetOtherName](https://apireference.aspose.com/net/cells/aspose.cells/globalizationsettings/methods/getothername) method to get a custom label based on the system's culture identifier.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-CustomTextForLabels-GlobalizationSettings.cs" >}}


The following snippet loads an existing spreadsheet containing a Pie chart and renders the chart to an image while utilizing the **CustomSettings** class created above.



{{< gist "aspose-com-gists" "24a8eac23c3325e20dababecf735a43b" "Examples-CSharp-Articles-CustomTextForLabels-UsingGlobalizationSettings.cs" >}}
