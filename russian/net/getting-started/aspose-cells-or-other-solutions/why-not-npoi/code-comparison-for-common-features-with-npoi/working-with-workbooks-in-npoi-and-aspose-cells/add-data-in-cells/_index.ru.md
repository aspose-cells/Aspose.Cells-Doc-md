---
title: Добавьте данные в Cells
type: docs
weight: 10
url: /ru/net/add-data-in-cells/
description: В этой статье объясняется, как добавить данные в Cells с помощью API Aspose.Cells for .NET.
keywords: C# Add Data in Cells, C# Insert Data to Worksheet, C# Set Data of Cell.
---
##  **Как добавить данные в Cells с помощью Aspose.Cells for .NET**
Aspose.Cells предоставляет класс Workbook, который представляет файл Excel Microsoft. Класс Workbook содержит WorksheetCollection, который обеспечивает доступ к каждому листу в файле Excel. Рабочий лист представлен классом Worksheet. Класс Worksheet предоставляет коллекцию Cellscollection. Каждый элемент коллекции Cells представляет объект класса Cell.

**C#**

{{< highlight "cs" >}}

 //Создание экземпляра объекта Workbook

Рабочая книга рабочая книга = новая рабочая книга();

//Доступ к добавленному листу в файле Excel

Рабочий лист рабочий лист = workbook.Worksheets[0];

интервал х = 1;

для (int я = 1; я<= 15; i++)

{

    for (int j = 0; j < 15; j++)

    {

        worksheet.Cells[i, j].Value = x++;

    }

}

workbook.Save("test.xlsx");


{{< /highlight >}}
##  **NPOI HSSF XSSF — добавить данные в Cells**
В NPOI row.createCell(1).setCellValue можно использовать для добавления данных в ячейки.

**C#**

{{< highlight "cs" >}}

 Рабочая книга IWorkbook = новая XSSFWorkbook();

ISheet лист1 = рабочая книга.CreateSheet("Лист1");

лист1.CreateRow(0).CreateCell(0).SetCellValue("Это образец");

интервал х = 1;

для (int я = 1; я<= 15; i++)

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
##  **Загрузить рабочий код**
 Скачать**Добавьте данные в Cells** создайте любой из нижеперечисленных сайтов социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Добавление данных в номер Cells](/cells/ru/net/add-data-in-cells/).

{{% /alert %}}
