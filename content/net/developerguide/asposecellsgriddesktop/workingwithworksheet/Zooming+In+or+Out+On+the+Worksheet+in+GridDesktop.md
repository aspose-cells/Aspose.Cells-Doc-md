+++
title = "Zooming In or Out On the Worksheet in GridDesktop" 
description = "" 
weight = 16620 
+++

Aspose.Cells for .NET : Zooming In or Out On the Worksheet in GridDesktop  

# Aspose.Cells for .NET : Zooming In or Out On the Worksheet in GridDesktop


Sometimes, when working with your data, you may want to enlarge the contents on the screen without actually changing the font size. For instance, you may have formatted your text so that it uses a small font. (This is often necessary to get all your information on a printout.) When working in the worksheet, however, the font is difficult to read because it is so small.

In Microsoft Excel, a zoom slider is available for zooming in and out of documents quickly and easily. The zoom slider is usually in the lower right corner of the software window.

Aspose.Cells also allows developers to set the worksheet's zoom factor, so the contents should be appeared as per your desired percentage value.

## Zooming In or Out Using Aspose.Cells.GridDesktop

Aspose.Cells provides Aspose.Cells.GridDesktop.Worksheet class that has a wide range of properties and methods for managing worksheets. To set a worksheet's zoom factor, use the `Worksheet` class' `Zoom` property. The zoom factor is set by assigned a numeric (integer) value to the `Zoom` property.

We build an MS Excel like zoom slider using TrackBar (.NET) control. In a WinForm project, we place the Aspose.Cells.GridDesktop control from Toolbox to the form and specify some properties to set its name, size or other aspects accordingly. Now, we place the TrackBar control @ lower right corner below the GridDesktop control, we also put a Label control that would show the percentage value you specify via TrackBar control's handle. We add relative lines of code in TrackBar's Scroll event, so when you scroll the Trackbar control, GridDesktop should zoom in or out to show the data/ contents in it.

A complete example is given below that demonstrates how to use the `Zoom` property to set the zoom factor of the active worksheet of GridDesktop. We first import a template Excel file to GridDesktop.

Write below code in the `Load` event of form to set the template Excel file in GridDesktop and trackbar value.

  
Now copy below code inside track `scroll` event and run the application. You will notice that moving track bar will change the zoom property of worksheet.

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [zoomslider1.png](https://docs2.aspose.com/cells/net/attachments/5017757/5113822.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [zoomslider2.png](https://docs2.aspose.com/cells/net/attachments/5017757/5113827.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [zoomslider3.png](https://docs2.aspose.com/cells/net/attachments/5017757/5113828.png) (image/png)  

