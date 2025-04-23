---
title: 文書情報パネル内で表示されるカスタムプロパティを追加する
type: docs
weight: 300
url: /ja/python-net/adding-custom-properties-visible-inside-document-information-panel/
---

## **ドキュメント情報パネルで表示されるカスタムプロパティの追加**

Aspose.Cells for Python via .NETを使って、ワークブック内にカスタムプロパティを追加し、ドキュメント情報パネルに表示させることができます。Microsoft Excelでファイル > 情報 > プロパティ > ドキュメントパネルの表示から開くことが可能です。

文書情報パネルで表示されるカスタムプロパティを追加するには、[**Workbook.content_type_properties.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/contenttypepropertycollection/add) メソッドを使用してください

次のサンプルコードでは、2つのカスタムプロパティを追加します。1つ目のプロパティにはタイプがなく、2つ目のプロパティにはDateTime型が指定されています。このコードで生成された出力Excelファイルを開くと、これらの2つのプロパティが文書情報パネル内に表示されます。

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Document-Properties-AddingCustomPropertiesVisible-1.py" >}}

### **関連記事**

{{% alert color="primary" %}}

- [Aspose.CellsでカスタムXMLパーツを使用する](/cells/ja/python-net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
