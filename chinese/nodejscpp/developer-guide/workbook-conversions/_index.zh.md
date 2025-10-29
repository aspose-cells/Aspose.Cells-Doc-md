---  
title: 将 Excel 转换为 Pdf、图像及其他格式  
linktitle: 工作簿转换  
type: docs  
weight: 65  
url: /zh/nodejs-cpp/convert-workbook-to-different-formats/  
description: 使用 Node.js 通过 C++ 将 Excel 文件转换为 Word、Excel、PowerPoint、PDF、CSV、JPG、HTML、MHT、ODS、BMP、PNG、SVG、TIFF、XPS、JSON、SQL、XML 等格式。  
---  

{{% alert color="primary" %}}  
Aspose.Cells支持多种格式之间的转换。技术上，转换意味着加载一个工作簿的一个文件格式，然后将其保存为另一个文件格式。  
{{% /alert %}}  

## **将 Excel 工作簿转换为 PDF**  
PDF文件被广泛用于组织、政府部门和个人之间交换文档。它是一种标准文档格式，软件开发人员经常被要求找到一种方法将Microsoft Excel文件转换为PDF文档。  

Aspose.Cells支持将Excel文件转换为PDF，并在转换过程中保持高度的视觉保真度。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Instantiate the Workbook object
// Open an Excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save the document in PDF format
workbook.save("output.pdf");
```  

## **将 Excel 工作簿转换为 JPG**  
Aspose.Cells 支持将 Excel 文件转换为 JPG。以下代码示例展示如何将工作簿保存为 JPG。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Convert workbook to JPG image.
workbook.save("Image1.jpg");
```  

## **将Excel工作簿转换为图像**  
Aspose.Cells 支持将 Excel 文件转换为图片。以下代码示例展示如何将工作簿保存为图片。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const book = new AsposeCells.Workbook(filePath);

// Convert workbook to BMP image.
book.save("Image1.bmp");
// Convert workbook to JPG image.
book.save("Image1.jpg");
// Convert workbook to Png image.
book.save("Image1.png");
// Convert workbook to EMF image.
book.save("Image1.emf");
// Convert workbook to GIF image.
book.save("Image1.gif");
```  

## **将Excel工作簿转换为XPS**  
XPS文档格式由结构化的XML标记组成，用于定义文档的布局和每个页面的视觉外观，同时还包括用于分发、归档、渲染、处理和打印文档的渲染规则。  

XPS的标记语言是XAML的子集，允许在文档中包含矢量图形元素，使用XAML来标记Windows Presentation Foundation（WPF）的基元。所使用的元素是根据路径和其他几何原语来描述的。  

实际上，XPS文件是一个使用开放打包约定的Unicode ZIP存档，包含构成文档的文件。这些文件包括每个页面的XML标记文件、文本、嵌入字体、光栅图像、2D矢量图形，以及数字版权管理信息。可以通过在支持ZIP文件的应用程序中打开XPS文件来查看其内容。  

从Aspose.Cells 6.0.0开始，支持将Microsoft Excel转换为XPS。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Open an Excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "Book1.xls"));

// Get the first worksheet
const sheet = workbook.getWorksheets().get(0);


// Render the sheet to xps            
const options = new AsposeCells.XpsSaveOptions();
const sheetSet = new AsposeCells.SheetSet([sheet.getIndex()]);
options.setSheetSet(sheetSet);
workbook.save(path.join(dataDir, "out_printingxps.out.xps"), options);


// Export the whole workbook to XPS
workbook.save(path.join(dataDir, "out_whole_printingxps.out.xps"), new AsposeCells.XpsSaveOptions());
```  

## **将 Excel 转换为 Ods、Sxc 和 Fods（OpenOffice / LibreOffice Calc）**  
Aspose.Cells 支持将 Excel 文件转换为 Ods、Sxc 和 Fods 格式。以下代码示例展示如何将 [模板](book1.xlsx) 转换为 Ods、Sxc 和 Fods 文件。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source workbook
const filePath = path.join(dataDir, "book1.xlsx");
const workbook = new AsposeCells.Workbook(filePath);

// Save as ods file 
workbook.save("Out.ods");

// Save as sxc file 
workbook.save("Out.sxc");

