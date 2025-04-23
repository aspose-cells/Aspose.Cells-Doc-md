---  
title: 边框设置
linktitle: 边框设置  
description: 如何使用 Node.js 通过 C++ 设置单元格边框样式和颜色。通过调整边框的宽度、样式和颜色，可以更好地控制单元格的外观和显示效果。  
keywords: Aspose.Cells，单元格边框设置，Node.js 通过 C++，边框宽度，边框样式，边框颜色  
type: docs  
weight: 40  
url: /zh/nodejs-cpp/cells-border-settings/  
---  

## **向单元格添加边框**  

微软Excel允许用户为单元格添加边框。边框类型取决于添加的位置。例如，上边框是添加到单元格顶部的位置。用户还可以修改线条样式和颜色。  

利用 Aspose.Cells for Node.js via C++，开发者可以像在 Microsoft Excel 中一样添加边框并自定义外观。这具有极大的灵活性。  

### **向单元格添加边框**  

Aspose.Cells提供了[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)类，代表一个Microsoft Excel文件。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)类包含一个[**worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--)集合，可访问Excel文件中的每个工作表。工作表由[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类表示。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet)类提供了[**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)集合。[**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells)集合中的每个元素都代表一个[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)类的对象。  

Aspose.Cells在[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell)类中提供了[**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--)方法，用于设置单元格的格式样式。[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)类还提供了添加边框的属性。  

#### **向单元格添加边框**  

开发者可以通过使用[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style)对象的[**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--)集合为单元格添加边框。边框类型作为索引传入[**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--)集合。所有边框类型都在[**BorderType**](https://reference.aspose.com/cells/nodejs-cpp/bordertype)枚举中预定义。  

**边框枚举**  

|**边框类型**|**描述**|  
| :- | :- |  
|BottomBorder| 底部边框线|  
|DiagonalDown| 从左上到右下的对角线|  
|DiagonalUp| 从左下到右上的对角线|  
|LeftBorder|左边框线|  
|RightBorder|右边框线|  
|TopBorder|顶部边框线|  

[**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--)集合存储所有边框。[**borders**](https://reference.aspose.com/cells/nodejs-cpp/style/#getBorders--)集合中的每个边框由[**Border**](https://reference.aspose.com/cells/nodejs-cpp/border)对象表示，提供两个属性，[**setColor**](https://reference.aspose.com/cells/nodejs-cpp/border/#setColor-color-)和[**setLineStyle**](https://reference.aspose.com/cells/nodejs-cpp/border/#setLineStyle-cellbordertype-)，分别设置边框的线色和线样式。  

要设置边框的线条颜色，使用 Color 枚举（属于 Node.js）选择颜色，并将其赋值给 Border 对象的 color 属性。  

通过从 [**CellBorderType**](https://reference.aspose.com/cells/nodejs-cpp/cellbordertype) 枚举中选择线条样式来设置边框的线条样式。  

**CellBorderType枚举**  

|**线条样式**|**描述**|  
| :- | :- |  
|DashDot|细长虚点线|  
|DashDotDot|细长虚点虚点线|  
|Dashed|虚线|  
|Dotted|点状线|  
|Double|双线|  
|Hair|细线|  
|MediumDashDot|中等虚点线|  
|MediumDashDotDot|中等虚点虚点线|  
|MediumDashed|中等虚线|  
|None|无线|  
|Medium|中线|  
|SlantedDashDot|倾斜中等虚点线|  
|Thick|粗线|  
|Thin|细线|  
选择一种线条样式，然后将其分配给 [**Border**](https://reference.aspose.com/cells/nodejs-cpp/border) 对象的 [**lineStyle**](https://reference.aspose.com/cells/nodejs-cpp/border/#setLineStyle-cellbordertype-) 属性。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AddBordersToCell.js" >}}

{{% alert color="primary" %}}  
你应该同时设置线条样式和颜色。两个对角线边框线应具有相同的线条样式和颜色。  
{{% /alert %}}  

#### **向单元格范围添加边框**  

也可以对一范围单元格添加边框，而不仅仅是单个单元格。首先，通过调用 [**cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 集合的 [**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) 方法创建一个单元格范围。它接受以下参数：  

- 第一行，范围的第一行。  
- 第一列，表示范围的第一列。  
- 行数，范围中的行数。  
- 列数，范围中的列数。  

[**createRange**](https://reference.aspose.com/cells/nodejs-cpp/cells/#createRange-string-string-) 方法返回一个 [**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) 对象，其中包含指定范围的单元格。[**Range**](https://reference.aspose.com/cells/nodejs-cpp/range) 对象提供一个 [**setOutlineBorder**](https://reference.aspose.com/cells/nodejs-cpp/range/#setOutlineBorder-bordertype-cellbordertype-cellscolor-) 方法，可以接受以下参数，为单元格范围添加边框：  

- **边框类型**，选择自 [**BorderType**](https://reference.aspose.com/cells/nodejs-cpp/bordertype) 枚举的边框类型。  
- **线条样式**，选择自 [**CellBorderType**](https://reference.aspose.com/cells/nodejs-cpp/cellbordertype) 枚举的边框线条样式。  
- **颜色**，线条颜色，从Color枚举中选择。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-AddBordersToRange.js" >}}


