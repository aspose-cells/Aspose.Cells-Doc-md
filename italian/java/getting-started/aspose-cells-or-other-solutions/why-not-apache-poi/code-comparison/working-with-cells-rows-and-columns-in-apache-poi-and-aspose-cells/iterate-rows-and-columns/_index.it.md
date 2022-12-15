---
title: Itera righe e colonne
type: docs
weight: 50
url: /it/java/iterate-rows-and-columns/
---
## **Aspose.Cells - Itera righe e colonne**

Righe e colonne possono essere ripetute utilizzando la raccolta di righe e colonne.

**Giava**

{{< highlight "java" >}}

 //Accedi all'intervallo di visualizzazione massimo

Intervallo intervallo = foglio di lavoro.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int trows = range.getRowCount();

System.out.println("Righe totali:" + trows);

System.out.println("Totale colonne:" + tcols);

RowCollection righe = cells.getRows();

 per (int i = 0 ; i< rows.getCount() ; i++)

{

	for (int j = 0 ; j < tcols ; j++)

	{

		System.out.print(cells.get(i,j).getName() + " - " + cells.get(i,j).getValue() + "\t");

	}

	System.out.println("");

}

{{< /highlight >}}

## **Apache POI SS - HSSF XSSF - Itera righe e colonne**

Le righe e Cells possono essere ripetute su Sheet. Il codice di esempio è menzionato di seguito:

**Giava**

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

## **Scarica il codice in esecuzione**

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## **Scarica il codice di esempio**

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/iterate)

