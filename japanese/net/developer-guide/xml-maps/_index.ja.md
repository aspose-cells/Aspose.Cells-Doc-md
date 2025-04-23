---
title: ExcelワークブックへのXMLのインポート 
linktitle: XMLマップ
type: docs
weight: 210
url: /ja/net/import-xml-map-inside-a-workbook-using-aspose-cells/
description: XMLデータファイルからデータをMicrosoft Excelにインポートする
---

{{% alert color="primary" %}}

Aspose.Cellsでは、ワークブック内でXMLマップをインポートするための[**Workbook.ImportXml()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/importxml/index)メソッドが利用可能です。以下の手順でMicrosoft ExcelでXMLマップをインポートすることができます。

- **開発**タブを選択
- XMLセクションで**インポート**をクリックし、必要な手順に従います。

インポートを完了するためにXMLデータを提供する必要があります。テストに使用できる[サンプルXMLデータ](5115037.txt)を以下に示します。

{{% /alert %}}

## **Microsoft Excelを使用してXML Mapをインポート**

以下のスクリーンショットは、Microsoft Excelを使用してXML Mapをインポートする方法を示しています。

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_1.png)|
| :- |

## **Aspose.Cellsを使用してXML Mapをインポートする**

次のサンプルコードは、[**Workbook.ImportXml()**](https://reference.aspose.com/cells/net/aspose.cells/workbook/methods/importxml/index)の使用法を示しています。このスクリーンショットに示すように、[出力Excelファイル](5115036.xlsx)が生成されます。

|![todo:image_alt_text](import-xml-map-inside-a-workbook-using-aspose-cells_2.png)|
| :- |

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ManagingWorkbooksWorksheets-ImportXmlData-ImportXmlDataIntoWorkbook.cs" >}}

## **高度なトピック**
- [XmlMapCollection.Addメソッドを使用してワークブックにXML Mapを追加する](/cells/ja/net/add-xml-map-inside-the-workbook-using-xmlmapcollection-add-method/)
- [ブック内のXMLマップにリンクされたXMLデータをエクスポート](/cells/ja/net/export-xml-data-linked-to-xml-map-inside-the-workbook/)
- [XMLマップのルート要素名を検出する](/cells/ja/net/find-the-root-element-name-of-xml-map/)
- [セルをXMLマップ要素にリンクする](/cells/ja/net/link-cells-to-xml-map-elements/)
- [ワークシート.XmlMapQueryメソッドを使用して、XMLマップパスにマップされたセルエリアをクエリします。](/cells/ja/net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/)

{{< app/cells/assistant language="csharp" >}}
