---
title: 在 Excel 格式之间转换
type: docs
weight: 20
url: /zh/net/convert-between-excel-formats/
---
## **将 Excel 转换为 PDF**

**PDF**文件广泛用于组织、政府部门和个人之间交换文件。它是一种标准文档格式，软件开发人员经常被要求找到一种方法将 Microsoft Excel 文件转换为**PDF**文件。
**Aspose.Cells**支持将Excel文件转换为PDF，并在转换过程中保持高视觉保真度。

Aspose.Cells for .NET 支持独立于其他软件从电子表格转换为PDF。使用 Workbook 类的 Save 方法将 Excel 文件保存到 PDF。 Save 方法提供将本机 Excel 文件转换为 PDF 格式的 SaveFormat.Pdf 枚举成员。

**转换**直接从电子表格到 PDF，而不是使用第三方工具或外部 API，有几个**优点**:

1. 直接转换不需要临时文件，因为整个过程都可以在内存中完成。
1. 不需要 XML 文件，因此可以轻松转换大文件。
1. 转换速度要快得多。

**将文件转换为 PDF：**

1. 实例化一个对象**工作簿**通过调用它的空构造函数来类。
1. 你可以**打开/加载**一个现有的模板文件，如果您是从头开始创建工作簿，则跳过此步骤。
1. 使用 Aspose.Cells' API 在电子表格上执行所需的工作（输入数据、应用格式、设置公式、插入图片或其他绘图对象等）。
1. 电子表格代码完成后，调用**工作簿类的保存方法**保存电子表格。文件格式应为 PDF，因此从 SaveFormat 枚举中选择 Pdf（预定义值）以生成最终的 PDF 文档。

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  workbook.Save(saveFileDialog1.FileName, SaveFormat.Pdf);

{{< /highlight >}}

## **将 Excel 转换为 MHTML**

**MHTML**将正常的 HTML 与外部资源（即通常链接进来的内容，如图像、动画、音频等）合并到一个文件中。它们用于文件扩展名为 .mht 的电子邮件。
Aspose.Cells支持读写MHTML文件。

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

  //Specify the HTML Saving Options

  HtmlSaveOptions sv = new HtmlSaveOptions(SaveFormat.MHtml);

  workbook.Save(saveFileDialog1.FileName, sv);

{{< /highlight >}}

## **将 Excel 转换为 XPS**

有时，您希望将包含多个工作表的工作簿转换或保存为文本格式。对于文本格式（例如 TXT、TabDelim、CSV 等），默认情况下 Microsoft Excel 和 Aspose.Cells 仅保存活动工作表的内容。

{{< highlight "csharp" >}}

  Workbook workbook = new Workbook(openFileDialog1.FileName);

 workbook.Save(saveFileDialog1.FileName, SaveFormat.CSV);

{{< /highlight >}}

## **下载示例代码**

- [Github](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/tag/MissingFeaturesOpenXMLExcelv1.1)
- [比特桶](https://bitbucket.org/asposemarketplace/aspose-for-openxml/downloads/Convert%20between%20Excel%20formats%20%28Aspose.Cells%29.zip)
