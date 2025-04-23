---  
title: 使用Node.js在C++中创建Excel工作表的透明图片  
linktitle: Create Transparent Image of Excel Worksheet  
type: docs  
weight: 170  
url: /zh/nodejs-cpp/create-transparent-image-of-excel-worksheet/  
description: 学习如何使用Aspose.Cells for Node.js via C++生成Excel工作表的透明图片。  
---  

{{% alert color="primary" %}}  

有时，您需要将工作表的图像生成为透明图像。您希望将透明度应用于所有没有填充颜色的单元格。Aspose.Cells提供[**ImageOrPrintOptions.getTransparent()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTransparent--)属性以将透明度应用于工作表图像。当此属性为**false**时，没有填充颜色的单元格将以白色绘制，当为**true**时，没有填充颜色的单元格将以透明绘制。  

{{% /alert %}}  

在下面的工作表图片中，没有应用透明度。没有填充颜色的单元格绘制成了白色。  

|**没有透明度的输出：单元格背景为白色**|  
| :- |  
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_1.png)|  

而在下面的工作表图片中，应用了透明度。没有填充颜色的单元格是透明的。  

|**启用透明度输出**|  
| :- |  
|![todo:image_alt_text](create-transparent-image-of-excel-worksheet_2.png)|  

下面的示例代码从 Excel 工作表生成一个透明的图像。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook object from source file
const wb = new AsposeCells.Workbook(path.join(sourceDir, "sampleCreateTransparentImage.xlsx"));

// Apply different image or print options
const imgOption = new AsposeCells.ImageOrPrintOptions();
imgOption.setImageType(AsposeCells.ImageType.Png);
imgOption.setHorizontalResolution(200);
imgOption.setVerticalResolution(200);
imgOption.setOnePagePerSheet(true);

// Apply transparency to the output image
imgOption.setTransparent(true);

// Create image after applying image or print options
const sr = new AsposeCells.SheetRender(wb.getWorksheets().get(0), imgOption);
sr.toImage(0, path.join(outputDir, "outputCreateTransparentImage.png"));
```  

