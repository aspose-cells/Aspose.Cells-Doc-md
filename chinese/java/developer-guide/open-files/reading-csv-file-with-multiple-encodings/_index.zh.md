---
title: 读取具有多种编码的CSV文件
type: docs
weight: 140
url: /zh/java/reading-csv-file-with-multiple-encodings/
---

{{% alert color="primary" %}} 

有时，您的CSV文件包含多种编码（Unicode、ANSI、UTF8、UTF7等）。Aspose.Cells允许您加载这些CSV文件，并将它们转换为其他格式，例如PDF或XLSX。

{{% /alert %}} 

Aspose.Cells提供了TxtLoadOptions.setMultiEncoded()方法，您需要将其设置为**true**，以正常加载具有多种编码的CSV文件。

以下截图显示了一个包含两行的样本CSV文件。第一行是用**ANSI**编码，第二行是用**Unicode**编码。

**输入文件** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_1.png)

以下截图显示了从上述CSV文件转换的XLSX文件，而未将TxtLoadOptions.setMultiEncoded()方法设置为true。您可以看到，Unicode文本未正确转换。

**输出文件1：未提供多重编码的处理** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_2.png)

以下截图显示了从上述CSV文件转换的XLSX文件，设置了TxtLoadOptions.setMultiEncoded()方法为true。您可以看到，Unicode文本现在已正确转换。

**输出文件2：IsMultiEncoded 已设置为 true** 

![todo:image_alt_text](reading-csv-file-with-multiple-encodings_3.png)

以下是将上述CSV文件正确转换为XLSX格式的示例代码。

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
