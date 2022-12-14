---
title: Найти значение в Cells
type: docs
weight: 20
url: /ru/net/find-value-in-cells/
---
## **Aspose.Cells - Найти значение в Cells**
В Microsoft Excel пользователи могут искать ячейки, содержащие определенные данные. Например, нажав**Редактировать**а потом**Находить**открывает диалоговое окно поиска. Пользователи вводят значение и нажимают**ХОРОШО**искать его. Excel выделяет совпадающие поля.

**C#**

{{< highlight "cs" >}}

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
## **Скачать рабочий код**
 Скачать**Найти значение в Cells** сформировать любой из перечисленных ниже сайтов социального кодирования:

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/AsposeCellsFeaturesMissinginNPOI_v1.0/Find.Value.In.Cells.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Поиск или поиск данных](/cells/ru/net/find-or-search-data/).

{{% /alert %}}
