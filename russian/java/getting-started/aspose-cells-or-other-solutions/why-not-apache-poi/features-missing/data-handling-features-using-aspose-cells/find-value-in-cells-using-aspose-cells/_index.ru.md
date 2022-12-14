---
title: Найдите значение в Cells, используя Aspose.Cells
type: docs
weight: 10
url: /ru/java/find-value-in-cells-using-aspose-cells/
---
## **Aspose.Cells - Найти значение в Cells**
В Microsoft Excel пользователи могут искать ячейки, содержащие определенные данные. Например, нажав**Редактировать**а потом**Находить**открывает диалоговое окно поиска. Пользователи вводят значение и нажимают**ХОРОШО**искать его. Excel выделяет совпадающие поля.

**Java**

{{< highlight "java" >}}

 //Instantiating a Workbook object

Workbook workbook = new Workbook("workbook.xls");

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.getWorksheets().get(0);

//Finding the cell containing the specified formula

Cells cells = worksheet.getCells();

//Instantiate FindOptions

FindOptions findOptions = new FindOptions();

//Finding the cell containing a string value that starts with "Or"

findOptions.setLookAtType(LookAtType.START_WITH);

Cell cell = cells.find("SH",null,findOptions);

//Printing the name of the cell found after searching worksheet

System.out.println("Name of the cell containing String: " + cell.getName());

{{< /highlight >}}
## **Скачать рабочий код**

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Скачать пример кода**
- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/search/AsposeFindCellsWithString.java)

{{% alert color="primary" %}} 

 Для получения более подробной информации посетите[Поиск или поиск данных](/cells/ru/java/find-or-search-data).

{{% /alert %}}
