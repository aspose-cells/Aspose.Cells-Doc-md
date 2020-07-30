---
title : "Insert a Picture Based on Cell Reference" 
description : "" 
weight : 20482 
toc : false
type: docs
url: /net/developerguide/technicalarticles/general/mngrowscolumnsandcells/insert+a+picture+based+on+cell+reference/
---

# Aspose.Cells for .NET : Insert a Picture Based on Cell Reference


Sometimes you have an empty picture and need to show data or contents in the picture by setting a cell reference in the Formula Bar. Aspose.Cells supports this feature (Microsoft Excel 2010).

## Inserting a Picture Based on Cell Reference

Aspose.Cells supports displaying the contents of a worksheet cell in an image shape. You can link the picture to the cell that contains the data that you want to display. Since the cell or cell range is linked to the graphic object, changes that you make to the data in that cell or cell range automatically appear in the graphic object. Add a picture to the worksheet by calling the [AddPicture](https://apireference.aspose.com/net/cells/aspose.cells.drawing/shapecollection/methods/addpicture/index) method of the [ShapeCollection](https://apireference.aspose.com/net/cells/aspose.cells.drawing/shapecollection) collection (encapsulated in the [Worksheet](https://apireference.aspose.com/net/cells/aspose.cells/worksheet) object). Specify the cell range by using the [Formula](https://apireference.aspose.com/net/cells/aspose.cells.drawing/picture/properties/formula) attribute of the [Picture](https://apireference.aspose.com/net/cells/aspose.cells.drawing/picture) object.

### Code Example

## Attachments:

![](https://docs2.aspose.com/cells/net/images/icons/bullet_blue.gif) [referencedpic.png](https://docs2.aspose.com/cells/net/attachments/5017634/5112279.png) (image/png)  

