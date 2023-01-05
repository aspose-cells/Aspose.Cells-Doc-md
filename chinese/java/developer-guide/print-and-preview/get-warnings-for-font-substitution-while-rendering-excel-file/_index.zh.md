---
title: 呈现 Excel 文件时获取字体替换警告
type: docs
weight: 120
url: /zh/java/get-warnings-for-font-substitution-while-rendering-excel-file/
---
{{% alert color="primary" %}}

有时，将 Microsoft Excel 文件呈现为 PDF 时，Aspose.Cells 会替换字体。 Aspose.Cells 提供了一项功能，通过发出警告让开发人员知道特定字体已被替换。这是一项有用的功能，可以帮助您确定 Aspose.Cells 呈现的 PDF 与实际 Excel 文件不同的原因，然后您可以采取适当的措施。例如，您可以安装缺少的字体，以使渲染结果看起来相同。

如果要在将 Excel 文件呈现为 PDF 时获取字体替换警告，请实现 IWarningCallback 接口并使用已实现的接口设置 PdfSaveOptions.setWarningCallback() 方法。

{{% /alert %}}

下面的屏幕截图显示了以下代码中使用的源 Excel 文件。它在单元格 A6 和 A7 中有一些文本的字体不能被 Microsoft Excel 很好地呈现。

![待办事项：图片_替代_文本](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)

Aspose.Cells 会将单元格 A6 和 A7 中的字体替换为合适的字体，如下所示。

![待办事项：图片_替代_文本](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)

## **下载源文件和输出 PDF**

您可以从以下链接下载源 Excel 文件和输出 PDF

- [来源.xlsx](5472700.xlsx)
- [输出.pdf](5472699.pdf)

下面的代码实现了[**警告回调**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback)并设置[**PdfSaveOptions.setWarningCallback()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#WarningCallback)方法与实现的接口。现在，无论何时在任何单元格中替换任何字体，Aspose.Cells 都会在 WarningCallback.warning() 方法中发出警告。

{{< highlight "java" >}}

 public class WarningCallback implements IWarningCallback {

    @Override

    public void warning(WarningInfo info) {

        if(info.getWarningType() == WarningType.FONT_SUBSTITUTION)

        {

            System.out.println("WARNING INFO: " + info.getDescription());

        }

    }

}

//........

//........

static void Run() throws Exception

{

    Workbook workbook = new Workbook("source.xlsx");

    PdfSaveOptions options = new PdfSaveOptions();

    options.setWarningCallback(new WarningCallback());

    workbook.save("output.pdf", options);

}

{{< /highlight >}}

## **警告输出**

转换源文件后，调试控制台输出以下警告：

{{< highlight "java" >}}

WARNING INFO: Font substitution: Font [ Athene Logos; Regular ]has been substituted in Cell [ A6 ]in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ]has been substituted in Cell [ A7 ]in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}}

如果您的电子表格包含公式，最好在将电子表格呈现为 PDF 格式之前调用 Workbook.calculateFormula 方法。这样做将确保重新计算公式相关值，并在 PDF 中呈现正确的值。

{{% /alert %}}
