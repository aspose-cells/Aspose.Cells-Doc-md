---
title: Pdf 通过 Node.js 结合 C++ 实现
linktitle: Pdf
type: docs
weight: 220
url: /zh/nodejs-cpp/convert-excel-to-pdf/
description: 学习如何使用 Aspose.Cells for Node.js via C++ 将 Excel 工作簿转换为 PDF。 
---

{{% alert color="primary" %}}
Aspose.Cells支持将Excel工作簿转换为PDF。在此示例中，我们将看到完整将Excel工作簿转换为PDF的过程。
{{% /alert %}}

## **将Excel工作簿转换为PDF**

PDF文件被广泛用于组织、政府部门和个人之间交换文档。它是一种标准文档格式，软件开发人员经常被要求找到一种方法将Microsoft Excel文件转换为PDF文档。

Aspose.Cells支持将Excel文件转换为PDF，并在转换过程中保持高度的视觉保真度。

{{% alert color="primary" %}}
Aspose.Cells for Node.js via C++ 直接在输出文档中写入API和版本号信息。例如，在渲染成 PDF 时，Aspose.Cells for Node.js via C++ 会将 **PDF 生产者** 字段填入值，如 'Aspose.Cells v23.2'。

请注意，您可以通过 [**PdfSaveOptions.getProducer()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getProducer--) 属性在输出文档中更改此信息。
{{% /alert %}}

### **直接转换**

Aspose.Cells for Node.js via C++ 支持独立于其他软件将电子表格转换为 PDF。只需使用 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类的 [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) 方法保存Excel文件为 PDF。[**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) 方法提供 [**SaveFormat.Pdf**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) 枚举成员，将原生的Excel文件转换为PDF格式。

按以下步骤直接将Excel电子表格转换为PDF格式：

