---
title: Fånga Cellinnehåll
type: docs
weight: 10
url: /sv/net/getting-cell-contents/
---

## **Aspose.Cells - Fånga Cellinnehåll**
Cells[0] eller Cells[namn] metoden finns tillgänglig för att komma åt celler.

**C#**

{{< highlight cs >}}

 Workbook workbook = new Workbook("../../data/test.xlsx");

Worksheet sheet1 = workbook.Worksheets[0];

Cells cells = sheet1.Cells;

Range range = sheet1.Cells.MaxDisplayRange;

int tcols = range.ColumnCount;

int trows = range.RowCount;

for (int i = 0 ; i < trows; i++)

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
## **NPOI - HSSF XSSF - Fånga Cellinnehåll**
NPOI tillhandahåller Cell klassen för att få åtkomst till olika egenskaper hos celler.

**C#**

{{< highlight cs >}}

 IWorkbook wb = new XSSFWorkbook("../../data/test.xlsx");

ISheet sheet1 = wb.GetSheetAt(0);

for (int index = 0; index <= sheet1.LastRowNum; index++)

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
## **Ladda ned körbar kod**
Hämta **Fånga Cellinnehåll** från någon av de nedan nämnda sociala kodningssidorna:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Getting.Cell.Contents.Aspose.Cells.zip)

{{% alert color="primary" %}} 

För mer detaljer, besök [Datahanteringsfunktioner](/cells/sv/net/data-handling-features-in-aspose-cells/).

{{% /alert %}}
{{< app/cells/assistant language="csharp" >}}
