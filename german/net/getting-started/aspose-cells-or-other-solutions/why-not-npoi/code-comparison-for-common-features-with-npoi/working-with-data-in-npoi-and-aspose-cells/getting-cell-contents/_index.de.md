---
title: Cell Inhalt erhalten
type: docs
weight: 10
url: /de/net/getting-cell-contents/
---
## **Aspose.Cells - Cell Inhalt erhalten**
Cells[0]oder Cells[name]Methode steht für den Zugriff auf Zellen zur Verfügung.

**C#**

{{< highlight "cs" >}}

 Arbeitsmappe Arbeitsmappe = neue Arbeitsmappe(../../data/test.xlsx");

Arbeitsblatt sheet1 = workbook.Worksheets[0];

Cells Zellen = Blatt1.Cells;

Bereich range = sheet1.Cells.MaxDisplayRange;

int tcols = range.ColumnCount;

int trows = range.RowCount;

 für (int i = 0 ; i< trows; i++)

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
## **NPOI - HSSF XSSF - Abrufen von Cell-Inhalten**
NPOI stellt die Klasse Cell bereit, um auf verschiedene Eigenschaften von Zellen zuzugreifen.

**C#**

{{< highlight "cs" >}}

 IWorkbook wb = new XSSFWorkbook(../../data/test.xlsx");

ISheet sheet1 = wb.GetSheetAt(0);

 für (int index = 0; index<= sheet1.LastRowNum; index++)

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
## **Laufcode herunterladen**
 Download**Cell Inhalt erhalten** Bilden Sie eine der unten genannten Social-Coding-Sites:

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Getting.Cell.Contents.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Weitere Informationen finden Sie unter[Datenverarbeitungsfunktionen](/cells/de/net/data-handling-features-in-aspose-cells/).

{{% /alert %}}
