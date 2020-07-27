+++
title = "Control External Resources using WorkbookSetting.StreamProvider" 
description = "" 
weight = 12132 
+++

Aspose.Cells for .NET : Control External Resources using WorkbookSetting.StreamProvider  

# Aspose.Cells for .NET : Control External Resources using WorkbookSetting.StreamProvider


{{< panel title="Contents Summary" style="primary" >}}
*   1 [Possible Usage Scenarios](#ControlExternalResourcesusingWorkbookSetting.StreamProvider-PossibleUsageScenarios)
*   2 [Control External Resources using WorkbookSetting.StreamProvider](#ControlExternalResourcesusingWorkbookSetting.StreamProvider-ControlExternalResourcesusingWorkbookSetting.StreamProvider)
*   3 [Sample Code](#ControlExternalResourcesusingWorkbookSetting.StreamProvider-SampleCode)
{{< /panel >}}
 

## Possible Usage Scenarios

Sometimes, your Excel file contains external resources e.g. linked images etc. Aspose.Cells allows you to control these external resources using [Workbook.Settings.StreamProvider](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/streamprovider) which takes the implementation of [IStreamProvider](https://apireference.aspose.com/net/cells/aspose.cells/istreamprovider) interface. Whenever you will try to render your worksheet containing external resources e.g. linked images, the methods of [IStreamProvider](https://apireference.aspose.com/net/cells/aspose.cells/istreamprovider) interface will be invoked which will enable you to take appropriate actions for your external resources.

## Control External Resources using WorkbookSetting.StreamProvider

The following sample code explains the usage of [Workbook.Settings.StreamProvider](https://apireference.aspose.com/net/cells/aspose.cells/workbooksettings/properties/streamprovider). It loads the [sample Excel file](https://docs2.aspose.com/cells/net/attachments/61542354/61767863.xlsx) containing a linked image. The code replaces the linked image with [Aspose Logo](https://docs2.aspose.com/cells/net/attachments/61542354/61767862.png) and renders the entire sheet into a single image using [SheetRender](https://apireference.aspose.com/net/cells/aspose.cells.rendering/sheetrender) class. The following screenshot shows the sample Excel file and its [rendered output image](https://docs2.aspose.com/cells/net/attachments/61542354/61767865.png) for a reference. As you can see, the broken linked image is replaced with Aspose Logo.

![](https://docs2.aspose.com/cells/net/attachments/61542354/61767864.png)  

## Sample Code

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [sampleLogo\_WorkbookSetting\_StreamProvider.png](https://docs2.aspose.com/cells/net/attachments/61542354/61767862.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Control-External-Resources-using-WorkbookSetting.StreamProvider.png](https://docs2.aspose.com/cells/net/attachments/61542354/61767864.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [sampleControlExternalResourcesUsingWorkbookSettingStreamProvider.xlsx](https://docs2.aspose.com/cells/net/attachments/61542354/61767863.xlsx) (application/vnd.openxmlformats-officedocument.spreadsheetml.sheet)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [outputControlExternalResourcesUsingWorkbookSettingStreamProvider.png](https://docs2.aspose.com/cells/net/attachments/61542354/61767865.png) (image/png)  

