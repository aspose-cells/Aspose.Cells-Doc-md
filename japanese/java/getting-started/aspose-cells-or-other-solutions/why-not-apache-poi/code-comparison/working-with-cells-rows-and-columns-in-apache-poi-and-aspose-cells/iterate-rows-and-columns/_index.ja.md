---
title: 行と列を反復する
type: docs
weight: 50
url: /ja/java/iterate-rows-and-columns/
description: Aspose.Cells for Java API を使用して行と列を反復する方法を学習します。
keywords: How to Iterate Rows and Columns in Java, Iterate Rows using Java, Java Iterate Columns. 
---
##  **Aspose.Cells for Java を使用して行と列を反復する方法**

行と列のコレクションを使用して、行と列を反復できます。

**Java**

{{< highlight "java" >}}

 //最大表示範囲にアクセスする

範囲範囲 = worksheet.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int trows = range.getRowCount();

System.out.println("合計行数:" + trows);

System.out.println("合計列数:" + tcols);

RowCollection 行 = cell.getRows();

 for (int i = 0 ; i< rows.getCount() ; i++)

{

	for (int j = 0 ; j < tcols ; j++)

	{

		System.out.print(cells.get(i,j).getName() + " - " + cells.get(i,j).getValue() + "\t");

	}

	System.out.println("");

}

{{< /highlight >}}

##  **Apache POI SS - HSSF XSSF - 行と列の反復**

行と Cells はシート上で反復できます。サンプルコードを以下に示します。

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

##  **実行コードをダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

##  **サンプルコードをダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/iterate)

