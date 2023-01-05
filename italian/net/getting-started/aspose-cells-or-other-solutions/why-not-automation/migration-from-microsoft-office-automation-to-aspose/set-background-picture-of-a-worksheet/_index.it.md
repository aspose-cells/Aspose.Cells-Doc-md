---
title: Impostare l'immagine di sfondo di un foglio di lavoro
type: docs
weight: 90
url: /it/net/set-background-picture-of-a-worksheet/
---
{{% alert color="primary" %}}

Le immagini di sfondo si trovano dietro il testo e le righe in un foglio di calcolo. Vengono utilizzati per fornire informazioni su una cartella di lavoro, ad esempio quando vengono utilizzati come filigrane di stato, ma possono anche aggiungere il marchio dell'azienda o la decorazione. Microsoft Excel consente agli utenti di aggiungere immagini di sfondo manualmente.

Gli sviluppatori possono anche aggiungere immagini di sfondo tramite le loro applicazioni, utilizzando Aspose.Cells for .NET o VSTO. Questo articolo mette a confronto i due approcci.

{{% /alert %}}

## **Impostazione di un'immagine di sfondo su un foglio di lavoro**

Per applicare un'immagine di sfondo a un foglio di calcolo:

1. Crea una cartella di lavoro e accedi al foglio a cui desideri applicare un'immagine di sfondo.
1. Applicare l'immagine di sfondo.
1. Salva la cartella di lavoro.

 Gli esempi di codice che seguono mostrano come eseguire prima questa operazione con[VSTO](/cells/it/net/set-background-picture-of-a-worksheet/) , utilizzando C# o Visual Basic, quindi con[Aspose.Cells for .NET](/cells/it/net/set-background-picture-of-a-worksheet/), sempre usando C# o Visual Basic.

Gli esempi di codice in questo articolo creano un foglio di lavoro con un'immagine di sfondo ripetuta, come quella nello screenshot seguente.

**È stato impostato uno sfondo per il foglio di lavoro.**

![cose da fare:immagine_alt_testo](set-background-picture-of-a-worksheet_1.png)

### **Impostazione delle immagini di sfondo con VSTO**

**C#**

{{< highlight "csharp" >}}

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

### **Impostazione delle immagini di sfondo con Aspose.Cells for .NET**

**C#**

{{< highlight "csharp" >}}

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

byte[]imageData = new Byte[fs.Length];

//Obtain the picture into the array of bytes from streams.

fs.Read(imageData, 0, imageData.Length);

//Close the stream.

fs.Close();



//Set the background image for the sheet.

sheet.SetBackground(imageData);



//Save the excel file.

workbook.Save(@"c:\BackgroundPicBook.xls");     



{{< /highlight >}}
