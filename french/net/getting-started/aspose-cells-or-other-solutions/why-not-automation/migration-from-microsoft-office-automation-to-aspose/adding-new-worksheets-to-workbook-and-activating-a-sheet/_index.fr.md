---
title: Ajout de nouvelles feuilles de calcul au classeur et activation d'une feuille
type: docs
weight: 10
url: /fr/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/
---
{{% alert color="primary" %}} 

Lorsque vous travaillez avec un fichier de modèle, il est parfois nécessaire d'ajouter des feuilles de calcul supplémentaires dans le classeur pour collecter des données. Les nouvelles cellules seront remplies de données aux positions et emplacements spécifiés dans chaque feuille de calcul.

De même, vous devrez peut-être qu'une feuille de calcul spécifique soit active et affichée en premier lorsque le fichier est ouvert dans Microsoft Excel. Une "feuille active" est la feuille sur laquelle vous travaillez dans un classeur. Le nom sur l'onglet de la feuille active est en gras par défaut.

 L'ajout de feuilles de calcul et la définition de la feuille active sont des tâches courantes et simples que les développeurs doivent savoir effectuer. Dans cet article, nous effectuons ces tâches en utilisant[VSTO](/cells/fr/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/) et[Aspose.Cells for .NET](/cells/fr/net/adding-new-worksheets-to-workbook-and-activating-a-sheet/).

{{% /alert %}} 
## **Ajout de feuilles de calcul et activation d'une feuille**
Pour les besoins de ce conseil de migration :

1. Ajoutez de nouvelles feuilles de calcul à un fichier Excel Microsoft existant.
1. Remplissez les données dans les cellules de chaque nouvelle feuille de calcul.
1. Activer une feuille dans le classeur.
1. Enregistrez en tant que fichier Excel Microsoft.

Vous trouverez ci-dessous des extraits de code parallèles pour VSTO (C#, VB) et Aspose.Cells for .NET (C#, VB), qui montrent comment accomplir ces tâches.
### **VSTO**
**C#**

{{< highlight "csharp" >}}

 .......

en utilisant Microsoft.VisualStudio.Tools.Applications.Runtime ;

en utilisant Excel = Microsoft.Office.Interop.Excel ;

en utilisant Office = Microsoft.Office.Core ;

en utilisant System.Reflection ;

.......

//Instancier l'objet Application.

Excel.Application excelApp = new Excel.ApplicationClass();

// Spécifiez le chemin du fichier Excel du modèle.

string myPath = @"d:\test\My_Book1.xls" ;

//Ouvre le fichier excel.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Valeur.manquante, Valeur.manquante,

Valeur.manquante, Valeur.manquante,

Valeur.manquante, Valeur.manquante,

Valeur.manquante, Valeur.manquante,

Valeur.manquante, Valeur.manquante,

Valeur.manquante, Valeur.manquante );

// Déclare un objet Worksheet.

Excel.Worksheet newWorksheet;

//Ajouter 5 nouvelles feuilles de calcul au classeur et remplir quelques données

//dans les cellules.

 pour (int je = 1; je< 6; i++)

{

//Add a worksheet to the workbook.

newWorksheet = Excel.Worksheet)excelApp.Worksheets.Add(Missing.Value, Missing.Value, Missing.Value, Missing.Value);

//Name the sheet.

newWorksheet.Name ="New_Sheet" + i.ToString();

//Get the Cells collection.

Excel.Range cells =  newWorksheet.Cells;

//Input a string value to a cell of the sheet.

cells.set_Item(i, i,"New_Sheet" + i.ToString());

}

//Activate the first worksheet by default.

((Excel.Worksheet)excelApp.ActiveWorkbook.Sheets[1]).Activate();

//Save As the excel file.

excelApp.ActiveWorkbook.SaveCopyAs(@"d:\test\out_My_Book1.xls");

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

**VB**

{{< highlight "csharp" >}}

 .......

Imports Microsoft.VisualStudio.Tools.Applications.Runtime

Imports Excel = Microsoft.Office.Interop.Excel

Imports Office = Microsoft.Office.Core

