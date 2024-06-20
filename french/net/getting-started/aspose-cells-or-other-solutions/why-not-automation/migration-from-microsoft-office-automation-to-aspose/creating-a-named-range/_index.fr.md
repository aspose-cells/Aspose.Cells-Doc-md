---
title: Création d une plage nommée
type: docs
weight: 70
url: /fr/net/creating-a-named-range/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET permet aux développeurs d'effectuer la plupart des tâches que les utilisateurs peuvent effectuer dans Microsoft Excel via leurs applications. Cet article explique comment appliquer une plage nommée de manière programmable.

Une plage nommée est une fonctionnalité Excel qui vous permet d'attribuer un nom à une cellule, ou à une plage de cellules, dans une feuille de calcul Excel. Vous pouvez ensuite utiliser le nom dans des formules pour faire référence à la cellule (ou à la plage). Des plages nommées de manière sensée rendent les formules plus faciles à comprendre.

Une plage nommée doit être unique dans son champ d'application, ne pas utiliser le même nom pour plusieurs plages dans une feuille de calcul. Des noms de plage descriptifs aident à éviter cela : par exemple, 'Sous-totalCommande' est plus descriptif que 'Sous-total' et moins susceptible d'être dupliqué sur une feuille.

{{% /alert %}}

## **Création d'une plage nommée**

Pour créer une plage nommée :

1. Mettez en place la feuille de calcul:
   1. Instancier un objet Application.
      (VSTO uniquement.)
   1. Ajouter un classeur.
   1. Obtenir la première feuille.
1. Créer une plage nommée :
   1. Définir une plage.
   1. Nommer la plage.
1. Enregistrez le fichier.

Les exemples de code ci-dessous montrent comment effectuer ces étapes à l'aide de [VSTO](/cells/fr/net/creating-a-named-range/) avec soit C# soit Visual Basic. Les exemples de code suivants montrent comment faire la même chose en utilisant [Aspose.Cells for .NET](/cells/fr/net/creating-a-named-range/), encore une fois avec soit C# soit Visual Basic.
### **Création d'une plage nommée avec VSTO**

**C#**

{{< highlight csharp >}}

 .......

using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Create Excel Object

Excel.ApplicationClass xl = new Excel.ApplicationClass();

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

wb.SaveCopyAs("C:\\Test_Range.xls")

//Quit Excel Object

xl.Quit();



{{< /highlight >}}

### **Création d'une plage nommée avec Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......


//Instantiating a Workbook object

Workbook workbook = new Workbook();

//Accessing the first worksheet in the Excel file

Worksheet worksheet = workbook.Worksheets[0];

//Creating a named range

Range range = worksheet.Cells.CreateRange("A1", "B4");

//Setting the name of the named range

range.Name = "Test_Range";

for (int row = 0; row < range.RowCount; row++)

{

    for (int column = 0; column < range.ColumnCount; column++)

    {

        range[row, column].PutValue("Test");

    }

}

//Saving the modified Excel file in default (that is Excel 2003) format

workbook.Save("C:\\Test_Range.xls");



{{< /highlight >}}
