---
title: 在呈现Excel文件为PDF时获取替换字体警告
type: docs
weight: 230
url: /zh/net/get-warnings-for-font-substitution-while-rendering-excel-file/
---

{{% alert color="primary" %}} 

有时，在将Microsoft Excel文件呈现为PDF时，Aspose.Cells会替换字体。Aspose.Cells提供了一个功能，通过触发警告来让开发人员知道已经替换了哪个特定的字体。这是一个有用的功能，可以帮助您确定为什么Aspose.Cells呈现的PDF看起来与原始Microsoft Excel文件不同，从而可以采取适当的行动。例如，安装缺失的字体，以使呈现结果看起来相同。

{{% /alert %}} 

在将Excel文件呈现为PDF时获取有关字体替换的警告，实现IWarningCallback接口并将PdfSaveOptions.WarningCallback属性设置为您实现的接口。

下面的屏幕截图显示了我们接下来要在以下代码中使用的源Excel文件。它在单元格A6和A7中有一些文本，这些文本的字体在Microsoft Excel中无法正常显示。

|**并非所有字体都能正确显示**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|
Aspose.Cells将会用适合的字体替换单元格A6和A7中的字体，如下所示。

|**替换的字体**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|
## **下载源文件和输出PDF**
您可以从以下链接下载源Excel文件和输出PDF

- [source.xlsx](5112611.xlsx)
- [output.pdf](5112616.pdf)
## **代码**
以下代码实现了 IWarningCallback，并将 PdfSaveOptions.WarningCallback 属性设置为该实现接口。现在，每当任何单元格中的任何字体将被替换时，Aspose.Cells 将在 WarningCallback.Warning() 方法中触发警告。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetWarningsForFontSubstitution-1.cs" >}}
## **输出**
将源Excel文件转换为PDF后，警告将输出到调试控制台，如下:

{{< highlight java >}}

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}} 

如果您的电子表格包含公式，最好在将电子表格渲染为PDF格式之前调用 Workbook.CalculateFormula 方法。这样做将确保重新计算依赖于公式的值，并在PDF中呈现正确的值。

{{% /alert %}}
