---
title : "Check Custom Number Format when Setting Style.Custom Property" 
description : "" 
weight : 16406 
toc : false
type: docs
url: /java/developerguide/technicalarticles/stl-dtfmt/check+custom+number+format+when+setting+style.custom+property/
---

# Aspose.Cells for Java : Check Custom Number Format when Setting Style.Custom Property


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Check the Custom Number Format when setting Style.Custom property](#check-the-custom-number-format-when-setting-style.custom-property)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

 

## Possible Usage Scenarios

If you assign invalid custom number format to [Style.Custom](https://apireference.aspose.com/java/cells/com.aspose.cells/style#Custom) property then Aspose.Cells will not throw any exception. But if you want that Aspose.Cells should check if the assigned custom number format is valid or not then please set the [Workbook.Settings.CheckCustomNumberFormat](https://apireference.aspose.com/java/cells/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) property to **true**.

## Check the Custom Number Format when setting Style.Custom property

The following sample code assigns an invalid custom number format to [Style.Custom](https://apireference.aspose.com/java/cells/com.aspose.cells/style#Custom) property. Since we have already set [Workbook.Settings.CheckCustomNumberFormat](https://apireference.aspose.com/java/cells/com.aspose.cells/workbooksettings#CheckCustomNumberFormat) property to **true**, therefore the API will throw  CellsException e.g. *Invalid number format*. 

## Sample Code

