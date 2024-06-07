---
title: 使用Aspose.Cells将每个工作表保存为不同的PDF
type: docs
weight: 80
url: /zh/java/save-each-worksheet-to-different-pdf-using-aspose-cells/
---

## **Aspose.Cells - 将每个工作表保存为不同的PDF**
Aspose.Cells支持将包含图像、图表等的XLS文件转换为PDF文档。Aspose.Cells for Java可以独立工作，将电子表格转换为PDF文档，您不再需要使用Aspose.Pdf for Java进行转换。转换也不需要创建/使用任何临时文件，因为整个过程可以在内存中完成。

**Java**

{{< highlight java >}}

 //Get the Excel file path

String filePath = dataDir + "workbook.xlsx";

//Instantiate a new workbook and open the Excel

//File from its location

Workbook workbook = new Workbook(filePath);

//Get the count of the worksheets in the workbook

int sheetCount = workbook.getWorksheets().getCount();

//Make all sheets invisible except first worksheet

for (int i = 1; i < workbook.getWorksheets().getCount(); i++)

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
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/worksheets/SaveEachWorksheetToDifferentPDF.java)

{{% alert color="primary" %}} 

有关详细信息，请访问[将每个工作表保存为不同的PDF文件](/cells/zh/java/save-each-worksheet-to-a-different-pdf-file)。

{{% /alert %}}
