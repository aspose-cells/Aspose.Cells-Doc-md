---
title: Aspose.Cells 8.8.2の公開API変更
type: docs
weight: 290
url: /ja/java/public-api-changes-in-aspose-cells-8-8-2/
---

{{% alert color="primary" %}} 

このドキュメントには、Aspose.Cells APIの8.8.1から8.8.2への変更についての詳細が記載されており、モジュール/アプリケーション開発者に興味を持つものが含まれます。新しいおよび更新された公開メソッド、追加、削除されたクラスなどだけでなく、Aspose.Cellsの裏側の挙動の変更の説明も含まれます。

{{% /alert %}} 
## **APIの追加**
### **空白の行および列を削除するときに参照を自動的に更新する**
Aspose.Cells for Java 8.8.2では、Cells.deleteBlankRowsおよびCells.deleteBlankColumnsのオーバーロードバージョンが公開されました。新しいメソッドはDeleteOptionsクラスのインスタンスを受け入れ、数式、グラフの系列データなどで発生する可能性がある破損した参照に対処するために使用できます。DeleteOptionsクラスには現在UpdateReferenceという名前のBoolean型のプロパティが1つだけあります。言及されたプロパティがtrueに設定され、DeleteOptionsクラスのインスタンスがCells.deleteBlankRowsおよびCells.deleteBlankColumnsメソッドに渡されると、APIは必要に応じて数式の参照を内部的に調整します。 

{{% alert color="primary" %}} 

この機能の詳細については、[空白の行および列を削除する際の更新された参照](/cells/ja/java/update-references-in-other-worksheets-while-deleting-blank-columns-and-rows-in-a-worksheet/)の詳細な記事を参照してください。

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Create an instance of Workbook & load an existing spreadsheet

Workbook book = new Workbook(dir + "sample.xlsx");

//Access worksheet from which blank rows/columns have to be deleted

Worksheet sheet = book.getWorksheets().get(0);

//Access cells of the desired worksheet

Cells cells = sheet.getCells();

//Create an instance of DeleteOptions class

DeleteOptions options = new DeleteOptions();

//Set UpdateReference property to true;

options.setUpdateReference(true);

//Delete all blank rows and columns

cells.deleteBlankColumns(options);

cells.deleteBlankRows(options);

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
