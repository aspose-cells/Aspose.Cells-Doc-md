---
title: Protéger et déprotéger des classeurs
type: docs
weight: 20
url: /fr/net/protecting-and-unprotecting-workbooks/
---

{{% alert color="primary" %}} 

Pour empêcher quelqu'un de modifier, déplacer ou supprimer accidentellement ou délibérément des feuilles de calcul, vous pouvez protéger les éléments du classeur avec ou sans mot de passe. Pour protéger la structure d'un classeur afin que les feuilles de calcul du classeur ne puissent pas être déplacées, supprimées, masquées, affichées, renommées et que de nouvelles feuilles de calcul ne puissent pas être insérées, spécifiez le ProtectionType comme Structure.

Pour protéger les fenêtres afin qu'elles aient la même taille et position chaque fois que le classeur est ouvert, spécifiez le ProtectionType comme Windows. Dans cet article, nous vous montrons comment [protéger](/cells/fr/net/protecting-and-unprotecting-workbooks/) et [déprotéger](/cells/fr/net/protecting-and-unprotecting-workbooks/) des classeurs en utilisant VSTO et Aspose.Cells for .NET pour que vous puissiez comparer les deux méthodes.

Aspose.Cells fonctionne indépendamment de l'automatisation de Microsoft Office et est conçu pour être facile à utiliser et à produire un code propre.

Protéger un classeur n'empêche pas les utilisateurs de modifier des cellules. Pour protéger les données, vous devez protéger les feuilles de calcul.

{{% /alert %}} 
## **Protéger un classeur**
Pour ouvrir un fichier Microsoft Excel existant, protéger le classeur avec des attributs de structure et de fenêtres, puis enregistrer le fichier.

Voici des extraits de code parallèles pour VSTO (C#, VB) et Aspose.Cells for .NET (C#, VB) qui montrent comment protéger un classeur.
### **VSTO**
**C#**

{{< highlight csharp >}}

 .......

using Microsoft.VisualStudio.Tools.Applications.Runtime;

using Excel = Microsoft.Office.Interop.Excel;

using Office = Microsoft.Office.Core;

using System.Reflection;

.......

//Instantiate the Application object.

Excel.Application excelApp = new Excel.ApplicationClass();

//Specify the template excel file path.

string myPath = @"d:\test\MyBook.xls";

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


### **Aspose.Cells for .NET**
**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......


//Specify the template excel file path.

string myPath = @"d:\test\MyBook.xls";

//Instantiate a new Workbook.

//Open the excel file.

Workbook workbook = new Workbook(myPath);

//Protect the workbook specifying a password with Structure and Windows attributes.

workbook.Protect(ProtectionType.All,"007");

//Save As the excel file.

workbook.Save(@"d:\test\MyBook.xls");



{{< /highlight >}}
## **Déprotection d'un classeur**
Pour déprotéger un classeur, utilisez les lignes de code suivantes pour VSTO (C#, VB) et Aspose.Cells for .NET (C#, VB).
### **VSTO**
**C#**

{{< highlight csharp >}}

 //Unprotect the workbook specifying its password.

excelApp.ActiveWorkbook.Unprotect("007");



{{< /highlight >}}


### **Aspose.Cells for .NET**
**C#**

{{< highlight csharp >}}

 //Unprotect the workbook specifying its password.

workbook.Unprotect("007");



{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
