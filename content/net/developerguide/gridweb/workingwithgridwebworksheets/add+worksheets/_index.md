---
title : "Add Worksheets" 
description : "" 
weight : 16684 
toc : false
type: docs
url: /net/developerguide/gridweb/workingwithgridwebworksheets/add+worksheets/
---

# Aspose.Cells for .NET : Add Worksheets


Worksheets are an integral part of Aspose.Cells.GridWeb. All data is managed and stored in the form of worksheets. Aspose.Cells.GridWeb allows developers to add one or more worksheets to the Aspose.Cells.GridWeb control. This topic shows simple approaches to adding worksheets to Aspose.Cells.GridWeb.

{{< panel title="Contents Summary" style="primary" >}}
*   1 [Adding a Worksheet](#adding-a-worksheet)
    *   1.1 [Without Specifying Sheet Name](#without-specifying-sheet-name)
    *   1.2 [With Specified Sheet Name](#with-specified-sheet-name)
{{< /panel >}}
 

## Adding a Worksheet

### Without Specifying Sheet Name

The simplest way to add a worksheet to Aspose.Cells.GridWeb is to call the `GridWorksheetCollection` collection's `Add` method in the GridWeb control. This creates worksheets that use default names (that is Sheet1, Sheet2, Sheet3 and so on) and adds them to the GridWeb control.

**Output: a worksheet with default name has been added to GridWeb**  
![](https://docs2.aspose.com/cells/net/attachments/5013781/5115348.png)

The `Add` method returns the new worksheet's index which can be used to access the instance of this worksheet. For more details on how to access worksheets, read [Access Worksheets](https://docs2.aspose.com/cells/net/developerguide/gridweb/workingwithgridwebworksheets/access+worksheets).

### With Specified Sheet Name

To add a worksheet with a specific name to the GridWeb control instead of using the default naming scheme, call an overloaded version of the `Add` method that takes the specified `SheetName`. For an instance, the example below adds a worksheet named Invoice.

**Output: a worksheet with a specified name has been added to GridWeb**  
![](https://docs2.aspose.com/cells/net/attachments/5013781/5115347.png)

The `Add` method accepting the worksheet name as string returns an instance of `GridWorksheet`.

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Add Worksheets-001.png](https://docs2.aspose.com/cells/net/attachments/5013781/5115275.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Add Worksheets-002.png](https://docs2.aspose.com/cells/net/attachments/5013781/5115274.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Add Worksheets-001.png](https://docs2.aspose.com/cells/net/attachments/5013781/5115288.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Add Worksheets-002.png](https://docs2.aspose.com/cells/net/attachments/5013781/5115287.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Add Worksheets-001.png](https://docs2.aspose.com/cells/net/attachments/5013781/5115106.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Add Worksheets-002.png](https://docs2.aspose.com/cells/net/attachments/5013781/5115105.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Add Worksheets-001.png](https://docs2.aspose.com/cells/net/attachments/5013781/5115348.png) (image/png)  
![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [Add Worksheets-002.png](https://docs2.aspose.com/cells/net/attachments/5013781/5115347.png) (image/png)  

