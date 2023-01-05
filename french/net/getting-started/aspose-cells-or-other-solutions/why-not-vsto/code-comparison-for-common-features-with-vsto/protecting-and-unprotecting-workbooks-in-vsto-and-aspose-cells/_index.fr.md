---
title: Protéger et déprotéger les classeurs dans VSTO et Aspose.Cells
type: docs
weight: 200
url: /fr/net/protecting-and-unprotecting-workbooks-in-vsto-and-aspose-cells/
---
Pour ouvrir un fichier Excel Microsoft existant, protégez le classeur avec la structure et les attributs Windows et enregistrez le fichier.

Vous trouverez ci-dessous des extraits de code parallèles pour VSTO (C#) et Aspose.Cells for .NET (C#) qui montrent comment protéger un classeur.
## **VSTO**
**Protéger le classeur**

{{< highlight "csharp" >}}

 //Instantiate the Application object.

   Excel.Application excelApp = Application;

//Excel.Application excelApp = Application;

//Specify the template excel file path.

  string myPath = "MyBook.xls";

//Open the excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value,

            Missing.Value, Missing.Value);

//Protect the workbook specifying a password with Structure and Windows attributes.

  excelApp.ActiveWorkbook.Protect("007", true, true);

//Save the file.

  excelApp.ActiveWorkbook.Save();

//Quit the Application.

  excelApp.Quit();

{{< /highlight >}}

**Déprotéger le classeur**

{{< highlight "csharp" >}}

  //Unprotect the workbook specifying its password.

  excelApp.ActiveWorkbook.Unprotect("007");

{{< /highlight >}}
## **Aspose.Cells**
**Protéger le classeur**

{{< highlight "csharp" >}}

 //Specify the template excel file path.

   string myPath = "Book1.xls";

//Instantiate a new Workbook.

//Open the excel file.

   Workbook workbook = new Workbook(myPath);

//Protect the workbook specifying a password with Structure and Windows attributes.

   workbook.Protect(ProtectionType.All, "007");

//Save As the excel file.

   workbook.Save("MyBook.xls");

{{< /highlight >}}

**Déprotéger le classeur**

{{< highlight "csharp" >}}

 //Unprotect the workbook specifying its password.

  workbook.Unprotect("007");

{{< /highlight >}}
## **Télécharger l'exemple de code**
- [GithubGenericName](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Protecting.and.Unprotecting.Workbooks.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Protecting%20and%20Unprotecting%20Workbooks%20\(Aspose.Cells\).zip/télécharger)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Protecting%20and%20Unprotecting%20Workbooks%20\(Aspose.Cells\).Zip *: français)
