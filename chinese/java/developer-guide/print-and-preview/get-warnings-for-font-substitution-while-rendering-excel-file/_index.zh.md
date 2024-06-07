---
title: 在呈现Excel文件为PDF时获取替换字体警告
type: docs
weight: 120
url: /zh/java/get-warnings-for-font-substitution-while-rendering-excel-file/
---

{{% alert color="primary" %}}

有时，在将Microsoft Excel文件渲染为PDF时，Aspose.Cells会替换字体。 Aspose.Cells提供了一个功能，可以通过触发警告来让开发人员知道特定字体已被替换。 这是一个有用的功能，可以帮助您确定为何Aspose.Cells渲染的PDF文件与实际的Excel文件不同，并且您可以采取适当的操作。 例如，您可以安装缺失的字体，以便渲染结果看起来相同。

如果要在将Excel文件渲染为PDF时获取字体替换的警告，则实现IWarningCallback接口并将PdfSaveOptions.setWarningCallback() 方法设置为您实现的接口。

{{% /alert %}}

下面的屏幕截图显示了下面的代码中使用的源Excel文件。 它在A6单元格和A7单元格中有一些文本，其字体不是由Microsoft Excel很好地渲染。

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)

Aspose.Cells将会用适合的字体替换单元格A6和A7中的字体，如下所示。

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)

## **下载源文件和输出PDF**

您可以从以下链接下载源Excel文件和输出PDF

- [source.xlsx](5472700.xlsx)
- [output.pdf](5472699.pdf)

以下代码实现了 [**IWarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback) 并设置了 [**PdfSaveOptions.setWarningCallback()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#WarningCallback) 方法为实现的接口。 现在，每当在任何单元格中替换任何字体时，Aspose.Cells将在WarningCallback.warning() 方法内触发警告。

{{< highlight java >}}

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

在转换源文件后，以下警告将输出到调试控制台：

{{< highlight java >}}

WARNING INFO: Font substitution: Font [ Athene Logos; Regular ] has been substituted in Cell [ A6 ] in Sheet [ Sheet1 ].

WARNING INFO: Font substitution: Font [ B Traffic; Regular ] has been substituted in Cell [ A7 ] in Sheet [ Sheet1 ].

{{< /highlight >}}

{{% alert color="primary" %}}

如果您的电子表格包含公式，则最好在将电子表格呈现为PDF格式之前调用Workbook.calculateFormula方法。 这样做将确保重新计算公式相关值，并在PDF中呈现正确的值。 

{{% /alert %}}
