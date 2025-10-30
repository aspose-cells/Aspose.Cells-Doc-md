---
title: ビルトインドキュメントプロパティのScaleCropおよびLinksUpToDateプロパティを設定する
type: docs
weight: 320
url: /ja/python-net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **可能な使用シナリオ**
[scale_crop](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/scale_crop) と [links_up_to_date](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/links_up_to_date) は、OpenXmlフォーマット内で定義された2つの拡張組み込みドキュメントプロパティです。これらの目的は次の通りです。
## **1) ScaleCrop**
この要素は、ドキュメントサムネイルの表示モードを示します。この要素を**TRUE**に設定すると、ドキュメントサムネイルを表示に合わせてスケーリングします。この要素を**FALSE**に設定すると、ドキュメントサムネイルを表示に合わせてクロップします。

この要素の可能な値は、W3C XML Schema booleanデータ型で定義されています。
## **2) LinksUpToDate**
この要素は、ドキュメント内のハイパーリンクが最新であるかどうかを示します。この要素を**TRUE**に設定すると、ハイパーリンクが更新されていることを示します。この要素を**FALSE**に設定すると、ハイパーリンクが更新されていないことを示します。

この要素の可能な値は、W3C XML Schema booleanデータ型で定義されています。
## **これらのプロパティを示すスクリーンショット**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **ビルトインドキュメントプロパティのScaleCropおよびLinksUpToDateプロパティを設定する**
次のサンプルコードは、[scale_crop](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/scale_crop) と [links_up_to_date](https://reference.aspose.com/cells/python-net/aspose.cells.properties/builtindocumentpropertycollection/links_up_to_date) の拡張組み込みドキュメントプロパティを設定します。このコードで生成された[出力エクセルファイル](5115500.xlsx)を確認し、その拡張子を.zipに変更して内容を抽出し、app.xmlをスクリーンショットのように表示してください。



{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-SettingScaleCropAndLinksUpToDateProperties.py" >}}
{{< app/cells/assistant language="python-net" >}}
