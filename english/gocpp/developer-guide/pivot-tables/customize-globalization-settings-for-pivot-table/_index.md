---
title: Customize Globalization Settings for Pivot Table with Golang via C++
linktitle: Customize Globalization Settings for Pivot Table
type: docs
weight: 50
url: /go-cpp/customize-globalization-settings-for-pivot-table/
description: Learn how to customize pivot table globalization settings using Aspose.Cells for C++.
---

## **Possible Usage Scenarios**

Sometimes you want to customize the *Pivot Total, Sub Total, Grand Total, All Items, Multiple Items, Column Labels, Row Labels, Blank Values* text as per your requirements. Aspose.Cells for C++ allows you to customize the globalization settings of the pivot table to deal with such scenarios. You can also use this feature to change the labels to other languages like Arabic, Hindi, Polish, etc.

## **Customize Globalization Settings for Pivot Table**

The following sample code explains how to customize globalization settings for the pivot table in C++. It creates a class *CustomPivotTableGlobalizationSettings* derived from the base class [**PivotGlobalizationSettings**](https://reference.aspose.com/cells/go-cpp/pivotglobalizationsettings/) and overrides all necessary methods. These methods return customized text for various pivot table elements. The code then assigns this implementation to the [**WorkbookSettings.GetPivotSettings()**](https://reference.aspose.com/cells/cpp/aspose.cells/globalizationsettings/getpivotsettings/) property. The example loads a [source Excel file](40468488.xlsx), refreshes pivot data, and saves it as [output PDF](40468487.pdf). The screenshot below shows customized labels in the output.

![todo:image_alt_text](customize-globalization-settings-for-pivot-table_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-CustomizeGlobalizationSettingsForPivotTable.go" >}}