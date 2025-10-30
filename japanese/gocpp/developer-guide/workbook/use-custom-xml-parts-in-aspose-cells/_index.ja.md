---
title: GolangとC++経由でAspose.Cellsを使ったカスタムXMLパーツの利用方法
linktitle: カスタムXMLパーツを使用する
type: docs
weight: 390
url: /ja/go-cpp/use-custom-xml-parts-in-aspose-cells/
description: Aspose.Cellsを使い、GolangとC++経由でExcelファイル内のカスタムXMLパーツのプログラム的な使用方法を学ぶ。
---

## Aspose.Cells でカスタムXMLパーツを使用する

カスタムXMLパーツは、SharePointなどのさまざまなアプリケーションによってExcelファイル内に格納されるXMLデータです。このデータは、それを必要とするさまざまなアプリケーションによって消費されます。Microsoft Excelはこのデータを使用しないため、GUIから追加する仕組みはありません。このデータは、**.xlsx**の拡張子を**.zip**に変更して開くか、またはサードパーティのWindows圧縮ユーティリティ（WinRARやWinZipなど）を使用してZIPファイルとして開くことで閲覧可能です。このデータは**customXml**フォルダ内にあります。

Aspose.Cellsの [**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/) メソッドを使ってカスタムXMLパーツを追加可能。

以下のサンプルコードは、[**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/)メソッドを使用して「Book Catalog XML」を追加し、その名前を「BookStore」にする例です。このコードの結果を示す画像は以下の通りです。ご覧の通り、「Book Catalog XML」は、「BookStore」ノード内に追加されました。これはこのプロパティの名前です。

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## C++によるカスタムXMLパーツの使用コード

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-UseCustomXmlPartsInAsposeCells.go" >}}
## 関連記事

- [ドキュメント情報パネル内に表示されるカスタムプロパティの追加](/cells/ja/cpp/adding-custom-properties-visible-inside-document-information-panel/)
