---  
title: 使用Node.js在C++中将工作表范围导出为图片  
linktitle: 导出工作表中的单元格范围为图像  
type: docs  
weight: 60  
url: /zh/nodejs-cpp/export-range-of-cells-in-a-worksheet-to-image/  
---  

## **可能的使用场景**  

你可以使用Aspose.Cells for Node.js via C++将工作表制作成图片，但有时你只需要导出工作表中的某个范围的单元格为图片。本文介绍如何实现这一点。  

## **导出工作表中的单元格范围为图像**  

为了取一个范围的图片，请设置打印区域为所需范围，然后将所有边距设置为0，同时将[**ImageOrPrintOptions.getOnePagePerSheet()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getOnePagePerSheet--)设置为**true**。以下代码示范了如何获取D8:G16范围的图片。下面是示例Excel文件（47153160.xlsx）的截图，可用于代码测试，任何Excel文件都可以使用此代码。  

## **示例 Excel 文件及其导出图像的屏幕截图**  

**![todo:image_alt_text](export-range-of-cells-in-a-worksheet-to-image_1.png)**  

执行该代码仅创建范围 D8:G16 的图像。  

**![todo:image_alt_text](Output-Image.png)**  

## **示例代码**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook from source file.
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "sampleExportRangeOfCellsInWorksheetToImage.xlsx"));

// Access the first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Set the print area with your desired range
worksheet.getPageSetup().setPrintArea("D8:G16");

// Set all margins as 0
worksheet.getPageSetup().setLeftMargin(0);
worksheet.getPageSetup().setRightMargin(0);
worksheet.getPageSetup().setTopMargin(0);
worksheet.getPageSetup().setBottomMargin(0);

// Set OnePagePerSheet option as true
const options = new AsposeCells.ImageOrPrintOptions();
options.setOnePagePerSheet(true);
options.setImageType(AsposeCells.ImageType.Jpeg);
options.setHorizontalResolution(200);
options.setVerticalResolution(200);

// Take the image of your worksheet
const sr = new AsposeCells.SheetRender(worksheet, options);
sr.toImage(0, path.join(outputDir, "outputExportRangeOfCellsInWorksheetToImage.jpg"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
