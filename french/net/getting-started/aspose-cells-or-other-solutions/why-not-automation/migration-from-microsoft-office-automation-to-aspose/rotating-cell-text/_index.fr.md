---
title: Rotation du texte des cellules
type: docs
weight: 100
url: /fr/net/rotating-cell-text/
---

{{% alert color="primary" %}}

Parfois, un en-tête de colonne est beaucoup plus large que les données dans les cellules en dessous. Cela peut causer un espace inutile sur la page. Une solution est de faire pivoter le texte verticalement afin qu'il occupe moins d'espace horizontal. Dans Microsoft Excel, faire pivoter du texte est facile. Heureusement, il est également possible de faire pivoter le texte de manière programmatique, afin que les développeurs puissent faire pivoter les étiquettes dans les feuilles de calcul qu'ils créent dans leurs applications.

Cet article examine comment faire pivoter le texte dans les cellules en utilisant [Aspose.Cells for .NET](/cells/fr/net/rotating-cell-text/) par rapport à faire la même chose avec [VSTO](/cells/fr/net/rotating-cell-text/).

{{% /alert %}}

## **Faire pivoter le texte dans les cellules**

Pour faire pivoter le texte dans une cellule sur une feuille de calcul, suivez les étapes suivantes:

1. Créez un classeur et obtenez une feuille de calcul.
1. Ajoutez du texte d'exemples.
1. Formatez le texte : rotation, ajoutez une couleur de fond.
1. Enregistrez le fichier.

Les exemples de code qui suivent montrent comment effectuer ces étapes d'abord dans [VSTO](/cells/fr/net/rotating-cell-text/), en utilisant soit C# soit Visual Basic, et ensuite dans [Aspose.Cells](/cells/fr/net/rotating-cell-text/), à nouveau en utilisant soit C# soit Visual Basic.

Les exemples de code dans cet article donnent le résultat montré ci-dessous.
**Une cellule avec du texte pivoté.**

![todo:image_alt_text](rotating-cell-text_1.png)

### **Pivoter le texte avec VSTO**

**C#**

{{< highlight csharp >}}

 using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

//Instantiate the Application object.

Excel.ApplicationClass ExcelApp = new Excel.ApplicationClass();

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Put some text into cell B2.

objSheet.Cells[2, 2] = "Aspose Heading";

//Define a range object(B2).

Excel.Range _range;

_range = objSheet.get_Range("B2", "B2");

//Specify the angle of rotation of the text.

_range.Orientation = 45;

//Set the background color.

_range.Interior.Color = System.Drawing.ColorTranslator.ToWin32(Color.FromArgb(0, 51, 105));

//Set the font color of cell text

_range.Font.Color = System.Drawing.ColorTranslator.ToOle(System.Drawing.Color.White);



//Save the excel file.

objBook.SaveCopyAs("c:\\VSTO_RotateText_test.xlsx");

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

#### **Pivoter le texte avec Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 // Instantiate a new Workbook.

 Workbook objworkbook = new Workbook();

// Get the First sheet.

Worksheet objworksheet = objworkbook.Worksheets[0];

// Get Cells.

Cells objcells = objworksheet.Cells;// Get a particular Cell.

Cell objcell = objcells["B2"];// Put some text value.

objcell.PutValue("Aspose Heading");



// Get associated style object of the cell.

Style objstyle = objcell.GetStyle();

// Specify the angle of rotation of the text.

objstyle.RotationAngle = 45;



// Set the custom fill color of the cells.

objstyle.ForegroundColor = Color.FromArgb(0, 51, 105);



// Set the background pattern for fill color.

objstyle.Pattern = BackgroundType.Solid;

// Set the font color of cell text

objstyle.Font.Color = Color.White;



// Assign the updated style object back to the cell

objcell.SetStyle(objstyle);



// Save the work book

objworkbook.Save("c:\\RotateText_test.xlsx");



{{< /highlight >}}
