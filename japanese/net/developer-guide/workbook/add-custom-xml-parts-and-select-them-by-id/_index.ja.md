---
title: カスタムXMLパーツの追加およびIDでの選択
type: docs
weight: 70
url: /ja/net/add-custom-xml-parts-and-select-them-by-id/
---

## **可能な使用シナリオ**

カスタムXMLパーツは、Microsoft Excelドキュメント内に格納されるXMLデータであり、それを処理するアプリケーションで使用されます。現時点では、Microsoft Excel UIで直接追加する方法はありませんが、VSTO、Aspose.Cellsなどを使用してプログラムで追加できます。Aspose.Cells APIを使用してカスタムXMLパーツを追加したい場合は[**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add)メソッドを使用してください。また、[**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id)プロパティを使用してそのIDを設定できます。同様に、IDでカスタムXMLパーツを選択したい場合は[**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)メソッドを使用できます。

## **カスタムXMLパーツの追加およびIDでの選択**

以下のサンプルコードは、まず[**Workbook.CustomXmlParts.Add()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/add)メソッドを使用して4つのカスタムXMLパーツを追加します。次に[**CustomXmlPart.ID**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpart/properties/id)プロパティを使用してそれらのIDを設定します。最後に[**Workbook.CustomXmlParts.SelectByID()**](https://reference.aspose.com/cells/net/aspose.cells.markup/customxmlpartcollection/methods/selectbyid)メソッドを使用して追加されたカスタムXMLパーツの1つを検索または選択します。以下のコードのコンソール出力も参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-AddCustomXMLPartsAndSelectThemByID.cs" >}}

## **コンソール出力**

{{< highlight java >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}
