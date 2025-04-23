---
title: Aspose.Cells 8.8.0でのパブリックAPIの変更
type: docs
weight: 270
url: /ja/java/public-api-changes-in-aspose-cells-8-8-0/
---

{{% alert color="primary" %}} 

このドキュメントは、バージョン8.7.2から8.8.0へのAspose.Cells APIの変更についてで、モジュール/アプリケーション開発者に関心があるかもしれないものです。新しいおよび更新されたパブリックメソッドだけでなく、追加されたものや削除されたクラスなども含まれますが、Aspose.Cellsの背後での挙動の変更の説明も含まれています。

{{% /alert %}} 
## **APIの追加**
### **外部接続のセル参照を取得する**
Aspose.Cells for Java 8.8.0では、スプレッドシートに格納されている外部接続の対象と出力のセル参照を取得するのに役立つ新しいプロパティが公開されています。 

1. QueryTable.ConnectionId: クエリテーブルの接続IDを取得します。
1. ExternalConnection.Id: 外部接続のIDを取得します。
1. ListObject.QueryTable: リンクされたQueryTableを取得します。

{{% alert color="primary" %}} 

この機能の詳細については、[外部データ接続に関連するクエリテーブルとリストオブジェクトの検索](/cells/ja/java/find-query-tables-and-list-objects-related-to-external-data-connections/)の詳細な記事を参照してください

{{% /alert %}} 
### **HTMLLoadOptions.KeepPrecisionプロパティを追加しました**
Aspose.Cells for Java 8.8.0では、HTMLファイルをインポートする際に長い数値値を指数表記に変換するかどうかを制御するために、HTMLLoadOptions.KeepPrecisionプロパティが追加されました。デフォルトでは、15桁を超える値は、HTML文字列またはファイルからデータがインポートされる場合には指数表記に変換されます。しかし、今後は、ユーザーはHTMLLoadOptions.KeepPrecisionプロパティの助けを借りてこの挙動を制御できます。該当のプロパティがtrueに設定されている場合、値は元のままインポートされます。

{{% alert color="primary" %}} 

この機能の詳細については、[大きな数値値を指数表記に変換しない](/cells/ja/java/avoid-exponential-notation-of-large-numbers-while-importing-from/)の詳細な記事を参照してください

{{% /alert %}} 

以下はシンプルな使用シナリオです。

**Java**

{{< highlight csharp >}}

 //Sample Html containing large number with digits greater than 15

String html = "<html>"

		+ "<body>"

		+ "<p>1234567890123456</p>"

		+ "</body>"

		+ "</html>";

//Convert Html to byte array

byte[] byteArray = html.getBytes();

//Set Html load options and keep precision true

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

loadOptions.setKeepPrecision(true);

//Convert byte array into stream

java.io.ByteArrayInputStream stream = new java.io.ByteArrayInputStream(byteArray);

//Create workbook from stream with Html load options

Workbook workbook = new Workbook(stream, loadOptions);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Auto fit the sheet columns

worksheet.autoFitColumns();

//Save the workbook

workbook.save(dataDir + "output.xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **HTMLLoadOptions.DeleteRedundantSpacesプロパティを追加しました**
Aspose.Cells for Java 8.8.0 has exposed the HTMLLoadOptions.DeleteRedundantSpaces property in order to keep or delete the extra spaces after the line break tag (<br> Tag) while importing the data from the HTML string or file. The HTMLLoadOptions.DeleteRedundantSpaces property has the default value as false that means, all extra spaces will be preserved and imported to the Workbook object, however, when set to true, the API will delete all the redundant spaces coming after the line break tag.

{{% alert color="primary" %}} 

この機能の詳細については、[HTMLから不要なスペースを削除](/cells/ja/java/delete-redundant-spaces-after-line-break-while-importing/)の詳細な記事を参照してください

{{% /alert %}} 

シンプルな使用シナリオは次のようになります。 

**Java**

{{< highlight csharp >}}

 //Sample Html containing redundant spaces after <br> tag

String html = "<html>"

		+ "<body>"

			+ "<table>"

				+ "<tr>"

					+ "<td>"

						+ "<br>    This is sample data"

						+ "<br>    This is sample data"

						+ "<br>    This is sample data"

					+ "</td>"

				+ "</tr>"

			+ "</table>"

		+ "</body>"

	+ "</html>";

//Convert Html to byte array

byte[] byteArray = html.getBytes();

//Set Html load options and keep precision true

HTMLLoadOptions loadOptions = new HTMLLoadOptions(LoadFormat.HTML);

loadOptions.setDeleteRedundantSpaces(true);

//Convert byte array into stream

java.io.ByteArrayInputStream stream = new java.io.ByteArrayInputStream(byteArray);

//Create workbook from stream with Html load options

Workbook workbook = new Workbook(stream, loadOptions);

//Access first worksheet

Worksheet worksheet = workbook.getWorksheets().get(0);

//Auto fit the sheet columns

worksheet.autoFitColumns();

//Save the workbook

workbook.save(dataDir + "output-" + loadOptions.getDeleteRedundantSpaces() + ".xlsx", SaveFormat.XLSX);

{{< /highlight >}}
### **Style.QuotePrefixプロパティを追加しました**
Aspose.Cells for Java 8.8.0では、Style.QuotePrefixプロパティが公開され、セルの値がシングルクォート記号で始まるかどうかを検出するためのものです。 

{{% alert color="primary" %}} 

この機能の詳細については、[セルの値がシングルクォート記号で始まるかどうかを検出](/cells/ja/java/find-if-the-cell-value-starts-with-single-quote-mark/)の詳細な記事を参照してください

{{% /alert %}} 

シンプルな使用シナリオは次のようになります。 

**Java**

{{< highlight csharp >}}

 //Create an instance of workbook

Workbook workbook = new Workbook();

//Access first worksheet from the collection

Worksheet worksheet = workbook.getWorksheets().get(0);

//Access cells A1 and A2

Cell a1 = worksheet.getCells().get("A1");

Cell a2 = worksheet.getCells().get("A2");

//Add simple text to cell A1 and text with quote prefix to cell A2

a1.putValue("sample");

a2.putValue("'sample");

//Print their string values, A1 and A2 both are same

System.out.println("String value of A1: " + a1.getStringValue());

System.out.println("String value of A2: " + a2.getStringValue());

//Access styles of cells A1 and A2

Style s1 = a1.getStyle();

Style s2 = a2.getStyle();

System.out.println();

//Check if A1 and A2 has a quote prefix

System.out.println("A1 has a quote prefix: " + s1.getQuotePrefix());

System.out.println("A2 has a quote prefix: " + s2.getQuotePrefix());

{{< /highlight >}}
## **非推奨API**
### **LoadOptions.ConvertNumericDataプロパティが非推奨になりました**
Aspose.Cells 8.8.0では、LoadOptions.ConvertNumericDataプロパティが非推奨となりました。HTMLLoadOptionsやTxtLoadOptionsクラスから対応するプロパティを使用してください。
{{< app/cells/assistant language="java" >}}
