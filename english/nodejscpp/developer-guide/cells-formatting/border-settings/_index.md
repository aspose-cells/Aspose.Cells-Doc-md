---  
title: Border Settings
linktitle: Border Settings  
description: How to use the Aspose.Cells library in Node.js via C++ to set the border style and color of cells. By adjusting the width, style, and color of the border, you have more control over how cells look and appear.  
keywords: Aspose.Cells, Cell Border Settings, Node.js via C++, Border Width, Border Style, Border Color  
type: docs  
weight: 40  
url: /nodejs-cpp/cells-border-settings/  
---  

## **Adding Borders to Cells**  

Microsoft Excel allows users to format cells by adding borders. The type of border depends on where it is added. For example, a top border is one added to the top position of a cell. Users can also modify the borders' line style and color.  

With Aspose.Cells for Node.js via C++, developers can add borders and customize what they look like in the same flexible way as in Microsoft Excel.  

### **Adding Borders to Cells**  

Aspose.Cells provides a class, [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) that represents a Microsoft Excel file. The [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) class contains a [**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) collection that allows access to each worksheet in the Excel file. A worksheet is represented by the [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class. The [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) class provides the [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection. Each item in the [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection represents an object of the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class.  

Aspose.Cells provides the [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) method in the [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) class. The [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) method is used to set a cell's formatting style. The [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) class provides properties for adding borders to cells.  

#### **Adding Borders to a Cell**  

Developers can add borders to a cell by using the [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) object's [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--) collection. The border type is passed as an index to the [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--) collection. All border types are pre-defined in the [**BorderType**](https://reference.aspose.com/cells/nodejs-cpp/bordertype) enumeration.  

**Border enumeration**  

|**Border Types**|**Description**|  
| :- | :- |  
|BottomBorder|A bottom border line|  
|DiagonalDown|A diagonal line from top left to right bottom|  
|DiagonalUp|A diagonal line from bottom left to right top|  
|LeftBorder|A left border line|  
|RightBorder|A right border line|  
|TopBorder|A top border line|  

The [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--) collection stores all borders. Each border in the [**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--) collection is represented by a [**Border**](https://reference.aspose.com/cells/nodejs-cpp/border) object which provides two properties, [**setColor**](https://reference.aspose.com/cells/nodejs-cpp/border/#setColor-color-) and [**setLineStyle**](https://reference.aspose.com/cells/nodejs-cpp/border/#setLineStyle-cellbordertype-) to set a border's line color and style respectively.  

To set a border's line color, select a color using the Color enumeration (part of Node.js) and assign it to the Border object's color property.  

The border's line style is set by selecting a line style from the [**CellBorderType**](https://reference.aspose.com/cells/nodejs-cpp/cellbordertype) enumeration.  

**CellBorderType enumeration**  

|**Line Styles**|**Description**|  
| :- | :- |  
|DashDot|Thin dash-dotted line|  
|DashDotDot|Thin dash-dot-dotted line|  
|Dashed|Dashed line|  
|Dotted|Dotted line|  
|Double|Double line|  
|Hair|Hairline|  
|MediumDashDot|Medium dash-dotted line|  
|MediumDashDotDot|Medium dash-dot-dotted line|  
|MediumDashed|Medium dashed line|  
|None|No line|  
|Medium|Medium line|  
|SlantedDashDot|Slanted medium dash-dotted line|  
|Thick|Thick line|  
|Thin|Thin line|  
Select one of the line styles and then assign it to the [**Border**](https://reference.aspose.com/cells/nodejs-cpp/border) object's [**lineStyle**](https://reference.aspose.com/cells/nodejs-cpp/border/#setLineStyle-cellbordertype-) property.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AddBordersToCell.js" >}}

{{% alert color="primary" %}}  
You should set both line style and color at the same time. The two diagonal border lines should have the same line style and color.  
{{% /alert %}}  

#### **Adding Borders to a Range of Cells**  

It is also possible to add borders to a range of cells rather than just a single cell. To do so, first, create a range of cells by calling the [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) collection's [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) method. It takes the following parameters:  

- First Row, the first row of the range.  
- First Column, represents the first column of the range.  
- Number of Rows, the number of rows in the range.  
- Number of Columns, the number of columns in the range.  

The [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) method returns a [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) object, which contains the specified range of cells. The [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) object provides a [**setOutlineBorder**](https://reference.aspose.com/cells/nodejs-cpp/range/#setOutlineBorder-bordertype-cellbordertype-cellscolor-) method that takes the following parameters to add a border to the range of cells:  

- **Border Type**, the border type, selected from the [**BorderType**](https://reference.aspose.com/cells/nodejs-cpp/bordertype) enumeration.  
- **Line Style**, the border line style, selected from the [**CellBorderType**](https://reference.aspose.com/cells/nodejs-cpp/cellbordertype) enumeration.  
- **Color**, the line color, selected from the Color enumeration.  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AddBordersToRange.js" >}}

  