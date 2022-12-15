---
title: 呈现 Excel 文件时获取字体替换警告
type: docs
weight: 230
url: /zh/net/get-warnings-for-font-substitution-while-rendering-excel-file/
---
{{% alert color="primary" %}} 

有时，将 Microsoft Excel 文件渲染为 PDF 时，Aspose.Cells 会替换字体。 Aspose.Cells 提供了一项功能，可让开发人员通过发出警告来了解已替换的特定字体。这是一个有用的功能，可以帮助您确定为什么 Aspose.Cells 呈现的 PDF 看起来与原始 Microsoft Excel 文件不同，以便您可以采取适当的措施。例如，安装缺少的字体以使渲染结果看起来相同。

{{% /alert %}} 

要在将 Excel 文件呈现为 PDF 时获取字体替换警告，请实施 IWarningCallback 接口并使用您实施的接口设置 PdfSaveOptions.WarningCallback 属性。

下面的屏幕截图显示了我们将在以下代码中使用的源 Excel 文件。它在单元格 A6 和 A7 中有一些文本，其字体无法由 Microsoft Excel 正确呈现。

|**并非所有字体都能正确呈现**|
|:- |
|![待办事项：图像_替代_文本](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|
Aspose.Cells 会将单元格 A6 和 A7 中的字体替换为合适的字体，如下所示。

|**替换字体**|
|:- |
|![待办事项：图像_替代_文本](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|
## **下载源文件并输出 PDF**
您可以从以下链接下载源 Excel 文件和输出 PDF

- [来源.xlsx](5112611.xlsx)
- [输出.pdf](5112616.pdf)
## **代码**
以下代码实现 IWarningCallback 并使用实现的接口设置 PdfSaveOptions.WarningCallback 属性。现在，无论何时在任何单元格中替换任何字体，Aspose.Cells 都会在 WarningCallback.Warning() 方法中发出警告。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetWarningsForFontSubstitution-1.cs" >}}
## **输出**
将源 Excel 文件转换为 PDF 后，警告将输出到调试控制台，如下所示：

{{< highlight "java" >}}

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ]has been substituted in Cell [ A6 ]in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ]has been substituted in Cell [ A7 ]in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}} 

如果您的电子表格包含公式，最好在将电子表格呈现为 PDF 格式之前调用 Workbook.CalculateFormula 方法。这样做将确保重新计算公式相关值，并在 PDF 中呈现正确的值。

{{% /alert %}}
