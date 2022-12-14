---
title: Ajouter des hyperliens vers Cells
type: docs
weight: 60
url: /fr/net/add-hyperlinks-to-cells/
---
{{% alert color="primary" %}}

Aspose.Cells for .NET vous permet d'effectuer presque toutes les tâches via votre application qu'un utilisateur peut effectuer dans Microsoft Excel. Cet article compare comment ajouter un lien hypertexte à une cellule dans une feuille de calcul à l'aide de VSTO et Aspose.Cells for .NET.

{{% /alert %}}

## **Ajout d'hyperliens au Cells**

Pour ajouter des liens hypertexte aux cellules d'une feuille de calcul, procédez comme suit :

1. Configurez la feuille de calcul :
 1. Instanciez un objet Application.
 (VSTO uniquement.)
 1. Ajoutez un classeur.
 1. Obtenez la première feuille.
 1. Ajoutez du texte aux cellules auxquelles vous ajouterez un lien hypertexte.
1. Ajouter un lien hypertexte.
1. Enregistrez le document.

 Ces étapes sont illustrées dans les exemples de code ci-dessous. Les premiers exemples montrent comment utiliser[VSTO](/cells/fr/net/add-hyperlinks-to-cells/) avec C# ou Visual Basic pour ajouter un lien hypertexte à une cellule. Les exemples qui suivent montrent comment faire la même chose en utilisant[Aspose.Cells for .NET](/cells/fr/net/add-hyperlinks-to-cells/), toujours en utilisant C# ou Visual Basic.

Les exemples de code génèrent un fichier Excel contenant un lien hypertexte dans la cellule A1 de la première feuille de calcul.

![tâche : image_autre_texte](add-hyperlinks-to-cells_1.png)

**Un lien hypertexte est ajouté à la cellule A1.**

### **Ajout d'hyperliens à Cells avec VSTO**

**C#**

{{< highlight "csharp" >}}

 .......



using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];



//Define a range object(A1).

Excel.Range _range;

_range = objSheet.get_Range("A1", "A1");

//Add a hyperlink to it.

objSheet.Hyperlinks.Add(_range, "http://www.aspose.com/", Type.Missing, "Click to go to Aspose site", "Aspose Site!");

//Save the excel file.

objBook.SaveCopyAs("c:\\Hyperlink_test.xls"); 

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **Ajout d'hyperliens à Cells avec Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook object.

Workbook workbook = new Workbook();

//Get the First sheet.

Worksheet worksheet = workbook.Worksheets[0];

//Define A1 Cell.

Aspose.Cells.Cell cell = worksheet.Cells["A1"];

//Add a hyperlink to it.

int index = worksheet.Hyperlinks.Add("A1", 1, 1, "http://www.aspose.com/");

worksheet.Hyperlinks[index].TextToDisplay = "Aspose Site!";

worksheet.Hyperlinks[index].ScreenTip = "Click to go to Aspose site";

//Save the excel file.

workbook.Save("c:\\Hyperlink_test.xls");       



{{< /highlight >}}