// Save as fods file 
workbook.save("Out.fods");
```  

## **将Excel工作簿转换为MHTML文件**  
MHTML结合了普通HTML以及外部资源（通常是链接的内容，如图像、动画、音频等）到一个文件中。它们通常用于以.mht文件扩展名的电子邮件。  

Aspose.Cells支持读取和写入MHTML文件。  

下面的代码示例显示了如何将工作簿保存为MHTML文件。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify the file path
const filePath = path.join(dataDir, "Book1.xlsx");

// Specify the HTML Saving Options
const sv = new AsposeCells.HtmlSaveOptions(AsposeCells.SaveFormat.MHtml);

// Instantiate a workbook and open the template XLSX file
const wb = new AsposeCells.Workbook(filePath);

// Save the MHT file
wb.save(`${filePath}.out.mht`, sv);
```  

## **将Excel工作簿转换为HTML**  
Aspose.Cells API 提供了导出电子表格为 HTML 格式的支持。为此，Aspose.Cells 使用 [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions) 类，提供控制输出 HTML 各个方面的灵活性。  

下面的代码示例显示了如何将工作簿保存为HTML文件。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in HTML format
wb.save(path.join(dataDir, "ConvertingToHTMLFiles_out.html"), AsposeCells.SaveFormat.Html);
```  

## **为HTML设置图像首选项**  
从 8.0.2 版本起，Aspose.Cells 已将 [**getImageOptions()**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions/#getImageOptions--) 公开给 [**HtmlSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/htmlsaveoptions) 类，使开发者在将电子表格保存为 HTML 格式时可以指定图片偏好。  

以下是可以应用的一些图像设置的详细信息。  

- [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/)：指定图像类型。请注意，所有形状，包括图表，在输出HTML中呈现为图像。   
- [**getQuality()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getQuality--)：指定图片的质量（0 到 100），当 [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/) 被指定为 Jpeg 时。  
- [**getVerticalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getVerticalResolution--)：获取或设置图像的垂直分辨率（每英寸点数）。  
- [**getHorizontalResolution()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getHorizontalResolution--)：获取或设置图像的水平分辨率（每英寸点数）。  
- [**TiffCompression**](https://reference.aspose.com/cells/nodejs-cpp/tiffcompression/)：在 [**ImageType**](https://reference.aspose.com/cells/nodejs-cpp/imagetype/) 被指定为 Tiff 时，获取或设置图片的压缩类型。  
- [**getTransparent()**](https://reference.aspose.com/cells/nodejs-cpp/imageorprintoptions/#getTransparent--)：指示当ImageFormat指定为Png时，图像的背景是否应该是透明的。  

## **将Excel工作簿转换为Markdown**  
Aspose.Cells API 支持将电子表格导出为 Markdown 格式。要将活动工作表导出为 Markdown，请将 [**SaveFormat.Markdown**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) 作为参数传递给 [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-) 方法的第二个参数。也可以使用 [**MarkdownSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/markdownsaveoptions) 类指定导出工作表到 Markdown 的其他设置。  

以下代码示例演示如何使用 [**SaveFormat.Markdown**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) 枚举成员将活动工作表导出为 Markdown。请参考由代码生成的 [输出 Markdown 文件](md_sample.txt)。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir; // Adjust as needed for source directory
const outputDir = dataDir; // Adjust as needed for output directory

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.md"), AsposeCells.SaveFormat.Markdown);
```  

## **将Excel工作簿转换为JSON**  
Aspose.Cells 支持将工作簿转换为 Json（JavaScript 对象表示法）文件。  

以下代码示例演示如何使用 [**SaveFormat.Json**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) 枚举成员将活动工作表导出为 Json。请参考代码将 [源文件](Book1.xlsx) 转换为 [输出 Json 文件](Book1.Json)。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Convert the workbook to json file.
workbook.save(path.join(dataDir, "book1.json"));
```  

## **将Excel转换为XML**  
Aspose.Cells 支持将工作簿转换为 Excel 2003 电子表格 XML 和普通 XML 数据。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Load your source workbook
const workbook = new AsposeCells.Workbook(filePath);

// Save as Excel 2003 Spreadsheet XML
workbook.save("Spreadsheet.xml");

// Save as plain XML data
const xmlSaveOptions = new AsposeCells.XmlSaveOptions();
workbook.save("data.xml", xmlSaveOptions);
```  

## **将Excel工作簿转换为TIFF**  
Aspose.Cells 支持将工作簿转换为 TIFF 文件。  

下面的代码片段显示了如何将Excel转换为TIFF：  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");

// Open a template excel file
const workbook = new AsposeCells.Workbook(filePath);

