---
title: Pdf
type: docs
weight: 220
url: /zh/net/convert-excel-to-pdf/
---

{{% alert color="primary" %}}

Aspose.Cells支持将Excel工作簿转换为PDF。在此示例中，我们将看到完整将Excel工作簿转换为PDF的过程。

{{% /alert %}}

## **将Excel工作簿转换为PDF**

PDF文件被广泛用于组织、政府部门和个人之间交换文档。它是一种标准文档格式，软件开发人员经常被要求找到一种方法将Microsoft Excel文件转换为PDF文档。

Aspose.Cells支持将Excel文件转换为PDF，并在转换过程中保持高度的视觉保真度。

{{% alert color="primary" %}}

Aspose.Cells for .NET 直接在输出文档中写入 API 和版本号的信息。例如，在将文档渲染为 PDF 时，Aspose.Cells for .NET 在 **PDF 生成器** 字段中填充值，例如 'Aspose.Cells v23.2'。

请注意，您可以通过 [**PdfSaveOptions.Producer**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/producer/) 属性在输出文档中更改此信息。

{{% /alert %}}

### **直接转换**

Aspose.Cells for .NET支持将电子表格独立转换为PDF，无需其他软件。只需使用[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类的[**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)方法将Excel文件保存为PDF。[**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)方法提供了将原生Excel文件转换为PDF格式的[**SaveFormat.Pdf**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)枚举成员。

按以下步骤直接将Excel电子表格转换为PDF格式：

通过调用其空构造函数实例化[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类的对象。
1. 您可以打开/加载现有模板文件，或者如果您是从头开始创建工作簿，则跳过此步骤。
1. 使用Aspose.Cells的API在电子表格上进行任何工作（输入数据，应用格式，设置公式，插入图片或其他绘图对象等）。
当电子表格代码完成时，调用[**Workbook**](https://reference.aspose.com/cells/net/aspose.cells/workbook)类的[**Save**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)方法保存电子表格。

文件格式应为PDF，因此从[**SaveFormat**](https://reference.aspose.com/cells/net/aspose.cells/saveformat)枚举中选择*Pdf*（预定义值）生成最终PDF文档。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

### **高级转换**

您还可以选择使用[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)类来设置转换的不同属性。设置[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)类的不同属性可控制输出PDF的打印、字体、安全性和压缩设置。最重要的属性是[**Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)，它使您能够将Excel文件保存为PDF/A兼容的PDF文件。

#### **将工作簿保存为PDF/A兼容文件**

下面提供的代码片段演示了如何使用[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)类将Excel文件保存为PDF/A兼容的PDF格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

请注意，随Aspose.Cells for .NET 5.3.0版本发布，添加了[**Compliance**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)属性。

{{% /alert %}}

#### **设置PDF创建时间**

使用[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)类，您可以获取或设置PDF创建时间。以下代码演示了使用[**PdfSaveOptions.CreatedTime**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime)属性设置PDF文件的创建时间。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

#### **设置ContentCopyForAccessibility选项**

使用[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)类，您可以获取或设置PDF的[**AccessibilityExtractContent**](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent)选项，以控制转换后PDF中的内容访问。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

#### **导出自定义属性到PDF**

使用[**PdfSaveOptions**](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)类，您可以将源工作簿中的自定义属性导出到PDF。提供了[**PdfCustomPropertiesExport**](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport)枚举用于指定属性的导出方式。这些属性可以通过单击“文件”然后选择“属性”在Adobe Acrobat Reader中观察。模板文件"sourceWithCustProps.xlsx"可在[此处](sourceWithCustProps.xlsx)下载进行测试，输出的PDF文件"outSourceWithCustProps"可在[此处](outSourceWithCustProps.pdf)进行分析。

![todo:image_alt_text](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

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

如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用[**Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)。这样做将确保重新计算公式相关值，并在PDF中呈现正确的值。

{{% /alert %}}

## **高级主题**
- [添加PDF书签](/cells/zh/net/add-pdf-bookmarks/)
- [使用命名目标添加PDF书签](/cells/zh/net/add-pdf-bookmarks-with-named-destinations/)
- [当没有需要打印的内容时，避免在输出PDF中出现空白页](/cells/zh/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [在保存为PDF时仅更改特定Unicode字符的字体](/cells/zh/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [控制在将MS Excel工作簿渲染为PDF时加载外部资源](/cells/zh/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [将XLSX文件转换为PDF格式](/cells/zh/net/convert-xlsx-file-to-pdf-format/)
- [将 Excel 文件转换为兼容 PDFA-1a 格式的 PDF](/cells/zh/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [将带有图片或图表的XLS文件转换为PDF](/cells/zh/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [为图表工作表创建PdfBookmarkEntry](/cells/zh/net/create-pdfbookmarkentry-for-chart-sheet/)
- [将所有工作表列调整到单个PDF页面上](/cells/zh/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [在使用DrawObjectEventHandler类呈现到PDF时获取DrawObject和边界](/cells/zh/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [在呈现Excel文件时获取字体替换的警告](/cells/zh/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [在将Excel渲染为PDF时忽略错误](/cells/zh/net/ignore-errors-while-rendering-excel-to-pdf/)
- [限制生成的页面数量-从Excel转换为PDF](/cells/zh/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [保存为PDF时打印注释](/cells/zh/net/print-comments-while-saving-to-pdf/)
- [在将Excel转换为PDF时呈现Office加载项](/cells/zh/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [将每个Excel工作表呈现为一个PDF页面-从Excel转换为PDF](/cells/zh/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [通过Aspose.Cells在输出PDF中呈现Unicode补充字符](/cells/zh/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [重新采样添加的图像-从Excel转换为PDF](/cells/zh/net/resampling-added-images-excel-to-pdf-conversion/)
- [将每个工作表保存为不同的PDF文件](/cells/zh/net/save-each-worksheet-to-a-different-pdf-file/)
- [以标准或最小尺寸保存Excel到PDF](/cells/zh/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [将指定的工作表保存为 PDF](/cells/zh/net/save-specified-worksheets-to-pdf/)
- [安全的PDF文件](/cells/zh/net/secure-pdf-documents/)
- [指定如何在输出PDF和图像中跨越字符串](/cells/zh/net/specify-how-to-cross-string-in-output-pdf-and-image/)
