---
title: Добавить данные в Cells
type: docs
weight: 10
url: /ru/net/add-data-in-cells/
---
## **Aspose.Cells - Добавить данные в Cells**
Aspose.Cells предоставляет класс Workbook, который представляет файл Microsoft Excel. Класс Workbook содержит коллекцию WorksheetCollection, которая обеспечивает доступ к каждому рабочему листу в файле Excel. Рабочий лист представлен классом Worksheet. Класс Worksheet предоставляет коллекцию Cells. Каждый элемент коллекции Cells представляет объект класса Cell.

**C#**

{{< highlight "cs" >}}

 //Создание экземпляра объекта Workbook

Рабочая книга рабочая книга = новая рабочая книга();

//Доступ к добавленному рабочему листу в файле Excel

Рабочий лист рабочего листа = рабочая книга.Рабочие листы[0];

интервал х = 1;

 для (целое я = 1; я<= 15; i++)

{

    for (int j = 0; j < 15; j++)

    {

        worksheet.Cells[i, j].Value = x++;

    }

}

workbook.Save("test.xlsx");


{{< /highlight >}}
## **NPOI HSSF XSSF — добавить данные в Cells**
В NPOI row.createCell(1).setCellValue можно использовать для добавления данных в ячейки.

**C#**

{{< highlight "cs" >}}

 Рабочая книга IWorkbook = новая XSSFWorkbook();

ISheet sheet1 = workbook.CreateSheet("Лист1");

лист1.CreateRow(0).CreateCell(0).SetCellValue("Это образец");

интервал х = 1;

 для (целое я = 1; я<= 15; i++)

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
## **Скачать рабочий код**
 Скачать**Добавить данные в Cells** сформировать любой из перечисленных ниже сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Add.Data.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Добавление данных в Cells](/cells/ru/net/add-data-in-cells/).

{{% /alert %}}
