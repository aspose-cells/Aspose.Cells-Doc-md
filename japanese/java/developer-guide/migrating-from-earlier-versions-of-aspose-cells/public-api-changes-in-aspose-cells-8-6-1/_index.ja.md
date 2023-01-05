---
title: パブリック API Aspose.Cells 8.6.1 の変更点
type: docs
weight: 210
url: /ja/java/public-api-changes-in-aspose-cells-8-6-1/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.6.0 から 8.6.1 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加されたクラスだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **HTML リンク ターゲット タイプのサポート**
Aspose.Cells for Java API のこのリリースでは、HtmlLinkTargetType という列挙型が、新しいプロパティ HtmlSaveOptions.LinkTargetType とともに公開されました。[HTML 形式への変換中に、スプレッドシート内のリンクのターゲット タイプを設定します](/cells/ja/java/change-the-html-link-target-type/)HtmlLinkTargetType 列挙の可能な値は次のとおりです。デフォルト値は SELF です。

1. HtmlLinkTargetType.BLANK: リンクされたドキュメント/ページを新しいウィンドウまたはタブで開きます。
1. HtmlLinkTargetType.PARENT: リンクされたドキュメント/ページを親フレームで開きます。
1. HtmlLinkTargetType.SELF: リンクがクリックされたのと同じフレームで、リンクされたドキュメント/ページを開きます。
1. HtmlLinkTargetType.TOP: リンクされたドキュメント/ページをウィンドウ全体で開きます。

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.setLinkTargetType(HtmlLinkTargetType.BLANK);


//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.save(outputFilePath, options);

{{< /highlight >}}
### **メソッド VbaModuleCollection.remove が追加されました**
Aspose.Cells for Java 8.6.1 は、VbaModuleCollection.remove メソッドの別のオーバーロードを公開しました。このメソッドは、Worksheet のインスタンスを受け入れて、指定された Worksheet に関連付けられたすべての VBA モジュールを削除できるようになりました。

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.getVbaProject().getModules();

//Remove the VBA modules from specific Worksheet

modules.remove(workbook.getWorksheets().get(0));

{{< /highlight >}}
### **メソッド RangeCollection.add が追加されました**
Aspose.Cells for Java 8.6.1 は、Range オブジェクトを特定のワークシートの範囲のコレクションに追加するために使用できる RangeCollection.Add メソッドを公開しました。

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.getWorksheets().get(0).getCells();

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.getRanges();

//Add another range to the collection

ranges.add(cells.createRange("A1:B4"));

{{< /highlight >}}
### **メソッド Cell.setCharacters を追加**
Cell.setCharacters メソッドを使用して、[リッチ テキストの部分を更新する](/cells/ja/java/access-and-update-the-portions-of-rich-text-of-cell/)特定の Cell オブジェクトの。 Cell.getCharacters メソッドを使用してテキストの一部にアクセスし、Cell.setCharacters メソッドを使用して修正を行うことができますが、**得る**メソッドは、フォント名、フォントの色、太さなどのさまざまなプロパティを設定するために操作できる FontSetting オブジェクトの配列を返します。**セットする**メソッドを使用して変更を適用できます。

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cells containing the Rich Text

Cell cell = worksheet.getCells().get("A1");

//Retrieve the array of FontSetting from the cell

FontSetting[]settings = cell.getCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].getFont().setName("Arial");

//Set the updated FontSetting

cell.setCharacters(settings);

{{< /highlight >}}
### **プロパティ VbaProject.isSigned が追加されました**
Aspose.Cells for Java 8.6.1 で使用できる VbaProject.isSigned プロパティが公開されました。[ワークブック内の VbaProject が署名されているかどうかをテストします](/cells/ja/java/check-if-vba-project-in-a-workbook-is-signed/).プロジェクトが署名されている場合、ブール型のプロパティは true を返します。

以下は、簡単な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VbaProject from the Workbook

VbaProject project = workbook.getVbaProject();

//Test if VbaProject is signed

if (project.isSigned())

{

    System.out.println("VBA Project is Signed");

}

else

{

	System.out.println("VBA Project is not Signed");

}

{{< /highlight >}}
## **変更された API**
### **メソッド Cell.getFormatConditions の変更**
v8.6.1 のリリースにより、Aspose.Cells for Java API は Cell.getFormatConditions メソッドの戻り値の型を変更し、FormatConditionCollection 型の配列を返すようになりました。
## **廃止された API**
### **メソッド Workbook.checkWriteProtectedPassword 廃止されました**
v8.6.1 のリリースにより、Workbook.checkWriteProtectedPassword メソッドは非推奨とマークされました。 WorkbookSettings.WriteProtection.validatePassword メソッドを使用することをお勧めします。このメソッドは、パラメーターとして文字列値を受け入れ、パスワードがスプレッドシートの事前設定パスワードと一致する場合はブール値を返します。
