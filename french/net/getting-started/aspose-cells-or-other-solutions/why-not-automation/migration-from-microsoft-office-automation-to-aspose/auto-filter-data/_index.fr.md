---
title: Filtrer automatiquement les données
type: docs
weight: 120
url: /fr/net/auto-filter-data/
---
{{% alert color="primary" %}}

Pour comprendre quelles données se trouvent dans une plage, il est souvent plus facile de trier et de filtrer les données que de regarder des colonnes de données non ordonnées. Le tri organise les données par ordre croissant ou décroissant, ce qui facilite la recherche de valeurs spécifiques. Le filtrage des données vous permet de n'afficher que certaines valeurs. Cela permet de se concentrer sur des éléments particuliers dans les enregistrements de vente, par exemple.

Les utilisateurs d'Excel Microsoft peuvent appliquer un filtrage automatique aux colonnes. Le filtrage automatique ajoute un menu en haut de la colonne, à partir duquel vous pouvez trier les données de colonne de filtrage. Cette fonctionnalité est également disponible pour les développeurs qui travaillent avec des feuilles de calcul Excel, via VSTO ou Aspose.Cells for .NET.

{{% /alert %}}

## **Filtrage automatique des données**

Pour appliquer le filtrage automatique à une colonne :

1. Créez un classeur.
1. Obtenez une feuille de travail.
1. Ajoutez des exemples de données.
1. Appliquer le filtre automatique.
1. Ajustement automatique des colonnes pour rendre l'affichage attrayant.
1. Enregistrez la feuille de calcul.

 Les exemples de code de cet article montrent comment effectuer ces étapes à l'aide de[VSTO](/cells/fr/net/auto-filter-data/) avec C# ou Visual Basic, ou en utilisant[Apose.Cells](/cells/fr/net/auto-filter-data/), toujours avec C# ou Visual Basic.

### **Filtrage automatique des données avec VSTO**

**C#**

{{< highlight "csharp" >}}

 using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;.........//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();



//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);



//Get the First sheet.

Excel.Worksheet sheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];



//Add data into A1 and B1 Cells as headers.

sheet.Cells[1, 1]= "Product ID";

sheet.Cells[1, 2]= "Product Name";

//Add data into details cells.

sheet.Cells[2, 1]= 1;

sheet.Cells[3, 1]= 2;

sheet.Cells[4, 1]= 3;

sheet.Cells[5, 1]= 4;

sheet.Cells[2, 2]= "Apples";

sheet.Cells[3, 2]= "Bananas";

sheet.Cells[4, 2]= "Grapes";

sheet.Cells[5, 2]= "Oranges";

//Enable Auto-filter.           

sheet.EnableAutoFilter = true;



//Create the range.

Excel.Range range = sheet.get_Range("A1", "B5");



//Auto-filter the range.

range.AutoFilter("1", "<>", Microsoft.Office.Interop.Excel.XlAutoFilterOperator.xlOr, "", true);

//Auto-fit the second column.

sheet.get_Range("B1", "B5").EntireColumn.AutoFit();



//Save the copy of workbook as .xlsx file.

objBook.SaveCopyAs("e:\\test2\\vsto_autofilter.xlsx");



{{< /highlight >}}

**Filtre automatique appliqué avec VSTO** 

![tâche : image_autre_texte](auto-filter-data_1.png)

### **Filtrage automatique des données avec Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 //Instantiate a new Workbook.

Workbook objBook = new Workbook();



//Get the First sheet.

Worksheet sheet = objBook.Worksheets["Sheet1"];

//Add data into A1 and B1 Cells as headers.

sheet.Cells[0, 0].PutValue("Product ID");

sheet.Cells[0, 1].PutValue("Product Name");

//Add data into details cells.

sheet.Cells[1, 0].PutValue(1);

sheet.Cells[2, 0].PutValue(2);

sheet.Cells[3, 0].PutValue(3);

sheet.Cells[4, 0].PutValue(4);

sheet.Cells[1, 1].PutValue("Apples");

sheet.Cells[2, 1].PutValue("Bananas");

sheet.Cells[3, 1].PutValue("Grapes");

sheet.Cells[4, 1].PutValue("Oranges");

//Auto-filter the range.

sheet.AutoFilter.Range = "A1:B5";

//Auto-fit the second column.

sheet.AutoFitColumn(1,0,4);

//Save the copy of workbook as .xlsx file.

objBook.Save("e:\\test2\\aspose-cells_autofilter.xlsx");



{{< /highlight >}}

**Filtre automatique appliqué avec Aspose.Cells for .NET** 

![tâche : image_autre_texte](auto-filter-data_2.png)
