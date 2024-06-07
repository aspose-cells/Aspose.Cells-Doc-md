---
title: Pdf
type: docs
weight: 220
url: /zh/python-net/convert-excel-to-pdf/
description: 学习如何使用Aspose.Cells for Python通过.NET API将Excel转换为PDF。
keywords: Python将Excel转换为PDF，使用Python将Excel转换为PDF，Python保存Excel为PDF，Python中的Excel转换为PDF。
---

{{% alert color="primary" %}}

Aspose.Cells for Python通过.NET支持将Excel工作簿直接转换为PDF。在此示例中，我们将看到将Excel工作簿完全转换为PDF。

{{% /alert %}}

## **将Excel工作簿转换为PDF**

PDF文件广泛用于组织、政府部门和个人之间交换文件。这是一种标准文档格式，软件开发人员经常被要求找到一种将Microsoft Excel文件转换为PDF文档的方法。

Aspose.Cells for Python通过.NET支持将Excel文件转换为PDF，并且在转换过程中保持高度视觉保真度。

{{% alert color="primary" %}}

Aspose.Cells for Python通过.NET直接在输出文档中写入关于API和版本号的信息。例如，在将文档渲染为PDF时，Aspose.Cells for Python通过.NET会在**PDF Producer**字段中填充值，例如 'Aspose.Cells for Python通过.NET v23.2'。

请注意，您可以通过**[PdfSaveOptions.producer](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/producer/)**属性更改输出文档中的此信息。

{{% /alert %}}

### **直接转换**

Aspose.Cells for Python通过.NET支持与其他软件独立地将电子表格转换为PDF。只需使用**[Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)**类的**[save](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)**方法将Excel文件保存为PDF。**[save](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)**方法提供**[SaveFormat.PDF](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)**枚举成员，将原生Excel文件转换为PDF格式。

按照以下步骤直接将Excel电子表格转换为PDF格式：

1. 通过调用其空构造函数来实例化**[Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)**类的对象。
1. 您可以打开/载入现有的模板文件，或者如果您是从头创建工作簿，可以跳过此步骤。
1. 使用Aspose.Cells for Python通过.NET的API在电子表格上执行任何操作（输入数据，应用格式，设置公式，插入图片或其他绘图对象等）。
1. 当电子表格代码完成时，调用**[Workbook](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)**类的**[save](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)**方法保存电子表格。

文件格式应为PDF，因此从**[SaveFormat](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)**枚举中选择*PDF*（预定义值）以生成最终PDF文档。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-XlstoPDFDirectConversation-1.py" >}}

### **高级转换**

您还可以选择使用**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)**类设置转换的不同属性。设置**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)**类的不同属性可控制输出PDF的打印、字体、安全和压缩设置。最重要的属性是**[PdfSaveOptions.compliance](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/)**，它使您能够将Excel文件保存为符合PDF/A标准的PDF文件。

#### **保存工作簿为PDF/A兼容文件**

下面提供的代码片段演示了如何使用**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)**类将Excel文件保存为符合PDF/A标准的PDF格式。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AdvancedConversiontoPdf-1.py" >}}

{{% alert color="primary" %}}

请注意，**[PdfSaveOptions.compliance](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/)** 属性是通过Aspose.Cells for Python via .NET发布的，适用于. NET 5.3.0 版本。

{{% /alert %}}

#### **设置PDF创建时间**

使用**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)** 类，可以获取或设置PDF文件的创建时间。以下代码示例展示了使用**[PdfSaveOptions.created_time](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/created_time/)**属性设置PDF文件的创建时间。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetPDFCreationTime-1.py" >}}

#### **设置AccessibilityExtractContent选项**

使用**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)** 类，可以获取或设置PDF **[PdfSecurityOptions.accessibility_extract_content](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/accessibility_extract_content/)** 选项来控制转换后PDF中内容的访问权限。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetContentCopyForAccessibility-1.py" >}}

#### **导出自定义属性至PDF**

使用**[PdfSaveOptions](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)** 类，可以将源工作簿中的自定义属性导出到PDF中。**[PdfCustomPropertiesExport](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfcustompropertiesexport/)**枚举类型用于指定导出属性的方式。这些属性可以在Adobe Acrobat Reader中观察，方法是单击“文件”，然后选择属性；示例文件“sourceWithCustProps.xlsx”可以从[这里](sourceWithCustProps.xlsx)下载以供测试，输出的PDF文件“outSourceWithCustProps”可以从[这里](outSourceWithCustProps.pdf)进行分析。

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ExportCustomPropertiesToPdf-1.py" >}}

### **转换属性**

我们努力在每个新版本中增强转换功能。Aspose.Cell的Excel转PDF转换仍然有一些限制。在转换为PDF格式时不支持MapChart。此外，某些绘图对象不受良好支持。

下表列出了使用Aspose.Cells for Python via .NET导出PDF时完全或部分支持的所有功能。该表未包含所有电子表格属性，但识别了不支持或部分支持的特性以进行PDF转换。

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

如果电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)方法。这样做可确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}

## **高级主题**
- [添加PDF书签](/cells/zh/python-net/add-pdf-bookmarks/)
- [使用命名目标添加PDF书签](/cells/zh/python-net/add-pdf-bookmarks-with-named-destinations/)
- [在输出PDF中避免空白页当没有内容需要打印时](/cells/zh/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [将XLSX文件转换为PDF格式](/cells/zh/python-net/convert-xlsx-file-to-pdf-format/)
- [将Excel文件转换为与PDFA-1a兼容的PDF格式](/cells/zh/python-net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [将带有图像或图表的XLS文件转换为PDF](/cells/zh/python-net/convert-xls-file-with-images-or-charts-to-pdf/)
- [为图表工作表创建PdfBookmarkEntry](/cells/zh/python-net/create-pdfbookmarkentry-for-chart-sheet/)
- [使所有工作表列适合单个PDF页面](/cells/zh/python-net/fit-all-worksheet-columns-on-single-pdf-page/)
- [在将Excel渲染为PDF时忽略错误](/cells/zh/python-net/ignore-errors-while-rendering-excel-to-pdf/)
- [限制生成的页面数-从Excel到PDF的转换](/cells/zh/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [在保存为PDF时打印评论](/cells/zh/python-net/print-comments-while-saving-to-pdf/)
- [在将Excel转为PDF时呈现Office附加组件](/cells/zh/python-net/render-office-add-ins-while-converting-excel-to-pdf/)
- [每个Excel工作表呈现一个PDF页面-从Excel到PDF的转换](/cells/zh/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [通过Aspose.Cells在输出PDF中呈现Unicode补充字符](/cells/zh/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [重新采样添加的图像-从Excel到PDF的转换](/cells/zh/python-net/resampling-added-images-excel-to-pdf-conversion/)
- [将每个工作表保存为不同的PDF文件](/cells/zh/python-net/save-each-worksheet-to-a-different-pdf-file/)
- [将Excel保存为标准或最小尺寸的PDF](/cells/zh/python-net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [保存指定的工作表至PDF](/cells/zh/python-net/save-specified-worksheets-to-pdf/)
- [安全的PDF文档](/cells/zh/python-net/secure-pdf-documents/)
- [指定如何在输出PDF和图像中跨越字符串](/cells/zh/python-net/specify-how-to-cross-string-in-output-pdf-and-image/)
