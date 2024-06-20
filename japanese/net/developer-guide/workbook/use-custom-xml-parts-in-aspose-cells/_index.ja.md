---
title: Aspose.Cells でカスタムXMLパーツを使用する
type: docs
weight: 390
url: /ja/net/use-custom-xml-parts-in-aspose-cells/
---

## Aspose.Cells でカスタムXMLパーツを使用する

カスタムXMLパーツは、SharePointなどの異なるアプリケーションによってExcelファイル内に保存されるXMLデータです。このデータは、それを必要とする異なるアプリケーションによって消費されます。Microsoft Excelはこのデータを使用しないため、追加するためのGUIはありません。 **.xlsx** の拡張子を **.zip** に変更し、**WinZip** を使用して開くことで、このデータを表示することができます。また、WinRARやWinZipなどの第3者Windows zipユーティリティを使用してZIPファイルを開くこともできます。データは **customXml** フォルダ内に存在します。

Aspose.Cellsを使用してカスタムXMLパーツを追加する場合は、 [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) メソッドを使用します。

以下のサンプルコードは、 [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) メソッドを使用し、**Book Catalog XML** を追加し、その名前を **BookStore** に設定しています。次の画像は、このコードの結果を示しています。Book Catalog XMLが **BookStore** ノード内に追加されていることがわかります。

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## カスタムXMLパーツを使用するC#コード

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-UsingCustomXmlParts-UsingCustomXmlParts.cs" >}}

## 関連記事

- [ドキュメント情報パネルで表示されるカスタムプロパティの追加](/cells/ja/net/adding-custom-properties-visible-inside-document-information-panel/)
