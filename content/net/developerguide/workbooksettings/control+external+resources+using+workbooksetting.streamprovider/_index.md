---
title : "Control External Resources using WorkbookSetting.StreamProvider" 
description : "" 
weight : 12132 
toc : false
type: docs
url: /net/developerguide/workbooksettings/control+external+resources+using+workbooksetting.streamprovider/
---

# Aspose.Cells for .NET : Control External Resources using WorkbookSetting.StreamProvider


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#possible-usage-scenarios)
*   2 [Control External Resources using WorkbookSetting.StreamProvider](#control-external-resources-using-workbooksetting.streamprovider)
*   3 [Sample Code](#sample-code)
{{< /panel >}}
 

## Possible Usage Scenarios

Sometimes, your Excel file contains external resources e.g. linked images etc. Aspose.Cells allows you to control these external resources using [Workbook.Settings.StreamProvider](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/streamprovider) which takes the implementation of [IStreamProvider](https://apireference.aspose.com/net/cells/aspose.cells/istreamprovider) interface. Whenever you will try to render your worksheet containing external resources e.g. linked images, the methods of [IStreamProvider](https://apireference.aspose.com/net/cells/aspose.cells/istreamprovider) interface will be invoked which will enable you to take appropriate actions for your external resources.

## Control External Resources using WorkbookSetting.StreamProvider

The following sample code explains the usage of [Workbook.Settings.StreamProvider](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/streamprovider). It loads the [sample Excel file](https://docs2.aspose.com/cells/net/attachments/61542354/61767863.xlsx) containing a linked image. The code replaces the linked image with [Aspose Logo](https://docs2.aspose.com/cells/net/attachments/61542354/61767862.png) and renders the entire sheet into a single image using [SheetRender](https://apireference.aspose.com/net/cells/aspose.cells.rendering/sheetrender) class. The following screenshot shows the sample Excel file and its [rendered output image](https://docs2.aspose.com/cells/net/attachments/61542354/61767865.png) for a reference. As you can see, the broken linked image is replaced with Aspose Logo.

![image](https://docs2.aspose.com/cells/net/attachments/61542354/61767864.png)  

## Sample Code

