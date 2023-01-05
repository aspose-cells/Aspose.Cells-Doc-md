---
title: Création d'une plage nommée dans VSTO et Aspose.Cells
type: docs
weight: 90
url: /fr/net/creating-a-named-range-in-vsto-and-aspose-cells/
---
Pour créer une plage nommée :

1.  Configurez la feuille de calcul :
 1. Instanciez un objet Application. (VSTO uniquement.)
 1. Ajoutez un classeur.
 1. Obtenez la première feuille.
1.  Créez une plage nommée :
 1. Définissez une plage.
 1. Nommez la plage.
 1. Enregistrez le fichier.

Les exemples de code ci-dessous montrent comment effectuer ces étapes en utilisant VSTO avec C#. Les exemples de code qui suivent montrent comment faire la même chose en utilisant Aspose.Cells for .NET, encore une fois avec C#.
## **VSTO**
{{< highlight "csharp" >}}

 //Create Excel Object

Excel.Application xl = Application;

//Create a new Workbook

Excel.Workbook wb = xl.Workbooks.Add(Missing.Value);

//Get Worksheets Collection

Excel.Sheets xlsheets = wb.Sheets;

//Select the first sheet

Excel.Worksheet excelWorksheet = (Excel.Worksheet)xlsheets[1];

//Select a range of cells

Excel.Range range = (Excel.Range)excelWorksheet.get_Range("A1:B4", Type.Missing);

//Add Name to Range

range.Name = "Test_Range";

//Put data in range cells

foreach (Excel.Range cell in range.Cells)

{

	cell.set_Value(Missing.Value, "Test");

}

//Save New Workbook

wb.SaveCopyAs("Test_Range.xls");

//Quit Excel Object

xl.Quit();

{{< /highlight >}}
## **Aspose.Cells**
{{< highlight "csharp" >}}

 //Instanciation d'un objet Workbook

classeur classeur = nouveau classeur();

//Accéder à la première feuille de calcul du fichier Excel

Feuille de calcul feuille de calcul = workbook.Worksheets[0] ;

//Création d'une plage nommée

Plage plage = worksheet.Cells.CreateRange("A1", "B4");

//Définition du nom de la plage nommée

range.Name = "Test_Range" ;

 pour (int ligne = 0; ligne< range.RowCount; row++)

{

	for (int column = 0; column < range.ColumnCount; column++)

	{

		range[row, column].PutValue("Test");

	}

}

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.Save("Test_Range.xls");


{{< /highlight >}}
## **Télécharger l'exemple de code**
- [GithubGenericName](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Creating.a.Named.Range.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Creating%20a%20Named%20Range%20\(Aspose.Cells\).zip/télécharger)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Creating%20a%20Named%20Range%20\(Aspose.Cells\).Zip *: français)
