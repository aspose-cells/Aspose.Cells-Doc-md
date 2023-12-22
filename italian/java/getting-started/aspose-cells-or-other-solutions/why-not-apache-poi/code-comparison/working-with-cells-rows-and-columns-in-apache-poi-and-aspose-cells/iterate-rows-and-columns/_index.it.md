---
title: Itera righe e colonne
type: docs
weight: 50
url: /it/java/iterate-rows-and-columns/
description: Scopri come ripetere righe e colonne tramite le API Aspose.Cells for Java.
keywords: How to Iterate Rows and Columns in Java, Iterate Rows using Java, Java Iterate Columns. 
---
##  **Come ripetere righe e colonne utilizzando Aspose.Cells for Java**

Righe e colonne possono essere ripetute utilizzando la raccolta di righe e colonne.

**Java**

{{< highlight "java" >}}

 //Accedi all'intervallo di visualizzazione massimo

Intervallo intervallo = worksheet.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int trows = range.getRowCount();

System.out.println("Righe totali:" + trows);

System.out.println("Col. totali:" + tcols);

RowCollection righe = cellule.getRows();

 for (int i = 0 ; i< rows.getCount() ; i++)

{

	for (int j = 0 ; j < tcols ; j++)

	{

		System.out.print(cells.get(i,j).getName() + " - " + cells.get(i,j).getValue() + "\t");

	}

	System.out.println("");

}

{{< /highlight >}}

##  **Apache POI SS - HSSF XSSF - Itera righe e colonne**

Le righe e Cells possono essere ripetute sul foglio. Il codice di esempio è menzionato di seguito:

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

##  **Scarica il codice in esecuzione**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

##  **Scarica il codice di esempio**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/iterate)

