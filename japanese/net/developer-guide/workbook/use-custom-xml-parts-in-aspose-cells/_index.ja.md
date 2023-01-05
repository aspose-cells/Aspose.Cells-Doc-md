---
title: Aspose.Cells でカスタム XML パーツを使用する
type: docs
weight: 390
url: /ja/net/use-custom-xml-parts-in-aspose-cells/
---
## Aspose.Cells でのカスタム XML パーツの使用

カスタム XML パーツは、SharePoint などのさまざまなアプリケーションによって Excel ファイル内に保存される XML データです。このデータは、それを必要とするさまざまなアプリケーションによって消費されます。 Microsoft Excel はこのデータを使用しないため、追加するための GUI はありません。の拡張子を変更すると、このデータを表示できます。**.xlsx**の中へ**。ジップ**そして、それを開くことによって**ウィンジップ**.また、WinRAR や WinZip などの 3rd part Windows zip ユーティリティを使用して ZIP ファイルを開くこともできます。データは、**customXml**フォルダ。

 Aspose.Cells を使用してカスタム XML パーツを追加できます。[**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index)方法。

次のサンプル コードでは、[**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index)メソッドを追加し、**書籍カタログ XML**そしてその名は**本屋**.次の図は、このコードの結果を示しています。ご覧のとおり、このプロパティの名前である BookStore ノード内に Book Catalog XML が追加されています。

![todo:画像_代替_文章](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:画像_代替_文章](use-custom-xml-parts-in-aspose-cells_2.png)

## C# カスタム XML パーツを使用するコード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingCustomXmlParts-UsingCustomXmlParts.cs" >}}

## 関連記事

- [ドキュメント情報パネル内に表示されるカスタム プロパティの追加](/cells/ja/net/adding-custom-properties-visible-inside-document-information-panel/)
