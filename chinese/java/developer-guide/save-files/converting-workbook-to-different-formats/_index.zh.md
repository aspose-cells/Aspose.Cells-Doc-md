---
title: 将工作簿转换为不同格式
type: docs
weight: 20
url: /zh/java/converting-workbook-to-different-formats/
---

{{% alert color="primary" %}}

Aspose.Cells支持多种格式之间的转换。技术上，转换意味着以一种文件格式加载工作簿，然后将其保存为另一种格式。

{{% /alert %}}

## **将Excel转换为XPS**

XPS文档格式包括结构化的XML标记，用于定义文档的布局和每个页面的视觉外观，以及用于分发、存档、渲染、处理和打印文档的渲染规则。

XPS的标记语言是XAML的一个子集，允许它在文档中包含矢量图形元素，使用XAML标记Windows Presentation Foundation（WPF）基元。所使用的元素是用路径和其他几何原语描述的。

事实上，XPS文件是使用“Open Packaging Conventions”作为Unicode ZIP存档的Unicode ZIP存档，其中包含构成文档的文件。这些文件包括每个页面的XML标记文件、文本、嵌入字体、光栅图像、2D矢量图形以及数字版权管理信息。可以通过在支持ZIP文件的应用程序中打开XPS文件来简单地查看XPS文件的内容。

从Aspose.Cells 6.0.0开始，支持将Microsoft Excel转换为XPS。

### **将单个工作表转换为XPS**

以下示例显示了如何将Excel文件中的单个工作表转换为XPS。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingsingleWorksheetToXPS-ConvertingsingleWorksheetToXPS.java" >}}

### **将整个工作簿导出为XPS**

以下示例显示了如何将整个工作簿转换为XPS格式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ExportWholeWorkbookToXPS-ExportWholeWorkbookToXPS.java" >}}

### **快速将Excel转换为XPS**

以下示例显示了直接将Excel文件转换为XPS格式的简单方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-QuickExcelToXPSConversion-QuickExcelToXPSConversion.java" >}}

## **将Excel转换为MHTML文件**

[MHTML](https://en.wikipedia.org/wiki/MHTML)将普通HTML与外部资源（通常链接的内容如图像、动画、音频等）合并到一个文件中。它们通常用于扩展名为.mht的电子邮件。

{{% alert color="primary" %}}

Aspose.Cells支持读取和编写MHTML文件。

{{% /alert %}}

将电子表格转换为MHTML是一个快速的操作，如下所示。

下面的代码示例展示了如何将工作簿保存为一个MHTML文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToMHTMLFiles-ConvertingToMHTMLFiles.java" >}}

## **将Excel文件转换为HTML**

Aspose.Cells API提供了将电子表格导出为HTML格式的支持。为此，Aspose.Cells使用**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**类，它允许开发人员控制输出HTML的几个方面。

下面的代码演示了如何使用**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**类将Microsoft Excel文件导出为HTML格式，而不指定其他参数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToHTMLFiles-ConvertingToHTMLFiles.java" >}}

{{% alert color="primary" %}}

通过将 **[SaveFormat.HTML](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)** 传递给 **[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))** 方法，可以实现相同的结果。

{{% /alert %}}

### **为 HTML 设置图片首选项**

从 8.0.2 开始，Aspose.Cells 已经为 **[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)** 类公开了 **[ImageOptions](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)**，允许开发人员在将电子表格保存为 HTML 格式时指定图片首选项。

可以应用的图片设置包括：

