---
title: Ajouter des bordures aux cellules dans une feuille de calcul
type: docs
weight: 50
url: /fr/net/add-borders-to-cells-in-a-worksheet/
---

{{% alert color="primary" %}}

Aspose.Cells for .NET vous permet d'effectuer presque toutes les tâches à travers votre application qu'un utilisateur peut effectuer dans Microsoft Excel. Aspose.Cells est performant et robuste et présente l'avantage supplémentaire de fonctionner de manière indépendante de l'automatisation Microsoft. Cet article montre comment ajouter des bordures aux cellules dans une feuille de calcul à l'aide de Aspose.Cells for .NET par rapport à VSTO.

{{% /alert %}}

## **Ajout de bordures aux cellules**

Pour ajouter des bordures aux cellules dans une feuille de calcul, suivez les étapes suivantes :

1. Mettez en place la feuille de calcul:
   1. Instancier un objet Application.
      (VSTO uniquement.)
   1. Ajouter un classeur.
   1. Obtenir la première feuille.
   1. Ajouter du texte aux cellules auxquelles vous ajouterez des bordures.
1. Ajouter des bordures :
   1. Définir une plage.
   1. Appliquer un style de bordure à la plage.
      Répétez pour chaque plage et chaque style de bordure que vous souhaitez définir. Cet exemple applique des bordures de type fin, moyen et épais.
1. Terminer :
   1. Ajuster automatiquement la colonne dans laquelle se trouvent les cellules pour adapter le texte proprement.
   1. Enregistrer le document.

Ces étapes sont illustrées dans le code ci-dessous. Les premiers exemples de code montrent comment les mettre en œuvre en utilisant [VSTO](/cells/fr/net/add-borders-to-cells-in-a-worksheet/) avec soit C# soit Visual Basic. Après les exemples VSTO, il y a des exemples qui montrent comment accomplir les mêmes étapes en utilisant [Aspose.Cells for .NET](/cells/fr/net/add-borders-to-cells-in-a-worksheet/), encore une fois en utilisant soit C# soit Visual Basic. Les exemples de code Aspose.Cells sont beaucoup plus courts car Aspose.Cells est optimisé pour un codage efficace.

Le code génère un fichier Excel avec un certain nombre de cellules sur la première feuille, chacune avec une bordure différente :

![todo:image_alt_text](add-borders-to-cells-in-a-worksheet_1.png)

**Cellules avec des bordures appliquées.**

### **Ajouter des bordures avec VSTO**

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



//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[2, 1] = "Hair Lines";

objSheet.Cells[4, 1] = "Thin Lines";

objSheet.Cells[6, 1] = "Medium Lines";

objSheet.Cells[8, 1] = "Thick Lines";

//Define a range object(A2).

Excel.Range _range;

_range = objSheet.get_Range("A2", "A2");

//Get the borders collection.

Excel.Borders borders = _range.Borders;

//Set the hair lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 1d;



//Define a range object(A4).

_range = objSheet.get_Range("A4", "A4");

//Get the borders collection.

borders = _range.Borders;

//Set the thin lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 2d;



//Define a range object(A6).

_range = objSheet.get_Range("A6", "A6");

//Get the borders collection.

borders = _range.Borders;

//Set the medium lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 3d;



//Define a range object(A8).

_range = objSheet.get_Range("A8", "A8");

//Get the borders collection.

borders = _range.Borders;

//Set the thick lines style.

borders.LineStyle = Excel.XlLineStyle.xlContinuous;

borders.Weight = 4d;



//Auto-fit Column A.

objSheet.get_Range("A2", "A2").EntireColumn.AutoFit();



//Save the excel file.

objBook.SaveAs("f:\\test\\ApplyBorders.xls",

Microsoft.Office.Interop.Excel.XlFileFormat.xlExcel8,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing,

Microsoft.Office.Interop.Excel.XlSaveAsAccessMode.xlNoChange,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing,

Type.Missing);



//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **Ajouter des bordures avec Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook.

Workbook objBook = new Workbook();  

//Get the First sheet.

Worksheet objSheet = objBook.Worksheets["Sheet1"];



//Put some text into different cells (A2, A4, A6, A8).

objSheet.Cells[1, 0].PutValue("Hair Lines");

objSheet.Cells[3, 0].PutValue("Thin Lines");

objSheet.Cells[5, 0].PutValue("Medium Lines");

objSheet.Cells[7, 0].PutValue("Thick Lines");

//Define a range object(A2).

Aspose.Cells.Range _range;

_range = objSheet.Cells.CreateRange("A2", "A2");

//Set the borders with hair lines style.

_range.SetOutlineBorders( CellBorderType.Hair, Color.Black);

//Define a range object(A4).

_range = objSheet.Cells.CreateRange("A4", "A4");

//Set the borders with thin lines style.

_range.SetOutlineBorders(CellBorderType.Thin, Color.Black);

//Define a range object(A6).

_range = objSheet.Cells.CreateRange("A6", "A6");

//Set the borders with medium lines style.

_range.SetOutlineBorders(CellBorderType.Medium, Color.Black);

//Define a range object(A8).

_range = objSheet.Cells.CreateRange("A8", "A8");

//Set the borders with thick lines style.

_range.SetOutlineBorders(CellBorderType.Thick, Color.Black);

//Auto-fit Column A.

objSheet.AutoFitColumn(0);

//Save the excel file.

objBook.Save("f:\\test\\ApplyBorders.xls");        



{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
