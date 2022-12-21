---
title: カスタム XML パーツを追加し、ID で選択する
type: docs
weight: 10
url: /ja/java/add-custom-xml-parts-and-select-them-by-id/
---
## **考えられる使用シナリオ**

カスタム XML パーツは、Microsoft Excel ドキュメント内に保存され、それらを処理するアプリケーションによって使用される XML データです。現時点では、Microsoft Excel UI を使用してそれらを直接追加する方法はありません。ただし、さまざまな方法でプログラムで追加できます。*VSTO*、使用*Aspose.Cells*などご利用ください[**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)) メソッドを使用して、Aspose.Cells API を使用してカスタム XML 部分を追加する場合。[**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID)財産。同様に、カスタム XML パーツを ID で選択する場合は、次を使用できます。[**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)） 方法。

## **カスタム XML パーツを追加し、ID で選択する**

次のサンプル コードは、最初に を使用して 4 つのカスタム XML パーツを追加します。[**Workbook.getCustomXmlParts().add()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#add(java.lang.Object)） 方法。次に、ID を使用して設定します。[**CustomXmlPart.ID**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpart#ID)財産。最後に、追加されたカスタム XML 部分の 1 つを検索または選択します。[**Workbook.getCustomXmlParts().selectByID()**](https://reference.aspose.com/cells/java/com.aspose.cells/customxmlpartcollection#selectByID(java.lang.String)） 方法。以下のコードのコンソール出力も参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Workbook-AddCustomXMLPartsAndSelectThemByID.java" >}}

## **コンソール出力**

{{< highlight "java" >}}

Found: CustomXmlPart ID Sport

{{< /highlight >}}
