---
title: Masquer et afficher les feuilles de calcul dans un classeur dans VSTO et Aspose.Cells
type: docs
weight: 140
url: /fr/net/hide-and-unhide-worksheets-in-a-workbook-in-vsto-and-aspose-cells/
---
Cet article compare le masquage et l'affichage des feuilles de calcul avec VSTO, en utilisant C# ou Visual Basic, pour effectuer la même tâche avec Aspose.Cells, en utilisant à nouveau C# ou Visual Basic. Aspose.Cells vous permet de travailler sans Microsoft Excel installé.

Les étapes pour masquer une feuille de calcul sont :

1. Ouvrez un fichier.
1. Obtenez une feuille de travail.
1. Masquez la feuille de calcul.
1. Enregistrez le fichier.
 Pour afficher à nouveau une feuille de calcul, activez simplement la visibilité de la feuille masquée.

Les exemples de code ci-dessous montrent d'abord comment masquer une feuille de calcul. Les premiers exemples montrent le processus avec VSTO, en utilisant soit C#, par rapport à l'utilisation de Aspose.Cells, à nouveau en utilisant soit C#.

Le deuxième ensemble d'exemples de code montre la ligne utilisée pour afficher la feuille de calcul dans VSTO ou Aspose.Cells.
## **Masquer des feuilles de calcul**
Vous trouverez ci-dessous des exemples de code pour VSTO et Aspose.Cells qui illustrent comment masquer une feuille de calcul dans un classeur.
### **VSTO**
{{< highlight "csharp" >}}

 //Instantiate the Application object.

Excel.Application excelApp = Application;

//Specify the template Excel file path.

string myPath = "Book1.xls";

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

objSheet.Visible = Excel.XlSheetVisibility.xlSheetHidden;

//Save As the Excel file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();


{{< /highlight >}}
### **Aspose.Cells**
{{< highlight "csharp" >}}

 //Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template Excel file path.

string myPath = "Book1.xls";

//Open the Excel file.

workbook.Open(myPath);

//Get the first sheet.

Aspose.Cells.Worksheet objSheet = workbook.Worksheets["Sheet1"];

//Hide the worksheet.

objSheet.IsVisible = false;

//Save As the Excel file.

workbook.Save("Book1.xls");

{{< /highlight >}}
## **Afficher la feuille de calcul**
Vous trouverez ci-dessous des exemples de code pour VSTO et Aspose.Cells qui illustrent comment afficher une feuille de calcul dans un classeur.
### **VSTO**
{{< highlight "csharp" >}}

 //Unhide the worksheet.

	objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight "csharp" >}}

 //Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
## **Télécharger l'exemple de code**
- [GithubGenericName](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Hide.and.Unhide.Worksheets.in.a.Workbook.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip/télécharger)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).Zip *: français)
