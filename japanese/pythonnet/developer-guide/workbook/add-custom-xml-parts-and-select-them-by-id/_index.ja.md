---
title: カスタムXMLパーツの追加およびIDでの選択
type: docs
weight: 70
url: /ja/python-net/add-custom-xml-parts-and-select-them-by-id/
---

## **可能な使用シナリオ**

カスタムXMLパーツは、Microsoft Excelドキュメント内に保存され、これらを扱うアプリケーションで使用されるXMLデータです。現在、Microsoft ExcelのUIを使用して直接追加する方法はありません。ただし、プログラム的にVSTOやAspose.Cellsなどを利用して追加できます。Aspose.Cells for Python via .NET APIを使用してカスタムXMLパーツを追加するには、[**Workbook.custom_xml_parts.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes)メソッドを使用してください。また、[**CustomXmlPart.id**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id)プロパティを使ってIDを設定できます。同様に、IDでカスタムXMLパーツを選択するには[**Workbook.custom_xml_parts.select_by_id()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str)メソッドを使用します。

## **カスタムXMLパーツの追加およびIDでの選択**

以下のサンプルコードは、まず[**Workbook.custom_xml_parts.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/add/#bytes-bytes)メソッドを使用して4つのカスタムXMLパーツを追加します。次に[**CustomXmlPart.id**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpart/id)プロパティを使用してそれらのIDを設定します。最後に[**Workbook.custom_xml_parts.select_by_id()**](https://reference.aspose.com/cells/python-net/aspose.cells.markup/customxmlpartcollection/select_by_id/#str)メソッドを使用して追加されたカスタムXMLパーツの1つを検索または選択します。以下のコードのコンソール出力も参照してください。

## **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-AddCustomXMLPartsAndSelectThemByID.py" >}}

## **コンソール出力**

{{< highlight java >}}

 Found: CustomXmlPart ID Sport

{{< /highlight >}}

