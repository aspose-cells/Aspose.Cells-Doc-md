---
title: セルの先頭のアポストロフィを表示する
type: docs
weight: 70
url: /ja/net/show-leading-apostrophe-in-cells/
---
 Microsoft Excel では、セルの値の先頭のアポストロフィが非表示になっています。 Aspose.Cells は、デフォルトでアポストロフィを表示する機能を提供します。このために、API が提供します。[Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle)財産。このプロパティは、[QuotePrefix](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix)単一引用符で始まる文字列値をセルに入力するときのプロパティ。の設定[Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle)プロパティへ**間違い**出力Excelファイルに先頭のアポストロフィが表示されます。

次のスクリーンショットは、アポストロフィが表示された出力 Excel ファイルを示しています。

![todo:画像_代替_文章](show-leading-apostrophe-in-cells_1.jpg)

次のコード スニペットは、ソースの Excel ファイルにスマート マーカーを使用してデータを追加することで、これを示しています。参照用にソースと出力の Excel ファイルが添付されています。

[ソースファイル](98107425.xlsx)

[出力ファイル](98107426.xlsx)
## **サンプルコード**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-1.cs" >}}

の実装*データオブジェクト*クラスは以下に与えられます

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-2.cs" >}}
