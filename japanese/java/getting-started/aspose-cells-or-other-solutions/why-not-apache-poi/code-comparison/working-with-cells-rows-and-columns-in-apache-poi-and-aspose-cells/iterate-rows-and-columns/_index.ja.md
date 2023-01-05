---
title: 行と列を繰り返す
type: docs
weight: 50
url: /ja/java/iterate-rows-and-columns/
---
## **Aspose.Cells - 行と列の反復**

行と列は、行と列のコレクションを使用して反復できます。

**Java**

{{< highlight "java" >}}

 //最大表示範囲にアクセス

範囲範囲 = worksheet.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int トロウ = range.getRowCount();

System.out.println("Total Rows:" + トロウ);

System.out.println("Total Cols:" + tcols);

RowCollection 行 = cells.getRows();

 for (int i = 0 ; i< rows.getCount() ; i++)

{

	for (int j = 0 ; j < tcols ; j++)

	{

		System.out.print(cells.get(i,j).getName() + " - " + cells.get(i,j).getValue() + "\t");

	}

	System.out.println("");

}

{{< /highlight >}}

## **Apache POI SS - HSSF XSSF - 行と列の反復**

行と Cells はシートで反復できます。サンプルコードを以下に示します。

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

## **実行中のコードをダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)

## **サンプルコードをダウンロード**

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/cellsrowscolumns/iterate)

