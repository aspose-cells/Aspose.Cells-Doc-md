---
title: ワークブックのカスタム数値の小数点記号とグループ区切り記号を指定する
type: docs
weight: 100
url: /ja/java/specify-custom-number-decimal-and-group-separators-for-workbook/
description: この記事では、Aspose.Cells for Java API.
keywords: specify custom decimal separator excel, specify custom decimal separator excel java, specify custom group separator excel, specify custom group separator excel java, specify custom decimal and group separator excel, specify custom decimal and group separator excel java, change decimal and group separator excel java, change decimal and group separator excel, change decimal separator excel, change decimal separator excel java, change group separator excel, change group separator excel java
---
{{% alert color="primary" %}}

 Microsoft Excel では、システム区切り記号を使用する代わりに、カスタムの小数点記号と桁区切り記号を指定できます。**高度な Excel オプション**下のスクリーンショットに示すように。

Aspose.Cells は[**WorkbookSettings.setNumberDecimalSeparator()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberDecimalSeparator)と[WorkbookSettings.setNumberGroupSeparator()](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#NumberGroupSeparator)プロパティを使用して、数値の書式設定/解析用のカスタム セパレータを設定します。

{{% /alert %}}

## **Microsoft Excel を使用したカスタム セパレータの指定**

1. 開ける**オプション**の中に**ファイル**タブ。
1. 開く**高度**タブ。
1. で設定を変更します。**編集オプション**セクション。

次のスクリーンショットは、**高度な Excel オプション**セクションを強調表示して、**カスタムセパレーター**.

![todo:画像_代替_文章](specify-custom-number-decimal-and-group-separators-for-workbook_1.png)

## **Aspose.Cells を使用したカスタム セパレータの指定**

次のサンプル コードは、Aspose.Cells API を使用してカスタム セパレータを指定する方法を示しています。これは、カスタム数値の小数点とグループ セパレータをそれぞれドットとスペースとして指定しています。だから数**123,456.789**として表示されます**123 456.789**コードによって生成された出力 PDF を示すスクリーンショットに示すように。

![todo:画像_代替_文章](specify-custom-number-decimal-and-group-separators-for-workbook_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SpecifyingCustomSeparators-SpecifyingCustomSeparators.java" >}}
