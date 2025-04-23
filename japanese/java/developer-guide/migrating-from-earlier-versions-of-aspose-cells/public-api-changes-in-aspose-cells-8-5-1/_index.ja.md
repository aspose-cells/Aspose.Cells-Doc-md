---
title: Aspose.Cells 8.5.1 での Public API 変更
type: docs
weight: 180
url: /ja/java/public-api-changes-in-aspose-cells-8-5-1/
---

{{% alert color="primary" %}} 

このドキュメントには、バージョン8.5.0から8.5.1へのAspose.Cells APIの変更が含まれており、モジュール/アプリケーション開発者に興味を持たれる可能性があるものです。新しいメソッドや更新されたpublicメソッド,[追加されたクラスなど](/cells/ja/java/public-api-changes-in-aspose-cells-8-5-1/)だけでなく、Aspose.Cellsの背後での挙動に変更がある場合についての説明も含まれています。

{{% /alert %}} 
## **APIの追加**
### **Workbook.Disposeメソッドを追加**
Aspose.Cells for Java 8.5.1では、Workbook.disposeメソッドを公開し、Workbookオブジェクトのアンマネージリソースを解放するようになりました。アンマネージリソースにアクセスするオブジェクトにのみdisposeパターンが使用されます。このようなオブジェクトには、ファイルやパイプハンドル、レジストリハンドル、ウェイトハンドル、またはアンマネージメモリブロックへのポインタなど、アンマネージリソースにアクセスするオブジェクトが含まれます。これは、ガベージコレクタが未使用の管理されたオブジェクトを効率的に回収できるが、アンマネージされたオブジェクトを回収できないためです。

**Java**

{{< highlight csharp >}}

 //Create workbook object

Workbook book = new Workbook();

//Call dispose method

book.dispose();

{{< /highlight >}}
### **Cell.getHeightOfValueメソッドを追加**
Aspose.Cells for Java 8.5.1では、Cell.getHeightOfValueメソッドを公開し、セル値の高さを取得するようになりました。このメソッドを使用することで、セル値の高さを計算し、そのセルの行の高さを設定することができます。詳細については、[セルの高さと幅を計算する方法](/cells/ja/java/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)の詳細な記事をご覧ください。
### **Enumeration TableDataSourceTypeを追加**
Aspose.Cells for Java 8.5.1では、ListObjectのデータソースタイプを取得するための列挙型com .aspose.cells.TableDataSourceTypeを公開しました。TableDataSourceType列挙型には以下のフィールドが含まれています。 

1. TableDataSourceType.QUERY_TABLE
1. TableDataSourceType.SHARE_POINT
1. TableDataSourceType.WORKSHEET
1. TableDataSourceType.XML
### **ListObject.DataSourceTypeプロパティを追加**
v8.5.1のリリースに伴い、Aspose.Cells APIは読み取り専用のListObject.DataSourceTypeプロパティを公開しました。このプロパティを使用して、ListObjectのデータソースタイプを検出することができます。

以下は最もシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 Workbook book = new Workbook("D:/book1.xlsx");

Worksheet sheet = book.getWorksheets().get(0);

ListObject listObject = sheet.getListObjects().get(0);

if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.QUERY_TABLE)

{

	System.out.println("Data Source Type is Query Table");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.SHARE_POINT)

{

	System.out.println("Data Source Type is SharePoint Linked List");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.WORKSHEET)

{

	System.out.println("Data Source Type is Excel Worksheet Table");

}

else if (listObject.getDataSourceType() == com.aspose.cells.TableDataSourceType.XML)

{

	System.out.println("Data Source Type is XML");

}

{{< /highlight >}}
{{< app/cells/assistant language="java" >}}
