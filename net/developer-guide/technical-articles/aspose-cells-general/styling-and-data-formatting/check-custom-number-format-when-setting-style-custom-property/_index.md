---
title: Check Custom Number Format when Setting Style.Custom Property
type: docs
weight: 170
url: /net/check-custom-number-format-when-setting-style-custom-property/
---

## **Possible Usage Scenarios**

If you assign invalid custom number format to [**Style.Custom**](https://apireference.aspose.com/cells/net/aspose.cells/style/properties/custom) property, then Aspose.Cells will not throw any exception. But if you want that Aspose.Cells should check if the assigned custom number format is valid or not, then please set the [**Workbook.Settings.CheckCustomNumberFormat**](https://apireference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) property to **true**.

## **Check Custom Number Format when setting Style.Custom property**

The following sample code assigns an invalid custom number format to [**Style.Custom**](https://apireference.aspose.com/cells/net/aspose.cells/style/properties/custom) property. Since, we have already set [**Workbook.Settings.CheckCustomNumberFormat**](https://apireference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/checkcustomnumberformat) property to **true**, therefore it throws exception e.g. Invalid number format. Please read the comments inside the code for more help.

## **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-StylingAndDataFormatting-CheckCustomFormatPattern.cs" >}}
