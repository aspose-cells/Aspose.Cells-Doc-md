---
title: 从 xlsx4j 中的工作表导出数据
type: docs
weight: 20
url: /zh/java/export-data-from-worksheets-in-xlsx4j/
---
## **Aspose.Cells - 从工作表导出数据**
Aspose.Cells 不仅允许其用户将数据从外部数据源导入工作表，还允许他们将工作表数据导出到数组。

**Java**

{{< highlight "java" >}}

//创建包含要打开的Excel文件的文件流

FileInputStream fstream = new FileInputStream(dataDir + "workbook.xls");

//实例化一个工作簿对象

工作簿工作簿=新工作簿（fstream）；

//访问Excel文件中的第一个工作表

工作表worksheet = workbook.getWorksheets().get(0);

//导出从第一个cell开始的7行2列的内容到Array。

对象数据表 [][]= worksheet.getCells().exportArray(4,0,7,8);

对于 (int i = 0 ; i< dataTable.length ; i++)

{

	System.out.println("["+ i +"]: "+ Arrays.toString(dataTable[i]));

}

{{< /highlight >}}
## **下载运行代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Xlsx4j-v1.0.0)
## **下载示例代码**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_Java_for_Xlsx4j/src/main/java/com/aspose/cells/examples/asposefeatures/datahandling/exportdatafromworksheets/AsposeExportDataFromWorksheets.java)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[从工作表导出数据](/java/exporting-data-from-worksheets).

{{% /alert %}}
