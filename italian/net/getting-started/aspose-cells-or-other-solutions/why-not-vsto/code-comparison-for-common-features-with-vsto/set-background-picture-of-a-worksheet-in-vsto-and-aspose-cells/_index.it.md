---
title: Imposta l'immagine di sfondo di un foglio di lavoro in VSTO e Aspose.Cells
type: docs
weight: 220
url: /it/net/set-background-picture-of-a-worksheet-in-vsto-and-aspose-cells/
---
Per applicare un'immagine di sfondo a un foglio di calcolo:

1. Crea una cartella di lavoro e accedi al foglio a cui desideri applicare un'immagine di sfondo.
1. Applicare l'immagine di sfondo.
1. Salva la cartella di lavoro.

Gli esempi di codice che seguono mostrano come eseguire questa operazione prima con VSTO, usando C# o Visual Basic, quindi con Aspose.Cells for .NET, sempre usando C# o Visual Basic.

Gli esempi di codice in questo articolo creano un foglio di lavoro con un'immagine di sfondo ripetuta, come quella nello screenshot qui sotto.

![cose da fare:immagine_alt_testo](picture1.png)

È stato impostato uno sfondo per il foglio di lavoro.

## **VSTO**

{{< highlight "csharp" >}}

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

{{< highlight "csharp" >}}

 //Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Get the first worksheet.

Worksheet sheet = workbook.Worksheets[0];

//Define a string variable to store the image path.

string ImageUrl = "pic.jpeg";

//Get the picture into the streams.

FileStream fs = File.OpenRead(ImageUrl);

//Define a byte array.

byte[]imageData = new Byte[fs.Length];

//Obtain the picture into the array of bytes from streams.

fs.Read(imageData, 0, imageData.Length);

//Close the stream.

fs.Close();

//Set the background image for the sheet.

sheet.SetBackground(imageData);

//Save the excel file.

workbook.Save("BackgroundPicBook.xls");

{{< /highlight >}}

## **Scarica il codice di esempio**

- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Set.Background.Picture.of.a.Worksheet.Aspose.Cells.zip)
- [SourceForge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Set%20Background%20Picture%20of%20a%20Worksheet%20\(Aspose.Cells\).zip/scarica)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Set%20Background%20Picture%20of%20a%20Worksheet%20\(Aspose.Cells\).cerniera lampo)
