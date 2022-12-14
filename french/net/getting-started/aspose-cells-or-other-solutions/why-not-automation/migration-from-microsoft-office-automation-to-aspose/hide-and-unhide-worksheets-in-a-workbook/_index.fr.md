---
title: Masquer et afficher des feuilles de calcul dans un classeur
type: docs
weight: 80
url: /fr/net/hide-and-unhide-worksheets-in-a-workbook/
---
{{% alert color="primary" %}}

Lors de la présentation de classeurs à des clients ou d'une présentation, il peut être utile de masquer des feuilles de calcul dans un classeur. Une approche structurée de la modélisation de feuilles de calcul suggère que les données, les formules et les visualisations telles que les graphiques soient conservées sur des feuilles séparées. Cette approche maintient la mise en page propre et simple et facilite la navigation dans le classeur. Lors de la présentation des résultats, vous souhaiterez peut-être masquer les données ou les feuilles de formule pour éviter toute distraction.

Les utilisateurs qui travaillent dans Microsoft Excel peuvent facilement masquer puis afficher (afficher) les feuilles de calcul. Les mêmes fonctionnalités sont disponibles pour les développeurs qui programment avec des feuilles de calcul Excel. Il existe différentes façons de travailler avec des feuilles de calcul à partir d'applications logicielles. Une méthode consiste à utiliser VSTO, une autre est Aspose.Cells for .NET.

{{% /alert %}}

## **Masquer et afficher des feuilles de calcul**

 Cet article compare[cache](/cells/fr/net/hide-and-unhide-worksheets-in-a-workbook/) et[démasquer](/cells/fr/net/hide-and-unhide-worksheets-in-a-workbook/) feuilles de travail avec[VSTO](/cells/fr/net/hide-and-unhide-worksheets-in-a-workbook/) , en utilisant C# ou Visual Basic, pour effectuer la même tâche avec[Aspose.Cells](/cells/fr/net/hide-and-unhide-worksheets-in-a-workbook/), en utilisant à nouveau C# ou Visual Basic. Aspose.Cells vous permet de travailler sans Microsoft Excel installé.

Les étapes pour masquer une feuille de calcul sont :

1. Ouvrez un fichier.
1. Obtenez une feuille de travail.
1. Masquez la feuille de calcul.
1. Enregistrez le fichier.

 À[afficher](/cells/fr/net/hide-and-unhide-worksheets-in-a-workbook/) une feuille de calcul à nouveau, activez simplement la visibilité de la feuille masquée.

 Les exemples de code ci-dessous montrent d'abord comment masquer une feuille de calcul. Les premiers échantillons montrent le processus avec[VSTO](/cells/fr/net/hide-and-unhide-worksheets-in-a-workbook/) , en utilisant C# ou Visual Basic, par rapport à l'utilisation[Aspose.Cells](/cells/fr/net/hide-and-unhide-worksheets-in-a-workbook/), en utilisant à nouveau C# ou Visual Basics.

 Le deuxième ensemble d'exemples de code montre la ligne utilisée pour afficher la feuille de calcul dans[VSTO](/cells/fr/net/hide-and-unhide-worksheets-in-a-workbook/) ou[Aspose.Cells](/cells/fr/net/hide-and-unhide-worksheets-in-a-workbook/).

## **Masquer des feuilles de calcul**

Vous trouverez ci-dessous des exemples de code pour VSTO et Aspose.Cells qui illustrent comment masquer une feuille de calcul dans un classeur.

### **Masquer des feuilles de calcul avec VSTO**

**C#**

{{< highlight "csharp" >}}



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


### **Masquer les feuilles de calcul avec Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}



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

## **Afficher les feuilles de calcul**

Vous trouverez ci-dessous des exemples de code pour VSTO et Aspose.Cells qui illustrent comment afficher une feuille de calcul dans un classeur.

### **Afficher une feuille de calcul avec VSTO**

**C#**

{{< highlight "csharp" >}}



//Unhide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;



{{< /highlight >}}


### **Afficher une feuille de calcul avec Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

//Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
