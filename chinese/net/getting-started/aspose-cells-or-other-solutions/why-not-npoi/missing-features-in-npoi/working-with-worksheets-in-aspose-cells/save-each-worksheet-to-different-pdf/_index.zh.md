---
title: 将每个工作表保存到不同的 PDF
type: docs
weight: 10
url: /zh/net/save-each-worksheet-to-different-pdf/
---
## **Aspose.Cells - 将每个工作表保存到不同的 PDF**
Aspose.Cells 支持将 XLS 文件（包含图像、图表等）转换为 PDF 文档。 Aspose.Cells for .NET 可以独立工作将电子表格转换为Pdf文档，您不再需要使用Aspose.Pdf for .NET进行转换。转换也不需要创建/使用任何临时文件，因为整个过程可以在内存中完成。

**C#**

{{< highlight "cs" >}}

 //实例化一个新工作簿并打开Excel

//文件从它的位置

工作簿 workbook = new Workbook("../../data/test.xlsx");

//获取工作簿中工作表的个数

int sheetCount = workbook.Worksheets.Count;

//使除第一个工作表外的所有工作表不可见

对于 (int i = 1; i< workbook.Worksheets.Count; i++)

{

    workbook.Worksheets[i].IsVisible = false;

}

//Take Pdfs of each sheet

for (int j = 0; j < workbook.Worksheets.Count; j++)

{

    Worksheet ws = workbook.Worksheets[j];

    workbook.Save(ws.Name + ".pdf");

    if (j < workbook.Worksheets.Count - 1)

    {

        workbook.Worksheets[j + 1].IsVisible = true;

        workbook.Worksheets[j].IsVisible =false;

    }

}

{{< /highlight >}}
## **下载运行代码**
下载**将每个工作表保存到不同的 PDF**形成以下任何一个社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Save.Each.Worksheet.to.Different.PDF.Aspose.Cells.zip)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[将每个工作表保存到不同的 PDF 文件](https://docs.aspose.com/cells/net/save-each-worksheet-to-a-different-pdf-file/).

{{% /alert %}}
