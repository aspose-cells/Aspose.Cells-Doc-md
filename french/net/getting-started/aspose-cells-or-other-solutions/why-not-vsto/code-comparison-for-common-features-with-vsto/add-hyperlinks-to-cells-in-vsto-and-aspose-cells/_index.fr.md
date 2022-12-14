---
title: Ajouter des hyperliens vers Cells dans VSTO et Aspose.Cells
type: docs
weight: 20
url: /fr/net/add-hyperlinks-to-cells-in-vsto-and-aspose-cells/
---
Pour ajouter des liens hypertexte aux cellules d'une feuille de calcul, procédez comme suit :

1.  Configurez la feuille de calcul :
 1. Instanciez un objet Application. (VSTO uniquement.)
 1. Ajoutez un classeur.
 1. Obtenez la première feuille.
 1. Ajoutez du texte aux cellules auxquelles vous ajouterez un lien hypertexte.
1. Ajouter un lien hypertexte.
1. Enregistrez le document.

Ces étapes sont illustrées dans les exemples de code ci-dessous. Les premiers exemples montrent comment utiliser VSTO avec soit C# pour ajouter un lien hypertexte à une cellule. Les exemples qui suivent montrent comment faire la même chose en utilisant Aspose.Cells for .NET, à nouveau en utilisant C#.

Les exemples de code génèrent un fichier Excel contenant un lien hypertexte dans la cellule A1 de la première feuille de calcul.

![tâche : image_autre_texte](picture1.png)

Un lien hypertexte est ajouté à la cellule A1.

## **VSTO**

{{< highlight "csharp" >}}

 //Instantiate the Application object.

Excel.Application ExcelApp = Application;

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

objBook.SaveCopyAs("Hyperlink_test.xls");

//Quit the Application.

ExcelApp.Quit();

{{< /highlight >}}

## **Aspose.Cells**

{{< highlight "csharp" >}}

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

workbook.Save("Hyperlink_test.xls");

{{< /highlight >}}

## **Télécharger l'exemple de code**

- [GithubGenericName](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Add.Hyperlinks.to.Cells.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip/télécharger)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).Zip *: français)
