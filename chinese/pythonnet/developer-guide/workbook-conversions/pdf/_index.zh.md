---
title: Pdf
type: docs
weight: 220
url: /zh/python-net/convert-excel-to-pdf/
description: 学习如何使用Aspose.Cells for Python via .NET API将Excel转换为PDF。
keywords: Python将Excel转换为PDF，使用Python将Excel转换为PDF，Python保存Excel为PDF，Python中的Excel转换为PDF。
---

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET支持将Excel工作簿转换为PDF。在此示例中，我们将看到如何将Excel工作簿完全转换为PDF。

{{% /alert %}}

## **将Excel工作簿转换为PDF**

PDF文件被广泛用于组织、政府部门和个人之间交换文档。它是一种标准文档格式，软件开发人员经常被要求找到一种方法将Microsoft Excel文件转换为PDF文档。

Aspose.Cells for Python via .NET 支持将 Excel 文件转换为 PDF，并在转换中保持高视觉保真度。

{{% alert color="primary" %}}

Aspose.Cells for Python via .NET直接在输出文档中写入有关API和版本号的信息。例如，在将文档呈现为PDF时，Aspose.Cells for Python via .NET使用值，如 'Aspose.Cells for Python via .NET v23.2'，填充**PDF Producer**字段。

请注意，您可以通过 [**PdfSaveOptions.producer**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/producer/) 属性在输出文档中更改此信息。

{{% /alert %}}

### **直接转换**

Aspose.Cells for Python via .NET支持独立于其他软件从电子表格转换为PDF。只需使用[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类的[**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)方法将Excel文件保存为PDF。[**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)方法提供[**SaveFormat.PDF**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)枚举成员，将原生Excel文件转换为PDF格式。

按以下步骤直接将Excel电子表格转换为PDF格式：

通过调用其空构造函数实例化[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类的对象。
1. 您可以打开/加载现有模板文件，或者如果您是从头开始创建工作簿，则跳过此步骤。
1. 使用Aspose.Cells for Python via .NET的API对电子表格进行任何工作（输入数据、应用格式、设置公式、插入图片或其他绘图对象等）。
当电子表格代码完成时，调用[**Workbook**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook)类的[**save**](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/save/#str-aspose.cells.SaveFormat)方法保存电子表格。

文件格式应为PDF，因此从[**SaveFormat**](https://reference.aspose.com/cells/python-net/aspose.cells/saveformat/)枚举中选择*PDF*（预定义值）来生成最终PDF文档。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-XlstoPDFDirectConversation-1.py" >}}

### **高级转换**

您还可以选择使用[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)类来设置转换的不同属性。设置[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)类的不同属性可控制输出PDF的打印、字体、安全性和压缩设置。最重要的属性是[**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/)，它使您能够将Excel文件保存为PDF/A兼容的PDF文件。

#### **将工作簿保存为PDF/A兼容文件**

下面提供的代码片段演示了如何使用[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)类将Excel文件保存为PDF/A兼容的PDF格式。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-AdvancedConversiontoPdf-1.py" >}}

{{% alert color="primary" %}}

请注意，[**PdfSaveOptions.compliance**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/compliance/)属性是在Aspose.Cells for Python via .NET for .NET 5.3.0中新增的。

{{% /alert %}}

#### **设置PDF创建时间**

使用[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)类，您可以获取或设置PDF创建时间。以下代码演示了使用[**PdfSaveOptions.created_time**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions/created_time/)属性设置PDF文件的创建时间。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetPDFCreationTime-1.py" >}}

#### **设置ContentCopyForAccessibility选项**

使用[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)类，您可以获取或设置PDF的[**PdfSecurityOptions.accessibility_extract_content**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/accessibility_extract_content/)选项，以控制转换后PDF中的内容访问。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-SetContentCopyForAccessibility-1.py" >}}

#### **导出自定义属性到PDF**

使用[**PdfSaveOptions**](https://reference.aspose.com/cells/python-net/aspose.cells/pdfsaveoptions)类，您可以将源工作簿中的自定义属性导出到PDF。提供了[**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/python-net/aspose.cells.rendering/pdfcustompropertiesexport/)枚举用于指定属性的导出方式。这些属性可以通过单击“文件”然后选择“属性”在Adobe Acrobat Reader中观察。模板文件"sourceWithCustProps.xlsx"可在[此处](sourceWithCustProps.xlsx)下载进行测试，输出的PDF文件"outSourceWithCustProps"可在[此处](outSourceWithCustProps.pdf)进行分析。

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "PDF-ExportCustomPropertiesToPdf-1.py" >}}

### **转换属性**

我们致力于增强每个新版本的转换功能。 Aspose.Cells的Excel转PDF转换仍然存在一些限制。 在转换为PDF格式时不支持MapChart。 还有一些绘图对象支持不佳。

下表列出了使用 Aspose.Cells for Python via .NET 导出PDF时完全或部分支持的所有功能。该表不是最终版本，也不涵盖所有电子表格属性，但它确实确定了不受支持或部分支持的功能，转换为PDF。

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

如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用[Workbook.calculate_formula](https://reference.aspose.com/cells/python-net/aspose.cells/workbook/calculate_formula/#)方法。这样做将确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}

## **高级主题**
- [添加PDF书签](/cells/zh/python-net/add-pdf-bookmarks/)
- [使用命名目标添加PDF书签](/cells/zh/python-net/add-pdf-bookmarks-with-named-destinations/)
- [当没有需要打印的内容时，避免在输出PDF中出现空白页](/cells/zh/python-net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [将XLSX文件转换为PDF格式](/cells/zh/python-net/convert-xlsx-file-to-pdf-format/)
- [将 Excel 文件转换为兼容 PDFA-1a 格式的 PDF](/cells/zh/python-net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [将带有图片或图表的XLS文件转换为PDF](/cells/zh/python-net/convert-xls-file-with-images-or-charts-to-pdf/)
- [为图表工作表创建PdfBookmarkEntry](/cells/zh/python-net/create-pdfbookmarkentry-for-chart-sheet/)
- [将所有工作表列调整到单个PDF页面上](/cells/zh/python-net/fit-all-worksheet-columns-on-single-pdf-page/)
- [在将Excel渲染为PDF时忽略错误](/cells/zh/python-net/ignore-errors-while-rendering-excel-to-pdf/)
- [限制生成的页面数量-从Excel转换为PDF](/cells/zh/python-net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [保存为PDF时打印注释](/cells/zh/python-net/print-comments-while-saving-to-pdf/)
- [在将Excel转换为PDF时呈现Office加载项](/cells/zh/python-net/render-office-add-ins-while-converting-excel-to-pdf/)
- [将每个Excel工作表呈现为一个PDF页面-从Excel转换为PDF](/cells/zh/python-net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [通过Aspose.Cells在输出PDF中呈现Unicode补充字符](/cells/zh/python-net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [重新采样添加的图像-从Excel转换为PDF](/cells/zh/python-net/resampling-added-images-excel-to-pdf-conversion/)
- [将每个工作表保存为不同的PDF文件](/cells/zh/python-net/save-each-worksheet-to-a-different-pdf-file/)
- [以标准或最小尺寸保存Excel到PDF](/cells/zh/python-net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [将指定的工作表保存为 PDF](/cells/zh/python-net/save-specified-worksheets-to-pdf/)
- [安全的PDF文件](/cells/zh/python-net/secure-pdf-documents/)
- [指定如何在输出PDF和图像中跨越字符串](/cells/zh/python-net/specify-how-to-cross-string-in-output-pdf-and-image/)
