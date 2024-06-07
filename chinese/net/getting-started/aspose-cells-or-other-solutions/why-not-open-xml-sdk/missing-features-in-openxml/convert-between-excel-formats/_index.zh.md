---
title: 在Excel格式之间转换
type: docs
weight: 20
url: /zh/net/convert-between-excel-formats/
---

## **将Excel转换为PDF**

**PDF**文件被广泛用于组织、政府部门和个人之间交换文档。它是一种标准文档格式，软件开发人员经常被要求找到一种将Microsoft Excel文件转换为**PDF**文档的方法。
**Aspose.Cells**支持将Excel文件转换为PDF，并在转换过程中保持高视觉保真度。

Aspose.Cells for .NET支持从电子表格转换为PDF，独立于其他软件。使用Workbook类的Save方法将Excel文件保存为PDF。Save方法提供了SaveFormat.Pdf枚举成员，将本机Excel文件转换为PDF格式。

**直接**从电子表格转换为PDF，而不使用第三方工具或外部API，具有以下**优点**：

1. 直接转换不需要临时文件，因为整个过程可以在内存中完成。
1. 不需要XML文件，因此可以轻松转换大文件。
1. 转换速度更快。

**要将文件转换为PDF：**

1. 通过调用其空构造函数实例化**Workbook**类的对象。
1. 可以**打开/加载**现有的模板文件，或者如果您是从头开始创建工作簿，则可以跳过此步骤。
1. 使用Aspose.Cells的API对电子表格进行所需的操作（输入数据，应用格式，设置公式，插入图片或其他绘图对象等）。
1. 当电子表格代码完成时，调用**Workbook类的Save方法**保存电子表格。文件格式应为PDF，因此从SaveFormat枚举中选择Pdf（一种预定义值）以生成最终的PDF文档。

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  workbook.Save(saveFileDialog1.FileName, SaveFormat.Pdf);

{{< /highlight >}}

## **将Excel转换为MHTML**

**MHTML**将普通HTML与外部资源（通常是链接的内容，如图像、动画、音频等）组合为一个文件。它们用于带有.mht文件扩展名的电子邮件。
Aspose.Cells支持读取和编写MHTML文件。

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  //Specify the HTML Saving Options

  HtmlSaveOptions sv = new HtmlSaveOptions(SaveFormat.MHtml);

  workbook.Save(saveFileDialog1.FileName, sv);

{{< /highlight >}}

## **将Excel转换为XPS**

有时，您希望将一个包含多个工作表的工作簿转换或保存为文本格式。对于文本格式（例如TXT、TabDelim、CSV等），默认情况下Microsoft Excel和Aspose.Cells只保存活动工作表的内容。

{{< highlight csharp >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

 workbook.Save(saveFileDialog1.FileName, SaveFormat.CSV);

{{< /highlight >}}

## **下载示例代码**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Convert%20between%20Excel%20formats%20%28Aspose.Cells%29.zip)
