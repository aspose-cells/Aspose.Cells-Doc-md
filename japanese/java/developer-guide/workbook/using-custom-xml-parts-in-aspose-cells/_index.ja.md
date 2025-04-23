---
title: Aspose.CellsでのカスタムXMLパーツの使用
type: docs
weight: 570
url: /ja/java/using-custom-xml-parts-in-aspose-cells/
---

{{% alert color="primary" %}} 

カスタムXMLパーツは、SharePointなどのさまざまなアプリケーションによってExcelファイル内に保存されるXMLデータです。このデータは必要なさまざまなアプリケーションによって消費されます。Microsoft Excelはこのデータを使用しないため、それを追加するためのGUIはありません。 **.xlsx**の拡張子を**.zip**に変更し、**WinRAR**を使用して開くことでこのデータを表示できます。データは、この画像に示されているように**customXml**フォルダ内に存在します。

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_1.png)

Aspose.Cellsを使ってカスタムXMLパーツを追加するには、 [Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add-java.lang.Object-) メソッドを使用します。

{{% /alert %}} 
## **Aspose.CellsでのカスタムXMLパーツの使用**
次のサンプルコードは [Workbook.getContentTypeProperties().add()](https://reference.aspose.com/cells/java/com.aspose.cells/contenttypepropertycollection#add-java.lang.Object-) を使用し、「Book Store」という名前の**Book Catalog Xml**を追加した例です。画像はこのコードの結果を示しており、Book Catalog XmlはBookStoreノード内に追加されています。

![todo:image_alt_text](using-custom-xml-parts-in-aspose-cells_2.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-UsingCustomXmlParts-UsingCustomXmlParts.java" >}}
## **関連記事**
{{% alert color="primary" %}} 

- [ドキュメント情報パネルで表示されるカスタムプロパティの追加](/cells/ja/java/adding-custom-properties-visible-inside-document-information-panel/)

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
