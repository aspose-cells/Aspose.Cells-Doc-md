---
title: Iterera rader och kolumner
type: docs
weight: 50
url: /sv/java/iterate-rows-and-columns/
---
## **Aspose.Cells - Iterera rader och kolumner**

Rader och kolumner kan itereras med rader och kolumner.

**Java**

{{< highlight "java" >}}

 //Åtkomst till det maximala visningsintervallet

Range range = workheet.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int trows = range.getRowCount();

System.out.println("Totalt antal rader:" + trows);

System.out.println("Totalt kol:" + tcols);

RowCollection rows = cells.getRows();

 för (int i = 0 ; i< rows.getCount() ; i++)

{

	for (int j = 0 ; j < tcols ; j++)

	{

		System.out.print(cells.get(i,j).getName() + " - " + cells.get(i,j).getValue() + "\t");

	}

	System.out.println("");

}

{{< /highlight >}}

## **Apache POI SS - HSSF XSSF - Iterera rader och kolumner**

Rader och Cells kan itereras på Kalkylark. Exempelkod nämns nedan:

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

## **Ladda ner Running Code**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## **Ladda ner exempelkod**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/iterate)

