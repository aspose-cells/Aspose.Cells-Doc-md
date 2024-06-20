---
title: Aspose.Cells 8.8.2の公開API変更
type: docs
weight: 280
url: /ja/net/public-api-changes-in-aspose-cells-8-8-2/
---

{{% alert color="primary" %}} 

このドキュメントには、Aspose.Cells APIの8.8.1から8.8.2への変更についての詳細が記載されており、モジュール/アプリケーション開発者に興味を持つものが含まれます。新しいおよび更新された公開メソッド、追加、削除されたクラスなどだけでなく、Aspose.Cellsの裏側の挙動の変更の説明も含まれます。

{{% /alert %}} 
## **APIの追加**
### **空白の行と列を削除する際に参照を自動的に更新**
Aspose.Cells for .NET 8.8.2では、Cells.DeleteBlankRowsおよびCells.DeleteBlankColumnsメソッドのオーバーロードバージョンが公開されました. 新しいメソッドはDeleteOptionsクラスのインスタンスを受け入れ、数式、チャートシリーズデータなどに起因する破損参照の状況を克服するために使用できます. 現在、DeleteOptionsクラスにはUpdateReferenceという名前のBoolean型プロパティのみがあります. 上記のプロパティがtrueに設定されており、DeleteOptionsクラスのインスタンスがCells.DeleteBlankRowsおよびCells.DeleteBlankColumnsメソッドに渡されると、APIは内部的に数式の参照を調整します（あれば）

{{% alert color="primary" %}} 

この機能の詳細については、[空白の行と列を削除しながら他のワークシートで更新された参照を削除](/cells/ja/net/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)の詳細な記事を参照してください

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

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
