---
title: Итерация строк и столбцов
type: docs
weight: 50
url: /ru/java/iterate-rows-and-columns/
description: Узнайте, как перебирать строки и столбцы с помощью API Aspose.Cells for Java.
keywords: How to Iterate Rows and Columns in Java, Iterate Rows using Java, Java Iterate Columns. 
---
##  **Как перебирать строки и столбцы, используя Aspose.Cells for Java**

Строки и столбцы можно перебирать, используя коллекцию строк и столбцов.

**Java**

{{< highlight "java" >}}

 //Доступ к максимальному диапазону отображения

Диапазон диапазона = worksheet.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int trows = range.getRowCount();

System.out.println("Всего строк:" + trows);

System.out.println("Всего столбцов:" + tcols);

RowCollection rows = cell.getRows();

 для (int i = 0; я< rows.getCount() ; i++)

{

	for (int j = 0 ; j < tcols ; j++)

	{

		System.out.print(cells.get(i,j).getName() + " - " + cells.get(i,j).getValue() + "\t");

	}

	System.out.println("");

}

{{< /highlight >}}

##  **Apache POI SS — HSSF XSSF — перебор строк и столбцов**

Строки и Cells можно повторять на листе. Пример кода указан ниже:

**Java**

{{< highlight "java" >}}

 Workbook wb = WorkbookFactory.create(inStream);

Sheet sheet = wb.getSheetAt(0);

for (Row row : sheet)

{

  for (Cell cell : row)

  {

    System.out.println("Iteration.");

  }

}

{{< /highlight >}}

##  **Загрузить рабочий код**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

##  **Скачать пример кода**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/iterate)

