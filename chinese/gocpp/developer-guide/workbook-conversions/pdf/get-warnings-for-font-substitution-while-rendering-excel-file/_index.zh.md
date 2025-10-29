---
title: 在使用 Golang 通过 C++ 渲染 Excel 文件时获取字体替代的警告
linktitle: 获取字体替换的警告
type: docs
weight: 230
url: /zh/go-cpp/get-warnings-for-font-substitution-while-rendering-excel-file/
description: 学习如何在使用 Golang 通过 C++ 将 Excel 文件渲染为 PDF 时获取字体替代的警告。
---

{{% alert color="primary" %}}

有时，在将Microsoft Excel文件渲染为PDF时，Aspose.Cells会替换字体。Aspose.Cells提供了一个功能，通过触发警告来让开发人员知道特定字体已被替换。这是一个有用的功能，可以帮助您确定为何Aspose.Cells渲染的PDF与原始Microsoft Excel文件看起来不同，因此您可以采取适当的行动。例如，安装缺失的字体，以便渲染结果看起来相同。

{{% /alert %}}

要在将Excel文件渲染为PDF时获取字体替换的警告信息，请实现`IWarningCallback`接口，并将`PdfSaveOptions.WarningCallback`属性设置为您的实现类。

下面的屏幕截图显示了我们将在以下代码中使用的源Excel文件。在单元格A6和A7中有一些文本，微软Excel无法正确呈现其中的字体。

|**并非所有字体都能正确呈现**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|

Aspose.Cells将使用合适的字体替换单元格A6和A7中的字体，如下所示。

|**替换字体**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|

## **下载源文件和输出PDF**
您可以从以下链接下载示例Excel文件和输出的PDF：

- [source.xlsx](5112611.xlsx)
- [output.pdf](5112616.pdf)

## **代码**
以下代码实现了`IWarningCallback`并使用实现的接口设置了`PdfSaveOptions.WarningCallback`属性。现在，每当任何字体在任何单元格中被替换时，Aspose.Cells将在`WarningCallback.Warning()`方法中触发警告。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-GetWarningsForFontSubstitutionWhileRenderingExcelFile.go" >}}
## **输出**
将源Excel文件转换为PDF后，警告将输出到调试控制台，例如：

{{< highlight java >}}
WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].
WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].
{{< /highlight >}}

{{% alert color="primary" %}}

如果您的电子表格包含公式，最好在将电子表格渲染为PDF格式之前调用`Workbook.CalculateFormula`方法。这样可以确保依赖公式的值被重新计算，并在PDF中显示正确的值。

{{% /alert %}}
