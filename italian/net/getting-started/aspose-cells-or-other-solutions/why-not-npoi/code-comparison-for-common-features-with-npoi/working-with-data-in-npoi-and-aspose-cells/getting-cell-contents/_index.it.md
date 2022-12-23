---
title: Ottenere Cell Contenuto
type: docs
weight: 10
url: /it/net/getting-cell-contents/
---
## **Aspose.Cells - Ottenere Cell Contenuto**
Il metodo Cells[0]o Cells[nome] è disponibile per accedere alle celle.

**C#**

{{< highlight "cs" >}}

 Cartella di lavoro cartella di lavoro = nuova cartella di lavoro("../../data/test.xlsx");

Foglio di lavoro foglio1 = cartella di lavoro.Fogli di lavoro[0];

Cells celle = foglio1.Cells;

Intervallo intervallo = sheet1.Cells.MaxDisplayRange;

int tcols = range.ColumnCount;

int trows = range.RowCount;

 per (int i = 0 ; i< trows; i++)

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
## **NPOI - HSSF XSSF - Ottenere Cell Contenuto**
NPOI fornisce la classe Cell per accedere a varie proprietà delle celle.

**C#**

{{< highlight "cs" >}}

 IWorkbook wb = new XSSFWorkbook("../../data/test.xlsx");

ISheet foglio1 = wb.GetSheetAt(0);

 for (int indice = 0; indice<= sheet1.LastRowNum; index++)

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
## **Scarica il codice in esecuzione**
 Scaricamento**Ottenere Cell Contenuto** formare uno dei siti di social coding sotto indicati:

- [Git Hub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Getting.Cell.Contents.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Per maggiori dettagli, visita[Funzionalità di gestione dei dati](/cells/it/net/data-handling-features-in-aspose-cells/).

{{% /alert %}}
