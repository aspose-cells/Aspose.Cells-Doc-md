---
title: Найти Значение в Ячейках
type: docs
weight: 20
url: /ru/net/find-value-in-cells/
---

## **Aspose.Cells - Найти Значение в Ячейках**
В Microsoft Excel пользователи могут искать ячейки, содержащие определенные данные. Например, щелкнув **Правка** и затем **Поиск**, открывается диалоговое окно поиска. Пользователь вводит значение и щелкает **OK** для поиска. Excel выделяет соответствующие поля.

**C#**

{{< highlight cs >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("../../data/test.xlsx");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Finding the cell containing the specified formula

Cells cells = worksheet.Cells;

//Instantiate FindOptions

FindOptions findOptions = new FindOptions();

//Finding the cell containing a string value that starts with "Or"

findOptions.LookAtType = LookAtType.StartWith;

Cell cell = cells.Find("SH", null, findOptions);

//Printing the name of the cell found after searching worksheet

Console.WriteLine("Name of the cell containing String: " + cell.Name);

{{< /highlight >}}
## **Скачать работающий код**
Скачать **Найти Значение в Ячейках** с любого из упомянутых выше социальных сайтов для кодинга:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Find.Value.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

Для получения более подробной информации посетите [Найти или Поиск Данных](/cells/ru/net/find-or-search-data/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
