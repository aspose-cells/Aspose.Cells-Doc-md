---
title: Création d'une plage nommée
type: docs
weight: 70
url: /fr/net/creating-a-named-range/
---
{{% alert color="primary" %}}

Aspose.Cells for .NET permet aux développeurs d'effectuer la plupart des tâches que les utilisateurs peuvent effectuer dans Microsoft Excel via leurs applications. Cet article explique comment appliquer une plage nommée par programmation.

Une plage nommée est une fonctionnalité Excel qui vous permet d'attribuer un nom à une cellule ou à une plage de cellules dans une feuille de calcul Excel. Vous pouvez ensuite utiliser le nom dans les formules pour faire référence à la cellule (ou à la plage). Des gammes bien nommées facilitent la compréhension des formules.

Une plage nommée doit être unique dans sa portée, n'utilisez donc pas le même nom pour plusieurs plages dans une feuille de calcul. Les noms de plage descriptifs permettent d'éviter cela : par exemple, OrderSubTotal est plus descriptif que SubTotal et également moins susceptible d'être dupliqué sur une feuille.

{{% /alert %}}

## **Création d'une plage nommée**

Pour créer une plage nommée :

1. Configurez la feuille de calcul :
 1. Instanciez un objet Application.
 (VSTO uniquement.)
 1. Ajoutez un classeur.
 1. Obtenez la première feuille.
1. Créez une plage nommée :
 1. Définissez une plage.
 1. Nommez la plage.
1. Enregistrez le fichier.

 Les exemples de code ci-dessous montrent comment effectuer ces étapes à l'aide de[VSTO](/cells/fr/net/creating-a-named-range/) avec C# ou Visual Basic. Les exemples de code qui suivent montrent comment faire la même chose en utilisant[Aspose.Cells for .NET](/cells/fr/net/creating-a-named-range/), toujours avec C# ou Visual Basic.
### **Création d'une plage nommée avec VSTO**

**C#**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

 .......

en utilisant Aspose.Cells ;

.......


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

workbook.Save("C:\\Test_Range.xls");



{{< /highlight >}}
