---
title: ドキュメント情報パネル内に表示されるカスタム プロパティの追加
type: docs
weight: 500
url: /ja/java/adding-custom-properties-visible-inside-document-information-panel/
---
{{% alert color="primary" %}}

Aspose.Cells を使用して、ドキュメント情報パネル内に表示されるワークブック オブジェクト内にカスタム プロパティを追加できます。 [ファイル] > [情報] > [プロパティ] > [ドキュメント パネルを表示] メニュー コマンドを使用して、Microsoft Excel でドキュメント情報パネルを開くことができます。

使ってください[**Workbook.getContentTypeProperties().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add(java.lang.Object)) ドキュメント情報パネルに表示されるカスタム プロパティを追加するメソッド

{{% /alert %}}

## **例**

次のサンプル コードは、2 つのカスタム プロパティを追加します。最初のプロパティには型がなく、2 番目のプロパティの型は DateTime です。このコードによって生成された出力 Excel ファイルを開くと、ドキュメント情報パネル内にこれら 2 つのプロパティが表示されます。

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-worksheets-management-AddingCustomProperties-AddingCustomProperties.java" >}}

## **関連記事**

{{% alert color="primary" %}}

- [Aspose.Cells でのカスタム XML パーツの使用](/cells/ja/java/using-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
