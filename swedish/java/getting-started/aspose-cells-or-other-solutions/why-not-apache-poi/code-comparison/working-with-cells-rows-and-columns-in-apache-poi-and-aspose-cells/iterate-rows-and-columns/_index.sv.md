---
title: Iterera rader och kolumner
type: docs
weight: 50
url: /sv/java/iterate-rows-and-columns/
description: Lär dig hur man itererar rader och kolumner genom de Aspose.Cells for Java API erna.
keywords: Hur man itererar rader och kolumner i Java, iterera rader med Java, Java itererar kolumner. 
---

## **Hur man itererar rader och kolumner med hjälp av Aspose.Cells for Java**

Rader och kolumner kan itereras med hjälp av rader och kolumner-samlingen.

**Java**

{{< highlight java >}}

 //Access the Maximum Display Range

Range range = worksheet.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int trows = range.getRowCount();

System.out.println("Total Rows:" + trows);

System.out.println("Total Cols:" + tcols);

RowCollection rows = cells.getRows();

for (int i = 0 ; i < rows.getCount() ; i++)

{

	for (int j = 0 ; j < tcols ; j++)

	{

		System.out.print(cells.get(i,j).getName() + " - " + cells.get(i,j).getValue() + "\t");

	}

	System.out.println("");

}

{{< /highlight >}}

## **Apache POI SS - HSSF XSSF - Iterera rader och kolumner**

Rader och celler kan itereras på kalkylarket. Exempelkoden anges nedan:

**Java**

{{< highlight java >}}

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

## **Ladda ned körbar kod**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## **Ladda ned provkoden**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/iterate)

{{< app/cells/assistant language="java" >}}
