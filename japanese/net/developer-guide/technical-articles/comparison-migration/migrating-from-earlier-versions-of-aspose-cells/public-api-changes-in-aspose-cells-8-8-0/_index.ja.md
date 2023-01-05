---
title: パブリック API Aspose.Cells 8.8.0 の変更点
type: docs
weight: 260
url: /ja/net/public-api-changes-in-aspose-cells-8-8-0/
---
{{% alert color="primary" %}} 

このドキュメントでは、モジュール/アプリケーション開発者にとって興味深い、バージョン 8.7.2 から 8.8.0 への Aspose.Cells API への変更について説明します。新規および更新されたパブリック メソッド、追加および削除されたクラスなどだけでなく、Aspose.Cells の舞台裏での動作の変更の説明も含まれています。

{{% /alert %}} 
## **追加された API**
### **外部接続用の Cell リファレンスを取得する**
Aspose.Cells for .NET 8.8.0 では、スプレッドシートに保存されている外部接続のターゲットおよび出力セル参照を取得するのに役立つ次の新しいプロパティが公開されています。

1. QueryTable.ConnectionId: クエリ テーブルの接続 ID を取得します。
1. ExternalConnection.Id: 外部接続の ID を取得します。
1. ListObject.QueryTable: リンクされた QueryTable を取得します。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[外部データ接続に関連するクエリ テーブルとリスト オブジェクトを検索する](/cells/ja/net/find-query-tables-and-list-objects-related-to-external-data-connections/)

{{% /alert %}} 
### **HTMLLoadOptions.KeepPrecision プロパティを追加**
Aspose.Cells for .NET 8.8.0 では、HTML ファイルのインポート中に長い数値を指数表記に変換することを制御するために、HTMLLoadOptions.KeepPrecision プロパティが追加されました。デフォルトでは、データが HTML 文字列またはファイルからインポートされている場合、15 桁を超える値は指数表記に変換されます。ただし、ユーザーは HTMLLoadOptions.KeepPrecision プロパティを使用してこの動作を制御できるようになりました。上記のプロパティが true に設定されている場合、値はソースにあるとおりにインポートされます。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[大きな数値の指数表記への変換を避ける](/cells/ja/net/avoid-exponential-notation-of-large-numbers-while-importing-from/)

{{% /alert %}} 

以下は、簡単な使用シナリオです。

**C#**

{{< highlight "csharp" >}}

 string html = @" 

<table data-cache=""not-cached"" class=""sortable""> 

   <tbody> 

    <tr> 

     <td class=""even"">9999999999999999</td> 

     <td class=""odd"">10.8%</td> 

    </tr> 

   </tbody> 

</table> 

";

byte[]byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.KeepPrecision = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

Worksheet sheet = workbook.Worksheets[0];

sheet.AutoFitColumns();

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **HTMLLoadOptions.DeleteRedundantSpaces プロパティを追加**
Aspose.Cells for .NET 8.8.0 では、改行タグ (<br>タグ) HTML 文字列またはファイルからデータをインポートするとき。 HTMLLoadOptions.DeleteRedundantSpaces プロパティのデフォルト値は false です。つまり、すべての余分なスペースが保持され、Workbook オブジェクトにインポートされます。ただし、true に設定すると、API は、改行タグの後にある余分なスペースをすべて削除します。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[HTML から余分なスペースを削除](/cells/ja/net/delete-redundant-spaces-after-line-break-while-importing/)

{{% /alert %}} 

簡単な使用シナリオは次のようになります。

**C#**

{{< highlight "csharp" >}}

 string html = @" 

<html>

    <body>

        <table>

            <tr>

                <td>

                    <br>    This is sample data 

                    <br>    This is sample data

                    <br>    This is sample data

                </td>

            </tr>

        </table>

    </body>

</html>

";

byte[]byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.DeleteRedundantSpaces = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Style.QuotePrefix プロパティを追加**
Aspose.Cells for .NET 8.8.0 では、セル値が一重引用符で始まるかどうかを検出するために Style.QuotePrefix プロパティが公開されました。

{{% alert color="primary" %}} 

この機能の詳細については、次の詳細記事を参照してください。[Cell 値の先頭にある単一引用符を検出する](/cells/ja/net/find-if-the-cell-value-starts-with-single-quote-mark/)

{{% /alert %}} 

簡単な使用シナリオは次のようになります。

**C#**

{{< highlight "csharp" >}}

 Workbook book = new Workbook();

Worksheet sheet = book.Worksheets[0];

Cell a1 = sheet.Cells["A1"];

Cell a2 = sheet.Cells["A2"];

a1.PutValue("sample");

a2.PutValue("'sample");

Console.WriteLine("String value of A1: " + a1.StringValue);

Console.WriteLine("String value of A2: " + a2.StringValue);

Style s1 = a1.GetStyle();

Style s2 = a2.GetStyle();

Console.WriteLine("A1 has a quote prefix: " + s1.QuotePrefix);

Console.WriteLine("A2 has a quote prefix: " + s2.QuotePrefix);

{{< /highlight >}}
## **廃止された API**
### **廃止された LoadOptions.ConvertNumericData プロパティ**
Aspose.Cells 8.8.0 では、LoadOptions.ConvertNumericData プロパティが廃止されました。 HTMLLoadOptions または TxtLoadOptions クラスの対応するプロパティを使用してください。
