---
title: 将工作簿转换为不同格式
type: docs
weight: 20
url: /zh/java/converting-workbook-to-different-formats/
---

{{% alert color="primary" %}}

Aspose.Cells支持多种格式之间的转换。技术上，转换意味着加载一个工作簿的一个文件格式，然后将其保存为另一个文件格式。

{{% /alert %}}

## **将Excel转换为XPS**

XPS文档格式包含结构化的XML标记，定义文档的布局和每个页面的视觉外观，以及用于分发、存档、渲染、处理和打印文档的呈现规则。

XPS的标记语言是XAML的一个子集，允许它在文档中包含矢量图形元素，使用XAML标记Windows Presentation Foundation (WPF)原语。所使用的元素用路径和其他几何原语来描述。

实际上，XPS文件是使用Open Packaging Conventions的Unicode ZIP归档，其中包含组成文档的文件。这些文件包括每个页面的XML标记文件、文本、嵌入字体、光栅图像、2D矢量图形，以及数字版权管理信息。XPS文件的内容可以通过简单地在支持ZIP文件的应用程序中打开来检查。

从Aspose.Cells 6.0.0开始，支持将Microsoft Excel转换为XPS。

### **将单个工作表转换为XPS**

以下示例显示如何将Excel文件中的单个工作表转换为XPS。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingsingleWorksheetToXPS-ConvertingsingleWorksheetToXPS.java" >}}

### **将整个工作簿导出为XPS**

以下示例显示如何将整个工作簿转换为XPS格式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ExportWholeWorkbookToXPS-ExportWholeWorkbookToXPS.java" >}}

### **快速将Excel转换为XPS格式**

以下示例展示了一种直接将Excel文件转换为XPS格式的简单方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-QuickExcelToXPSConversion-QuickExcelToXPSConversion.java" >}}

## **将Excel转换为MHTML文件**

[MHTML](https://en.wikipedia.org/wiki/MHTML)结合了普通HTML和外部资源；换句话说，通常链接的像图像、动画、音频等内容合并为一个文件。它们用于扩展名为.mht的电子邮件。

{{% alert color="primary" %}}

Aspose.Cells支持读取和写入MHTML文件。

{{% /alert %}}

将电子表格转换为MHTML是一个快速的操作，如下所示。

下面的代码示例显示了如何将工作簿保存为MHTML文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToMHTMLFiles-ConvertingToMHTMLFiles.java" >}}

## **将Excel文件转换为HTML**

Aspose.Cells API支持将电子表格导出为HTML格式。为此，Aspose.Cells使用**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**类，允许开发人员控制输出HTML的几个方面。

下面的代码演示了如何使用**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**类导出Microsoft Excel文件到HTML格式，而不指定其他参数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToHTMLFiles-ConvertingToHTMLFiles.java" >}}

{{% alert color="primary" %}}

通过将**[SaveFormat.HTML](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)**传递给**[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))**方法，您可以达到相同的结果。

{{% /alert %}}

### **为HTML设置图像首选项**

从8.0.2开始，Aspose.Cells已经在HtmlSaveOptions类中公开了**[ImageOptions](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)**，允许开发人员在将电子表格保存为HTML格式时指定图像首选项。

可以应用的图像设置有：

