---
title: VSTO および Aspose.Cells でブック内のワークシートを非表示および再表示する
type: docs
weight: 140
url: /ja/net/hide-and-unhide-worksheets-in-a-workbook-in-vsto-and-aspose-cells/
---
この記事では、C# または Visual Basic を使用して VSTO でワークシートを非表示および再表示することと、C# または Visual Basic を使用して Aspose.Cells で同じタスクを実行することを比較します。 Aspose.Cells では、Microsoft Excel がインストールされていなくても作業できます。

ワークシートを非表示にする手順は次のとおりです。

1. ファイルを開きます。
1. ワークシートを取得します。
1. ワークシートを非表示にします。
1. ファイルを保存します。
ワークシートを再度表示するには、非表示のシートの表示をオンに切り替えます。

以下のコード サンプルは、最初にワークシートを非表示にする方法を示しています。最初のサンプルは、C# を使用した Aspose.Cells と比較して、C# を使用した VSTO のプロセスを示しています。

コード サンプルの 2 番目のセットは、VSTO または Aspose.Cells でワークシートを再表示するために使用される行を示しています。
## **ワークシートを非表示にする**
以下は、ブック内のワークシートを非表示にする方法を示す VSTO および Aspose.Cells のコード サンプルです。
### **VSTO**
{{< highlight "csharp" >}}

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
{{< highlight "csharp" >}}

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
## **ワークシートの再表示**
以下は、VSTO と Aspose.Cells のコード サンプルで、ブック内のワークシートを再表示する方法を示しています。
### **VSTO**
{{< highlight "csharp" >}}

 //Unhide the worksheet.

	objSheet.Visible = Excel.XlSheetVisibility.xlSheetVisible;

{{< /highlight >}}
### **Aspose.Cells**
{{< highlight "csharp" >}}

 //Unhide the worksheet.

objSheet.IsVisible = true;

{{< /highlight >}}
## **サンプルコードをダウンロード**
- [ギットハブ](https://github.com/asposemarketplace/Aspose_for_VSTO/releases/download/Aspose.Cells1.1/Hide.and.Unhide.Worksheets.in.a.Workbook.Aspose.Cells.zip)
- [ソースフォージ](https://sourceforge.net/projects/asposevsto/files/Aspose.Cells%20Vs%20VSTO%20Excel/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\).zip/ダウンロード)
- [ビットバケット](https://bitbucket.org/asposemarketplace/aspose-for-vsto/downloads/Hide%20and%20Unhide%20Worksheets%20in%20a%20Workbook%20\(Aspose.Cells\)。ジップ）
