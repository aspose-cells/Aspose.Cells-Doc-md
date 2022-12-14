---
title: Obtenir le contenu Cell
type: docs
weight: 10
url: /fr/net/getting-cell-contents/
---
## **Aspose.Cells - Obtenir Cell Contenu**
La méthode Cells[0] ou Cells[nom] est disponible pour accéder aux cellules.

**C#**

{{< highlight "cs" >}}

 Classeur classeur = nouveau classeur("../../data/test.xlsx");

Feuille de calcul feuille1 = classeur. Feuilles de travail[0] ;

Cells cellules = feuille1.Cells ;

Plage de plage = feuille1.Cells.MaxDisplayRange ;

int tcols = range.ColumnCount ;

int trows = range.RowCount ;

 pour (int je = 0 ; je< trows; i++)

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
## **NPOI - HSSF XSSF - Obtenir Cell Table des matières**
NPOI fournit la classe Cell pour accéder à diverses propriétés des cellules.

**C#**

{{< highlight "cs" >}}

 IWorkbook wb = new XSSFWorkbook("../../data/test.xlsx");

ISheet feuille1 = wb.GetSheetAt(0);

 pour (int index = 0; index<= sheet1.LastRowNum; index++)

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
## **Télécharger le code d'exécution**
 Télécharger**Obtenir le contenu Cell** forment l'un des sites de codage social mentionnés ci-dessous :

- [GitHub](https://github.com/aspose-cells/Aspose.Cells-for-.NET/releases/download/Aspose.Cells_vs_NPOI_1.0/Getting.Cell.Contents.Aspose.Cells.zip)

{{% alert color="primary" %}} 

 Pour plus de détails, visitez[Fonctionnalités de traitement des données](/cells/fr/net/data-handling-features-in-aspose-cells/).

{{% /alert %}}
