---
title: Masquer et afficher des feuilles de calcul dans un classeur
type: docs
weight: 80
url: /fr/net/hide-and-unhide-worksheets-in-a-workbook/
---

{{% alert color="primary" %}}

Lors de la présentation de classeurs aux clients, ou lors d'une présentation, il peut être utile de masquer des feuilles de calcul dans un classeur. Une approche structurée de la modélisation de feuilles de calcul suggère que les données, les formules et les visualisations telles que les graphiques sont conservées sur des feuilles séparées. Cette approche permet de maintenir une mise en page propre et simple et rend le classeur plus facile à naviguer. Lors de la présentation des résultats, vous pouvez vouloir masquer les feuilles de données ou de formules de la vue pour éviter les distractions.

Les utilisateurs qui travaillent dans Microsoft Excel peuvent facilement masquer puis afficher (montrer) des feuilles de calcul. Les mêmes fonctionnalités sont disponibles pour les développeurs qui programment avec des feuilles de calcul Excel. Il existe différentes façons de travailler avec des feuilles de calcul à partir d'applications logicielles. Une méthode consiste à utiliser VSTO, une autre est Aspose.Cells for .NET.

{{% /alert %}}

## **Masquer et afficher des feuilles de calcul**

Cet article compare [la masquage](/cells/fr/net/hide-and-unhide-worksheets-in-a-workbook/) et [la révélation](/cells/fr/net/hide-and-unhide-worksheets-in-a-workbook/) des feuilles de calcul avec [VSTO](/cells/fr/net/hide-and-unhide-worksheets-in-a-workbook/), en utilisant soit C# soit Visual Basic, pour effectuer la même tâche avec [Aspose.Cells](/cells/fr/net/hide-and-unhide-worksheets-in-a-workbook/), encore une fois en utilisant soit C# soit Visual Basic. Aspose.Cells vous permet de travailler sans Microsoft Excel installé.

Les étapes pour masquer une feuille de calcul sont :

1. Ouvrir un fichier.
1. Obtenir une feuille de calcul.
1. Masquer la feuille de calcul.
1. Enregistrez le fichier.

Pour [afficher de nouveau](/cells/fr/net/hide-and-unhide-worksheets-in-a-workbook/) une feuille de calcul, basculez simplement la visibilité pour la feuille masquée.

Les exemples de code ci-dessous montrent d'abord comment masquer une feuille de calcul. Les premiers exemples montrent le processus avec [VSTO](/cells/fr/net/hide-and-unhide-worksheets-in-a-workbook/), en utilisant soit C# soit Visual Basic, comparé à l'utilisation de [Aspose.Cells](/cells/fr/net/hide-and-unhide-worksheets-in-a-workbook/), encore une fois en utilisant soit C# soit Visual Basic.

Le deuxième ensemble d'exemples de code montre la ligne utilisée pour rendre de nouveau visible la feuille de calcul dans [VSTO](/cells/fr/net/hide-and-unhide-worksheets-in-a-workbook/) ou [Aspose.Cells](/cells/fr/net/hide-and-unhide-worksheets-in-a-workbook/).

## **Masquage des feuilles de calcul**

Ci-dessous se trouvent des échantillons de code pour VSTO et Aspose.Cells qui illustrent comment masquer une feuille de calcul dans un classeur.

### **Masquage des feuilles de calcul avec VSTO**

**C#**

{{< highlight csharp >}}



.......



using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......



//Instantiate the Application object.

Excel.Application excelApp = new Excel.ApplicationClass();



//Specify the template Excel file path.

string myPath=@"d:\test\MyBook.xls";



//Open the Excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);



//Get the first sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)excelApp.ActiveWorkbook.Sheets["Sheet1"];

//Hide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetHidden

//Save As the Excel file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}


### **Masquage des feuilles de calcul avec Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}



.......



using Aspose.Cells;



.......



//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template Excel file path.

string myPath = @"d:\test\MyBook.xls";

//Open the Excel file.

workbook.Open(myPath);

//Get the first sheet.

Aspose.Cells.Worksheet objSheet = workbook.Worksheets["Sheet1"];

//Hide the worksheet.

objSheet.IsVisible = false;

//Save As the Excel file.

workbook.Save(@"d:\test\MyBook.xls");



{{< /highlight >}}

## **Révélation des feuilles de calcul**

Ci-dessous se trouvent des échantillons de code pour VSTO et Aspose.Cells qui illustrent comment réafficher une feuille de calcul dans un classeur.

### **Révéler une feuille de calcul avec VSTO**

**C#**

{{< highlight csharp >}}



//Unhide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;



{{< /highlight >}}


### **Afficher une feuille de calcul avec Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

//Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
