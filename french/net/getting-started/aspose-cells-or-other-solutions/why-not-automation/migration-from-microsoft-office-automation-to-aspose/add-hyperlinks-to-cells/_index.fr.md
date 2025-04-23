---
title: Ajouter des liens hypertexte aux cellules
type: docs
weight: 60
url: /fr/net/add-hyperlinks-to-cells/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET vous permet d'effectuer presque toutes les tâches au sein de votre application qu'un utilisateur peut effectuer dans Microsoft Excel. Cet article compare comment ajouter un lien hypertexte à une cellule dans une feuille de calcul en utilisant VSTO et Aspose.Cells for .NET.

{{% /alert %}}

## **Ajouter des hyperliens aux cellules**

Pour ajouter des hyperliens aux cellules d'une feuille de calcul, suivez les étapes suivantes :

1. Mettez en place la feuille de calcul:
   1. Instancier un objet Application.
      (VSTO uniquement.)
   1. Ajouter un classeur.
   1. Obtenir la première feuille.
   1. Ajouter du texte aux cellules auxquelles vous ajouterez un hyperlien.
1. Ajouter un hyperlien.
1. Enregistrer le document.

Ces étapes sont présentées dans les exemples de code ci-dessous. Le premier exemple montre comment utiliser [VSTO](/cells/fr/net/add-hyperlinks-to-cells/) avec C# ou Visual Basic pour ajouter un hyperlien à une cellule. Les exemples suivants montrent comment faire la même chose en utilisant [Aspose.Cells for .NET](/cells/fr/net/add-hyperlinks-to-cells/), toujours en utilisant C# ou Visual Basic.

Les exemples de code génèrent un fichier Excel qui comporte un hyperlien dans la cellule A1 de la première feuille de calcul.

![todo:image_alt_text](add-hyperlinks-to-cells_1.png)

**Un hyperlien est ajouté à la cellule A1.**

### **Ajout d'hyperliens aux cellules avec VSTO**

**C#**

{{< highlight csharp >}}

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

### **Ajout d'hyperliens aux cellules avec Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

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
{{< app/cells/assistant language="csharp" >}}
