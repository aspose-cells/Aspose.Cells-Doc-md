---
title: 在Excel格式之间进行转换
type: docs
weight: 20
url: /zh/net/convert-between-excel-formats/
---

## **将Excel转换为PDF**

**PDF**文件被广泛用于组织之间、政府部门和个人之间的文档交换。这是一种标准文档格式，经常要求软件开发人员找到一种将Microsoft Excel文件转换为**PDF**文件的方法。
**Aspose.Cells**支持将Excel文件转换为PDF，并在转换过程中保持高度的视觉保真度。

Aspose.Cells for .NET 支持将电子表格转换为 PDF，独立于其他软件。使用 Workbook 类的 Save 方法将 Excel 文件保存为 PDF。Save 方法提供 SaveFormat.Pdf 枚举成员，可将原生 Excel 文件转换为 PDF 格式。

直接从电子表格转换为PDF，而不使用第三方工具或外部API，有一些**优势**：

1. 直接转换不需要临时文件，因为整个过程可以在内存中完成。
1. 不需要 XML 文件，因此可以轻松转换大文件。
1. 转换速度更快。

**将文件转换为PDF:**

1. 调用其空构造函数实例化 **Workbook** 类的对象。
1. 如果要从头开始创建工作簿，则可以 **打开/加载** 现有模板文件，或者跳过此步骤。
1. 使用Aspose.Cells的API在电子表格上执行所需的工作（输入数据，应用格式，设置公式，插入图片或其他绘图对象等）。
1. 当电子表格代码完成时，调用**Workbook类的Save方法**来保存电子表格。文件格式应为PDF，因此从SaveFormat枚举中选择Pdf（预定义值）以生成最终的PDF文档。

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  workbook.Save(saveFileDialog1.FileName, SaveFormat.Pdf);

{{< /highlight >}}

## **将Excel转换为MHTML**

**MHTML** 将常规HTML与外部资源结合在一起（即通常链接的内容，如图像、动画、音频等），放在一个文件中。它们用于带有.mht文件扩展名的电子邮件。
Aspose.Cells支持读取和写入MHTML文件。

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  //Specify the HTML Saving Options

  HtmlSaveOptions sv = new HtmlSaveOptions(SaveFormat.MHtml);

  workbook.Save(saveFileDialog1.FileName, sv);

{{< /highlight >}}

## **将Excel转换为XPS**

有时，您希望将包含多个工作表的工作簿转换或保存为文本格式。对于文本格式（例如TXT、TabDelim、CSV等），默认情况下，Microsoft Excel和Aspose.Cells仅保存活动工作表的内容。

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

 workbook.Save(saveFileDialog1.FileName, SaveFormat.CSV);

{{< /highlight >}}

## **下载示例代码**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Convert%20between%20Excel%20formats%20%28Aspose.Cells%29.zip)
