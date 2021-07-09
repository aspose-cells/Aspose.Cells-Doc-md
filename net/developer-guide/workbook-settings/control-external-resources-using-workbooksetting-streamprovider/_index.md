---
title: Control External Resources using WorkbookSetting.StreamProvider
type: docs
weight: 10
url: /net/control-external-resources-using-workbooksetting-streamprovider/
---

## **Possible Usage Scenarios**

Sometimes, your Excel file contains external resources e.g. linked images, etc. Aspose.Cells allows you to control these external resources using [**Workbook.Settings.StreamProvider**](https://apireference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider) that takes the implementation of the [**IStreamProvider**](https://apireference.aspose.com/cells/net/aspose.cells/istreamprovider) interface. Whenever you will try to render your worksheet containing external resources e.g. linked images, the methods of the [**IStreamProvider**](https://apireference.aspose.com/cells/net/aspose.cells/istreamprovider) interface will be invoked which will enable you to take appropriate actions for your external resources.

## **Control External Resources using WorkbookSetting.StreamProvider**

The following sample code explains the usage of the [**Workbook.Settings.StreamProvider**](https://apireference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/streamprovider). It loads the [sample Excel file](61767863.xlsx) containing a linked image. The code replaces the linked image with [Aspose Logo](61767862.png) and renders the entire sheet into a single image using [**SheetRender**](https://apireference.aspose.com/cells/net/aspose.cells.rendering/sheetrender) class. The following screenshot shows the sample Excel file and its [rendered output image](61767865.png) for a reference. As you can see, the broken linked image is replaced with Aspose Logo.

![todo:image_alt_text](control-external-resources-using-workbooksetting-streamprovider_1.png)

## **Sample Code**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-WorkbookSettings-ControlExternalResourcesUsingWorkbookSetting_StreamProvider-1.cs" >}}
