---
title: 行および列の反復処理
type: docs
weight: 50
url: /ja/java/iterate-rows-and-columns/
description: Aspose.Cells for JavaAPIを使用して行と列をイテレートする方法を学ぶ。
keywords: Javaで行と列をイテレートする方法、Javaを使用して行をイテレートする方法、Javaで列をイテレートする方法。 
---

## **Aspose.Cells for Javaを使用して行と列をイテレートする方法。**

行と列は、行と列のコレクションを使用してイテレートすることができます。

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

## **Apache POI SS - HSSF XSSF - 行と列をイテレートする。**

Sheet上で行とセルをイテレートすることができます。以下にサンプルコードが記載されています。

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

## **ランニングコードのダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## **サンプルコードをダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/iterate)

{{< app/cells/assistant language="java" >}}
