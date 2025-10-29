---  
title: 通过Node.js在C++中将工作表转换为图片和按页面转换工作表为图片  
linktitle: 将工作表转换为图像以及按页将工作表转换为图像  
type: docs  
weight: 80  
url: /zh/nodejs-cpp/converting-worksheet-to-image-and-worksheet-to-image-by-page/  
---  

{{% alert color="primary" %}}  
本文旨在为开发者提供详细的指南，了解如何将工作表转换为图片文件，以及将多页面工作表转换为每页一张图片的方法。  

有时，您可能需要将工作表呈现为图像，例如在应用程序或网页中使用。您可能需要将图像插入 Word 文档、PDF 文件、PowerPoint 演示文稿中，或者在其他一些场景中使用它们。简单来说，您希望将工作表呈现为图像。Aspose.Cells 支持将 Microsoft Excel 文件中的工作表转换为图像。Aspose.Cells 还支持将工作簿转换为多个图像文件，每页一个。  

您可以使用Office自动化来实现这一点，但Office自动化有它自己的缺点。有几个原因和问题涉及其中：例如安全性、稳定性、可伸缩性/速度、价格和功能。简而言之，有很多原因，但主要原因是微软自己强烈建议不要使用Office自动化。  
{{% /alert %}}  

## **使用Aspose.Cells for Node.js via C++将工作表转换为图片文件**  

本文介绍如何创建控制台应用程序，将工作表转换为图片，以及使用Aspose.Cells API以几行简单的代码将工作表转换为一张图片或每个工作表一张图片。  

你需要导入多个与渲染功能相关的类，比如[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/)、[**ImageOrPrintOptions**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/)、[**WorkbookRender**](https://reference.aspose.com/cells/nodejs-cpp/workbookrender/)等。[**SheetRender**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/)类代表一张工作表，用于渲染工作表的图片，具有一个重载的[**toImage(number)**](https://reference.aspose.com/cells/nodejs-cpp/sheetrender/#toImage-number-)方法，可以直接将工作表转换为带有任何属性或选项的图像文件。它可以返回一个图像对象，你可以将图像保存到磁盘/流中。支持的图像格式包括BMP、PNG、GIF、JPG、JPEG、TIFF、EMF等几种。  

本文解释了如何：  

- 将工作表转换为图像  
- 将工作表中的每个页面转换为图像  

此任务显示如何使用Aspose.Cells将模板工作簿中的工作表转换为图像文件。  

### **设置项目**  

1. 首先，[下载Aspose.Cells for Node.js via C++](https://downloads.aspose.com/cells/nodejs-cpp)。  
1. 在你的开发计算机上安装它。所有[Aspose](http://www.aspose.com/)组件安装后，均处于评估模式。评估模式没有时间限制，只会在生成的文档中加入水印。现在启动你的开发环境，创建一个新的控制台应用程序。本示例使用Node.js控制台应用，但你可以使用任何与Node.js集成的设置。将Aspose.Cells引用到已创建的项目中。  

### **将工作表转换为图像文件**  

我在Microsoft Excel中创建了一个新工作簿，并在第一个工作表中添加了一些数据：**Testbook.xlsx**（1个工作表）。接下来，将模板文件的工作表Sheet1转换为名为SheetImage.jpg的图像文件。  

以下是组件用来完成任务的代码。它将**Testbook.xlsx**中的Sheet1转换为图像文件，以说明这种转换有多么简便。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

// Open a template excel file
const filePath = path.join(sourceDir, "sampleConvertWorksheettoImageFile.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Get the first worksheet.
const sheet = workbook.getWorksheets().get(0);

// Define ImageOrPrintOptions
const imgOptions = new AsposeCells.ImageOrPrintOptions();
imgOptions.setOnePagePerSheet(true);

// Specify the image format
imgOptions.setImageType(AsposeCells.ImageType.Jpeg);

// Render the sheet with respect to specified image/print options
const sr = new AsposeCells.SheetRender(sheet, imgOptions);

// Save the image file
const outputFilePath = outputDir + "outputConvertWorksheettoImageFile.jpg";

sr.toImage(0, outputFilePath);
```  

## **使用Aspose.Cells for Node.js via C++按页面将工作表转换为图片文件**  

此示例演示如何使用Aspose.Cells将模板工作簿中具有多个页面的工作表转换为每页一个图像文件。  

### **按页转换工作表为图像**  

我在Microsoft Excel中创建了一个新工作簿，并在第一个工作表中添加了一些数据：**Testbook2.xlsx**（1个工作表）。  

现在，将模板文件的工作表Sheet1转换为图像文件（每页一个文件）。由于我已经创建了执行复制任务的控制台应用程序，因此我将跳过创建控制台应用程序的步骤，直接转移到工作表转换步骤。  

以下是组件完成任务所使用的代码。它将Testbook2.xlsx中的Sheet1按页转换为图像文件。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");
// Output directory
const outputDir = path.join(__dirname, "output");

const filePath = path.join(sourceDir, "sampleConvertWorksheetToImageByPage.xlsx");
const workbook = new AsposeCells.Workbook(filePath);
const sheet = workbook.getWorksheets().get(0);

const options = new AsposeCells.ImageOrPrintOptions();
options.setHorizontalResolution(200);
options.setVerticalResolution(200);
options.setImageType(AsposeCells.ImageType.Tiff);

// Sheet2Image By Page conversion
const sr = new AsposeCells.SheetRender(sheet, options);
for (let j = 0; j < sr.getPageCount(); j++) 
{
sr.toImage(j, outputDir + "outputConvertWorksheetToImageByPage_" + (j + 1) + ".tif");
}
```  


{{< app/cells/assistant language="nodejs-cpp" >}}
