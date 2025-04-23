---  
title: 为工作簿渲染指定单独或私有字体集，使用 Node.js 通过 C++  
linktitle: 指定工作簿渲染的个体或私有字体集  
type: docs  
weight: 40  
url: /zh/nodejs-cpp/specify-individual-or-private-set-of-fonts-for-workbook-rendering/  
description: 学习如何使用 Aspose.Cells for Node.js via C++ 指定工作簿渲染的单独或私有字体集。  
---  

## **可能的使用场景**  

通常，您会为所有工作簿指定字体目录或字体列表，但有时需要为特定工作簿指定单独或私有的字体集。Aspose.Cells for Node.js via C++ 提供了 [**IndividualFontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/individualfontconfigs) 类，可用于指定此类字体集。  

## **指定工作簿渲染的个体或私有字体集**  

以下示例加载了带有单独或私有字体集的 [示例Excel文件](67338268.xlsx)，使用 [**IndividualFontConfigs**](https://reference.aspose.com/cells/nodejs-cpp/individualfontconfigs) 类指定。请查看示例中的字体文件（67338271.zip）以及由其生成的 PDF（67338269.pdf）。截图显示如果字体成功找到，输出 PDF 的效果。  

![todo:image_alt_text](specify-individual-or-private-set-of-fonts-for-workbook-rendering_1.png)  

## **示例代码**  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Path of your custom font directory.
const customFontsDir = "C:\\TempDir\\CustomFonts";

// Specify individual font configs custom font directory.
const fontConfigs = new AsposeCells.IndividualFontConfigs();

// If you comment this line or if custom font directory is wrong or 
// if it does not contain required font then output pdf will not be rendered correctly.
fontConfigs.setFontFolder(customFontsDir, false);

// Specify load options with font configs.
const opts = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
opts.setFontConfigs(fontConfigs);

const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sampleSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.xlsx");
// Output directory
const outputDir = path.join(__dirname, "output");
// Load the sample Excel file with individual font configs. 
const wb = new AsposeCells.Workbook(filePath, opts);

// Save to PDF format.
wb.save(outputDir + "outputSpecifyIndividualOrPrivateSetOfFontsForWorkbookRendering.pdf", AsposeCells.SaveFormat.Pdf);
```  

