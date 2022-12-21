---
title: Cell コンテンツの取得
type: docs
weight: 10
url: /ja/java/getting-cell-contents/
---
## **Aspose.Cells - Cell コンテンツの取得**
Cells.get() メソッドを使用してセルにアクセスできます。

**Java**

{{< highlight "java" >}}

 //Excel ファイルの最初のワークシートにアクセスする

ワークシート ワークシート = workbook.getWorksheets().get(0);

Cells セル = worksheet.getCells();

//最大表示範囲にアクセス

範囲範囲 = worksheet.getCells().getMaxDisplayRange();

int tcols = range.getColumnCount();

int トロウ = range.getRowCount();

System.out.println("Total Rows:" + トロウ);

System.out.println("Total Cols:" + tcols);

// アクセス値 Cell B4

//=====================================================

System.out.println(cells.get("B4").getValue());

Cell セル = セル.get(3,1); //アクセス値 Cell B4

System.out.println(cell.getValue());

//=====================================================

RowCollection 行 = cells.getRows();

 for (int i = 0 ; i< rows.getCount() ; i++)

{

	for (int j = 0 ; j < tcols ; j++)

	{

		if (cells.get(i,j).getType() != CellValueType.IS_NULL)

		{

			System.out.println(cells.get(i,j).getName() + " - " + cells.get(i,j).getValue());

		}

	}

}

{{< /highlight >}}
## **Apache POI SS - HSSF XSSF - 取得 Cell 目次**
Apache POI は、セルのさまざまなプロパティにアクセスするための Cell クラスを提供します。

**Java**

{{< highlight "java" >}}

 Sheet sheet1 = wb.getSheetAt(0);

for (Row row : sheet1) {

    for (Cell cell : row) {

        CellReference cellRef = new CellReference(row.getRowNum(), cell.getColumnIndex());

        System.out.print(cellRef.formatAsString());

        System.out.print(" - ");

        switch (cell.getCellType()) {

            case Cell.CELL_TYPE_STRING:

                System.out.println(cell.getRichStringCellValue().getString());

                break;

            case Cell.CELL_TYPE_NUMERIC:

                if (DateUtil.isCellDateFormatted(cell)) {

                    System.out.println(cell.getDateCellValue());

                } else {

                    System.out.println(cell.getNumericCellValue());

                }

                break;

            case Cell.CELL_TYPE_BOOLEAN:

                System.out.println(cell.getBooleanCellValue());

                break;

            case Cell.CELL_TYPE_FORMULA:

                System.out.println(cell.getCellFormula());

                break;

            default:

                System.out.println();

        }

    }

}

{{< /highlight >}}
## **実行中のコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/releases/tag/Aspose.Cells_Java_for_Apache_POI_SS-v1.0.0)
## **サンプルコードをダウンロード**
- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-Java/tree/master/Plugins/Aspose_Cells_for_Apache_POI/Aspose-Cells-for-Apache-POI-(Maven)/src/main/java/com/aspose/cells/examples/featurescomparison/datahandling/gettingcellcontent)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[Aspose.Cells を使用したデータ処理機能](/cells/ja/java/data-handling-features-using-aspose-cells/)

{{% /alert %}}
