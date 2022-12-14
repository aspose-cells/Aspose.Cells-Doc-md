---
title: PDF格式
type: docs
weight: 220
url: /zh/net/convert-excel-to-pdf/
---
{{% alert color="primary" %}}

Aspose.Cells 支持Excel工作簿转PDF。在此示例中，我们将看到 Excel 工作簿完全转换为 PDF。

{{% /alert %}}

## **将 Excel 工作簿转换为 PDF**

PDF 文件广泛用于在组织、政府部门和个人之间交换文档。它是一种标准文档格式，软件开发人员经常被要求找到一种将 Microsoft Excel 文件转换为 PDF 文档的方法。

Aspose.Cells 支持将Excel文件转换为PDF，并在转换过程中保持高视觉保真度。

{{% alert color="primary" %}}

 Aspose.Cells for .NET 直接在输出文件中写入API和Version Number的信息。例如，在将文档呈现为 PDF 时，Aspose.Cells for .NET 会填充**应用**值为“Aspose.Cells”的字段和**PDF制作器**具有值的字段，例如“Aspose.Cells v17.9”。

请注意，您不能指示 Aspose.Cells for .NET 更改或从输出文档中删除此信息。

{{% /alert %}}

### **直接转换**

 Aspose.Cells for .NET 支持独立于其他软件从电子表格转换为PDF。只需使用 将 Excel 文件保存为 PDF**[工作簿](https://reference.aspose.com/cells/net/aspose.cells/workbook)**班级'**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**方法。这**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**方法提供了**[保存格式.Pdf](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**将本机 Excel 文件转换为 PDF 格式的枚举成员。

按照以下步骤将 Excel 电子表格直接转换为 PDF 格式：

1. 实例化一个对象**[工作簿](https://reference.aspose.com/cells/net/aspose.cells/workbook)**通过调用它的空构造函数来类。
1. 如果您从头开始创建工作簿，您可以打开/加载现有模板文件或跳过此步骤。
1. 使用 Aspose.Cells' API 在电子表格上执行任何工作（输入数据、应用格式、设置公式、插入图片或其他绘图对象等）。
1. 电子表格代码完成后，调用**[工作簿](https://reference.aspose.com/cells/net/aspose.cells/workbook)**班级'**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**保存电子表格的方法。

文件格式应为 PDF，因此请选择*PDF格式*（预定义值）来自**[保存格式](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**枚举以生成最终的 PDF 文档。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

### **高级转换**

您也可以选择使用**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**类来为转换设置不同的属性。设置不同的属性**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**类使您可以控制输出 PDF 的打印、字体、安全和压缩设置。最重要的属性是**[合规性](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**这使您能够将 Excel 文件保存为 PDF/A 兼容的 PDF 文件。

#### **将工作簿保存为 PDF/A 编译文件**

下面提供的代码片段演示了如何使用**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**类将 Excel 文件保存为 PDF/A 兼容的 PDF 格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

请注意，**[合规性](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**属性是在 Aspose.Cells for .NET 5.3.0 版本中添加的。

{{% /alert %}}

#### **设置 PDF 创建时间**

随着**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**类，可以获取或设置PDF创建时间。下面的代码演示了使用**[PdfSaveOptions.CreatedTime](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime)**属性设置PDF文件的创建时间。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

#### **设置 ContentCopyForAccessibility 选项**

随着**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**类，您可以获取或设置 PDF**[AccessibilityExtractContent](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent)**选项来控制转换后的 PDF 中的内容访问。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

#### **将自定义属性导出为 PDF**

随着**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**类，您可以将源工作簿中的自定义属性导出到 PDF。**[PdfCustomPropertiesExport](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport)**枚举器用于指定导出属性的方式。可以在 Adobe Acrobat Reader 中通过单击“文件”然后单击“属性”选项来观察这些属性，如下图所示。可以下载模板文件“sourceWithCustProps.xlsx”[这里](sourceWithCustProps.xlsx)用于测试和输出 PDF 文件“outSourceWithCustProps”可用[这里](outSourceWithCustProps.pdf)进行分析。

![待办事项：图片_替代_文本](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

### **转换属性**

我们致力于增强每个新版本的转换功能。 Aspose.Cell 的 Excel 到 PDF 转换仍然有一些限制。转换为 PDF 格式时，某些电子表格格式可能会丢失。此外，尚不支持某些绘图对象。

下表列出了使用 Aspose.Cells 导出到 PDF 时完全或部分支持的所有功能。此表不是最终的，也没有涵盖所有电子表格属性，但它确实标识了转换为 PDF 时不支持或部分支持的功能.

|**文档元素**|**属性**|**支持的**|**笔记**|
|:- |:- |:- |:- |
|结盟||是的||
|后台设置||是的||
|边界|颜色|是的||
|边界|线型|是的||
|边界|行宽|是的||
|Cell数据||是的||
|注释||是的||
|条件格式||是的||
|文档属性||是的||
|绘图对象||部分地|支持的对象：TextBox、Line、Rectangle、Oval、GroupBox、Button、CheckBox、RadioButton、ListBox、ComboBox、Label|
|字体|尺寸|是的||
|字体|颜色|是的||
|字体|风格|是的||
|字体|强调|是的||
|字体|效果|部分地|仅支持删除线效果|
|图片||是的||
|超级链接||是的||
|图表||部分地||
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
|RTL（从右到左）语言||是的||

{{% alert color="primary" %}}

如果您的电子表格包含公式，最好调用**[工作簿.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)**就在将电子表格呈现为 PDF 格式之前。这样做将确保重新计算公式相关值，并在 PDF 中呈现正确的值。

{{% /alert %}}

## **推进主题**
- [添加 PDF 书签](/cells/zh/net/add-pdf-bookmarks/)
- [添加带有命名目标的 PDF 书签](/cells/zh/net/add-pdf-bookmarks-with-named-destinations/)
- [当没有可打印的内容时，避免在输出 PDF 中出现空白页](/cells/zh/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [保存为 PDF 时仅更改特定 Unicode 字符的字体](/cells/zh/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [在呈现为 PDF 时控制 MS Excel 工作簿中外部资源的加载](/cells/zh/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [将 XLS 文件转换为 PDF 格式](/cells/zh/net/convert-an-xls-file-to-pdf-format/)
- [将 Excel 文件转换为与 PDFA-1a 兼容的 PDF 格式](/cells/zh/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [将带有图像或图表的 XLS 文件转换为 PDF](/cells/zh/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [为图表工作表创建 PdfBookmarkEntry](/cells/zh/net/create-pdfbookmarkentry-for-chart-sheet/)
- [使所有工作表列都适合单个 PDF 页面](/cells/zh/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [使用 DrawObjectEventHandler 类在呈现为 PDF 时获取 DrawObject 和 Bound](/cells/zh/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [呈现 Excel 文件时获取字体替换警告](/cells/zh/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [将 Excel 呈现为 PDF 时忽略错误](/cells/zh/net/ignore-errors-while-rendering-excel-to-pdf/)
- [限制生成的页数 - Excel 到 PDF 的转换](/cells/zh/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [保存为 PDF 时打印注释](/cells/zh/net/print-comments-while-saving-to-pdf/)
- [在将 Excel 转换为 PDF 时呈现 Office 加载项](/cells/zh/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [每个 Excel 工作表渲染一个 PDF 页面 - Excel 到 PDF 的转换](/cells/zh/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [通过 Aspose.Cells 在输出 PDF 中渲染 Unicode 增补字符](/cells/zh/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [重新采样添加的图像 - Excel 到 PDF 的转换](/cells/zh/net/resampling-added-images-excel-to-pdf-conversion/)
- [将每个工作表保存到不同的 PDF 文件](/cells/zh/net/save-each-worksheet-to-a-different-pdf-file/)
- [以标准或最小尺寸将 Excel 保存为 PDF](/cells/zh/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [保护 PDF 文档](/cells/zh/net/secure-pdf-documents/)
- [指定如何在输出 PDF 和图像中交叉字符串](/cells/zh/net/specify-how-to-cross-string-in-output-pdf-and-image/)
