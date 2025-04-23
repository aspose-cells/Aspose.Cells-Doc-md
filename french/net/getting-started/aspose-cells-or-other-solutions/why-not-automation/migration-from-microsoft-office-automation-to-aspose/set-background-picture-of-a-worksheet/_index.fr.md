---
title: Définir l image d arrière plan d une feuille de calcul
type: docs
weight: 90
url: /fr/net/set-background-picture-of-a-worksheet/
---

{{% alert color="primary" %}}

Les images d'arrière-plan se situent derrière le texte et les lignes dans une feuille de calcul. Elles sont utilisées pour donner des informations sur un classeur, par exemple lorsqu'elles sont utilisées comme filigranes d'état, mais peuvent également ajouter une image de marque d'entreprise ou une décoration. Microsoft Excel permet aux utilisateurs d'ajouter manuellement des images d'arrière-plan.

Les développeurs peuvent également ajouter des images d'arrière-plan via leurs applications, en utilisant soit Aspose.Cells for .NET soit VSTO. Cet article compare les deux approches.

{{% /alert %}}

## **Définir une image d'arrière-plan sur une feuille de calcul**

Pour appliquer une image d'arrière-plan à une feuille de calcul :

1. Créez un classeur et accédez à la feuille à laquelle vous souhaitez appliquer une image d'arrière-plan.
1. Appliquez l'image d'arrière-plan.
1. Enregistrez le classeur.

Les exemples de code suivants montrent comment faire cela d'abord avec [VSTO](/cells/fr/net/set-background-picture-of-a-worksheet/), en utilisant soit C# soit Visual Basic, puis avec [Aspose.Cells for .NET](/cells/fr/net/set-background-picture-of-a-worksheet/), encore une fois en utilisant soit C# soit Visual Basic.

Les exemples de code dans cet article créent une feuille de calcul avec une image d'arrière-plan répétitive, comme celle dans la capture d'écran ci-dessous.

**Un arrière-plan a été défini pour la feuille de calcul.**

![todo:image_alt_text](set-background-picture-of-a-worksheet_1.png)

### **Définition d'images d'arrière-plan avec VSTO**

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

//Set a background picture for the sheet.

objSheet.SetBackgroundPicture("e:\\test\\school.jpg");

//Save the excel file.

objBook.SaveCopyAs("c:\\BackgroundPicBook.xls");

//Quit the Application.

ExcelApp.Quit();



{{< /highlight >}}

### **Définition d'images d'arrière-plan avec Aspose.Cells for .NET**

**C#**

{{< highlight csharp >}}

 .......

using Aspose.Cells;

.......

//Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Get the first worksheet. 

Worksheet sheet = workbook.Worksheets[0];



//Define a string variable to store the image path.

string ImageUrl = @"e:\test\school.jpg";

//Get the picture into the streams.

FileStream fs = File.OpenRead(ImageUrl);

//Define a byte array.

byte[] imageData = new Byte[fs.Length];

//Obtain the picture into the array of bytes from streams.

fs.Read(imageData, 0, imageData.Length);

//Close the stream.

fs.Close();



//Set the background image for the sheet.

sheet.SetBackground(imageData);



//Save the excel file.

workbook.Save(@"c:\BackgroundPicBook.xls");     



{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
