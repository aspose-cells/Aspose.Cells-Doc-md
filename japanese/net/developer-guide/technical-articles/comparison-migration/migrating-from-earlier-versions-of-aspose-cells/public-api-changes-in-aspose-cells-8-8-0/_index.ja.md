---
title: Aspose.Cells 8.8.0でのパブリックAPIの変更
type: docs
weight: 260
url: /ja/net/public-api-changes-in-aspose-cells-8-8-0/
---

{{% alert color="primary" %}} 

このドキュメントは、バージョン8.7.2から8.8.0へのAspose.Cells APIの変更についてで、モジュール/アプリケーション開発者に関心があるかもしれないものです。新しいおよび更新されたパブリックメソッドだけでなく、追加されたものや削除されたクラスなども含まれますが、Aspose.Cellsの背後での挙動の変更の説明も含まれています。

{{% /alert %}} 
## **APIの追加**
### **外部接続のセル参照を取得する**
Aspose.Cells for .NET 8.8.0では、スプレッドシートに保存されている外部接続の対象セル参照および出力セル参照を取得するのに役立つ以下の新しいプロパティが公開されています。

1. QueryTable.ConnectionId: クエリテーブルの接続IDを取得します。
1. ExternalConnection.Id: 外部接続のIDを取得します。
1. ListObject.QueryTable: リンクされたQueryTableを取得します。

{{% alert color="primary" %}} 

この機能の詳細については、[外部データ接続に関連する検索クエリテーブルとリストオブジェクトを見つける](/cells/ja/net/find-query-tables-and-list-objects-related-to-external-data-connections/)の詳細な記事をご覧ください。

{{% /alert %}} 
### **HTMLLoadOptions.KeepPrecisionプロパティを追加しました**
Aspose.Cells for .NET 8.8.0では、HTMLファイルをインポートする際に長い数値を指数表記に変換するかどうかを制御するために、HTMLLoadOptions.KeepPrecisionプロパティが追加されました。デフォルトでは、15桁を超える値はHTML文字列やファイルからインポートされる場合、指数表記に変換されます。しかし、HTMLLoadOptions.KeepPrecisionプロパティを使用することで、この挙動を制御できます。該当するプロパティがtrueに設定されている場合、値は元の状態でインポートされます。

{{% alert color="primary" %}} 

この機能の詳細については、[大きな数値の指数表記を回避](/cells/ja/net/avoid-exponential-notation-of-large-numbers-while-importing-from/)の詳細な記事をご覧ください。

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**C#**

{{< highlight csharp >}}

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

byte[] byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.KeepPrecision = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

Worksheet sheet = workbook.Worksheets[0];

sheet.AutoFitColumns();

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **HTMLLoadOptions.DeleteRedundantSpacesプロパティを追加しました**
Aspose.Cells for .NET 8.8.0 has exposed the HTMLLoadOptions.DeleteRedundantSpaces property in order to keep or delete the extra spaces after the line break tag (<br> Tag) while importing the data from the HTML string or file. The HTMLLoadOptions.DeleteRedundantSpaces property has the default value as false that means, all extra spaces will be preserved and imported to the Workbook object, however, when set to true, the API will delete all the redundant spaces coming after the line break tag.

{{% alert color="primary" %}} 

この機能の詳細については、[HTMLから冗長なスペースを削除](/cells/ja/net/delete-redundant-spaces-after-line-break-while-importing/)の詳細な記事をご覧ください。

{{% /alert %}} 

シンプルな使用シナリオは次のようになります。

**C#**

{{< highlight csharp >}}

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

byte[] byteArray = Encoding.UTF8.GetBytes(html);

HTMLLoadOptions loadOptions = new Aspose.Cells.HTMLLoadOptions(LoadFormat.Html);

loadOptions.DeleteRedundantSpaces = true;

MemoryStream stream = new MemoryStream(byteArray);

Workbook workbook = new Workbook(stream, loadOptions);

workbook.Save(dir + "output.xlsx");

{{< /highlight >}}


### **Style.QuotePrefixプロパティを追加しました**
Aspose.Cells for .NET 8.8.0では、セルの値が一重引用符で始まるかどうかを検出するために、Style.QuotePrefixプロパティが公開されました。

{{% alert color="primary" %}} 

この機能の詳細については、[セルの値が一重引用符で始まるかどうかを検出](/cells/ja/net/find-if-the-cell-value-starts-with-single-quote-mark/)の詳細な記事をご覧ください。

{{% /alert %}} 

シンプルな使用シナリオは次のようになります。

**C#**

{{< highlight csharp >}}

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
## **非推奨API**
### **LoadOptions.ConvertNumericDataプロパティが非推奨になりました**
Aspose.Cells 8.8.0では、LoadOptions.ConvertNumericDataプロパティが非推奨となりました。HTMLLoadOptionsやTxtLoadOptionsクラスから対応するプロパティを使用してください。
{{< app/cells/assistant language="csharp" >}}
