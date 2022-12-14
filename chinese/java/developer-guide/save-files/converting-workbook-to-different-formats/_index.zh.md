---
title: 将工作簿转换为不同格式
type: docs
weight: 20
url: /zh/java/converting-workbook-to-different-formats/
---
{{% alert color="primary" %}}

Aspose.Cells 支持多种格式之间的转换。从技术上讲，转换意味着以一种文件格式加载工作簿并将其保存为另一种文件格式。

{{% /alert %}}

## **将 Excel 转换为 XPS**

XPS 文档格式由定义文档布局和每个页面的视觉外观的结构化 XML 标记以及用于分发、存档、呈现、处理和打印文档的呈现规则组成。

XPS 的标记语言是 XAML 的一个子集，它允许它在文档中合并矢量图形元素，使用 XAML 标记 Windows Presentation Foundation (WPF) 原语。使用的元素根据路径和其他几何图元进行描述。

XPS 文件实际上是使用开放打包约定的 Unicoded ZIP 存档，其中包含构成文档的文件。其中包括每个页面的 XML 标记文件、文本、嵌入字体、光栅图像、2D 矢量图形以及数字版权管理信息。只需在支持 ZIP 文件的应用程序中将其打开，即可检查 XPS 文件的内容。

从 Aspose.Cells 6.0.0 开始，支持 Microsoft Excel tp XPS 转换。

### **将单个工作表转换为 XPS**

以下示例显示如何将 Excel 文件中的单个工作表转换为 XPS。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingsingleWorksheetToXPS-ConvertingsingleWorksheetToXPS.java" >}}

### **将整个工作簿导出到 XPS**

下面的示例演示如何将整个工作簿转换为 XPS 格式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ExportWholeWorkbookToXPS-ExportWholeWorkbookToXPS.java" >}}

### **快速 Excel 到 XPS 的转换**

下面的示例展示了一种将 Excel 文件直接转换为 XPS 格式的简单方法。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-QuickExcelToXPSConversion-QuickExcelToXPSConversion.java" >}}

## **将 Excel 转换为 MHTML 文件**

