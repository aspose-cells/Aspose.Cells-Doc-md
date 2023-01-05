---
title: パブリック API Aspose.Cells の変更点 8.8.2
type: docs
weight: 280
url: /ja/net/public-api-changes-in-aspose-cells-8-8-2/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.8.1 から 8.8.2 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **空白の行と列を削除しながら参照を自動的に更新する**
Aspose.Cells for .NET 8.8.2 は、Cells.DeleteBlankRows および Cells.DeleteBlankColumns メソッドのオーバーロードされたバージョンを公開しました。新しいメソッドは、DeleteOptions クラスのインスタンスを受け入れることができ、数式、チャート シリーズ データなどの壊れた参照が原因で発生する可能性がある状況を克服するために使用できます。現在、DeleteOptions クラスには、UpdateReference という名前のブール型のプロパティである 1 つのメンバーしかありません。上記のプロパティが true に設定され、DeleteOptions クラスのインスタンスが Cells.DeleteBlankRows & Cells.DeleteBlankColumns メソッドに渡された場合、API は変更に対応するために数式参照 (存在する場合) を内部的に調整します。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[更新された参照で空白の行と列を削除する](/cells/ja/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/).

{{% /alert %}} 

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 //Create an instance of Workbook & load an existing spreadsheet

var book = new Workbook(dir + "sample.xlsx");

//Access worksheet from which blank rows/columns have to be deleted

var sheet = book.Worksheets[0];

//Access cells of the desired worksheet

var cells = sheet.Cells;

//Create an instance of DeleteOptions class

DeleteOptions options = new DeleteOptions();

//Set UpdateReference property to true;

options.UpdateReference = true;

//Delete all blank rows and columns

cells.DeleteBlankColumns(options);

cells.DeleteBlankRows(options);

{{< /highlight >}}
