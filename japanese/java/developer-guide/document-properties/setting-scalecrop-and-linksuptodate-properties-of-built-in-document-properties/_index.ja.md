---
title: ビルトインドキュメントプロパティのScaleCropおよびLinksUpToDateプロパティを設定する
type: docs
weight: 1050
url: /ja/java/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---

## **可能な使用シナリオ**
[ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) および[LinksUpToDate](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) は、OpenXml形式で定義されている2つの拡張組み込みドキュメントプロパティです。これらのプロパティの目的は次のとおりです。
## **1) ScaleCrop**
この要素は、ドキュメントサムネイルの表示モードを示します。この要素を**true**に設定すると、ドキュメントサムネイルが表示に合わせてスケーリングされます。この要素を**false**に設定すると、ドキュメントサムネイルが表示に合うように切り取られます。

この要素の可能な値は、W3C XML Schema booleanデータ型で定義されています。
## **2) LinksUpToDate**
この要素は、ドキュメント内のハイパーリンクが最新かどうかを示します。この要素を**true**に設定すると、ハイパーリンクが更新されていることを示します。この要素を**false**に設定すると、ハイパーリンクが古くなっていることを示します。

この要素の可能な値は、W3C XML Schema booleanデータ型で定義されています。
## **これらのプロパティを示すスクリーンショット**
![todo:image_alt_text](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **ビルトインドキュメントプロパティのScaleCropおよびLinksUpToDateプロパティを設定する**
次のサンプルコードは、ワークブックの[ScaleCrop](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#ScaleCrop) および[LinksUpToDate](https://reference.aspose.com/cells/java/com.aspose.cells/builtindocumentpropertycollection#LinksUpToDate) 拡張組み込みドキュメントプロパティを設定します。このコードで生成された[output excel file](5472494.xlsx)に拡張子を変更して.zipにし、その内容を抽出し、上記のスクリーンショットと同様にaap.xmlを表示してください。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-SettingScaleCropLinksUpToDate-SettingScaleCropLinksUpToDate.java" >}}
