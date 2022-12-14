---
title: Ajout de nouvelles feuilles de calcul au classeur et activation d'une feuille dans VSTO et Aspose.Cells
type: docs
weight: 30
url: /fr/net/adding-new-worksheets-to-workbook-and-activating-a-sheet-in-vsto-and-aspose-cells/
---
## **Conseil de migration :**
1. Ajoutez de nouvelles feuilles de calcul à un fichier Excel Microsoft existant.
1. Remplissez les données dans les cellules de chaque nouvelle feuille de calcul.
1. Activer une feuille dans le classeur.
1. Enregistrez en tant que fichier Excel Microsoft.

Vous trouverez ci-dessous des extraits de code parallèles pour VSTO (C#) et Aspose.Cells for .NET (C#), qui montrent comment accomplir ces tâches.

**VSTO**

{{< highlight "csharp" >}}

//Objet d'application initial

Excel.Application excelApp = Application;

// Spécifiez le chemin du fichier Excel du modèle.

string myPath = "Book1.xls" ;

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

 pour (int je = 1; je< 6; i++){

                //Add a worksheet to the workbook.

                newWorksheet = (Excel.Worksheet)excelApp.Worksheets.Add(Missing.Value, Missing.Value,

                Missing.Value, Missing.Value);

                //Name the sheet.

                newWorksheet.Name = "New_Sheet" + i.ToString();

                //Get the Cells collection.

                Excel.Range cells = newWorksheet.Cells;

                //Input a string value to a cell of the sheet.

                cells.set_Item(i, i, "New_Sheet" + i.ToString());

            }

//Activate the first worksheet by default.

((Excel.Worksheet)excelApp.ActiveWorkbook.Sheets[1]).Activate();

//Save As the excel file.

excelApp.ActiveWorkbook.SaveCopyAs("out_Book1.xls");

//Quit the Application.

excelApp.Quit();



{{< /highlight >}}

**Aspose.Cells**

{{< highlight "csharp" >}}

 //Instancier une instance de licence et définir le fichier de licence

//par son chemin

Aspose.Cells.License license = new Aspose.Cells.License();

licence.SetLicense("Aspose.Total.lic");

// Spécifiez le chemin du fichier Excel du modèle.

string myPath = "Book1.xls" ;

// Instancier un nouveau classeur.

//Ouvre le fichier excel.

Classeur classeur = nouveau classeur (myPath);

// Déclare un objet Worksheet.

Feuille de travail newWorksheet;

//Ajouter 5 nouvelles feuilles de calcul au classeur et remplir quelques données

//dans les cellules.

 pour (int je = 0; je< 5; i++){

                //Add a worksheet to the workbook.

                newWorksheet = workbook.Worksheets[workbook.Worksheets.Add()];

                //Name the sheet.

                newWorksheet.Name = "New_Sheet" + (i + 1).ToString();

                //Get the Cells collection.

                Cells cells = newWorksheet.Cells;

                //Input a string value to a cell of the sheet.

                cells[i, i].PutValue("New_Sheet" + (i + 1).ToString());

            }

//Activate the first worksheet by default.

workbook.Worksheets.ActiveSheetIndex = 0;

//Save As the excel file.

workbook.Save("out_My_Book1.xls");

{{< /highlight >}}
## **Télécharger l'exemple de code**
- [GithubGenericName](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Adding.New.Worksheets.to.Workbook.and.Activating.a.Sheet.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\).zip/télécharger)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Adding%20New%20Worksheets%20to%20Workbook%20and%20Activating%20a%20Sheet%20\(Aspose.Cells\).Zip *: français)
