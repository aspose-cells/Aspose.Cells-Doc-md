---
title: ワークシート.XmlMapQueryメソッドを使用して、XMLマップパスにマップされたセルエリアをクエリします。
type: docs
weight: 60
url: /ja/java/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **可能な使用シナリオ**

Aspose.Cellsを使用して、[**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap))メソッドを使ってXMLマップパスにマップされたセルエリアをクエリできます。パスが存在する場合、XMLマップ内のそのパスに関連するセルエリアのリストが返されます。[**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap))メソッドの最初のパラメータはXML要素パスを指定し、2番目のパラメータはクエリしたいXMLマップを指定します。

## **ワークシート.XmlMapQueryメソッドを使用して、XMLマップパスにマップされたセルエリアをクエリします。**

次のスクリーンショットは、コードで使用される[sample Excelファイル](55541818.xlsx)内のMicrosoft ExcelがXMLマップを表示しています。コードはXMLマップを2回クエリし、コンソールに表示される[**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap))メソッドによって返されるセルエリアのリストを以下のように出力します。

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-QueryCellAreasMappedToXmlMapPath.java" >}}

## **コンソール出力**

{{< highlight java >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]

Aspose.Cells.CellArea(B1:B8)[0,1,7,1]

Aspose.Cells.CellArea(C1:C8)[0,2,7,2]

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]

Aspose.Cells.CellArea(E1:E8)[0,4,7,4]

Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]

{{< /highlight >}}

## **リストオブジェクト/テーブルからXMLパスを取得する**

XMLデータはワークシートにインポートできます。ワークシートのListObjectsからXMLパスが必要な場合があります。この機能はSheet1.ListObjects(1).XmlMap.DataBindingのような式を使用することでExcelで利用できます。Aspose.Cellsでも、[**ListObject.getXmlMap().getDataBinding().getUrl()**](https://reference.aspose.com/cells/java/com.aspose.cells/xmldatabinding#Url)を呼び出すことで同じ機能を利用できます。次の例がこの機能を示しています。テンプレートファイルやその他のソースファイルは次のリンクからダウンロードできます。

1. [XMLData.xlsx](XMLData.xlsx)
1. [CountryList.xml](CountryList.xml)
1. [FoodList.xml](FoodList.xml)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-GetXMLPathFromListObject.java" >}}
