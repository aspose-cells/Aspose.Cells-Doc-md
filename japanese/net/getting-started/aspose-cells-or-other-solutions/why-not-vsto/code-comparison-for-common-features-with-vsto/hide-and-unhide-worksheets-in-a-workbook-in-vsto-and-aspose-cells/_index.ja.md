---
title: VSTOとAspose.Cellsでワークブック内のワークシートを非表示および表示する
type: docs
weight: 140
url: /ja/net/hide-and-unhide-worksheets-in-a-workbook-in-vsto-and-aspose-cells/
---

この記事では、VSTOを使用してワークシートを非表示および表示し、C＃またはVisual Basicを使用し、同じタスクをAspose.Cellsを使用して実行する方法について比較しています。 Aspose.Cellsを使用すると、Microsoft Excelをインストールせずに作業できます。

ワークシートを非表示にする手順：

1. ファイルを開く。
1. ワークシートを取得する。
1. ワークシートを非表示にする。
1. ファイルを保存します。
   ワークシートを再表示するには、非表示になったシートの表示をトグルするだけです。

以下のコードサンプルでは、最初にワークシートを非表示にする方法を示します。最初のサンプルはVSTOを使用し、C＃を使用した場合と、Aspose.Cellsを使用し、再度C＃を使用した場合について比較しています。

2番目のコードサンプルセットは、VSTOまたはAspose.Cellsでワークシートを非表示にするために使用される行を示します。
## **ワークシートを非表示にする**
以下は、VSTOおよびAspose.Cellsのコードサンプルで、ワークブック内のワークシートを非表示にする方法を示しています。
### **VSTO**
{{< highlight csharp >}}

 //Instantiate the Application object.

Excel.Application excelApp = Application;

//Specify the template Excel file path.

string myPath = "Book1.xls";

//Open the Excel file.

excelApp.Workbooks.Open(myPath, Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value,

Missing.Value, Missing.Value);

//Get the first sheet.

Excel.Worksheet objSheet = (Excel.Worksheet)excelApp.ActiveWorkbook.Sheets["Sheet1"];

//Hide the worksheet.

objSheet.Visible = Excel.XlSheetVisibility.xlSheetHidden;

//Save As the Excel file.

excelApp.ActiveWorkbook.Save();

//Quit the Application.

excelApp.Quit();


{{< /highlight >}}
### **Aspose.Cells**
{{< highlight csharp >}}

 //Instantiate a new Workbook.

Workbook workbook = new Workbook();

//Specify the template Excel file path.

string myPath = "Book1.xls";

//Open the Excel file.

workbook.Open(myPath);

//Get the first sheet.

Aspose.Cells.Worksheet objSheet = workbook.Worksheets["Sheet1"];

//Hide the worksheet.

objSheet.IsVisible = false;

//Save As the Excel file.

workbook.Save("Book1.xls");

{{< /highlight >}}
## **ワークシートの非表示を解除する**
以下は、VSTOおよびAspose.Cellsのコードサンプルで、ワークブック内のワークシートを非表示から表示する方法を示しています。
### **VSTO**
{{< highlight csharp >}}

 //Unhide the worksheet.

	objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight csharp >}}

 //Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [Github](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Hide.and.Unhide.Worksheets.in.a.Workbook.Aspose.Cells.zip)
- [Sourceforge](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip/download)
- [Bitbucket](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip)
{{< app/cells/assistant language="csharp" >}}
