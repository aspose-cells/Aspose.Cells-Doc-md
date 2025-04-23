---
title: HtmlSaveOptions.TableCssIdプロパティでテーブル要素スタイルをプレフィックス
type: docs
weight: 110
url: /ja/python-net/prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property/
---

## **可能な使用シナリオ**

Aspose.Cellsには、ワークシートのCSSを[**HtmlSaveOptions.table_css_id**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/table_css_id)プロパティで接頭辞としてエクスポートする機能があります。このような値として**MyTest_TableCssId**などの値を設定すると、以下に示すようなテーブル要素のスタイルが見つかります。

{{< highlight java >}}

 table#MyTest_TableCssId

#MyTest_TableCssId tr

#MyTest_TableCssId col

#MyTest_TableCssId br

etc.

{{< /highlight >}}

以下のスクリーンショットは、[**HtmlSaveOptions.table_css_id**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/table_css_id)プロパティの使用による出力HTMLに対する効果を示しています。

![todo:image_alt_text](prefix-table-elements-styles-with-htmlsaveoptions-tablecssid-property_1.png)

## **HtmlSaveOptions.TableCssIdプロパティの使用方法についてのサンプルコードを以下に説明します。参照のために、コードによって生成された[output HTML](60489791.zip)を確認してください。**

次のサンプルコードは、[**HtmlSaveOptions.table_css_id**](https://reference.aspose.com/cells/python-net/aspose.cells/htmlsaveoptions/table_css_id)プロパティを使用する方法を示しています。コードによって生成された[output HTML](60489790.zip)の参照用です。

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "HTML-PrefixTableElementsStylesWithHtmlSaveOptions_TableCssIdProperty.py" >}}
