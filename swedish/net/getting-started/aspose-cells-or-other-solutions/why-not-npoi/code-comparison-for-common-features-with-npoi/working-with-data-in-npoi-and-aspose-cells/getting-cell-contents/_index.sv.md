---
title: Hämta Cell Innehåll
type: docs
weight: 10
url: /sv/net/getting-cell-contents/
---
## **Aspose.Cells - Få Cell Innehåll**
Metoden Cells[0] eller Cells[name] är tillgänglig för att komma åt celler.

**C#**

{{< highlight "cs" >}}

 Arbetsbok arbetsbok = ny arbetsbok("../../data/test.xlsx");

Arbetsblad sheet1 = workbook.Worksheets[0];

Cells celler = ark1.Cells;

Områdesområde = ark1.Cells.MaxDisplayRange;

int tcols = range.ColumnCount;

int trows = range.RowCount;

 för (int i = 0 ; i< trows; i++)

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
## **NPOI - HSSF XSSF - Få Cell Innehåll**
NPOI tillhandahåller klassen Cell för åtkomst till olika egenskaper hos celler.

**C#**

{{< highlight "cs" >}}

 IWorkbook wb = new XSSFWorkbook("../../data/test.xlsx");

ISark ark1 = wb.GetSheetAt(0);

 för (int index = 0; index<= sheet1.LastRowNum; index++)

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
## **Ladda ner Running Code**
 Ladda ner**Hämta Cell Innehåll** bilda någon av nedan nämnda sociala kodningswebbplatser:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Getting.Cell.Contents.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 För mer information, besök[Datahanteringsfunktioner](/cells/sv/net/data-handling-features-in-aspose-cells/).

{{% /alert %}}
