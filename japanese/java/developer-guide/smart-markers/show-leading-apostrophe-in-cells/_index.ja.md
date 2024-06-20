---
title: セル内の先頭のアポストロフィの表示
type: docs
weight: 20
url: /ja/java/show-leading-apostrophe-in-cells/
---

## **セル内の先頭アポストロフィを表示する**

Microsoft Excelでは、セルの値の先頭にあるアポストロフィは非表示になります。Aspose.Cellsは、デフォルトでアポストロフィを表示する機能を提供しています。これにより、APIが[**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)プロパティを提供します。このプロパティは、セルの先頭にシングルクオートで始まる文字列値を入力する際に[**QuotePrefix**](https://reference.aspose.com/cells/java/com.aspose.cells/Style#QuotePrefix)プロパティを設定するかどうかを示します。[**Workbook.Settings.QuotePrefixToStyle**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#QuotePrefixToStyle)プロパティを**false**に設定すると、出力されたExcelファイルに先頭のアポストロフィが表示されます。

次のスクリーンショットは、先頭のアポストロフィが表示される出力Excelファイルを示しています。

![todo:image_alt_text](show-leading-apostrophe-in-cells_1.jpg)

このコードスニペットでは、ソースExcelファイルにSmart Markersでデータを追加しています。ソースファイルと出力ファイルは参照のために添付されています。

[ソースファイル](AllowLeadingApostropheSample.xlsx)

[出力ファイル](AllowLeadingApostropheSample_out.xlsx)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-Workbook-AllowLeadingApostrophe-1.java" >}}

*DataObject* クラスの実装は以下のとおりです

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-HelperClasses-DataObject-1.java" >}}
