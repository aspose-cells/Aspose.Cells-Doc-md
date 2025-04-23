---
title: 在呈现Excel文件为PDF时，有时会进行字体替换。Aspose.Cells提供了一个功能，让开发人员知道特定字体已经被替换，从而发出警告。这是一个有用的功能，可以帮助您确定为什么Aspose.Cells呈现的PDF与实际Excel文件不同，并且您可以采取相应的措施。例如，您可以安装缺少的字体，以便呈现结果看起来一致。
type: docs
weight: 120
url: /zh/java/get-warnings-for-font-substitution-while-rendering-excel-file/
---

{{% alert color="primary" %}}

有时，在将Microsoft Excel文件渲染为PDF时，Aspose.Cells会替换字体。Aspose.Cells提供了一个功能，通过触发警告来让开发人员知道特定字体已经被替换。这是一个有用的功能，可以帮助您确定为什么Aspose.Cells呈现的PDF与实际的Excel文件不同，然后您可以采取适当的措施。例如，您可以安装缺失的字体，以便呈现结果看起来相同。

如果您想在呈现Excel文件为PDF时获得有关字体替换的警告，请实现IWarningCallback接口，并将PdfSaveOptions.setWarningCallback()方法设置为您实现的接口。

{{% /alert %}}

以下截图显示了下面代码中使用的源Excel文件。 单元格A6和A7中有一些文本，其字体在Microsoft Excel中无法正确呈现。

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_1.png)

Aspose.Cells将使用合适的字体替换单元格A6和A7中的字体，如下所示。

![todo:image_alt_text](get-warnings-for-font-substitution-while-rendering-excel-file_2.png)

## **下载源文件和输出PDF**

您可以从以下链接下载源Excel文件和输出PDF

- [source.xlsx](5472700.xlsx)
- [output.pdf](5472699.pdf)

以下代码实现[**IWarningCallback**](https://reference.aspose.com/cells/java/com.aspose.cells/IWarningCallback)并设置实现接口的[**PdfSaveOptions.setWarningCallback()**](https://reference.aspose.com/cells/java/com.aspose.cells/pdfsaveoptions#WarningCallback)方法。现在，无论在任何单元格中是否替换字体，Aspose.Cells都会在WarningCallback.warning()方法内触发警告。

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

如果您的电子表格包含公式，最好在将电子表格呈现为PDF格式之前调用Workbook.calculateFormula方法。这样做将确保重新计算基于公式的值，并且在PDF中呈现正确的值。 

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