Imports System.Reflection

.......

'Instantiate the Application object.

Dim excelApp As Excel.Application = New Excel.ApplicationClass()

'Specify the template excel file path.

Dim myPath As String = "d:\test\My_Book1.xls"

'Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value, Missing.Value)

'Declare a Worksheet object.

Dim newWorksheet As Excel.Worksheet

'Add 5 new worksheets to the workbook and fill some data

'into the cells.

Dim i As Integer

For i = 1 To 5 Step 1

'Add a worksheet to the workbook.

newWorksheet = CType(excelApp.Worksheets.Add(Missing.Value, Missing.Value, Missing.Value, Missing.Value), Excel.Worksheet)

'Name the sheet.

newWorksheet.Name ="New_Sheet" & i.ToString()

'Get the Cells collection.

Dim cells As Excel.Range = newWorksheet.Cells

'Input a string value to a cell of the sheet.

cells.Item(i, i) = "New_Sheet" & i.ToString()

Next

'Activate the first worksheet by default.

CType(excelApp.ActiveWorkbook.Sheets(1), Excel.Worksheet).Activate()

'Save As the excel file.

excelApp.ActiveWorkbook.SaveCopyAs("d:\test\out_My_Book1.xls")

'Quit the Application.

excelApp.Quit()



{{< /highlight >}}
### **Aspose.Cells for .NET**
**C#**

{{< highlight "csharp" >}}

 .......

en utilisant Aspose.Cells ;

.......

//Instancier une instance de licence et définir le fichier de licence

//par son chemin

Aspose.Cells.License license = new Aspose.Cells.License();

licence.SetLicense("Aspose.Cells.lic");

// Spécifiez le chemin du fichier Excel du modèle.

string myPath =@"d:\test\My_Book1.xls" ;

// Instancier un nouveau classeur.

//Ouvre le fichier excel.

Classeur classeur = nouveau classeur (myPath);

// Déclare un objet Worksheet.

Feuille de travail newWorksheet;

//Ajouter 5 nouvelles feuilles de calcul au classeur et remplir quelques données

//dans les cellules.

 pour (int je = 0; je< 5; i++)

{

//Add a worksheet to the workbook.

newWorksheet = workbook.Worksheets[workbook.Worksheets.Add()];

//Name the sheet.

newWorksheet.Name = "New_Sheet" + (i+1).ToString();

//Get the Cells collection.

Cells cells =  newWorksheet.Cells;

//Input a string value to a cell of the sheet.

cells[i, i].PutValue("New_Sheet" + (i+1).ToString());

}

//Activate the first worksheet by default.

workbook.Worksheets.ActiveSheetIndex = 0;

//Save As the excel file.

workbook.Save(@"d:\test\out_My_Book1.xls");



{{< /highlight >}}

**VB**

{{< highlight "csharp" >}}

 .......

Imports Aspose.Cells

.......

'Instantiate an instance of license and set the license file

'through its path

Dim license As Aspose.Cells.License = New Aspose.Cells.License

license.SetLicense("Aspose.Cells.lic")

'Specify the template excel file path.

Dim myPath As String ="d:\test\My_Book1.xls"

'Instantiate a new Workbook.

'Open the excel file.

Dim workbook As Workbook = New Workbook(myPath)

'Declare a Worksheet object.

Dim newWorksheet As Worksheet

'Add 5 new worksheets to the workbook and fill some data

'into the cells.

Dim i As Integer

For i = 0 To 4 Step 1

'Add a worksheet to the workbook.

newWorksheet = workbook.Worksheets(workbook.Worksheets.Add())

'Name the sheet.

newWorksheet.Name = "New_Sheet" + (i + 1).ToString()

'Get the Cells collection.

Dim cells As Cells = newWorksheet.Cells

'Input a string value to a cell of the sheet.

cells(i, i).PutValue("New_Sheet" + (i + 1).ToString())

Next

'Activate the first worksheet by default.

workbook.Worksheets.ActiveSheetIndex = 0

'Save As the excel file.

workbook.Save("c:\test\out_My_Book1.xls")



{{< /highlight >}}
