---
title: Rotation du texte Cell
type: docs
weight: 100
url: /fr/net/rotating-cell-text/
---
{{% alert color="primary" %}}

Parfois, un en-tête de colonne est beaucoup plus large que les données des cellules ci-dessous. Cela peut créer des espaces blancs inutiles sur la page. Une solution consiste à faire pivoter le texte verticalement afin qu'il occupe moins d'espace horizontal. Dans Microsoft Excel, la rotation du texte est facile. Heureusement, il est également possible de faire pivoter le texte par programmation, afin que les développeurs puissent faire pivoter les étiquettes dans les feuilles de calcul qu'ils créent dans leurs applications.

 Cet article explique comment faire pivoter du texte dans des cellules à l'aide de[Aspose.Cells for .NET](/cells/fr/net/rotating-cell-text/) par rapport à faire la même chose avec[VSTO](/cells/fr/net/rotating-cell-text/).

{{% /alert %}}

## **Rotation du texte dans Cells**

Pour faire pivoter du texte dans une cellule d'une feuille de calcul, procédez comme suit :

1. Créez un classeur et obtenez une feuille de calcul.
1. Ajoutez des exemples de texte.
1. Formatez le texte : faites pivoter, ajoutez une couleur d'arrière-plan.
1. Enregistrez le fichier.

 Les exemples de code qui suivent montrent comment effectuer ces étapes en premier dans[VSTO](/cells/fr/net/rotating-cell-text/) , en utilisant C# ou Visual Basic, puis dans[Aspose.Cells](/cells/fr/net/rotating-cell-text/), en utilisant à nouveau C# ou Visual Basic.

Les exemples de code de cet article donnent la sortie indiquée ci-dessous.
**Une cellule avec du texte pivoté.**

![tâche : image_autre_texte](rotating-cell-text_1.png)

### **Rotation de texte avec VSTO**

**C#**

{{< highlight "csharp" >}}

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

objSheet.Cells[2, 2]= "Aspose Heading";

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

#### **Rotation du texte avec Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

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
