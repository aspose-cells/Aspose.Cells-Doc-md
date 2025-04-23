---
title: Aspose.Cells 8.6.1 での Public API 変更
type: docs
weight: 200
url: /ja/net/public-api-changes-in-aspose-cells-8-6-1/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cells API のバージョン 8.6.0 から 8.6.1 への変更点について説明しており、モジュール/アプリケーション開発者に興味を持たれるかもしれません。追加されたクラスなどだけでなく、Aspose.Cells の内部動作の変更についても説明しています。

{{% /alert %}} 
## **APIの追加**
### **HTML リンクターゲットタイプのサポート**
このリリースでは、Aspose.Cells for .NET APIにより、HtmlLinkTargetTypeという列挙型、およびHtmlSaveOptions.LinkTargetTypeという新しいプロパティが公開され、スプレッドシートをHTML形式に変換する際にリンクのターゲットタイプを設定できるようになりました。HtmlLinkTargetType列挙型の可能な値は、デフォルト値がSelfを含む下記のようになります。

1. HtmlLinkTargetType.Blank: リンクされたドキュメント/ページを新しいウィンドウやタブで開きます。
1. HtmlLinkTargetType.Parent: リンクされたドキュメント/ページを親フレームで開きます。
1. HtmlLinkTargetType.Self: リンクがクリックされたフレームと同じフレームでリンクされたドキュメント/ページを開きます。
1. HtmlLinkTargetType.Top: リンクされたドキュメント/ページをウィンドウの全体に開きます。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.LinkTargetType = HtmlLinkTargetType.Blank;

//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.Save(outputFilePath, options);

{{< /highlight >}}


### **VbaModuleCollection.Remove メソッドの追加**
Aspose.Cells for .NET 8.6.1では、VbaModuleCollection.Removeメソッドの別のオーバーロードが公開され、指定されたWorksheetに関連するすべてのVBAモジュールを削除するためにWorksheetのインスタンスを受け入れるようになりました。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.VbaProject.Modules;

//Remove the VBA modules from specific Worksheet

modules.Remove(workbook.Worksheets[0]);

{{< /highlight >}}


### **RangeCollection.Add メソッドの追加**
Aspose.Cells for .NET 8.6.1により、RangeCollection.Add メソッドが公開され、特定のWorksheetのための範囲のコレクションにRangeオブジェクトを追加するために使用できます。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.Worksheets[0].Cells;

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.Ranges;

//Add another range to the collection

ranges.Add(cells.CreateRange("A1:B4"));

{{< /highlight >}}


### **Cell.SetCharacters メソッドの追加**
Cell.SetCharacters メソッドは、指定されたCellオブジェクトのリッチテキストの部分を[更新する](/cells/ja/net/access-and-update-the-portions-of-rich-text-of-cell/)ために使用できます。Cell.GetCharactersメソッドはテキストの部分にアクセスするために使用し、その後、FontSettingオブジェクトの配列が返され、そのオブジェクトを操作してフォント名、フォントカラー、太字などのさまざまなプロパティを設定できます。その後、変更を適用するためにCell.SetCharactersメソッドを使用できます。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.Worksheets[0];

//Access the cells containing the Rich Text

Cell cell = worksheet.Cells["A1"];

//Retrieve the array of FontSetting from the cell

FontSetting[] settings = cell.GetCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].Font.Name = "Arial";

//Set the updated FontSetting

cell.SetCharacters(settings);

{{< /highlight >}}


### **VbaProject.IsSigned プロパティを追加**
Aspose.Cells for .NET 8.6.1では、VbaProject.IsSignedプロパティが公開され、ブール型のプロパティはプロジェクトが署名されているかどうかをテストするために使用されます。プロジェクトが署名されている場合、trueを返します。

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VbaProject from the Workbook

VbaProject project = workbook.VbaProject;

//Test if VbaProject is signed

if (project.IsSigned)

{

    Console.WriteLine("VBA Project is Signed");

}

else

{

    Console.WriteLine("VBA Project is not Signed");

}

{{< /highlight >}}
## **APIの変更**
### **Cell.GetFormatConditions メソッドを変更**
v8.6.1のリリースに伴い、Aspose.Cells for .NET APIはCell.GetFormatConditionsメソッドの戻り値タイプを修正し、現在はFormatConditionCollectionの配列を返します。
## **非推奨API**
### **Workbook.CheckWriteProtectedPassword メソッドを非推奨にしました**
v8.6.1 のリリースに伴い、Workbook.CheckWriteProtectedPassword メソッドが非推奨となりました。スプレッドシートの事前設定されたパスワードと一致する場合に真偽値を返す WorkbookSettings.WriteProtection.ValidatePassword メソッドを使用することが推奨されます。
{{< app/cells/assistant language="csharp" >}}
