---
title: Aspose.Cells 8.6.1 での Public API 変更
type: docs
weight: 210
url: /ja/java/public-api-changes-in-aspose-cells-8-6-1/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cells API のバージョン 8.6.0 から 8.6.1 への変更点について説明しており、モジュール/アプリケーション開発者に興味を持たれるかもしれません。追加されたクラスなどだけでなく、Aspose.Cells の内部動作の変更についても説明しています。

{{% /alert %}} 
## **APIの追加**
### **HTML リンクターゲットタイプのサポート**
このリリースの Aspose.Cells for Java API では、新しい列挙型である HtmlLinkTargetType と HtmlSaveOptions.LinkTargetType という新しいプロパティが公開され、スプレッドシートを HTML 形式に変換する際のリンクのターゲットタイプを[設定することができます](/cells/ja/java/change-the-html-link-target-type/)。HtmlLinkTargetType 列挙型の可能な値は、デフォルト値が SELF である次のようになります。

1. HtmlLinkTargetType.BLANK: リンクされたドキュメント/ページを新しいウィンドウまたはタブで開きます。
1. HtmlLinkTargetType.PARENT: リンクされたドキュメント/ページを親フレームで開きます。
1. HtmlLinkTargetType.SELF: リンクがクリックされたフレームでリンクされたドキュメント/ページを開きます。
1. HtmlLinkTargetType.TOP: リンクされたドキュメント/ページをウィンドウの全体で開きます。

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Create an instance of HtmlSaveOptions

HtmlSaveOptions options = new HtmlSaveOptions();

//Set the LinkTargetType property to appropriate value

options.setLinkTargetType(HtmlLinkTargetType.BLANK);


//Convert the spreadsheet to HTML with preset HtmlSaveOptions

workbook.save(outputFilePath, options);

{{< /highlight >}}
### **VbaModuleCollection.remove メソッドが追加されました**
Aspose.Cells for Java 8.6.1 では、VbaModuleCollection.remove メソッドのオーバーロードが追加され、指定された Worksheet に関連付けられたすべての VBA モジュールを削除するために、Worksheet のインスタンスを受け入れることができるようになりました。

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the VBA modules from the Workbook

VbaModuleCollection modules = workbook.getVbaProject().getModules();

//Remove the VBA modules from specific Worksheet

modules.remove(workbook.getWorksheets().get(0));

{{< /highlight >}}
### **RangeCollection.add メソッドが追加されました**
Aspose.Cells for Java 8.6.1 では、RangeCollection.Add メソッドが公開され、特定の Worksheet の範囲コレクションに Range オブジェクトを追加するために使用できます。

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Retrieve the Cells of the first worksheet in the workbook

Cells cells = workbook.getWorksheets().get(0).getCells();

//Retrieve the range collection from first worksheet of the Workbook

RangeCollection ranges = cells.getRanges();

//Add another range to the collection

ranges.add(cells.createRange("A1:B4"));

{{< /highlight >}}
### **Cell.setCharactersメソッドの追加**
Cell.setCharactersメソッドは、指定されたCellオブジェクトのリッチテキストの一部を更新するために使用できます。Cell.getCharactersメソッドはテキストの部分にアクセスするために使用され、その後Cell.setCharactersメソッドを使用して変更を行うことができます。**get**メソッドは、フォント名、フォントカラー、太字などのさまざまなプロパティを設定するために操作できるFontSettingオブジェクトの配列を返します。**set**メソッドは、変更を適用するために使用できます。

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Load a spreadsheet

Workbook workbook = new Workbook(inputFilePath);

//Access first worksheet of the workbook

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access the cells containing the Rich Text

Cell cell = worksheet.getCells().get("A1");

//Retrieve the array of FontSetting from the cell

FontSetting[] settings = cell.getCharacters();

//Modify the Font Name for the first FontSetting 

settings[0].getFont().setName("Arial");

//Set the updated FontSetting

cell.setCharacters(settings);

{{< /highlight >}}
### **VbaProject.isSignedプロパティの追加**
Aspose.Cells for Java 8.6.1では、VbaProject.isSignedプロパティが公開されました。これを使用してWorkbook内のVbaProjectが署名されているかどうかをテストすることができます。

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

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
## **APIの変更**
### **Cell.getFormatConditionsメソッドの変更**
v8.6.1のリリースに伴い、Aspose.Cells for Java APIはCell.getFormatConditionsメソッドの戻り値の型を変更し、現在はFormatConditionCollectionの配列を返します。
## **非推奨API**
### **Workbook.checkWriteProtectedPasswordメソッドの非推奨化**
v8.6.1のリリースに伴い、Workbook.checkWriteProtectedPasswordメソッドは非推奨となりました。スプレッドシートの事前設定されたパスワードに一致する場合、WorkbookSettings.WriteProtection.validatePasswordメソッドを使用することが推奨されます。
