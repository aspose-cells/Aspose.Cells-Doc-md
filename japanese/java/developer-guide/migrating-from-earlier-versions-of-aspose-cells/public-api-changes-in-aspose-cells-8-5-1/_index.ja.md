---
title: パブリック API Aspose.Cells 8.5.1 の変更点
type: docs
weight: 180
url: /ja/java/public-api-changes-in-aspose-cells-8-5-1/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.5.0 から 8.5.1 への Aspose.Cells API への変更について説明します。新規および更新された public メソッドだけでなく、[クラス追加など](/cells/ja/java/public-api-changes-in-aspose-cells-8-5-1/)だけでなく、Aspose.Cells の舞台裏での動作の変更についても説明します。

{{% /alert %}} 
## **追加された API**
### **メソッド Workbook.Dispose が追加されました**
Aspose.Cells for Java 8.5.1 では、Workbook オブジェクトのアンマネージ リソースを解放する Workbook.dispose メソッドが公開されました。 Dispose パターンは、ファイルおよびパイプ ハンドル、レジストリ ハンドル、待機ハンドル、アンマネージ メモリのブロックへのポインターなど、アンマネージ リソースにアクセスするオブジェクトに対してのみ使用されます。これは、ガベージ コレクターが未使用の管理対象オブジェクトを効率的に再利用できるが、管理されていないオブジェクトを再利用できないためです。

**Java**

{{< highlight "csharp" >}}

 //Create workbook object

Workbook book = new Workbook();

//Call dispose method

book.dispose();

{{< /highlight >}}
### **メソッド Cell.getHeightOfValue を追加**
Aspose.Cells for Java 8.5.1 では、セル値の高さを取得する Cell.getHeightOfValue メソッドが公開されました。このメソッドを使用すると、セル値の高さを計算し、そのセルの行の高さをそれぞれ設定できます。の詳細記事をチェック[セルの高さと幅を計算する方法](/cells/ja/java/calculate-the-width-and-height-of-the-cell-value-in-unit-of-pixels/).
### **列挙 TableDataSourceType が追加されました**
Aspose.Cells for Java 8.5.1 では、列挙 com.aspose.cells.TableDataSourceType を公開して、ListObject のデータ ソース タイプを取得しました。次のフィールドとしての TableDataSourceType 列挙。

1. TableDataSourceType.QUERY_TABLE
1. TableDataSourceType.SHARE_POINT
1. TableDataSourceType.WORKSHEET
1. TableDataSourceType.XML
### **プロパティ ListObject.DataSourceType が追加されました**
v8.5.1 のリリースにより、Aspose.Cells API は、ListObject のデータ ソース タイプを検出するために使用できる読み取り専用の ListObject.DataSourceType プロパティを公開しました。

これが最も単純な使用シナリオです。

**Java**

{{< highlight "csharp" >}}

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
