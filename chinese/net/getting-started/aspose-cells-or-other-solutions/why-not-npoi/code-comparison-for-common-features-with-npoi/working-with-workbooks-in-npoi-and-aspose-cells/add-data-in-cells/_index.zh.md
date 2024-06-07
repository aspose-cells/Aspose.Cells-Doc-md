---
title: 在单元格中添加数据
type: docs
weight: 10
url: /zh/net/add-data-in-cells/
description: 本文介绍如何使用Aspose.Cells为.NET API在单元格中添加数据。
keywords: 在C＃中向单元格添加数据，C＃中将数据插入工作表，C＃中设置单元格的数据。
---


## **如何使用Aspose.Cells为.NET添加单元格中的数据**
Aspose.Cells提供了一个类，Workbook，代表一个Microsoft Excel文件。Workbook类包含一个WorksheetCollection，允许访问Excel文件中的每个工作表。工作表由Worksheet类表示。Worksheet类提供了一个Cells集合。Cells集合中的每个项代表Cell类的对象。

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the added worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

int x = 1;

for (int i = 1; i <= 15; i++)

{

    for (int j = 0; j < 15; j++)

    {

        worksheet.Cells[i, j].Value = x++;

    }

}

workbook.Save("test.xlsx");


{{< /highlight >}}
## **NPOI HSSF XSSF - 向单元格中添加数据**
在NPOI中，row.createCell(1).setCellValue可用于向单元格中添加数据。

**C#**

{{< highlight cs >}}

 IWorkbook workbook = new XSSFWorkbook();

ISheet sheet1 = workbook.CreateSheet("Sheet1");

sheet1.CreateRow(0).CreateCell(0).SetCellValue("This is a Sample");

int x = 1;

for (int i = 1; i <= 15; i++)

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
从以下社交编码网站之一下载**在单元格中添加数据**：

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

欲了解更多详情，请访问[向单元格添加数据](/cells/zh/net/add-data-in-cells/)。

{{% /alert %}}
