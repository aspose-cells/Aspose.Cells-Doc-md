---
title: 在 Cells 中添加数据
type: docs
weight: 10
url: /zh/net/add-data-in-cells/
---
## **Aspose.Cells - 在 Cells 中添加数据**
Aspose.Cells 提供了一个类 Workbook，它表示一个 Microsoft Excel 文件。 Workbook 类包含一个 WorksheetCollection，它允许访问 Excel 文件中的每个工作表。工作表由 Worksheet 类表示。 Worksheet 类提供了一个 Cellscollection。 Cells 集合中的每一项都代表 Cell 类的一个对象。

**C#**

{{< highlight "cs" >}}

//实例化一个工作簿对象

工作簿workbook = new Workbook();

//访问Excel文件中添加的工作表

工作表worksheet = workbook.Worksheets[0];

整数 x = 1;

对于 (int i = 1; i<= 15; i++)

{

    for (int j = 0; j < 15; j++)

    {

        worksheet.Cells[i, j].Value = x++;

    }

}

workbook.Save("test.xlsx");


{{< /highlight >}}
## **NPOI HSSF XSSF - 在 Cells 中添加数据**
在 NPOI 中，row.createCell(1).setCellValue 可用于在单元格中添加数据。

**C#**

{{< highlight "cs" >}}

 IWorkbook 工作簿 = new XSSFWorkbook();

ISheet sheet1 = workbook.CreateSheet("Sheet1");

sheet1.CreateRow(0).CreateCell(0).SetCellValue("这是一个样本");

整数 x = 1;

对于 (int i = 1; i<= 15; i++)

{

	IRow row = sheet1.CreateRow(i);

	for (int j = 0; j < 15; j++)

	{

		row.CreateCell(j).SetCellValue(x++);

	}

}

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();

{{< /highlight >}}
## **下载运行代码**
下载**在 Cells 中添加数据**形成以下任何一个社交编码网站：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[添加数据到 Cells](/cells/zh/net/add-data-in-cells/).

{{% /alert %}}
