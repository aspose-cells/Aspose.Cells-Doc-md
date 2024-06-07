---
title: Pdf
type: docs
weight: 220
url: /zh/net/convert-excel-to-pdf/
---

{{% alert color="primary" %}}

Aspose.Cells支持将Excel工作簿转换为PDF。在此示例中，我们将看到将Excel工作簿完全转换为PDF的过程。

{{% /alert %}}

## **将Excel工作簿转换为PDF**

PDF文件广泛用于组织、政府部门和个人之间交换文件。这是一种标准文档格式，软件开发人员经常被要求找到一种将Microsoft Excel文件转换为PDF文档的方法。

Aspose.Cells支持将Excel文件转换为PDF，并在转换中保持高视觉保真度。

{{% alert color="primary" %}}

Aspose.Cells for .NET直接在输出文档中写入有关API和版本号的信息。例如，在将文档呈现为PDF时，Aspose.Cells for .NET将**PDF Producer**字段填充为值，例如 'Aspose.Cells v23.2'。

请注意，您可以通过**[PdfSaveOptions.Producer](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/producer/)**属性来更改输出文档中的此信息。

{{% /alert %}}

### **直接转换**

Aspose.Cells for .NET支持将电子表格独立地转换为PDF，无需其他软件。只需使用 **[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)** 类的 **[Save](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** 方法将Excel文件保存为PDF。**[Save](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** 方法提供了 **[SaveFormat.Pdf](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** 枚举成员，用于将原生Excel文件转换为PDF格式。

按照以下步骤直接将Excel电子表格转换为PDF格式：

1. 通过调用空构造函数来实例化 **[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)** 类的对象。
1. 您可以打开/载入现有的模板文件，或者如果您是从头创建工作簿，可以跳过此步骤。
1. 使用Aspose.Cells的API在电子表格上进行任何工作（输入数据，应用格式，设置公式，插入图片或其他绘图对象等）。
1. 当电子表格代码完成时，调用 **[Workbook](https://reference.aspose.com/cells/net/aspose.cells/workbook)** 类的 **[Save](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)** 方法保存电子表格。

文件格式应为PDF，所以从 **[SaveFormat](https://reference.aspose.com/cells/net/aspose.cells/saveformat)** 枚举中选择 *Pdf*（预定义值）以生成最终的PDF文档。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

### **高级转换**

您还可以选择使用 **[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** 类设置转换的不同属性。设置 **[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** 类的不同属性可以控制输出PDF的打印、字体、安全性和压缩设置。最重要的属性是 **[Compliance](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**，它使您能够将Excel文件保存为PDF/A兼容的PDF文件。

#### **保存工作簿为PDF/A兼容文件**

下面的代码片段演示了如何使用 **[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** 类将Excel文件保存为PDF/A兼容PDF格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

请注意，**[Compliance](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)** 属性是在发布Aspose.Cells for .NET 5.3.0时添加的。

{{% /alert %}}

#### **设置PDF创建时间**

使用 **[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** 类，您可以获取或设置PDF的创建时间。以下代码演示了如何使用 **[PdfSaveOptions.CreatedTime](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime)** 属性来设置PDF文件的创建时间。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

#### **设置AccessibilityExtractContent选项**

使用 **[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** 类，您可以获取或设置PDF **[AccessibilityExtractContent](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent)** 选项以控制转换后PDF中的内容访问。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

#### **导出自定义属性至PDF**

通过 **[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)** 类，您可以将源工作簿中的自定义属性导出到PDF。可为每个属性指定导出方式，这些属性可以在Adobe Acrobat Reader中通过单击“文件”然后单击属性来查看，如下图所示。可以从此处下载模板文件"sourceWithCustProps.xlsx" 进行测试，输出的PDF文件"outSourceWithCustProps" 可在此处进行分析。

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

### **转换属性**

我们努力在每个新版本中增强转换功能。Aspose.Cell的Excel转PDF转换仍然有一些限制。在转换为PDF格式时不支持MapChart。此外，某些绘图对象不受良好支持。

接下来的表格列出了使用Aspose.Cells导出为PDF时完全或部分支持的所有功能。这张表格不是最终版本，也没有涵盖所有电子表格属性，但它确实识别了那些在转换为PDF时不受支持或仅部分支持的功能。

|**文档元素**|**属性**|**是否支持**|**备注**|
| :- | :- | :- | :- |
|对齐| |是| |
|背景设置| |是| |
|边框|颜色|是| |
|边框|线条样式|是| |
|边框|线宽|是| |
|单元格数据| |是| |
|评论| |是| |
|条件格式| |是| |
|文档属性| |是| |
|绘图对象| |部分支持|不支持绘图对象的阴影和3D效果；WordArt和SmartArt部分支持。|
|字体|大小|是| |
|字体|颜色|是| |
|字体|样式|是| |
|字体|下划线|是| |
|字体|效果|是||
|图像| |是| |
|超链接| |是| |
|图表| |部分支持|不支持MapChart。|
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
|从右向左（RTL）语言| |是| |

{{% alert color="primary" %}}

如果您的电子表格中包含公式，最好在将电子表格呈现为PDF格式之前调用**[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)**。这样做将确保重新计算基于公式的值，并正确值呈现在PDF中。

{{% /alert %}}

## **高级主题**
- [添加PDF书签](/cells/zh/net/add-pdf-bookmarks/)
- [使用命名目标添加PDF书签](/cells/zh/net/add-pdf-bookmarks-with-named-destinations/)
- [在输出PDF中避免空白页当没有内容需要打印时](/cells/zh/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [在保存为PDF时仅更改特定Unicode字符的字体](/cells/zh/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [在将MS Excel工作簿渲染为PDF时控制加载外部资源](/cells/zh/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [将XLSX文件转换为PDF格式](/cells/zh/net/convert-xlsx-file-to-pdf-format/)
- [将Excel文件转换为与PDFA-1a兼容的PDF格式](/cells/zh/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [将带有图像或图表的XLS文件转换为PDF](/cells/zh/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [为图表工作表创建PdfBookmarkEntry](/cells/zh/net/create-pdfbookmarkentry-for-chart-sheet/)
- [使所有工作表列适合单个PDF页面](/cells/zh/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [在使用DrawObjectEventHandler类将Excel渲染为PDF时获取DrawObject和Bound](/cells/zh/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [在渲染Excel文件时获取字体替代的警告](/cells/zh/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [在将Excel渲染为PDF时忽略错误](/cells/zh/net/ignore-errors-while-rendering-excel-to-pdf/)
- [限制生成的页面数-从Excel到PDF的转换](/cells/zh/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [在保存为PDF时打印评论](/cells/zh/net/print-comments-while-saving-to-pdf/)
- [在将Excel转为PDF时呈现Office附加组件](/cells/zh/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [每个Excel工作表呈现一个PDF页面-从Excel到PDF的转换](/cells/zh/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [通过Aspose.Cells在输出PDF中呈现Unicode补充字符](/cells/zh/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [重新采样添加的图像-从Excel到PDF的转换](/cells/zh/net/resampling-added-images-excel-to-pdf-conversion/)
- [将每个工作表保存为不同的PDF文件](/cells/zh/net/save-each-worksheet-to-a-different-pdf-file/)
- [将Excel保存为标准或最小尺寸的PDF](/cells/zh/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [保存指定的工作表至PDF](/cells/zh/net/save-specified-worksheets-to-pdf/)
- [安全的PDF文档](/cells/zh/net/secure-pdf-documents/)
- [指定如何在输出PDF和图像中跨越字符串](/cells/zh/net/specify-how-to-cross-string-in-output-pdf-and-image/)