[HTML格式](https://en.wikipedia.org/wiki/MHTML)将普通 HTML 与外部资源相结合；也就是说，通常将图像、动画、音频等内容链接到一个文件中。它们用于文件扩展名为 .mht 的电子邮件。

{{% alert color="primary" %}}

Aspose.Cells 支持读写MHTML文件。

{{% /alert %}}

将电子表格转换为 MHTML 是一项快速操作，如下所示。

下面的代码示例显示了如何将工作簿另存为 MHTML 文件。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToMHTMLFiles-ConvertingToMHTMLFiles.java" >}}

## **将 Excel 文件转换为 HTML**

 Aspose.Cells API 支持将电子表格导出为 HTML 格式。为此，Aspose.Cells 使用**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**允许开发人员控制输出 HTML 的几个方面的类。

下面的代码演示了如何使用**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**类将 Microsoft Excel 文件导出为 HTML 格式而不指定其他参数。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-ConvertingToHTMLFiles-ConvertingToHTMLFiles.java" >}}

{{% alert color="primary" %}}

您可以通过传递来获得相同的结果**[保存格式.HTML](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#HTML)**到**[工作簿.保存](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))**方法。

{{% /alert %}}

### **为 HTML 设置图像首选项**

从8.0.2开始，Aspose.Cells暴露了**[图像选项](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)**为了**[HtmlSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/HtmlSaveOptions)**类，它允许开发人员在将电子表格保存为 HTML 格式时指定图像首选项。

可以应用的图像设置有：

- **[图像类型](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#ImageType)**：获取或设置图像类型。请注意，所有形状（包括图表）在输出 HTML 中呈现为图像。
- **[质量](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Quality)**: 当ImageFormat指定为Jpeg时，获取或设置图像质量，范围为0到100。
- **[垂直分辨率](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#VerticalResolution)**: 获取或设置图像的垂直分辨率（以每英寸点数为单位）。
- **[水平分辨率](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#HorizontalResolution)**: 获取或设置图像的水平分辨率（以每英寸点数为单位）。
- **[TiffCompression](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#TiffCompression)**：获取或设置ImageFormat为Tiff时图像的压缩类型。
- **[透明](https://reference.aspose.com/cells/java/com.aspose.cells/imageorprintoptions#Transparent)**指示当 ImageFormat 指定为 Png 时图像的背景是否应该透明。

下面的代码演示了如何使用**[HtmlSaveOptions.ImageOptions](https://reference.aspose.com/cells/java/com.aspose.cells/htmlsaveoptions#ImageOptions)**指定不同的首选项。

|**导出前的电子表格视图**|**导出后的 HTML 视图**|
|:- |:- |
|![导出前的电子表格视图](converting-workbook-to-different-formats_1.png)|![导出后的 HTML 视图](converting-workbook-to-different-formats_2.png)|

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-SettingImagePrefrencesforHTML-SettingImagePrefrencesforHTML.java" >}}

## **将 Excel 转换为 PDF 文件**

PDF 文档被广泛用作组织、政府部门和个人之间交换文档的标准格式。软件开发人员经常被要求设计一种方法来轻松地将 Microsoft Excel 文件转换为 PDF 文档。 Aspose.Cells 支持这些功能。本文展示了如何。

### **将 Excel 转换为 PDF**

 Microsoft Excel 到 PDF 的转换是在 Aspose.Cells for Java 2.3.0 中引入的。从该版本中，Aspose.Cells 可以[直接将电子表格转换为PDF](#direct-conversion) （包含[PDF/A](#saving-excel-spreadsheets-to-pdfa-complied-files)), 没有其他产品。要使用旧版本 Aspose.Cells 转换电子表格，[使用 Aspose.PDF 进行转换](#conversion-with-asposepdf-asposecells-prior-to-230).

Aspose.Cell 将电子表格转换为 PDF，具有很高的准确性和保真度。然而，有一些[限制](/cells/zh/java/converting-workbook-to-different-formats/#conversion-attributes)，列在本文末尾。

{{% alert color="primary" %}}

 Aspose.Cells for Java 直接在输出文件中写入API和Version Number的信息。例如，在将文档呈现为 PDF 时，Aspose.Cells for Java 会填充**应用**值为“Aspose.Cells”的字段和**PDF制作器**具有值的字段，例如“Aspose.Cells for Java v17.9”。

请注意，您不能指示 Aspose.Cells for Java 更改或从输出文档中删除此信息。

{{% /alert %}}

#### **直接转换**

使用 将 Excel 文件直接保存为 PDF**[工作簿.保存](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))**方法，并提供**[保存格式.PDF](https://reference.aspose.com/cells/java/com.aspose.cells/saveformat#PDF)**接口成员。像这样直接转换是最高效的转换方式。它不会丢失数据或格式，但会保持输出的 PDF 看起来像输入的 Excel 文件。

要在保存为 PDF 时指定安全选项，请使用**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-Excel2PDFConversion-Excel2PDFConversion.java" >}}

#### **高级转换**

您也可以选择使用**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**类来为转换设置不同的属性。设置不同的属性**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**类将使您能够控制生成的 PDF 文件的打印、字体、安全和压缩设置。最显着的财产是**[合规性](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#Compliance)**使您能够将 Excel 文件保存为 PDF/A 兼容的 PDF 文件。

##### **将 Excel 电子表格保存为 PDF/A 编译文件**

下面提供的代码片段演示了**[PdfSaveOptions](https://reference.aspose.com/cells/java/com.aspose.cells/PdfSaveOptions)**类将 Excel 文件保存为 PDF/A 兼容的 PDF 格式。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-AdvancedConversiontoPdf-AdvancedConversiontoPdf.java" >}}

#### **使用 Aspose.Pdf 转换：Aspose.Cells 2.3.0 之前**

对于版本 2.3.0 之前的 Aspose.Cells 版本，您需要使用类似的组件[Aspose.PDF for Java](/pdf/java/)将电子表格转换为 PDF 文件。 Aspose.Cells 和 Aspose.PDF 一起工作，通过中间步骤将电子表格转换为 PDF。

要使用 Aspose.Cells 和 Aspose.PDF 将电子表格转换为 PDF：

1. 实例化一个对象**[工作簿](https://reference.aspose.com/cells/java/com.aspose.cells/Workbook)**通过调用它的空构造函数来类。
1. 使用 Aspose.Cells API 在电子表格上做您想要的工作。
1. 打电话给**[工作簿.保存](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#save(java.io.OutputStream,%20com.aspose.cells.SaveOptions))**保存电子表格的方法：
1. 将文件格式设置为 XML。
 1. 在FileFormatType界面选择Aspose_Pdf（预定义值）。这指示 save 方法以与 Aspose.PDF Schema 兼容的 XML 形式生成电子表格，以便 Aspose.PDF for Java 然后可以生成 PDF 文档。
1. 创建 XML 文件后，在 aspose.pdf 包中创建 Pdf 类的对象。
1. 调用 Pdf 类的 bindXML 方法并传递输出 XML 文件的名称。
1. 调用 Pdf 类的保存方法生成 PDF 文档。

下面以一个例子实现上述步骤。

{{% alert color="primary" %}}

如果您的电子表格包含公式，最好调用**[工作簿.计算公式](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#calculateFormula())**在将电子表格呈现为 PDF 格式之前的方法。这样做将确保重新计算公式相关值，并在 PDF 中呈现正确的值。

{{% /alert %}}

#### **转换属性**

我们努力改进每个版本的 Aspose.Cells 的转换和其他方面。 Excel 到 PDF 的转换有一些限制。电子表格中指定的某些格式设置可能会丢失，并且并非所有绘图对象都受支持。

下表列出了使用 Aspose.Cells 导出为 PDF 时完全或部分支持的所有功能。此表不是最终表，未涵盖所有电子表格属性。它还可以识别那些可能不支持或部分支持转换的功能。

{{% alert color="primary" %}}

|**文档元素**|**属性**|**网络支持**|**笔记**|
|:- |:- |:- |:- |
|结盟||是的||
|回转||部分地|仅支持 90 和 -90。|
|后台设置||是的||
|边界|颜色|是的||
|边界|线型|是的||
|边界|行宽|是的||
|Cell数据||是的||
|注释||不||
|条件格式||是的||
|文档属性||是的||
|绘图对象||是的||
|字体|尺寸|是的||
|字体|颜色|是的||
|字体|风格|是的||
|字体|强调|是的||
|字体|效果|部分地|仅支持删除线效果|
|图片||是的||
|超级链接||是的||
|图表||是的||
|合并 Cells||是的||
|分页符||是的||
|页面设置|页眉页脚|是的||
|页面设置|边距|是的||
|页面设置|页面方向|是的||
|页面设置|页面大小|是的||
|页面设置|打印区域|是的||
|页面设置|打印标题|是的||
|页面设置|缩放|是的||
|行高/列宽||是的||
{{% /alert %}}
