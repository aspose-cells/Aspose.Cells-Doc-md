---
title: パブリック API Aspose.Cells 8.5.1 の変更点
type: docs
weight: 170
url: /ja/net/public-api-changes-in-aspose-cells-8-5-1/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.5.0 から 8.5.1 への Aspose.Cells API への変更について説明します。新規および更新された public メソッドだけでなく、[クラス追加など](/cells/ja/net/public-api-changes-in-aspose-cells-8-5-1/)だけでなく、Aspose.Cells の舞台裏での動作の変更についても説明します。

{{% /alert %}} 
## **追加された API**
### **メソッド Workbook.Dispose が追加されました**
Workbook オブジェクトは、単一の Dispose メソッドを持つ System.IDisposable インターフェイスを実装するようになりました。 Workbook.Dispose メソッドを直接呼び出すか、Using 構造体で Workbook オブジェクトを作成して、このメソッドを自動的に呼び出すことができます。

**C#**

{{< highlight "csharp" >}}

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


### **メソッド Cell.GetHeightOfValue を追加**
Aspose.Cells for .NET 8.5.1 では、セル値の高さを取得する Cell.GetHeightOfValue メソッドが公開されました。このメソッドを使用すると、セル値の高さを計算し、そのセルの行の高さをそれぞれ設定できます。の詳細記事をチェック[セルの高さと幅を計算する方法](/cells/ja/net/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **列挙 TableDataSourceType が追加されました**
Aspose.Cells for .NET 8.5.1 では、列挙型 Aspose.Cells.Tables.TableDataSourceType が公開され、ListObject のデータ ソース タイプが取得されました。次のフィールドとしての TableDataSourceType 列挙。

1. TableDataSourceType.QueryTable
1. TableDataSourceType.SharePoint
1. TableDataSourceType.Worksheet
1. TableDataSourceType.XML
### **プロパティ ListObject.DataSourceType が追加されました**
v8.5.1 のリリースにより、Aspose.Cells API は、ListObject のデータ ソース タイプを検出するために使用できる読み取り専用の ListObject.DataSourceType プロパティを公開しました。

これが最も単純な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

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
