---
title: Zeilen und Spalten iterieren
type: docs
weight: 50
url: /de/java/iterate-rows-and-columns/
---
## **Aspose.Cells – Zeilen und Spalten iterieren**

Zeilen und Spalten können mithilfe der Zeilen- und Spaltensammlung iteriert werden.

**Java**

{{< highlight "java" >}}

 // Zugriff auf den maximalen Anzeigebereich

Bereich range = worksheet.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int trows = range.getRowCount();

System.out.println("Gesamtzeilen:" + trows);

System.out.println("Total Cols:" + tcols);

RowCollection rows = cells.getRows();

 für (int i = 0 ; i< rows.getCount() ; i++)

{

	for (int j = 0 ; j < tcols ; j++)

	{

		System.out.print(cells.get(i,j).getName() + " - " + cells.get(i,j).getValue() + "\t");

	}

	System.out.println("");

}

{{< /highlight >}}

## **Apache POI SS - HSSF XSSF - Zeilen und Spalten durchlaufen**

Zeilen und Cells können auf Sheet iteriert werden. Beispielcode ist unten erwähnt:

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

## **Laufcode herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## **Beispielcode herunterladen**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/iterate)

