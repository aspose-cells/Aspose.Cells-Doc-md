---
title: Définir l image d arrière plan d une feuille de calcul dans VSTO et Aspose.Cells
type: docs
weight: 220
url: /fr/net/set-background-picture-of-a-worksheet-in-vsto-and-aspose-cells/
---

Pour appliquer une image d'arrière-plan à une feuille de calcul :

1. Créez un classeur et accédez à la feuille à laquelle vous souhaitez appliquer une image d'arrière-plan.
1. Appliquez l'image d'arrière-plan.
1. Enregistrez le classeur.

Les exemples de code suivants montrent comment faire cela d'abord avec VSTO, en utilisant soit C# soit Visual Basic, puis avec Aspose.Cells for .NET, de nouveau en utilisant soit C# soit Visual Basic.

Les exemples de code de cet article créent une feuille de calcul avec une image d'arrière-plan répétée, comme celle de la capture d'écran ci-dessous.

![todo:image_alt_text](picture1.png)

Un arrière-plan a été défini pour la feuille de calcul.

## **VSTO**

{{< highlight csharp >}}

 //Instantiate the Application object.

Excel.Application ExcelApp = Application;

//Add a Workbook.

Excel.Workbook objBook = ExcelApp.Workbooks.Add(System.Reflection.Missing.Value);

//Get the First sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)objBook.Sheets["Sheet1"];

//Set a background picture for the sheet.

objSheet.SetBackgroundPicture("pic.jpeg");

//Save the excel file.

objBook.SaveCopyAs("BackgroundPicBook.xls");

//Quit the Application.

ExcelApp.Quit();

{{< /highlight >}}

## **Aspose.Cells**

{{< highlight csharp >}}

 //Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Get the first worksheet.

Worksheet sheet = workbook.Worksheets[0];

//Define a string variable to store the image path.

string ImageUrl = "pic.jpeg";

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

workbook.Save("BackgroundPicBook.xls");

{{< /highlight >}}

## **Télécharger le code source d'exemple**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Set.Background.Picture.of.a.Worksheet.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Set%20Background%20Picture%20of%20a%20Worksheet%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Set%20Background%20Picture%20of%20a%20Worksheet%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
