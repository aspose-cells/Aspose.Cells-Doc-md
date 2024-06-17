---
title: 使用多种编码方式读取CSV文件
type: docs
weight: 140
url: /zh/java/reading-csv-file-with-multiple-encodings/
---

{{% alert color="primary" %}} 

有时，您的CSV文件包含多种编码（Unicode、ANSI、UTF8、UTF7等）。 Aspose.Cells允许您加载此类CSV文件并将其转换为其他格式，例如PDF或XLSX。

{{% /alert %}} 

Aspose.Cells 提供了 TxtLoadOptions.setMultiEncoded() 方法，您需要将其设置为 **true** 才能正确加载具有多种编码的 CSV 文件。

以下截图显示了一个包含两行的示例 CSV 文件。第一行是以 **ANSI** 编码，第二行是以 **Unicode** 编码。

输入文件 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)

以下截图显示了从上述 CSV 文件转换而来的 XLSX 文件，该文件在没有将 TxtLoadOptions.setMultiEncoded() 方法设置为 true 的情况下进行转换。如您所见，Unicode 文本未能正确转换。

**输出文件 1: 未做多重编码的处理** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)

以下截图显示了在将 TxtLoadOptions.setMultiEncoded() 方法设置为 true 后，从上述 CSV 文件转换而来的 XSLX 文件。如您所见，Unicode 文本现在已经正确转换。

**输出文件 2: IsMultiEncoded 已设置为 true** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)

以下是将上述 CSV 文件正确转换为 XLSX 格式的示例代码。

**Java**

{{< highlight csharp >}}

 String filePath = "F:\\Downloads\\MutliEncoded.csv";

//Set Multi Encoded Property to True

TxtLoadOptions options = new TxtLoadOptions();

options.setMultiEncoded(true);

//Load the CSV file into Workbook

Workbook workbook = new Workbook(filePath, options);

//Save it in XLSX format

workbook.save(filePath + ".out.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
