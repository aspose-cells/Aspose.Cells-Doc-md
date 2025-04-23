---
title: Ajouter des hyperliens aux cellules dans VSTO et Aspose.Cells
type: docs
weight: 20
url: /fr/net/add-hyperlinks-to-cells-in-vsto-and-aspose-cells/
---

Pour ajouter des hyperliens aux cellules d'une feuille de calcul, suivez les étapes suivantes :

1. Mettez en place la feuille de calcul: 
   1. Instancier un objet Application. (VSTO uniquement)
   1. Ajouter un classeur.
   1. Obtenir la première feuille.
   1. Ajouter du texte aux cellules auxquelles vous ajouterez un hyperlien.
1. Ajouter un hyperlien.
1. Enregistrer le document.

Ces étapes sont présentées dans les exemples de code ci-dessous. Le premier exemple montre comment utiliser VSTO avec C# pour ajouter un hyperlien à une cellule. Les exemples qui suivent montrent comment faire la même chose en utilisant Aspose.Cells for .NET, encore une fois en utilisant C#.

Les exemples de code génèrent un fichier Excel qui comporte un hyperlien dans la cellule A1 de la première feuille de calcul.

![todo:image_alt_text](picture1.png)

Un hyperlien est ajouté à la cellule A1.

## **VSTO**

{{< highlight csharp >}}

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

{{< highlight csharp >}}

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

## **Télécharger le code source d'exemple**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Add.Hyperlinks.to.Cells.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Add%20Hyperlinks%20to%20Cells%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
