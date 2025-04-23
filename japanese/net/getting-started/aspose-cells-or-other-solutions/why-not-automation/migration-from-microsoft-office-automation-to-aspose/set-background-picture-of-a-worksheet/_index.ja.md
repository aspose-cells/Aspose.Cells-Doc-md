---
title: ワークシートの背景画像の設定
type: docs
weight: 90
url: /ja/net/set-background-picture-of-a-worksheet/
---

{{% alert color="primary" %}}

背景画像は、スプレッドシートのテキストと行の背後に配置されます。ステータスウォーターマークとして使用されたり、企業ブランディングや装飾などの情報を提供するために使用されます。Microsoft Excel では、ユーザーは手動で背景画像を追加できます。

開発者は、Aspose.Cells for .NET または VSTO を使用してアプリケーションを介して背景画像を追加することもできます。この記事はこれら2つの方法を比較します。

{{% /alert %}}

## **ワークシートに背景画像を適用するには:**

スプレッドシートに背景画像を適用するには:

1. ワークブックを作成し、背景画像を適用するシートにアクセスします。
1. 背景画像を適用します。
1. ワークブックを保存します。

次に示すコード例は、まず[C#](/cells/ja/net/set-background-picture-of-a-worksheet/)またはVisual Basicを使用して[VSTO](/cells/ja/net/set-background-picture-of-a-worksheet/)で行う方法、そして再び[C#](/cells/ja/net/set-background-picture-of-a-worksheet/)またはVisual Basicを使用して[Aspose.Cells for .NET](/cells/ja/net/set-background-picture-of-a-worksheet/)で行う方法を示しています。

この記事のコード例では、スクリーンショット下に示すように、繰り返しの背景画像を含むワークシートを作成します。

**ワークシートに背景が設定されました。**

![todo:image_alt_text](set-background-picture-of-a-worksheet_1.png)

### **VSTOを使用して背景画像を設定**

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

### **Aspose.Cells for .NETを使用して背景画像を設定**

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
