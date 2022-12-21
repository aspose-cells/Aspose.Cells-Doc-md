---
title: Aspose.Cells でのカスタム XML パーツの使用
type: docs
weight: 570
url: /ja/java/using-custom-xml-parts-in-aspose-cells/
---
{{% alert color="primary" %}} 

カスタム XML パーツは、SharePoint などのさまざまなアプリケーションによって Excel ファイル内に保存される XML データです。このデータは、それを必要とするさまざまなアプリケーションによって消費されます。 Microsoft Excel はこのデータを使用しないため、追加するための GUI はありません。の拡張子を変更すると、このデータを表示できます。**.xlsx**の中へ**。ジップ**そして、それを開くことによって**WinRAR** .データは内部に存在します**customXml**このイメージに示すようにフォルダ。

![todo:画像_代替_文章](using-custom-xml-parts-in-aspose-cells_1.png)

 Aspose.Cells を使用してカスタム XML パーツを追加できます。[Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\)） 方法。

{{% /alert %}} 
## **Aspose.Cells でのカスタム Xml パーツの使用**
次のサンプル コードでは、[Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add\(java.lang.Object\) ) メソッドを追加し、**書籍カタログ XML**そしてその名は**本屋**.次の図は、このコードの結果を示しています。ご覧のとおり、このプロパティの名前である BookStore ノード内に Book Catalog Xml が追加されています。

![todo:画像_代替_文章](using-custom-xml-parts-in-aspose-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingCustomXmlParts-UsingCustomXmlParts.java" >}}
## **関連記事**
{{% alert color="primary" %}} 

- [ドキュメント情報パネル内に表示されるカスタム プロパティの追加](/cells/ja/java/adding-custom-properties-visible-inside-document-information-panel/)

{{% /alert %}}
