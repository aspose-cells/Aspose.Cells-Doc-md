---
title: HtmlSaveOptions.TableCssIdプロパティでテーブル要素スタイルをプレフィックス
type: docs
weight: 110
url: /ja/net/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
---

## **可能な使用シナリオ**

Aspose.Cellsには、ワークシートのCSSを[**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/tablecssid)プロパティで接頭辞としてエクスポートする機能があります。このような値として**MyTest_TableCssId**などの値を設定すると、以下に示すようなテーブル要素のスタイルが見つかります。

{{< highlight java >}}

 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.

{{< /highlight >}}

以下のスクリーンショットは、[**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/tablecssid)プロパティの使用による出力HTMLに対する効果を示しています。

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **HtmlSaveOptions.TableCssIdプロパティの使用方法についてのサンプルコードを以下に説明します。参照のために、コードによって生成された[output HTML](60489791.zip)を確認してください。**

次のサンプルコードは、[**HtmlSaveOptions.TableCssId**](https://reference.aspose.com/cells/net/aspose.cells/htmlsaveoptions/properties/tablecssid)プロパティを使用する方法を示しています。コードによって生成された[output HTML](60489790.zip)の参照用です。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-HTML-PrefixTableElementsStylesWithHtmlSaveOptions_TableCssIdProperty.cs" >}}
