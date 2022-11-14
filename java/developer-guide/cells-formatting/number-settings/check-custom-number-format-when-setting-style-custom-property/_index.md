---
title: Check Custom Number Format when Setting Style.Custom Property
type: docs
weight: 160
url: /java/check-custom-number-format-when-setting-style-custom-property/
---

## **Possible Usage Scenarios**

If you assign invalid custom number format to [**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) property then Aspose.Cells will not throw any exception. But if you want that Aspose.Cells should check if the assigned custom number format is valid or not then please set the [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) property to **true**.

## **Check the Custom Number Format when setting Style.Custom property**

The following sample code assigns an invalid custom number format to [**Style.Custom**](https://reference.aspose.com/cells/java/com.aspose.cells/style#Custom) property. Since we have already set [**Workbook.Settings.CheckCustomNumberFormat**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) property to **true**, therefore the API will throw  CellsException e.g. *Invalid number format*.

## **Sample Code**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-data-CheckCustomNumberFormat-CheckCustomNumberFormat.java" >}}
