---
title: 組み込みドキュメント プロパティの ScaleCrop および LinksUpToDate プロパティの設定
type: docs
weight: 320
url: /ja/net/setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties/
---
## **考えられる使用シナリオ**
[スケールクロップ](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop)と[LinksUpToDate](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate)OpenXml 形式内で定義された 2 つの拡張組み込みドキュメント プロパティです。これらのプロパティの目的は次のとおりです。
## **1) スケールクロップ**
この要素は、ドキュメント サムネイルの表示モードを示します。この要素を**真実**ドキュメントのサムネイルを表示に合わせてスケーリングできるようにします。この要素を**間違い**ドキュメントのサムネイルのトリミングを有効にして、ディスプレイに収まるセクションのみを表示します。

この要素の可能な値は、W3C XML スキーマのブール データ型によって定義されます。
## **2) LinksUpToDate**
この要素は、ドキュメント内のハイパーリンクが最新かどうかを示します。この要素を**真実**ハイパーリンクが更新されたことを示します。この要素を**間違い**ハイパーリンクが古くなっていることを示します。

この要素の可能な値は、W3C XML スキーマのブール データ型によって定義されます。
## **app.xml ファイル内のこれらのプロパティを示すスクリーンショット**
![todo:画像_代替_文章](setting-scalecrop-and-linksuptodate-properties-of-built-in-document-properties_1.png)
## **組み込みドキュメント プロパティの ScaleCrop および LinksUpToDate プロパティの設定**
次のサンプル コードは、[スケールクロップ](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/scalecrop)と[LinksUpToDate](https://reference.aspose.com/cells/net/aspose.cells.properties/builtindocumentpropertycollection/properties/linksuptodate)ワークブックの拡張された組み込みドキュメント プロパティ。を確認してください[出力エクセルファイル](5115500.xlsx)上のスクリーンショットに示すように、このコードで生成された拡張子を .zip に変更してコンテンツを抽出し、app.xml を表示します。



{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-SettingScaleCropAndLinksUpToDateProperties.cs" >}}
