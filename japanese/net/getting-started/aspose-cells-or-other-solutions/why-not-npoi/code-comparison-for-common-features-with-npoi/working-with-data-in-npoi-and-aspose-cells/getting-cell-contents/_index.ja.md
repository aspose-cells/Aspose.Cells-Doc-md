---
title: Cell コンテンツの取得
type: docs
weight: 10
url: /ja/net/getting-cell-contents/
---
## **Aspose.Cells - Cell コンテンツの取得**
Cells[0]または Cells[name]メソッドを使用して、セルにアクセスできます。

**C#**

{{< highlight "cs" >}}

 Workbook workbook = new Workbook("../../data/test.xlsx");

ワークシート sheet1 = workbook.Worksheets[0];

Cells セル = sheet1.Cells;

範囲範囲 = sheet1.Cells.MaxDisplayRange;

int tcols = range.ColumnCount;

int トロウ = range.RowCount;

 for (int i = 0 ; i< trows; i++)

{

	for (int j = 0 ; j < tcols ; j++)

	{

		if (cells[i, j].Type != CellValueType.IsNull)

		{

			Console.WriteLine(cells[i, j].Name + " - " + cells[i, j].Value);

		}

	}

}

{{< /highlight >}}
## **NPOI - HSSF XSSF - 取得 Cell 目次**
NPOI は、セルのさまざまなプロパティにアクセスするための Cell クラスを提供します。

**C#**

{{< highlight "cs" >}}

 IWorkbook wb = new XSSFWorkbook("../../data/test.xlsx");

ISheet sheet1 = wb.GetSheetAt(0);

 for (int インデックス = 0; インデックス<= sheet1.LastRowNum; index++)

{

    IRow row = sheet1.GetRow(index);

    foreach (ICell cell in row.Cells)

    {

        CellReference cellRef = new CellReference(row.RowNum, cell.ColumnIndex);

        Console.Write(cellRef.FormatAsString());

        Console.Write(" - ");

        switch (cell.CellType)

        {

            case CellType.String:

                Console.Write(cell.StringCellValue);

                break;

            case CellType.Numeric:

                if (DateUtil.IsCellDateFormatted(cell))

                    Console.Write(cell.DateCellValue);

                else

                    Console.Write(cell.NumericCellValue);

                break;

            case CellType.Boolean:

                Console.Write(cell.BooleanCellValue);

                break;

            case CellType.Formula:

                Console.Write(cell.CellFormula);

                break;

        }

        Console.WriteLine();

    }

}

{{< /highlight >}}
## **実行中のコードをダウンロード**
ダウンロード**Cell コンテンツの取得**以下のソーシャル コーディング サイトのいずれかを形成します。

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Getting.Cell.Contents.Aspose.Cells.zip)

{{% alert color="primary" %}} 

詳細については、次を参照してください。[データ処理機能](/cells/ja/net/data-handling-features-in-aspose-cells/).

{{% /alert %}}
