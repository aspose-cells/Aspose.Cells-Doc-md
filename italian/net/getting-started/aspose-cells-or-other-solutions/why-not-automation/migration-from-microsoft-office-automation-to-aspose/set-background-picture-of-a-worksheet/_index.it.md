---
title: Impostare un immagine di sfondo di un foglio di lavoro
type: docs
weight: 90
url: /it/net/set-background-picture-of-a-worksheet/
---

{{% alert color="primary" %}}

Le immagini di sfondo si trovano dietro il testo e le linee in un foglio di calcolo. Sono utilizzate per fornire informazioni su un libro di lavoro, ad esempio quando vengono utilizzate come filigrane di stato, ma possono anche aggiungere il marchio aziendale o la decorazione. Microsoft Excel consente agli utenti di aggiungere manualmente immagini di sfondo.

Gli sviluppatori possono anche aggiungere immagini di sfondo tramite le loro applicazioni, utilizzando sia Aspose.Cells for .NET che VSTO. Questo articolo confronta i due approcci.

{{% /alert %}}

## **Impostare un'immagine di sfondo su un foglio di lavoro**

Per applicare un'immagine di sfondo a un foglio di calcolo:

1. Creare un libro di lavoro e accedere al foglio su cui si desidera applicare un'immagine di sfondo.
1. Applicare l'immagine di sfondo.
1. Salvare il libro di lavoro.

Gli esempi di codice che seguono mostrano come fare questo prima con [VSTO](/cells/it/net/set-background-picture-of-a-worksheet/), utilizzando C# o Visual Basic, e poi con [Aspose.Cells for .NET](/cells/it/net/set-background-picture-of-a-worksheet/), nuovamente utilizzando C# o Visual Basic.

Gli esempi di codice in questo articolo creano un foglio di lavoro con un'immagine di sfondo ripetuta, simile a quella nella schermata sottostante.

**È stata impostata un'immagine di sfondo per il foglio di lavoro.**

![todo:image_alt_text](set-background-picture-of-a-worksheet_1.png)

### **Impostazione dell'immagine di sfondo con VSTO**

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

### **Impostare le immagini di sfondo con Aspose.Cells for .NET**

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
