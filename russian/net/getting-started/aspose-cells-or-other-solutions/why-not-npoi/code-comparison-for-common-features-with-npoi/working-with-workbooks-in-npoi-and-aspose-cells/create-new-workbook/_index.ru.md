---
title: Создание новой книги
type: docs
weight: 20
url: /ru/net/create-new-workbook/
---

## **Aspose.Cells - Создание новой книги**
Класс Workbook доступен для простого использования

**C#**

{{< highlight cs >}}

 Workbook workbook = new Workbook(); // Creating a Workbook object

workbook.Save("test.xlsx", SaveFormat.Xlsx); //Workbooks can be saved in many formats

{{< /highlight >}}
## **NPOI - HSSF XSSF - Создание новой книги**
Создание новой книги с использованием класса Workbook и сохранение с помощью FileOutputStream.

**C#**

{{< highlight cs >}}

 IWorkbook workbook = new XSSFWorkbook();

workbook.CreateSheet("Sheet A1");

workbook.CreateSheet("Sheet A2");

workbook.CreateSheet("Sheet A3");

FileStream sw = File.Create("test.xlsx");

workbook.Write(sw);

sw.Close();

{{< /highlight >}}
## **Скачать работающий код**
Загрузить **Создание новой книги** с любого из нижеуказанных сайтов социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Create.New.Workbook.Aspose.Cells.zip)
{{< app/cells/assistant language="csharp" >}}
