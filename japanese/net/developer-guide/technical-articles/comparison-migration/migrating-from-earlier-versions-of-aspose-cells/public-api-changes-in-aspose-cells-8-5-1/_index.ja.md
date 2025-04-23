---
title: Aspose.Cells 8.5.1 での Public API 変更
type: docs
weight: 170
url: /ja/net/public-api-changes-in-aspose-cells-8-5-1/
---

{{% alert color="primary" %}} 

このドキュメントでは、Aspose.Cells API のバージョン8.5.0から8.5.1への変更点を、モジュール/アプリケーション開発者の興味を引く可能性があるものとして記載しています。新しく追加されたメソッドやクラスなどに加えて、[変更された動作の説明](/cells/ja/net/public-api-changes-in-aspose-cells-8-5-1/)も含まれています。

{{% /alert %}} 
## **APIの追加**
### **Workbook.Disposeメソッドを追加**
Workbook オブジェクトは現在 System.IDisposable インターフェースを実装しており、単一の Dispose メソッドを持っています。直接 Workbook.Dispose メソッドを呼び出すか、Using構造体内で Workbook オブジェクトを作成して、このメソッドを自動的に呼び出すことができます。

**C#**

{{< highlight csharp >}}

 //Create workbook object

Workbook book = new Workbook();

//Call Dispose method

book.Dispose();

//Call Dispose method via Using statement

using (Workbook book = new Workbook())

{

    //do processing

}

{{< /highlight >}}


### **Cell.GetHeightOfValue メソッドが追加されました**
Aspose.Cells for .NET 8.5.1 で Cell.GetHeightOfValue メソッドが公開されました。このメソッドを使用することで、セル値の高さを算出し、そのセルの行の高さを設定することができます。詳細については、[セルの高さと幅を計算する方法](/cells/ja/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/)の記事をご確認ください。
### **TableDataSourceType 列挙型が追加されました**
Aspose.Cells for .NET 8.5.1 は Aspose.Cells.Tables.TableDataSourceType の列挙を公開して、ListObject のデータソースタイプを取得するために使用できます。

1. TableDataSourceType.QueryTable
1. TableDataSourceType.SharePoint
1. TableDataSourceType.Worksheet
1. TableDataSourceType.XML
### **ListObject.DataSourceTypeプロパティを追加**
v8.5.1のリリースに伴い、Aspose.Cells APIは読み取り専用のListObject.DataSourceTypeプロパティを公開しました。このプロパティを使用して、ListObjectのデータソースタイプを検出することができます。

以下は最もシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

 Workbook book = new Workbook("D:/book1.xlsx");

Worksheet sheet = book.Worksheets[0];

ListObject listObject = sheet.ListObjects[0];

if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.QueryTable)

{

    Console.WriteLine("Data Source Type is Query Table");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.SharePoint)

{

    Console.WriteLine("Data Source Type is SharePoint Linked List");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.Worksheet)

{

    Console.WriteLine("Data Source Type is Excel Worksheet Table");

}

else if (listObject.DataSourceType == Aspose.Cells.Tables.TableDataSourceType.XML)

{

    Console.WriteLine("Data Source Type is XML");

}

{{< /highlight >}}
{{< app/cells/assistant language="csharp" >}}