// Save file to tiff
workbook.save("out.tiff");
```  

## **将Excel工作簿转换为DOCX**  
Aspose.Cells API 支持将电子表格转换为 DOCX 格式。将工作簿导出为 DOCX 时，请将 [**SaveFormat.Docx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) 作为参数传递给 [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-) 方法的第二个参数。也可以使用 [**DocxSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/docxsaveoptions) 类指定导出工作表到 DOCX 的其他设置。  

以下代码示例演示如何使用 [**SaveFormat.Docx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) 枚举成员将活动工作表导出为 DOCX。请参考由代码生成的 [输出 DOCX 文件](Book1.docx)。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir;
const outputDir = dataDir;

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.docx"), AsposeCells.SaveFormat.Docx);
```  

## **将Excel工作簿转换为PPTX**  
Aspose.Cells API 支持将电子表格转换为 PPTX 格式。将工作簿导出为 PPTX 时，请将 [**SaveFormat.Pptx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) 作为参数传递给 [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-) 方法的第二个参数。也可以使用 [**PptxSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/pptxsaveoptions) 类指定导出工作表到 PPTX 的其他设置。  

以下代码示例演示如何使用 [**SaveFormat.Pptx**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) 枚举成员将活动工作表导出为 PPTX。请参考由代码生成的 [输出 PPTX 文件](Book1.pptx)。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const sourceDir = dataDir;
const outputDir = path.join(dataDir, "output/");

// Open the template file
const workbook = new AsposeCells.Workbook(path.join(sourceDir, "Book1.xlsx"));

// Save as Markdown
workbook.save(path.join(outputDir, "Book1.pptx"), AsposeCells.SaveFormat.Pptx);
```  

## **将 Excel 工作簿转换为 EPUB**  
Aspose.Cells API 支持将电子表格转换为 EPUB 格式。将工作簿导出为 EPUB 时，请将 [**SaveFormat.Epub**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) 作为参数传递给 [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-) 方法的第二个参数。也可以使用 [**EBookSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/ebooksaveoptions) 类指定导出工作表到 Epub 的其他设置。  

以下代码示例演示如何使用 [**SaveFormat.Epub**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) 枚举成员将活动工作表导出为 EPUB。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Save it in EPUB format
workbook.save(path.join(dataDir, "ConvertingToEPUBFiles_out.epub"), AsposeCells.SaveFormat.Epub);
```  

## **将 Excel 工作簿转换为 AZW3**  
Aspose.Cells API 支持将电子表格转换为 AZW3 格式。将工作簿导出为 AZW3 时，请将 [**SaveFormat.Azw3**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) 作为参数传递给 [**Workbook.save(string, SaveOptions)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#save-string-saveoptions-) 方法的第二个参数。也可以使用 [**EBookSaveOptions**](https://reference.aspose.com/cells/nodejs-cpp/ebooksaveoptions) 类指定导出工作表到 AZW3 的其他设置。  

以下代码示例演示如何利用 [**SaveFormat.Azw3**](https://reference.aspose.com/cells/nodejs-cpp/saveformat) 枚举成员将活动工作表导出为 AZW3。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify the file path
const filePath = path.join(dataDir, "sample.xlsx");

// Load your sample excel file in a workbook object
const wb = new AsposeCells.Workbook(filePath);

// Save it in AZW3 format
wb.save(path.join(dataDir, "ConvertingToEPUBFiles_out.azw3"), AsposeCells.SaveFormat.Azw3);
```  

## **高级主题**  
- [将XLSB的修订版转换为XLSM](/cells/zh/nodejs-cpp/convert-revision-of-xlsb-to-xlsm/)  
- [HTML](/cells/zh/nodejs-cpp/convert-excel-to-html/)  
- [图像](/cells/zh/nodejs-cpp/convert-excel-to-image/)  
- [Json](/cells/zh/nodejs-cpp/convert-workbook-to-json/)  
- [将 Excel 工作簿转换为 Ods、Sxc 和 Fods（OpenOffice / LibreOffice calc）。](/cells/zh/nodejs-cpp/convert-excel-to-ods/)  
- [Pdf](/cells/zh/nodejs-cpp/convert-excel-workbook-to-pdf/)  
- [转换 Excel 为 CSV、TSV 和 Txt](/cells/zh/nodejs-cpp/convert-excel-to-csv-tsv-and-txt/)  
- [跟踪文档转换进度](/cells/zh/nodejs-cpp/track-document-conversion-progress/)  
- [将CSV、TSV和TXT转换为Excel](/cells/zh/nodejs-cpp/convert-csv-tsv-and-txt-to-excel/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
