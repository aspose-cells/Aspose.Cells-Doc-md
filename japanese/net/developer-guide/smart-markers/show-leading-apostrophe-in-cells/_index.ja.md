---
title: セル内の先頭のアポストロフィの表示
type: docs
weight: 70
url: /ja/net/show-leading-apostrophe-in-cells/
---

Microsoft Excel では、セルの値の先頭にあるアポストロフィは非表示になります。Aspose.Cells では、デフォルトでアポストロフィを表示する機能が提供されます。これには、API が [Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) プロパティを提供しています。このプロパティは、シングルクオートで始まる文字列値をセルに入力する際に、[QuotePrefix](https://reference.aspose.com/cells/net/aspose.cells/style/properties/quoteprefix) プロパティを設定するかどうかを示します。[Workbook.Settings.QuotePrefixToStyle](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/quoteprefixtostyle) プロパティを **false** に設定すると、出力Excelファイルに先頭のアポストロフィが表示されます。

次のスクリーンショットは、先頭のアポストロフィが表示される出力Excelファイルを示しています。

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

このコードスニペットでは、ソースExcelファイルにSmart Markersでデータを追加しています。ソースファイルと出力ファイルは参照のために添付されています。

[ソースファイル](98107425.xlsx)

[出力ファイル](98107426.xlsx)
## **サンプルコード**
{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-1.cs" >}}

*DataObject* クラスの実装は以下のとおりです

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Workbook-AllowLeadingApostrophe-2.cs" >}}
{{< app/cells/assistant language="csharp" >}}
