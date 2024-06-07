---
title: 保存每个工作表为不同的PDF
type: docs
weight: 10
url: /zh/net/save-each-worksheet-to-different-pdf/
---

## **Aspose.Cells - 将每个工作表保存为不同的PDF**
Aspose.Cells支持将包含图像、图表等内容的XLS文件转换为PDF文档。Aspose.Cells for .NET可以独立工作，将电子表格转换为PDF文档，无需再使用Aspose.Pdf for .NET进行转换。转换也不需要创建/使用任何临时文件，整个过程可以在内存中完成。

**C#**

{{< highlight cs >}}

 //Instantiate a new workbook and open the Excel

//File from its location

Workbook workbook = new Workbook("../../data/test.xlsx");

//Get the count of the worksheets in the workbook

int sheetCount = workbook.Worksheets.Count;

//Make all sheets invisible except first worksheet

for (int i = 1; i < workbook.Worksheets.Count; i++)

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
从以下提到的任何社交编码网站下载**将每个工作表保存为不同的PDF**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Save.Each.Worksheet.to.Different.PDF.Aspose.Cells.zip)

{{% alert color="primary" %}} 

有关更多详细信息，请访问[将每个工作表保存为不同的PDF文件](https://docs.aspose.com/cells/net/save-each-worksheet-to-a-different-pdf-file/)。

{{% /alert %}}
