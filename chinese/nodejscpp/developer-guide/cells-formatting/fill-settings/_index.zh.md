---  
title: 填充设置
linktitle: 填充设置  
description: 了解如何使用 Aspose.Cells 库在 Node.js 中通过 C++ 自定义单元格的填充设置、背景和风格。  
keywords: Aspose.Cells，单元格，填充设置，背景，样式，Node.js 通过 C++  
type: docs  
weight: 50  
url: /zh/nodejs-cpp/cells-fill-settings/  
---  

## **颜色和背景图案**  

Microsoft Excel可以设置单元格的前景（轮廓）和背景（填充）颜色以及背景图案。  

Aspose.Cells还以灵活的方式支持这些功能。在本主题中，我们将学习如何使用Aspose.Cells来使用这些功能。  

### **设置颜色和背景图案**  

Aspose.Cells 提供一个类 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 来表示一个 Microsoft Excel 文件。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类包含一个 [**Worksheets**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#getWorksheets--) 集合，可访问 Excel 文件中的每个工作表。工作表由 [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类表示。[**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet) 类提供一个 [**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 集合。[**Cells**](https://reference.aspose.com/cells/nodejs-cpp/cells) 集合中的每一项代表一个 [**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) 类的对象。  

[**Cell**](https://reference.aspose.com/cells/nodejs-cpp/cell) 具有用于获取和设置单元格格式的 [**getStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#getStyle--) 和 [**setStyle**](https://reference.aspose.com/cells/nodejs-cpp/cell/#setStyle-style-) 方法。[**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) 类提供设置单元格前景色和背景色的属性。Aspose.Cells 提供一个 [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype) 枚举，包含一组预定义的背景图案类型，具体如下。  

|**背景图案**|**描述**|  
| :- | :- |  
|DiagonalCrosshatch|代表对角线交叉图案  
|DiagonalStripe|代表对角线条纹图案  
|Gray6|代表6.25%灰色图案  
|Gray12|代表12.5%灰色图案  
|Gray25|代表25%灰色图案  
|Gray50|代表50%灰色图案  
|Gray75|代表75%灰色图案  
|HorizontalStripe|代表水平条纹图案  
|None|代表无背景  
|ReverseDiagonalStripe|代表反对角线条纹图案  
|Solid|代表实线图案  
|ThickDiagonalCrosshatch|代表粗对角线交叉图案  
|ThinDiagonalCrosshatch|代表细对角线交叉图案  
|ThinDiagonalStripe|代表细对角线条纹图案  
|ThinHorizontalCrosshatch|代表细水平交叉图案  
|ThinHorizontalStripe|代表细水平条纹图案  
|ThinReverseDiagonalStripe|代表细反对角线条纹图案  
|ThinVerticalStripe|代表细竖条纹图案|  
|VerticalStripe|代表竖条纹图案|  

在下面的示例中，A1单元格的前景色已设置，但A2配置为具有前景色和背景色的垂直条纹背景模式。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-SetColorsAndBackgroundPatterns.js" >}}


### **重要知识**  

{{% alert color="primary" %}}  

- 要设置单元格的前景色或背景色，可以使用 [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) 对象的 [**setForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundColor-color-) 或 [**setBackgroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setBackgroundColor-color-) 方法。这两种方法只有在 [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) 对象的 [**Pattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) 属性被配置时才会生效。  
- [**setForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#setForegroundColor-color-) 方法设置单元格的阴影色。  
  [**setPattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) 方法指定用于前景色或背景色的背景图案类型。Aspose.Cells 提供一个枚举 [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype)，包含一组预定义的背景图案类型。  
- 如果从 [**BackgroundType**](https://reference.aspose.com/cells/nodejs-cpp/backgroundtype) 枚举中选择 *BackgroundType.None*，则不会应用前景色。  
  同样，如果选择 *BackgroundType.None* 或 *BackgroundType.Solid* 值，则不会应用背景色。  
- 在检索单元格的阴影/填充颜色时，如果 [**Style.setPattern**](https://reference.aspose.com/cells/nodejs-cpp/style/#setPattern-backgroundtype-) 是 *BackgroundType.None*，[**Style.getForegroundColor**](https://reference.aspose.com/cells/nodejs-cpp/style/#getForegroundColor--) 将返回 *Color.Empty*。  

{{% /alert %}}  

### **应用梯度填充效果**  

要将所需的渐变填充效果应用于单元格，请相应使用 [**Style**](https://reference.aspose.com/cells/nodejs-cpp/style) 对象的 [**setTwoColorGradient**](https://reference.aspose.com/cells/nodejs-cpp/style/#setTwoColorGradient-color-color-gradientstyletype-number-) 方法。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-ApplyGradientFillEffects.js" >}}


## **颜色和调色板**  

调色板是在创建图像时可用的颜色数量。在演示文稿中使用标准调色板可以让用户创建一致的外观。每个Microsoft Excel（97-2003）文件都有一个包含可应用于单元格、字体、网格线、图形对象、填充和图表中的线条的56种颜色的调色板。  

使用 Aspose.Cells 不仅可以使用调色板的现有颜色，还可以使用自定义颜色。在使用自定义颜色之前，首先将其添加到调色板中。  

本主题讨论如何向调色板中添加自定义颜色。  

### **向调色板中添加自定义颜色**  

Aspose.Cells 支持 Microsoft Excel 的 56 种颜色调色板。要使用在调色板中未定义的自定义颜色，需要将颜色添加到调色板中。  

Aspose.Cells 提供一个类 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)，代表一个 Microsoft Excel 文件。[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类提供一个 [**changePalette**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#changePalette-color-number-) 方法，接受以下参数以添加自定义颜色以修改调色板：  

- Custom Color，要添加的自定义颜色。  
- Index，自定义颜色在调色板中的索引，将替换指定的颜色。应该在 0-55 之间。  

下面的示例在应用于字体之前向调色板中添加了自定义颜色（兰花紫）。  

{{< gist "aspose-cells-gists" "c7b55cbeb75eaaae989115230a7619eb" "Cells-Formatting-FillSettings-AddCustomColorsToPalette.js" >}}


{{% alert color="primary" %}}  

调色板只能容纳 56 种颜色。当向调色板中添加自定义颜色时，调色板会改变，文件中用先前颜色格式化的任何元素也会发生变化。因此，在更改调色板时，请务必小心。此外，在 XLS（Excel 97 - 2003）文件格式中，这是唯一的限制，XLSX 或其他高级 MS Excel（2007/2010 或 2013）文件格式则没有这种限制。  

{{% /alert %}}  

{{< app/cells/assistant language="nodejs-cpp" >}}
