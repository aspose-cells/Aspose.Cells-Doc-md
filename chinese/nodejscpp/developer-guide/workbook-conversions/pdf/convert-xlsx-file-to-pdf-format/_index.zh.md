---
title: 使用C++ via Node.js将XLSX文件转换为PDF格式
linktitle: 将XLSX文件转换为PDF格式
type: docs
weight: 30
url: /zh/nodejs-cpp/convert-xlsx-file-to-pdf-format/
description: 本指南介绍如何使用Aspose.Cells for Node.js via C++将Excel文件（XLSX）转换为PDF格式。 
---

{{% alert color="primary" %}}

PDF（便携式文档格式）表示与用于创建这些文档的软件、硬件和操作系统无关。 PDF文件可以以一种与设备无关和与分辨率无关的方式表示任何组合的文本、图形和图像。 PDF文件通常是经过压缩的，因此占用的空间比原始文件少。

 有时你需要将Microsoft Excel文件转换为PDF。为此，你需要一个快速、安全、准确且可靠的解决方案，能够在全球范围内分发PDF文档。有许多转换工具可以完成此任务，但必须确保原始Excel文档的布局在输出PDF中保持不变。图像、图表、形状、数据格式、字体、属性、颜色、页面设置、文本方向、边框、图表等都应准确无误地呈现。，[Aspose.Cells](https://products.aspose.com/cells/nodejs-cpp/)确保高保真转换。

 本文件旨在全面介绍如何将包含图片、图表、格式等的Microsoft Excel文件转换为PDF。为此，展示了如何在Node.js中创建一个简单的控制台应用程序，利用Aspose.Cells API将Excel文件转换为PDF。转换具有高度的精度和准确性。

{{% /alert %}}

## **将Excel转换为PDF**

 这个示例使用Excel文件（SampleInput.xlsx）作为模板。工作簿包含带有图表和图片的工作表。每个工作表使用不同类型的格式，包括字体、属性、颜色、阴影效果和边框。第一个工作表有柱状图，最后一个工作表有图片。

### **模板Excel文件**

 模板文件包含三个工作表，包括图表和作为媒体的图片。第一个工作表有图表，最后一个工作表包含图片，如下面的截图所示。

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet2.png)|
| :- | :- |
|第一个工作表 **（销售预测）**|第二个工作表 **（销售报告）**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Sheet4.png)|
|第三个工作表 **（数据录入）**|最后一个工作表 **（图像）**|

### **转换过程**

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const designerFile = path.join(dataDir, "SampleInput.xlsx");
const pdfFile = path.join(dataDir, "Output.out.pdf");

try {
// Open the template excel file
const wb = new AsposeCells.Workbook(designerFile);

// Save the pdf file.
wb.save(pdfFile, AsposeCells.SaveFormat.Pdf);
} catch (e) {
console.log(e.message);
}
```

{{% alert color="primary" %}}

 如果电子表格中包含公式，最好在将电子表格导出为PDF前调用[Workbook.calculateFormula()](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)方法。这样可以确保公式依赖的值被重新计算，并在PDF中显示正确的值。

{{% /alert %}}

### **结果**

当上述代码运行后，在应用程序目录的Files文件夹中创建了一个PDF文件。
以下屏幕截图显示了PDF页面。 请注意，页眉和页脚也在输出PDF文件中保留。

|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted1.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted2.png)|
| :- | :- |
|第一个工作表 **（销售预测）**|第二个工作表 **（销售报告）**|
|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted3.png)|![todo:image_alt_text](Convert_an_XLS_File_to_PDF_Converted4.png)|
|第三个工作表 **（数据录入）**|最后一个工作表 **（图像）**|
{{< app/cells/assistant language="nodejs-cpp" >}}