通过调用其空构造函数实例化[**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook)类的对象。
1. 您可以打开/加载现有模板文件，或者如果您是从头开始创建工作簿，则跳过此步骤。
1. 使用Aspose.Cells的API在电子表格上进行任何工作（输入数据，应用格式，设置公式，插入图片或其他绘图对象等）。
1. 完成电子表格代码后，调用 [**Workbook**](https://reference.aspose.com/cells/nodejs-cpp/workbook) 类的 [**save(string, SaveFormat)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveformat-) 方法保存电子表格。

文件格式应为PDF，因此从[**SaveFormat**](https://reference.aspose.com/cells/nodejs-cpp/saveformat)枚举中选择*Pdf*（预定义值）生成最终PDF文档。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xls");

// Instantiate the Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save the document in PDF format
workbook.save(path.join(dataDir, "output.pdf"), AsposeCells.SaveFormat.Pdf);
```

### **高级转换**

您还可以选择使用[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)类来设置转换的不同属性。设置[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)类的不同属性可控制输出PDF的打印、字体、安全和压缩设置。 

最重要的属性是[**getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--)，它允许您设置PDF的标准兼容级别。目前，您可以保存为PDF 1.4、PDF 1.5、PDF 1.6、PDF 1.7、PDF/A-1a、PDF/A-1b、PDF/A-2a、PDF/A-2b、PDF/A-2u、PDF/A-3a、PDF/A-2ab和PDF/A-3u格式。请注意，使用PDF/A格式时，输出文件大小大于常规PDF文件大小。

#### **将工作簿保存为PDF/A兼容文件**

下面提供的代码片段演示了如何使用[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)类将Excel文件保存为PDF/A兼容的PDF格式。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate new workbook
const workbook = new AsposeCells.Workbook();

// Insert a value into the A1 cell in the first worksheet
workbook.getWorksheets().get(0).getCells().get(0, 0).putValue("Testing PDF/A");

// Define PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set the compliance type
pdfSaveOptions.setCompliance(AsposeCells.PdfCompliance.PdfA1b);

// Save the file
workbook.save(path.join(dataDir, "output.pdf"), pdfSaveOptions);
```

{{% alert color="primary" %}}
请注意，[**getCompliance()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCompliance--) 属性是在 Aspose.Cells for Node.js via C++ 5.3.0 版本中新增的。
{{% /alert %}}

#### **设置PDF创建时间**

使用[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)类，您可以获取或设置PDF创建时间。以下代码演示了使用[**PdfSaveOptions.getCreatedTime()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions/#getCreatedTime--)属性设置PDF文件的创建时间。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const inputPath = path.join(dataDir, "Book1.xlsx");
// Load excel file containing charts
const workbook = new AsposeCells.Workbook(inputPath);

// Create an instance of PdfSaveOptions
const options = new AsposeCells.PdfSaveOptions();
options.setCreatedTime(new Date());

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save(path.join(dataDir, "output.pdf"), options);
```

#### **设置ContentCopyForAccessibility选项**

使用[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)类，您可以获取或设置PDF的[**getAccessibilityExtractContent()**](https://reference.aspose.com/cells/nodejs-cpp/pdfsecurityoptions/#getAccessibilityExtractContent--)选项，以控制转换后PDF中的内容访问。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const inputPath = path.join(sourceDir, "BookWithSomeData.xlsx");

// Load excel file containing some data
const workbook = new AsposeCells.Workbook(inputPath);

// Create an instance of PdfSaveOptions and pass SaveFormat to the constructor
const pdfSaveOpt = new AsposeCells.PdfSaveOptions();

// Create an instance of PdfSecurityOptions
const securityOptions = new AsposeCells.PdfSecurityOptions();

// Set AccessibilityExtractContent to true
securityOptions.setAccessibilityExtractContent(false);

// Set the security option in the PdfSaveOptions
pdfSaveOpt.setSecurityOptions(securityOptions);

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save(path.join(outputDir, "outFile.pdf"), pdfSaveOpt);
```

#### **导出自定义属性到PDF**

使用[**PdfSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pdfsaveoptions)类，您可以将源工作簿中的自定义属性导出到PDF。提供了[**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/nodejs-cpp/pdfcustompropertiesexport/)枚举用于指定属性的导出方式。这些属性可以通过单击“文件”然后选择“属性”在Adobe Acrobat Reader中观察。模板文件"sourceWithCustProps.xlsx"可在[此处](sourceWithCustProps.xlsx)下载进行测试，输出的PDF文件"outSourceWithCustProps"可在[此处](outSourceWithCustProps.pdf)进行分析。

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sourceWithCustProps.xlsx");

// Load excel file containing custom properties
const workbook = new AsposeCells.Workbook(filePath);

// Create an instance of PdfSaveOptions
const pdfSaveOptions = new AsposeCells.PdfSaveOptions();

// Set CustomPropertiesExport property to PdfCustomPropertiesExport.Standard
pdfSaveOptions.setCustomPropertiesExport(AsposeCells.PdfCustomPropertiesExport.Standard);

// Save the workbook to PDF format while passing the object of PdfSaveOptions
workbook.save("outSourceWithCustProps.pdf", pdfSaveOptions);
```

### **转换属性**

我们致力于增强每个新版本的转换功能。 Aspose.Cells的Excel转PDF转换仍然存在一些限制。 在转换为PDF格式时不支持MapChart。 还有一些绘图对象支持不佳。

下表列出了使用Aspose.Cells导出为PDF时全部或部分支持的所有功能。 该表不是最终版本，不涵盖所有电子表格属性，但确实标识了在转换为PDF时不支持或部分支持的功能。

|**文档元素**|**属性**|**支持**|**备注**|
| :- | :- | :- | :- |
|对齐| |支持| |
|背景设置| |支持| |
|边框|颜色|支持| |
|边框|线条样式|支持| |
|边框|线宽|支持| |
|单元格数据| |是| |
|备注| |是| |
|条件格式| |是| |
|文档属性| |是| |
|绘图对象| |部分|绘图对象的阴影和3D效果支持不佳；WordArt和智能图表部分支持。|
|字体|大小|是| |
|字体|颜色|是| |
|字体|样式|是| |
|字体|下划线|是| |
|字体|效果|是| |
|图像| |是| |
|超链接| |是| |
|图表| |部分|不支持地图图表。|
|合并单元格| |是| |
|分页符| |是| |
|页面设置|页眉/页脚|是| |
|页面设置|页边距|是| |
|页面设置|页面方向|是| |
|页面设置|页面大小|是| |
|页面设置|打印区域|是| |
|页面设置|打印标题|是| |
|页面设置|缩放|是| |
|行高/列宽| |是| |
|RTL (从右到左) 语言| |是| |

{{% alert color="primary" %}}
如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用 [**Workbook.calculateFormula()**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#calculateFormula--)。这样做将确保重新计算依赖于公式的值，并在PDF中呈现正确的值。
{{% /alert %}}

## **高级主题**
- [使用命名目标添加PDF书签](/cells/zh/nodejs-cpp/add-pdf-bookmarks-with-named-destinations/)
- [当没有需要打印的内容时，避免在输出PDF中出现空白页](/cells/zh/nodejs-cpp/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [在保存为PDF时仅更改特定Unicode字符的字体](/cells/zh/nodejs-cpp/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [将XLSX文件转换为PDF格式](/cells/zh/nodejs-cpp/convert-xlsx-file-to-pdf-format/)
- [将 Excel 文件转换为兼容 PDFA-1a 格式的 PDF](/cells/zh/nodejs-cpp/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [将带有图片或图表的XLS文件转换为PDF](/cells/zh/nodejs-cpp/convert-xls-file-with-images-or-charts-to-pdf/)
- [为图表工作表创建PdfBookmarkEntry](/cells/zh/nodejs-cpp/create-pdfbookmarkentry-for-chart-sheet/)
- [将所有工作表列调整到单个PDF页面上](/cells/zh/nodejs-cpp/fit-all-worksheet-columns-on-single-pdf-page/)
- [在使用DrawObjectEventHandler类呈现到PDF时获取DrawObject和边界](/cells/zh/nodejs-cpp/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [在呈现Excel文件时获取字体替换的警告](/cells/zh/nodejs-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [在将Excel渲染为PDF时忽略错误](/cells/zh/nodejs-cpp/ignore-errors-while-rendering-excel-to-pdf/)
- [限制生成的页面数量-从Excel转换为PDF](/cells/zh/nodejs-cpp/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [保存为PDF时打印注释](/cells/zh/nodejs-cpp/print-comments-while-saving-to-pdf/)
- [在将Excel转换为PDF时呈现Office加载项](/cells/zh/nodejs-cpp/render-office-add-ins-while-converting-excel-to-pdf/)
- [将每个Excel工作表呈现为一个PDF页面-从Excel转换为PDF](/cells/zh/nodejs-cpp/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [通过Aspose.Cells在输出PDF中呈现Unicode补充字符](/cells/zh/nodejs-cpp/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [重新采样添加的图像-从Excel转换为PDF](/cells/zh/nodejs-cpp/resampling-added-images-excel-to-pdf-conversion/)
- [将每个工作表保存为不同的PDF文件](/cells/zh/nodejs-cpp/save-each-worksheet-to-a-different-pdf-file/)
- [以标准或最小尺寸保存Excel到PDF](/cells/zh/nodejs-cpp/save-excel-into-pdf-with-standard-or-minimum-size/)
- [将指定的工作表保存为 PDF](/cells/zh/nodejs-cpp/save-specified-worksheets-to-pdf/)
- [安全的PDF文件](/cells/zh/nodejs-cpp/secure-pdf-documents/)
- [指定如何在输出PDF和图像中跨越字符串](/cells/zh/nodejs-cpp/specify-how-to-cross-string-in-output-pdf-and-image/)
