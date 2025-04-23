---
title: Masquer et afficher des feuilles de calcul dans un classeur en VSTO et Aspose.Cells
type: docs
weight: 140
url: /fr/net/hide-and-unhide-worksheets-in-a-workbook-in-vsto-and-aspose-cells/
---

Cet article compare la dissimulation et la réapparition des feuilles de calcul avec VSTO, en utilisant soit C# soit Visual Basic, à l'exécution de la même tâche avec Aspose.Cells, en utilisant à nouveau soit C# soit Visual Basic. Aspose.Cells vous permet de travailler sans avoir Microsoft Excel installé.

Les étapes pour masquer une feuille de calcul sont :

1. Ouvrir un fichier.
1. Obtenir une feuille de calcul.
1. Masquer la feuille de calcul.
1. Enregistrez le fichier.
   Pour réafficher une feuille de calcul, il suffit de basculer la visibilité de la feuille masquée.

Les échantillons de code ci-dessous montrent d'abord comment masquer une feuille de calcul. Les premiers échantillons montrent le processus avec VSTO, en utilisant soit C#, par rapport à l'utilisation d'Aspose.Cells, à nouveau en utilisant soit C#.

Le deuxième ensemble d'échantillons de code montre la ligne utilisée pour réafficher la feuille de calcul dans VSTO ou Aspose.Cells.
## **Masquage des feuilles de calcul**
Ci-dessous se trouvent des échantillons de code pour VSTO et Aspose.Cells qui illustrent comment masquer une feuille de calcul dans un classeur.
### **VSTO**
{{< highlight csharp >}}

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
{{< highlight csharp >}}

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
## **Réaffichage des feuilles de calcul**
Ci-dessous se trouvent des échantillons de code pour VSTO et Aspose.Cells qui illustrent comment réafficher une feuille de calcul dans un classeur.
### **VSTO**
{{< highlight csharp >}}

 //Unhide the worksheet.

	objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight csharp >}}

 //Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
## **Télécharger le code source d'exemple**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Hide.and.Unhide.Worksheets.in.a.Workbook.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
