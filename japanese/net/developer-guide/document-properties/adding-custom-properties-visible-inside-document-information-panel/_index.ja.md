---
title: 文書情報パネル内で表示されるカスタムプロパティを追加する
type: docs
weight: 300
url: /ja/net/adding-custom-properties-visible-inside-document-information-panel/
---

## **ドキュメント情報パネルで表示されるカスタムプロパティの追加**

Aspose.Cellsを使用すると、ワークブックオブジェクト内に文書情報パネルで表示されるカスタムプロパティを追加できます。Microsoft Excelで文書情報パネルを開くには、ファイル > 情報 > プロパティ > ドキュメントパネルを選択します。

文書情報パネルで表示されるカスタムプロパティを追加するには、[**Workbook.ContentTypeProperties.Add()**](https://reference.aspose.com/cells/net/aspose.cells.properties/contenttypepropertycollection/methods/add/index) メソッドを使用してください

次のサンプルコードでは、2つのカスタムプロパティを追加します。1つ目のプロパティにはタイプがなく、2つ目のプロパティにはDateTime型が指定されています。このコードで生成された出力Excelファイルを開くと、これらの2つのプロパティが文書情報パネル内に表示されます。

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-AddingCustomPropertiesVisible-1.cs" >}}

### **関連記事**

{{% alert color="primary" %}}

- [Aspose.CellsでカスタムXMLパーツを使用する](/cells/ja/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
