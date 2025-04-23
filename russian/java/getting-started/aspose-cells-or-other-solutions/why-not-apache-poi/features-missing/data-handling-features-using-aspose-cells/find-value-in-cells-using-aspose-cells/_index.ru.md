---
title: Поиск значения в ячейках с использованием Aspose.Cells
type: docs
weight: 10
url: /ru/java/find-value-in-cells-using-aspose-cells/
---

## **Aspose.Cells - Найти Значение в Ячейках**
В Microsoft Excel пользователи могут искать ячейки, содержащие определенные данные. Например, щелкнув **Правка** и затем **Поиск**, открывается диалоговое окно поиска. Пользователь вводит значение и щелкает **OK** для поиска. Excel выделяет соответствующие поля.

**Java**

{{< highlight java >}}

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
## **Скачать работающий код**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **Загрузить образец кода**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/blob/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/asposefeatures/search/AsposeFindCellsWithString.java)

{{% alert color="primary" %}} 

Дополнительные сведения см. по адресу [Поиск данных](/cells/ru/java/find-or-search-data).

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