- **[ImageType](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#ImageType)**：获取或设置图像类型。请注意，在输出的HTML中，包括图表在内的所有形状都会呈现为图像。
- **[Quality](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Quality)**：获取或设置当ImageFormat指定为Jpeg时，图像质量在0到100之间。
- **[VerticalResolution](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#VerticalResolution)**：获取或设置图像的垂直分辨率（每英寸点数）。
- **[HorizontalResolution](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#HorizontalResolution)**：获取或设置图像的水平分辨率（每英寸点数）。
- **[TiffCompression](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#TiffCompression)**：获取或设置图像格式指定为Tiff时的压缩类型。
- **[Transparent](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent)**：如果ImageFormat指定为Png，则指示图像背景是否应为透明。

以下代码演示了如何使用**[HtmlSaveOptions.ImageOptions](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)**来指定不同的首选项。

|**导出前的电子表格视图**|**导出后的HTML视图**|
| :- | :- |
|![导出前的电子表格视图](converting-workbook-to-different-formats_1.png)|![导出后的HTML视图](converting-workbook-to-different-formats_2.png)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SettingImagePrefrencesforHTML-SettingImagePrefrencesforHTML.java" >}}

## **将Excel转换为PDF文件**

PDF文档被广泛用作组织机构、政府部门和个人之间交换文档的标准格式。软件开发人员经常被要求设计一种轻松将Microsoft Excel文件转换为PDF文档的方式。Aspose.Cells支持这些功能。本文展示了如何做。

### **将Excel转换为PDF**

Aspose.Cells for Java 2.3.0 引入了 Microsoft Excel 到 PDF 的转换功能。从该版本开始，Aspose.Cells 可以[直接将电子表格转换为 PDF](#direct-conversion)（包括[PDF/A](#saving-excel-spreadsheets-to-pdfa-complied-files)），无需另一种产品。要在较旧版本的 Aspose.Cells 中转换电子表格，[请使用 Aspose.PDF 进行转换](#conversion-with-asposepdf-asposecells-prior-to-230)。

Aspose.Cells将电子表格转换为PDF时具有高度的准确性和保真度。但是，本文末尾列出了一些[限制](/cells/zh/java/converting-workbook-to-different-formats/#conversion-attributes)。

{{% alert color="primary" %}}

Aspose.Cells for Java 直接将有关 API 和版本号的信息写入输出文档。例如，在将文档渲染为 PDF 时，Aspose.Cells for Java 将**应用程序**字段填充为值 'Aspose.Cells'，并将**PDF 生成器**字段填充为值，例如 'Aspose.Cells for Java v17.9'。

请注意，您无法指示 Aspose.Cells for Java 更改或删除输出文档中的此信息。

{{% /alert %}}

#### **直接转换**

使用**[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))**方法直接将Excel文件保存为PDF，并提供**[SaveFormat.PDF](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)**接口成员。这种直接转换是最有效的转换方法。它不会丢失数据或格式，而且保持所输出PDF看起来像输入的Excel文件。

要在保存为PDF时指定安全选项，请使用**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-Excel2PDFConversion-Excel2PDFConversion.java" >}}

#### **高级转换**

您还可以选择使用 **[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** 类来设置转换的不同属性。设置  **[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** 类的不同属性将使您控制结果 PDF 文件的打印，字体，安全性和压缩设置。最值得注意的属性是 **[Compliance](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance)**，它使您能够将 Excel 文件保存为符合 PDF/A 标准的 PDF 文件。

##### **将 Excel 电子表格保存为 PDF/A 标准文件**

下面提供的代码片段演示了使用 **[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)** 类将 Excel 文件保存为符合 PDF/A 标准的 PDF 格式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AdvancedConversiontoPdf-AdvancedConversiontoPdf.java" >}}

#### **使用 Aspose.Pdf 进行转换：之前的 Aspose.Cells 优于 2.3.0**

对于版本在 2.3.0 之前的 Aspose.Cells，您需要使用类似 [Aspose.PDF for Java](/pdf/java/) 的组件将电子表格转换为 PDF 文件。Aspose.Cells 和 Aspose.PDF 配合使用通过一个中间步骤将电子表格转换为 PDF。

使用 Aspose.Cells 和 Aspose.PDF 将电子表格转换为 PDF：

1. 通过调用其空构造函数，实例化 **[Workbook](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)** 类的对象。
1. 使用 Aspose.Cells API 在电子表格上执行您期望的操作。
1. 调用 **[Workbook.save](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))** 方法保存电子表格：
   1. 将文件格式设置为 XML。
   1. 从 FileFormatType 接口中选择 Aspose_Pdf（一个预定义值）。这将指示保存方法生成一个与 Aspose.PDF Schema 兼容的 XML 格式电子表格，以便随后 Aspose.PDF for Java 生成 PDF 文档。
1. 创建 aspose.pdf 包中 Pdf 类的对象时，即建立 XML 文件 。
1. 调用 Pdf 类的 bindXML 方法，并传递输出 XML 文件的名称。
1. 调用 Pdf 类的 save 方法生成 PDF 文档。

上述步骤在下面的示例中实现。

{{% alert color="primary" %}}

如果您的电子表格包含公式，则最好在将电子表格呈现为 PDF 格式之前调用 **[Workbook.calculateFormula](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula())** 方法。这样做可以确保重新计算公式依赖值，并将正确的值呈现在 PDF 中。

{{% /alert %}}

#### **转换属性**

我们努力改进每个版本的 Aspose.Cells 的转换和其他方面。Excel 到 PDF 的转换有一些限制。电子表格中指定的一些格式设置可能会丢失，而且不是所有绘图对象都受支持。

下表列出了使用 Aspose.Cells 导出为 PDF 时完全或部分支持的所有功能。该表格不是最终版本，也不包括所有电子表格属性。它还可以识别可能不受支持或部分支持的功能。

{{% alert color="primary" %}}

|**文档元素**|**属性**|**净支持**|**备注**|
| :- | :- | :- | :- |
|对齐| |支持| |
|旋转| |部分|仅支持 90 和 -90。|
|背景设置| |支持| |
|边框|颜色|支持| |
|边框|线条样式|支持| |
|边框|线宽|支持| |
|单元格数据| |是| |
|评论| |否| |
|条件格式| |是| |
|文档属性| |是| |
|绘图对象| |是| |
|字体|大小|是| |
|字体|颜色|是| |
|字体|样式|是| |
|字体|下划线|是| |
|字体|效果|部分支持|仅支持删除线效果|
|图像| |是| |
|超链接| |是| |
|图表| |是| |
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
