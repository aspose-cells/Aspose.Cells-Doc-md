---
title: Установить заголовки для печати
type: docs
weight: 30
url: /ru/net/set-print-titles/
---
## **Aspose.Cells - Установить заголовки для печати**
Aspose.Cells позволяет указать, что заголовки строк и столбцов будут повторяться на всех страницах печатного листа. Для этого используйте[Настройка страницы](https://reference.aspose.com/cells/net/aspose.cells/pagesetup)свойства класса PrintTitleColumns и PrintTitleRows.

Строки или столбцы, которые будут повторяться, определяются путем передачи их номеров строк или столбцов. Например, строки определяются как $1:$2, а столбцы — как $A:$B.

**C#**

{{< highlight "cs" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows= "$1:$2";

{{< /highlight >}}
## **Скачать рабочий код**
 Скачать**Установить заголовки для печати** сформировать любой из перечисленных ниже сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Print.Titles.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Настройка параметров печати](/cells/ru/net/setting-print-options/).

{{% /alert %}}
