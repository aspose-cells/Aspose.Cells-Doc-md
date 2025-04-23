---
title: 文書情報パネル内で表示されるカスタムプロパティを追加する
type: docs
weight: 500
url: /ja/java/adding-custom-properties-visible-inside-document-information-panel/
---

{{% alert color="primary" %}}

Aspose.Cellsを使用すると、ワークブックオブジェクト内に文書情報パネルで表示されるカスタムプロパティを追加できます。Microsoft Excelで文書情報パネルを開くには、ファイル > 情報 > プロパティ > ドキュメントパネルを選択します。

ドキュメント情報パネルに表示されるカスタムプロパティを追加するには、[**Workbook.getContentTypeProperties().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add-java.lang.Object-) メソッドを使用してください

{{% /alert %}}

## **例**

次のサンプルコードでは、2つのカスタムプロパティを追加します。1つ目のプロパティにはタイプがなく、2つ目のプロパティにはDateTime型が指定されています。このコードで生成された出力Excelファイルを開くと、これらの2つのプロパティが文書情報パネル内に表示されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-AddingCustomProperties-AddingCustomProperties.java" >}}

## **関連記事**

{{% alert color="primary" %}}

- [Aspose.Cells でカスタム XML パーツを使用する](/cells/ja/java/using-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
