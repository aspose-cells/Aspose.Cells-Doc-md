---
title: Итерация строк и столбцов
type: docs
weight: 50
url: /ru/java/iterate-rows-and-columns/
---
## **Aspose.Cells - Итерация строк и столбцов**

Строки и столбцы можно повторять, используя коллекцию строк и столбцов.

**Java**

{{< highlight "java" >}}

 // Доступ к максимальному диапазону отображения

Диапазон диапазона = рабочий лист.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int trows = range.getRowCount();

System.out.println("Всего строк:" + trows);

System.out.println("Всего столбцов:" + tcols);

RowCollection rows = Cells.getRows();

 для (int я = 0 ; я< rows.getCount() ; i++)

{

	for (int j = 0 ; j < tcols ; j++)

	{

		System.out.print(cells.get(i,j).getName() + " - " + cells.get(i,j).getValue() + "\t");

	}

	System.out.println("");

}

{{< /highlight >}}

## **Apache POI SS — HSSF XSSF — Итерация строк и столбцов**

Строки и Cells могут повторяться на листе. Пример кода указан ниже:

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

## **Скачать рабочий код**

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## **Скачать пример кода**

- [Гитхаб](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/itate)

