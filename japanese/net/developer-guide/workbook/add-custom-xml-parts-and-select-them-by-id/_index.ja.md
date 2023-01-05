---
title: カスタム XML パーツを追加し、ID で選択する
type: docs
weight: 70
url: /ja/net/add-custom-xml-parts-and-select-them-by-id/
---
## **考えられる使用シナリオ**

カスタム XML パーツは、Microsoft Excel ドキュメント内に保存され、それらを処理するアプリケーションによって使用される XML データです。現時点では、Microsoft Excel UI を使用してそれらを直接追加する方法はありません。ただし、VSTO を使用したり、Aspose.Cells を使用したりするなど、さまざまな方法でプログラムで追加できます。使用してください。[**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add)Aspose.Cells API を使用してカスタム XML 部分を追加する場合は、メソッドを使用します。[**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id)財産。同様に、カスタム XML パーツを ID で選択する場合は、次を使用できます。[**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)方法。

## **カスタム XML パーツを追加し、ID で選択する**

次のサンプル コードは、最初に を使用して 4 つのカスタム XML パーツを追加します。[**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add)方法。次に、ID を次のように設定します。[**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id)財産。最後に、追加されたカスタム XML 部分の 1 つを検索または選択します。[**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)方法。以下のコードのコンソール出力も参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-AddCustomXMLPartsAndSelectThemByID.cs" >}}

## **コンソール出力**

{{< highlight "java" >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}
