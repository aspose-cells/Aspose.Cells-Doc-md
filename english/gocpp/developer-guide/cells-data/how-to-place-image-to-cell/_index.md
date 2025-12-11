---
title: How to Insert Picture in Cell with Golang via C++
linktitle: How to Insert Picture in Cell
type: docs
weight: 130
url: /go-cpp/how-to-insert-picture-in-cell/
description: Learn how to insert a picture into a cell with Aspose.Cells using C++.
keywords: How to Insert Picture in Cell, Insert Picture over Cells, Place Picture in Cell, Place Picture over Cells, How to place image in cell, How to place image over cells, Switch between Picture in Cell and Picture over Cells, Switch between Place in Cell and Place over Cells.
---

## **Possible Usage Scenarios**
The image adds a touch of brightness to your worksheet and provides a visual representation of the content. It also makes it easier for you to understand the data and come up with insights. Although you have been able to use images in Excel for many years, Excel has only recently enabled the feature of images becoming actual cell values. Even if the layout of the drawing is modified, it will still be attached to the data. You can use it in tables, sorting, filtering, including in formulas, and so on!

## **How to Insert Picture in Cell Using Excel**
To insert a picture into a cell in Excel, follow these steps:

1. Go to the **Insert** tab and click on the **Pictures** option.  
2. Select **Place in Cell**. Choose one of the following sources from the *Insert Picture From* dropdown menu (**This Device**, **Stock Images**, and **Online Pictures**). **This Device** inserts a picture from your device. **Stock Images** inserts a picture from the stock image collection. **Online Pictures** inserts a picture from the web.  
   <br>
   <img src="1.png" width=60% />
3. Select the picture and insert it into a cell.  
   <br>
   <img src="8.png" width=60% />

## **How to Insert Picture over Cells Using Excel**
To insert a picture over cells in Excel, follow these steps:

1. Go to the **Insert** tab and click on the **Pictures** option.  
2. Select **Place over Cells**. Choose one of the following sources from the *Insert Picture From* dropdown menu (**This Device**, **Stock Images**, and **Online Pictures**). **This Device** inserts a picture from your device. **Stock Images** inserts a picture from the stock image collection. **Online Pictures** inserts a picture from the web.  
   <br>
   <img src="2.png" width=60% />
3. Select the picture and insert it over cells.  
   <br>
   <img src="3.png" width=60% />

## **How to Switch from Picture in Cell to Picture over Cells Using Excel**
You can easily switch from **Picture in Cell** to **Picture over Cells**. Please follow these steps:

1. Right‑click on the cell and select **Picture in Cell** > **Place over Cells**.  
   <br>
   <img src="4.png" width=60% />
2. The result after switching is as follows:  
   <br>
   <img src="5.png" width=60% />

## **How to Switch from Picture over Cells to Picture in Cell Using Excel**
You can easily switch from **Picture over Cells** to **Picture in Cell**. Please follow these steps:

1. Right‑click on the picture and select **Place in Cell**.  
   <br>
   <img src="6.png" width=60% />
2. The result after switching is as follows:  
   <br>
   <img src="7.png" width=60% />

## **How to Insert Picture in Cell Using C++**
Insert a picture in a cell using Aspose.Cells. Please see the following sample code. After executing the example code, a picture will be inserted into a cell.

1. Instantiate a `Workbook` object.  
2. Get the cell where you want to insert the picture.  
3. Set the `Cell.EmbeddedImage` property.  
4. Finally, save the workbook in the [output XLSX](out.xlsx) format.  

## **Sample Code**

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-HowToPlaceImageToCell.go" >}}