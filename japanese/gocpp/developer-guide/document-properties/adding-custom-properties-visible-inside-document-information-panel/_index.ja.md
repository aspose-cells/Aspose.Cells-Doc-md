---
title: Golang経由のC++でドキュメント情報パネル内に表示されるカスタムプロパティを追加
linktitle: 文書情報パネル内で表示されるカスタムプロパティを追加する
type: docs
weight: 300
url: /ja/go-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: Aspose.Cellsを使ってGolang経由のC++でドキュメント情報パネルに表示されるカスタムプロパティを追加する方法を学ぶ。
---

## **ドキュメント情報パネルで表示されるカスタムプロパティの追加**

Aspose.Cellsを使用すると、ワークブックオブジェクト内に文書情報パネルで表示されるカスタムプロパティを追加できます。Microsoft Excelで文書情報パネルを開くには、ファイル > 情報 > プロパティ > ドキュメントパネルを選択します。

[**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/go-cpp/contenttypepropertycollection/add_string_string/)メソッドを使用して、ドキュメント情報パネルに表示されるカスタムプロパティを追加してください。

次のサンプルコードは、2つのカスタムプロパティを追加します。最初のプロパティにはタイプがなく、2つ目のプロパティにはDateTimeタイプがあります。このコードで生成されたExcelファイルを開くと、これらの2つのプロパティがドキュメント情報パネル内に表示されます。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-AddingCustomPropertiesVisibleInsideDocumentInformationPanel.go" >}}
### **関連記事**

{{% alert color="primary" %}}

- [Aspose.CellsでカスタムXMLパーツを使用する](/cells/ja/cpp/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
