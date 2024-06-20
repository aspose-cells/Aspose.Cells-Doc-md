---
title: Установка Заголовков для Печати
type: docs
weight: 30
url: /ru/net/set-print-titles/
---

## **Aspose.Cells - Установка Заголовков для Печати**
Aspose.Cells позволяет указывать строки и столбцы заголовков для повторения на всех страницах напечатанного листа. Для этого используйте класс [PageSetup](https://reference.aspose.com/cells/net/aspose.cells/pagesetup) свойства PrintTitleColumns и PrintTitleRows.

Строки или столбцы, которые будут повторяться, определяются путем передачи их номеров строки или столбца. Например, строки определяются как $1:$2, а столбцы определяются как $A:$B.

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Obtaining the reference of the PageSetup of the worksheet

PageSetup pageSetup = workbook.Worksheets[0].PageSetup;

//Defining column numbers A & B as title columns

pageSetup.PrintTitleColumns = "$A:$B";

//Defining row numbers 1 & 2 as title rows

pageSetup.PrintTitleRows= "$1:$2";

{{< /highlight >}}
## **Скачать работающий код**
Скачать **Установка заголовков для печати** с любого из упомянутых ниже сайтов социального кодирования:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Set.Print.Titles.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Для получения более подробной информации перейдите на [Настройка параметров печати](/cells/ru/net/setting-print-options/).

{{% /alert %}}
