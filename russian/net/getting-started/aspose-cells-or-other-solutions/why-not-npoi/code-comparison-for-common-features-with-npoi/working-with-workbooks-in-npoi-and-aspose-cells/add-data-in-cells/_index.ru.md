---
title: Добавление данных в ячейки
type: docs
weight: 10
url: /ru/net/add-data-in-cells/
description: В этой статье объясняется, как добавлять данные в ячейки с использованием API Aspose.Cells for .NET.
keywords: C# Добавление данных в ячейки, C# Вставка данных в лист, C# Установка данных ячейки.
---


## **Как добавить данные в ячейки с использованием Aspose.Cells for .NET**
Aspose.Cells предоставляет класс, Workbook, который представляет собой файл Microsoft Excel. Класс Workbook содержит WorksheetCollection, который позволяет получить доступ к каждому рабочему листу в файле Excel. Лист представлен классом Worksheet. Класс Worksheet предоставляет коллекцию Cells. Каждый элемент в коллекции Cells представляет объект класса Cell.

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
## **NPOI HSSF XSSF - Добавление данных в ячейки**
В NPOI можно использовать row.createCell(1).setCellValue для добавления данных в ячейки.

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
## **Скачать работающий код**
Скачать **Добавление данных в ячейки** с любого из указанных сайтов социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Для получения дополнительной информации посетите [Добавление данных в ячейки](/cells/ru/net/add-data-in-cells/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
