---
title: Using GlobalizationSettings Class for Custom Subtotal Labels and the “Other” Label of a Pie Chart with Golang via C++
linktitle: Using GlobalizationSettings Class
type: docs
weight: 70
url: /go-cpp/using-globalizationsettings-class-for-custom-subtotal-labels-and-other-label-of-pie-chart/
description: Learn how to use the GlobalizationSettings class in Aspose.Cells for Go via C++ to customize subtotal labels and modify the “Other” label in pie charts.
---

## **Possible Usage Scenarios**

Aspose.Cells APIs have exposed the [**GlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/) class in order to deal with scenarios where the user wishes to use custom labels for subtotals in a spreadsheet. Moreover, the [**GlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/) class can also be used to modify the **Other** label for a pie chart while rendering a worksheet or chart.

## **Introduction to GlobalizationSettings Class**

The [**GlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/) class currently offers the following three methods, which can be overridden in a custom class to obtain desired labels for the subtotals or to render custom text for the **Other** label of a pie chart.

1. [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/gettotalname/): Gets the total name.
2. [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/getgrandtotalname/): Gets the grand total name.

### **Custom Labels for Subtotals**

The [**GlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/) class can be used to customize subtotal labels by overriding the [**GlobalizationSettings.GetTotalName**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/gettotalname/) & [**GlobalizationSettings.GetGrandTotalName**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/getgrandtotalname/) methods, as demonstrated below.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UsingGlobalizationsettingsClassForCustomSubtotalLabelsAndOtherLabelOfPieChart.go" >}}

In order to inject custom labels, you must assign the `WorkbookSettings.GetGlobalizationSettings()` property to an instance of the **CustomSettings** class defined above before adding the subtotals to the worksheet.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UsingGlobalizationsettingsClassForCustomSubtotalLabelsAndOtherLabelOfPieChart-1.go" >}}

{{% alert color="primary" %}}

The [**GlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/globalizationsettings/) class only works for adding new subtotals. If a spreadsheet already contains subtotals, their labels cannot be modified.

{{% /alert %}}

### **Custom Text for the “Other” Label of a Pie Chart**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UsingGlobalizationsettingsClassForCustomSubtotalLabelsAndOtherLabelOfPieChart-2.go" >}}

The following snippet loads an existing spreadsheet containing a pie chart and renders the chart to an image while utilizing the **GlobalCustomSettings** class created above.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UsingGlobalizationsettingsClassForCustomSubtotalLabelsAndOtherLabelOfPieChart-3.go" >}}
{{< app/cells/assistant language="go" >}}
