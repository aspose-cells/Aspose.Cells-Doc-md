---
title: ワークシートの背景画像を設定する
type: docs
weight: 90
url: /ja/net/set-background-picture-of-a-worksheet/
---
{{% alert color="primary" %}}

背景画像は、スプレッドシートのテキストと行の後ろにあります。これらは、たとえばステータスの透かしとして使用される場合など、ワークブックに関する情報を提供するために使用されますが、会社のブランディングや装飾を追加することもできます。 Microsoft Excel では、ユーザーが背景画像を手動で追加できます。

開発者は、Aspose.Cells for .NET または VSTO を使用して、アプリケーションから背景画像を追加することもできます。この記事では、2 つのアプローチを比較します。

{{% /alert %}}

## **ワークシートに背景画像を設定する**

背景画像をスプレッドシートに適用するには:

1. ワークブックを作成し、背景画像を適用するシートにアクセスします。
1. 背景画像を適用します。
1. ブックを保存します。

以下のコード サンプルは、最初にこれを行う方法を示しています。[VSTO](/cells/ja/net/set-background-picture-of-a-worksheet/) 、C# または Visual Basic を使用し、次に[Aspose.Cells for .NET](/cells/ja/net/set-background-picture-of-a-worksheet/)、再び C# または Visual Basic を使用します。

この記事のコード例では、下のスクリーンショットのように、背景画像が繰り返されるワークシートを作成します。

**ワークシートの背景が設定されました。**

![todo:画像_代替_文章](set-background-picture-of-a-worksheet_1.png)

### **VSTO で背景画像を設定する**

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

### **Aspose.Cells for .NET で背景画像を設定する**

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
