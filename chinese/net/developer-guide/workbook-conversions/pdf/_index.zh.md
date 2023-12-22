---
title: Pdf
type: docs
weight: 220
url: /zh/net/convert-excel-to-pdf/
---
{{% alert color="primary" %}}

Aspose.Cells支持将Excel工作簿转换为PDF。在本例中，我们将看到Excel工作簿到PDF的完整转换。

{{% /alert %}}

##  **将 Excel 工作簿转换为 PDF**

PDF 文件广泛用于组织、政府部门和个人之间交换文件。它是一种标准文档格式，软件开发人员经常被要求找到一种将 Microsoft Excel 文件转换为 PDF 文档的方法。

Aspose.Cells支持将Excel文件转换为PDF，并在转换中保持高视觉保真度。

{{% alert color="primary" %}}

 Aspose.Cells for .NET 直接将API和版本号的信息写入输出文档中。例如，将 Document 渲染为 PDF 时，将填充 Aspose.Cells for .NET**PDF 制片人**具有值的字段，例如“Aspose.Cells v23.2”。

请注意，您可以通过以下方式更改输出文档中的此信息**[PdfSaveOptions.Producer](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/ Producer/)**财产。

{{% /alert %}}

###  **直接转换**

 Aspose.Cells for .NET 支持从电子表格到 PDF 的转换，独立于其他软件。只需使用以下命令将 Excel 文件保存到 PDF**[工作簿](https://reference.aspose.com/cells/net/aspose.cells/workbook)**班级'**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**方法。这**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**方法提供了**[SaveFormat.Pdf](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**将本机 Excel 文件转换为 PDF 格式的枚举成员。

按照以下步骤直接将Excel电子表格转换为PDF格式：

1. 实例化一个对象**[工作簿](https://reference.aspose.com/cells/net/aspose.cells/workbook)**类通过调用其空构造函数。
1. 您可以打开/加载现有模板文件，或者如果您从头开始创建工作簿，则可以跳过此步骤。
1. 使用 Aspose.Cells' API 在电子表格上执行任何工作（输入数据、应用格式、设置公式、插入图片或其他绘图对象等）。
1. 电子表格代码完成后，调用**[工作簿](https://reference.aspose.com/cells/net/aspose.cells/workbook)**班级'**[保存](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/save/index)**保存电子表格的方法。

文件格式应为 PDF，因此选择*Pdf*（预定义值）来自**[保存格式](https://reference.aspose.com/cells/net/aspose.cells/saveformat)**枚举生成最终的PDF文档。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-XlstoPDFDirectConversation-1.cs" >}}

###  **高级转换**

您还可以选择使用**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**类为转换设置不同的属性。设置不同的属性**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**类使您可以控制输出 PDF 的打印、字体、安全性和压缩设置。最重要的属性是**[合规性](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**它使您能够将 Excel 文件保存为 PDF/A 兼容的 PDF 文件。

####  **将工作簿保存到 PDF/A 编译文件**

下面提供的代码片段演示了如何使用**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**类将 Excel 文件保存为 PDF/A 兼容的 PDF 格式。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-AdvancedConversiontoPdf-1.cs" >}}

{{% alert color="primary" %}}

请注意，**[合规性](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/compliance)**Aspose.Cells for .NET 5.3.0 版本中添加了属性。

{{% /alert %}}

####  **设置PDF创建时间**

随着**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**类中，可以获取或设置PDF创建时间。下面的代码演示了使用**[PdfSaveOptions.CreatedTime](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions/properties/createdtime)**属性设置 PDF 文件的创建时间。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetPDFCreationTime-1.cs" >}}

####  **设置 ContentCopyForAccessibility 选项**

随着**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**类，可以获取或设置PDF**[AccessibilityExtractContent](https://reference.aspose.com/cells/net/aspose.cells.rendering.pdfsecurity/pdfsecurityoptions/properties/accessibilityextractcontent)**选项来控制转换后的 PDF 中的内容访问。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-SetContentCopyForAccessibility-1.cs" >}}

####  **将自定义属性导出到 PDF**

随着**[PdfSaveOptions](https://reference.aspose.com/cells/net/aspose.cells/pdfsaveoptions)**类，您可以将源工作簿中的自定义属性导出到 PDF.**[PdfCustomPropertiesExport](https://reference.aspose.com/cells/net/aspose.cells.rendering/pdfcustompropertiesexport)**提供枚举器用于指定导出属性的方式。通过单击“文件”，然后单击“属性”选项，可以在 Adobe Acrobat Reader 中观察这些属性，如下图所示。可以下载模板文件“sourceWithCustProps.xlsx”[这里](sourceWithCustProps.xlsx)用于测试和输出 PDF 文件“outSourceWithCustProps”可用[这里](outSourceWithCustProps.pdf)进行分析。

![待办事项：图像_替代_文本](convert-excel-workbook-to-pdf_1.png)

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-ExportCustomPropertiesToPdf-1.cs" >}}

###  **转换属性**

我们致力于增强每个新版本的转换功能。 Aspose.Cell 的 Excel 到 PDF 的转换仍然有一些限制。转换为 PDF 格式时不支持 MapChart。此外，某些绘图对象也没有得到很好的支持。

下表列出了使用 Aspose.Cells 导出到 PDF 时完全或部分支持的所有功能。此表不是最终的，并且不涵盖所有电子表格属性，但它确实标识了转换为 PDF 时不支持或部分支持的那些功能。

|**文档元素**|**属性**|**支持的**|**笔记**|
| :- | :- | :- | :- |
|结盟| |是的| |
|背景设置| |是的| |
|边界|颜色|是的| |
|边界|线条样式|是的| |
|边界|行宽|是的| |
|Cell 数据| |是的| |
|评论| |是的| |
|条件格式| |是的| |
|文档属性| |是的| |
|绘制对象| |部分|绘图对象的阴影和 3D 效果无法得到很好的支持；部分支持艺术字和智能艺术。|
|字体|尺寸|是的| |
|字体|颜色|是的| |
|字体|风格|是的| |
|字体|强调|是的| |
|字体|效果|是的||
|图片| |是的| |
|超级链接| |是的| |
|图表| |部分|不支持地图图表。|
|合并Cells| |是的| |
|分页符| |是的| |
|页面设置|页眉页脚|是的| |
|页面设置|边距|是的| |
|页面设置|页面方向|是的| |
|页面设置|页面大小|是的| |
|页面设置|打印区|是的| |
|页面设置|打印标题|是的| |
|页面设置|缩放|是的| |
|行高/列宽| |是的| |
|RTL（从右到左）语言| |是的| |

{{% alert color="primary" %}}

如果您的电子表格包含公式，最好致电**[Workbook.CalculateFormula()](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/calculateformula)**就在将电子表格渲染为 PDF 格式之前。这样做将确保重新计算公式相关值，并在 PDF 中呈现正确的值。

{{% /alert %}}

##  **高级主题**
- [添加PDF书签](/cells/zh/net/add-pdf-bookmarks/)
- [添加 PDF 具有指定目的地的书签](/cells/zh/net/add-pdf-bookmarks-with-named-destinations/)
- [当没有任何内容可打印时，避免输出中出现空白页 PDF](/cells/zh/net/avoid-blank-page-in-output-pdf-when-there-is-nothing-to-print/)
- [保存到 PDF 时仅更改特定 Unicode 字符的字体](/cells/zh/net/change-the-font-on-just-the-specific-unicode-characters-while-saving-to-pdf/)
- [渲染到 PDF 时控制 MS Excel 工作簿中外部资源的加载](/cells/zh/net/control-loading-of-external-resources-in-ms-excel-workbook-while-rendering-to-pdf/)
- [将 XLSX 文件转换为 PDF 格式](/cells/zh/net/convert-xlsx-file-to-pdf-format/)
- [将 Excel 文件转换为与 PDFA-1a 兼容的 PDF 格式](/cells/zh/net/convert-excel-file-to-pdf-format-compatible-with-pdfa-1a/)
- [将包含图像或图表的 XLS 文件转换为 PDF](/cells/zh/net/convert-xls-file-with-images-or-charts-to-pdf/)
- [为图表表创建 PdfBookmarkEntry](/cells/zh/net/create-pdfbookmarkentry-for-chart-sheet/)
- [将所有工作表列放在单个 PDF 页上](/cells/zh/net/fit-all-worksheet-columns-on-single-pdf-page/)
- [使用 DrawObjectEventHandler 类渲染到 PDF 时获取 DrawObject 并绑定](/cells/zh/net/get-drawobject-and-bound-while-rendering-to-pdf-using-drawobjecteventhandler-class/)
- [渲染 Excel 文件时收到字体替换警告](/cells/zh/net/get-warnings-for-font-substitution-while-rendering-excel-file/)
- [将 Excel 渲染为 PDF 时忽略错误](/cells/zh/net/ignore-errors-while-rendering-excel-to-pdf/)
- [限制生成的页面数 - Excel 到 PDF 转换](/cells/zh/net/limit-the-number-of-pages-generated-excel-to-pdf-conversion/)
- [保存到 PDF 时打印评论](/cells/zh/net/print-comments-while-saving-to-pdf/)
- [将 Excel 转换为 PDF 时呈现 Office 加载项](/cells/zh/net/render-office-add-ins-while-converting-excel-to-pdf/)
- [每个 Excel 工作表渲染一页 PDF - Excel 到 PDF 转换](/cells/zh/net/render-one-pdf-page-per-excel-worksheet-excel-to-pdf-conversion/)
- [将输出 PDF 中的 Unicode 增补字符渲染为 Aspose.Cells](/cells/zh/net/render-unicode-supplementary-characters-in-output-pdf-by-aspose-cells/)
- [对添加的图像重新采样 - Excel 到 PDF 转换](/cells/zh/net/resampling-added-images-excel-to-pdf-conversion/)
- [将每个工作表保存到不同的 PDF 文件](/cells/zh/net/save-each-worksheet-to-a-different-pdf-file/)
- [将 Excel 保存为标准或最小大小的 PDF](/cells/zh/net/save-excel-into-pdf-with-standard-or-minimum-size/)
- [将指定工作表保存到PDF](/cells/zh/net/save-specified-worksheets-to-pdf/)
- [安全 PDF 文件](/cells/zh/net/secure-pdf-documents/)
- [指定如何交叉输出 PDF 和图像中的字符串](/cells/zh/net/specify-how-to-cross-string-in-output-pdf-and-image/)
