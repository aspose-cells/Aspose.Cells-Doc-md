---
title: 读取具有多种编码的 CSV 文件
type: docs
weight: 140
url: /zh/java/reading-csv-file-with-multiple-encodings/
---
{{% alert color="primary" %}} 

有时，您的 CSV 文件包含多个编码（Unicode、ANSI、UTF8、UTF7 等）。 Aspose.Cells 允许您加载此类 CSV 文件并将其转换为其他格式，例如 PDF 或 XLSX。

{{% /alert %}} 

 Aspose.Cells提供了TxtLoadOptions.setMultiEncoded()方法，需要设置为**真的**正确加载具有多种编码的 CSV 文件。

以下屏幕截图显示了一个包含两行的示例 CSV 文件。第一行在**美标**编码，第二行是**统一码**编码

**输入文件** 

![待办事项：图像_替代_文本](reading-csv-file-with-multiple-encodings_1.png)

以下屏幕截图显示了从上述 CSV 文件转换而来的 XLSX 文件，没有将 TxtLoadOptions.setMultiEncoded() 方法设置为 true。如您所见，Unicode 文本未正确转换。

**输出文件 1：没有为多重编码做出调整** 

![待办事项：图像_替代_文本](reading-csv-file-with-multiple-encodings_2.png)

以下屏幕截图显示了将 TxtLoadOptions.setMultiEncoded() 方法设置为 true 后从上述 CSV 文件转换而来的 XSLX 文件。如您所见，Unicode 文本现在已正确转换。

**输出文件 2：IsMultiEncoded 设置为 true** 

![待办事项：图像_替代_文本](reading-csv-file-with-multiple-encodings_3.png)

下面是将上述 CSV 文件正确转换为 XLSX 格式的示例代码。

**Java**

{{< highlight "csharp" >}}

 String filePath = "F:\\Downloads\\MutliEncoded.csv";

//Set Multi Encoded Property to True

TxtLoadOptions options = new TxtLoadOptions();

options.setMultiEncoded(true);

//Load the CSV file into Workbook

Workbook workbook = new Workbook(filePath, options);

//Save it in XLSX format

workbook.save(filePath + ".out.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
