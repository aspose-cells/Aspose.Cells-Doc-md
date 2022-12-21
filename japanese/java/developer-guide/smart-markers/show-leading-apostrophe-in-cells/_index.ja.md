---
title: セルの先頭のアポストロフィを表示する
type: docs
weight: 20
url: /ja/java/show-leading-apostrophe-in-cells/
---
## **セルの先頭のアポストロフィを表示する**

Microsoft Excel では、セルの値の先頭のアポストロフィが非表示になっています。 Aspose.Cells は、デフォルトでアポストロフィを表示する機能を提供します。このために、API が提供します。[**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)財産。このプロパティは、[**QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/Style#QuotePrefix)単一引用符で始まる文字列値をセルに入力するときのプロパティ。の設定[**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)プロパティへ**間違い**出力Excelファイルに先頭のアポストロフィが表示されます。

次のスクリーンショットは、アポストロフィが表示された出力 Excel ファイルを示しています。

![todo:画像_代替_文章](show-leading-apostrophe-in-cells_1.jpg)

次のコード スニペットは、ソースの Excel ファイルにスマート マーカーを使用してデータを追加することで、これを示しています。参照用にソースと出力の Excel ファイルが添付されています。

[ソースファイル](AllowLeadingApostropheSample.xlsx)

[出力ファイル](AllowLeadingApostropheSample_out.xlsx)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AllowLeadingApostrophe-1.java" >}}

の実装*データオブジェクト*クラスは以下に与えられます

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HelperClasses-DataObject-1.java" >}}
