---
title: 在 xlsx4j 中将每个工作表保存到不同的 PDF
type: docs
weight: 50
url: /zh/java/save-each-worksheet-to-different-pdf-in-xlsx4j/
---
## **Aspose.Cells - 将每个工作表保存到不同的 PDF**
Aspose.Cells 支持将 XLS 文件（包含图像、图表等）转换为 PDF 文档。 Aspose.Cells for Java 可以独立工作将电子表格转换为Pdf文档，您不再需要使用Aspose.Pdf for Java进行转换。转换也不需要创建/使用任何临时文件，因为整个过程可以在内存中完成。

**Java**

{{< highlight "java" >}}

 //获取Excel文件路径

String filePath = dataDir + "workbook.xlsx";

//实例化一个新工作簿并打开Excel

//文件从它的位置

工作簿 workbook = new Workbook(filePath);

//获取工作簿中工作表的个数

int sheetCount = workbook.getWorksheets().getCount();

//使除第一个工作表外的所有工作表不可见

对于 (int i = 1; i< workbook.getWorksheets().getCount(); i++)

{

     workbook.getWorksheets().get(i).setVisible(false);

}

//Take Pdfs of each sheet

for (int j = 0; j < workbook.getWorksheets().getCount(); j++)

{

    Worksheet ws = workbook.getWorksheets().get(j);

    workbook.save(dataPath + ws.getName() + ".pdf");

    if (j < workbook.getWorksheets().getCount() - 1)

    {

       workbook.getWorksheets().get(j + 1).setVisible(true);

       workbook.getWorksheets().get(j).setVisible(false);

    }

}

{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/saveeachworksheettopdf/AsposeSaveEachWorksheetToDifferentPDF.java)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[将每个工作表保存到不同的 PDF 文件](/cells/zh/java/save-each-worksheet-to-a-different-pdf-file).

{{% /alert %}}
