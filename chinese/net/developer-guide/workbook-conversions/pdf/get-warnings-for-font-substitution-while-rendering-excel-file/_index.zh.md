---
title: 在呈现Excel文件为PDF时，有时会进行字体替换。Aspose.Cells提供了一个功能，让开发人员知道特定字体已经被替换，从而发出警告。这是一个有用的功能，可以帮助您确定为什么Aspose.Cells呈现的PDF与实际Excel文件不同，并且您可以采取相应的措施。例如，您可以安装缺少的字体，以便呈现结果看起来一致。
type: docs
weight: 230
url: /zh/net/get-warnings-for-font-substitution-while-rendering-excel-file/
---

{{% alert color="primary" %}} 

有时，在将Microsoft Excel文件渲染为PDF时，Aspose.Cells会替换字体。Aspose.Cells提供了一个功能，通过触发警告来让开发人员知道特定字体已被替换。这是一个有用的功能，可以帮助您确定为何Aspose.Cells渲染的PDF与原始Microsoft Excel文件看起来不同，因此您可以采取适当的行动。例如，安装缺失的字体，以便渲染结果看起来相同。

{{% /alert %}} 

要在将Excel文件呈现为PDF时获取字体替换的警告，请实现 IWarningCallback 接口，并使用您实现的接口设置 PdfSaveOptions.WarningCallback 属性。

下面的屏幕截图显示了我们将在以下代码中使用的源Excel文件。在单元格A6和A7中有一些文本，微软Excel无法正确呈现其中的字体。

|**并非所有字体都能正确呈现**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)|
Aspose.Cells将使用合适的字体替换单元格A6和A7中的字体，如下所示。

|**替换字体**|
| :- |
|![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)|
## **下载源文件和输出PDF**
您可以从以下链接下载源Excel文件和输出PDF

- [source.xlsx](5112611.xlsx)
- [output.pdf](5112616.pdf)
## **代码**
以下代码实现了IWarningCallback并将PdfSaveOptions.WarningCallback属性设置为实现的接口。现在，每当Aspose.Cells将在任何单元格中替换字体时，将在WarningCallback.Warning()方法内触发警告。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-GetWarningsForFontSubstitution-1.cs" >}}
## **输出**
将源Excel文件转换为PDF后，警告将输出到调试控制台，例如：

{{< highlight java >}}

 WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}} 

如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用Workbook.CalculateFormula方法。这样做将确保重新计算公式相关值，并在PDF中呈现正确的值。

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
