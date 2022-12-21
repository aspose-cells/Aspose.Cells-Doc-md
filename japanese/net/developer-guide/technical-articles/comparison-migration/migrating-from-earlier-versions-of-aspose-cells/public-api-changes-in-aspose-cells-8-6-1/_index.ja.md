---
title: パブリック API Aspose.Cells 8.6.1 の変更点
type: docs
weight: 200
url: /ja/net/public-api-changes-in-aspose-cells-8-6-1/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.6.0 から 8.6.1 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加されたクラスだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **HTML リンク ターゲット タイプのサポート**
Aspose.Cells for .NET API のこのリリースでは、HtmlLinkTargetType という列挙型が、新しいプロパティ HtmlSaveOptions.LinkTargetType とともに公開されました。[HTML 形式への変換中にスプレッドシートのリンクのターゲット タイプを設定する](/cells/ja/net/change-the-html-link-target-type/)HtmlLinkTargetType 列挙体の可能な値は次のとおりです。既定値は Self です。

1. HtmlLinkTargetType.Blank: リンクされたドキュメント/ページを新しいウィンドウまたはタブで開きます。
1. HtmlLinkTargetType.Parent: リンクされたドキュメント/ページを親フレームで開きます。
1. HtmlLinkTargetType.Self: リンクがクリックされたのと同じフレームで、リンクされたドキュメント/ページを開きます。
1. HtmlLinkTargetType.Top: リンクされたドキュメント/ページをウィンドウ全体で開きます。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.LinkTargetType = HtmlLinkTargetType.Blank;

//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.Save(outputFilePath, options);

{{< /highlight >}}


### **メソッド VbaModuleCollection.Remove が追加されました**
Aspose.Cells for .NET 8.6.1 は、VbaModuleCollection.Remove メソッドの別のオーバーロードを公開しました。このメソッドは、Worksheet のインスタンスを受け入れて、指定された Worksheet に関連付けられているすべての VBA モジュールを削除できるようになりました。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.VbaProject.Modules;

//Remove the VBA modules from specific Worksheet

modules.Remove(workbook.Worksheets[0]);

{{< /highlight >}}


### **メソッド RangeCollection.Add が追加されました**
Aspose.Cells for .NET 8.6.1 は、Range オブジェクトを特定のワークシートの範囲のコレクションに追加するために使用できる RangeCollection.Add メソッドを公開しました。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.Worksheets[0].Cells;

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.Ranges;

//Add another range to the collection

ranges.Add(cells.CreateRange("A1:B4"));

{{< /highlight >}}


### **メソッド Cell.SetCharacters を追加**
Cell.SetCharacters メソッドを使用して、[リッチ テキストの部分を更新する](/cells/ja/net/access-and-update-the-portions-of-rich-text-of-cell/)特定の Cell オブジェクトの。 Cell.GetCharacters メソッドを使用してテキストの一部にアクセスし、Cell.SetCharacters メソッドを使用して修正を行うことができますが、**取得する**メソッドは、フォント名、フォントの色、太さなどのさまざまなプロパティを設定するために操作できる FontSetting オブジェクトの配列を返します。**セットする**メソッドを使用して変更を適用できます。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.Worksheets[0];

//Access the cells containing the Rich Text

Cell cell = worksheet.Cells["A1"];

//Retrieve the array of FontSetting from the cell

FontSetting[]settings = cell.GetCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].Font.Name = "Arial";

//Set the updated FontSetting

cell.SetCharacters(settings);

{{< /highlight >}}


### **プロパティ VbaProject.IsSigned が追加されました**
Aspose.Cells for .NET 8.6.1 で使用できる VbaProject.IsSigned プロパティが公開されました。[ワークブック内の VbaProject が署名されているかどうかをテストします](/cells/ja/net/check-if-vba-project-in-a-workbook-is-signed/).プロジェクトが署名されている場合、ブール型のプロパティは true を返します。

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

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
## **変更された API**
### **メソッド Cell.GetFormatConditions が変更されました**
v8.6.1 のリリースにより、Aspose.Cells for .NET API は Cell.GetFormatConditions メソッドの戻り値の型を変更し、FormatConditionCollection 型の配列を返すようになりました。
## **廃止された API**
### **メソッド Workbook.CheckWriteProtectedPassword 廃止されました**
v8.6.1 のリリースにより、Workbook.CheckWriteProtectedPassword メソッドは非推奨とマークされました。文字列値をパラメーターとして受け入れ、パスワードがスプレッドシートの事前設定パスワードと一致する場合はブール値を返す WorkbookSettings.WriteProtection.ValidatePassword メソッドを使用することをお勧めします。