- **[ImageType](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#ImageType)**: 获取或设置图像类型。请注意，输出 HTML 中的所有形状(包括图表)都作为图像呈现。
- **[Quality](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Quality)**: 获取或设置图像质量，范围为 0 到 100(Jpeg 格式时)。
- **[VerticalResolution](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#VerticalResolution)**: 获取或设置图像的垂直分辨率(每英寸的点数)。
- **[HorizontalResolution](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#HorizontalResolution)**: 获取或设置图像的水平分辨率(每英寸的点数)。
- **[TiffCompression](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#TiffCompression)**: 获取或设置图像格式为 Tiff 时的压缩类型。
- **[Transparent](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent)**: 当图像格式指定为 Png 时，表示图像的背景是否应透明。

下面的代码演示了如何使用 **[HtmlSaveOptions.ImageOptions](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)** 来指定不同的首选项。

|**导出前的电子表格视图**|**导出后的 HTML 视图**|
| :- | :- |
|![导出前的电子表格视图](converting-workbook-to-different-formats_1.png)|![导出后的 HTML 视图](converting-workbook-to-different-formats_2.png)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SettingImagePrefrencesforHTML-SettingImagePrefrencesforHTML.java" >}}

## **将 Excel 转换为 PDF 文件**

PDF 文档被广泛用作组织、政府部门和个人之间交换文档的标准格式。软件开发人员经常被要求设计一种简单地将 Microsoft Excel 文件转换为 PDF 文档的方法。Aspose.Cells 支持这些功能。本文介绍了如何进行操作。

### **将Excel转换为PDF**

Aspose.Cells for Java 2.3.0 引入了将电子表格转换为 PDF 的功能。从那个版本开始，Aspose.Cells 可以直接[将电子表格转换为 PDF](#直接转换) (包括[PDF/A](#将 Excel 电子表格保存为 PDF/A 编制文件))，无需其他产品。要在较早版本的 Aspose.Cells 中转换电子表格，[使用 Aspose.PDF 进行转换](#使用 AsposePDF 进行转换-AsposeCells 230 之前)。

Aspose.Cell's可以高度准确地将电子表格转换为 PDF 文件。但是，本文末尾列出了一些[限制](/cells/zh/java/converting-workbook-to-different-formats/#conversion-attributes)。

{{% alert color="primary" %}}

Aspose.Cells for Java 在输出文档中直接写入关于 API 和版本号的信息。例如，在将文档渲染为 PDF 时，Aspose.Cells for Java 会填充 **Application** 字段的值为 'Aspose.Cells'，**PDF Producer** 字段填充一个值，例如 'Aspose.Cells for Java v17.9'。

请注意，您不能指示Aspose.Cells for Java更改或删除输出文档中的这些信息。

{{% /alert %}}

#### **直接转换**

使用 **[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))** 方法直接将 Excel 文件保存为 PDF，并提供 **[SaveFormat.PDF](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)** 接口成员。直接转换是最高效的转换方法。它不会丢失数据或格式，而是使输出的 PDF 看起来与输入的 Excel 文件类似。

要在保存为 PDF 时指定安全选项，请使用 **[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-Excel2PDFConversion-Excel2PDFConversion.java" >}}

#### **高级转换**

您还可以选择使用 **[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** 类为转换设置不同属性。设置 **[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** 类的不同属性将使您对结果 PDF 文件的打印、字体、安全和压缩设置拥有控制权。最值得注意的属性是 **[Compliance](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance)**，它使您能够将 Excel 文件保存为 PDF/A 兼容的 PDF 文件。

##### **将 Excel 电子表格保存为 PDF/A 编制文件**

下面提供的代码片段演示了使用 **[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** 类将 Excel 文件保存为 PDF/A 兼容的 PDF 格式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AdvancedConversiontoPdf-AdvancedConversiontoPdf.java" >}}

#### **使用 Aspose.PDF 进行转换：Aspose.Cells 230 之前**

对于 Aspose.Cells 版本 2.3.0 之前的版本，您需要使用像[Aspose.PDF for Java](/pdf/java/)这样的组件将电子表格转换为 PDF 文件。Aspose.Cells 和 Aspose.PDF 一起工作，通过一个中间步骤将电子表格转换为 PDF。

使用 Aspose.Cells 和 Aspose.PDF 将电子表格转换为 PDF：

1. 通过调用其空构造函数，实例化 **[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)** 类的对象。
1. 使用 Aspose.Cells API 对电子表格进行所需的操作。
1. 调用 **[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))** 方法保存电子表格：
   1. 将文件格式设置为 XML。
   1. 从FileFormatType接口中选择Aspose_Pdf（一个预定义值）。这会将save方法指向生成与Aspose.PDF Schema兼容的XML形式的电子表格，以便Aspose.PDF for Java可以生成PDF文档。
1. 创建aspose.pdf包中的Pdf类的对象。
1. 调用Pdf类的bindXML方法并传递输出XML文件的名称。
1. 调用Pdf类的save方法生成PDF文档。

上述步骤在下面的示例中实现。

{{% alert color="primary" %}}

如果您的电子表格包含公式，最好在将电子表格渲染为PDF格式之前调用[Workbook.calculateFormula](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula())方法。这样做将确保重新计算基于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}

#### **转换属性**

我们努力改进每个版本的Aspose.Cells的转换和其他方面。Excel转PDF转换有一些限制。电子表格中指定的某些格式设置可能会丢失，并且不是所有绘图对象都受支持。

下表列出了使用Aspose.Cells导出到PDF时完全或部分支持的所有功能。该表格是不完全的，不包括所有电子表格属性。它还可以确定可能不受支持或仅部分支持的功能。

{{% alert color="primary" %}}

|**文档元素**|**属性**|**是否支持**|**备注**|
| :- | :- | :- | :- |
|对齐| |是| |
|旋转| |部分|仅支持90和-90。|
|背景设置| |是| |
|边框|颜色|是| |
|边框|线条样式|是| |
|边框|线宽|是| |
|单元格数据| |是| |
|注释| |否| |
|条件格式| |是| |
|文档属性| |是| |
|绘图对象| |是| |
|字体|大小|是| |
|字体|颜色|是| |
|字体|样式|是| |
|字体|下划线|是| |
|字体|效果|部分|仅支持删除线效果|
|图像| |是| |
|超链接| |是| |
|图表| |是| |
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
{{% /alert %}}
