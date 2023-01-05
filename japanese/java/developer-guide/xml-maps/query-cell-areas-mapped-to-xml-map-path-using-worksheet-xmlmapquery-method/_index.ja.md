---
title: Worksheet.XmlMapQuery メソッドを使用して XML マップ パスにマップされた Cell エリアをクエリします。
type: docs
weight: 60
url: /ja/java/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---
## **考えられる使用シナリオ**

を使用して、Aspose.Cells で XML マップ パスにマップされたセル領域をクエリできます。[**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)） 方法。パスが存在する場合、XML マップ内のそのパスに関連するセル領域のリストが返されます。の最初のパラメーター[**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)メソッドは XML 要素のパスを指定し、2 番目のパラメーターは照会する XML マップを指定します。

## **Worksheet.XmlMapQuery メソッドを使用して XML マップ パスにマップされた Cell エリアをクエリします。**

次のスクリーンショットは、Microsoft Excel が XML マップを表示している様子を示しています。[サンプル Excel ファイル](55541818.xlsx)コードで使用されます。このコードは、XML マップに対して 2 回クエリを実行し、[**Worksheet.xmlMapQuery()**](https://reference.aspose.com/cells/java/com.aspose.cells/worksheet#xmlMapQuery(java.lang.String,%20com.aspose.cells.XmlMap)) 以下に示すように、コンソールでメソッドを実行します。

![todo:画像_代替_文章](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

## **サンプルコード**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-QueryCellAreasMappedToXmlMapPath.java" >}}

## **コンソール出力**

{{< highlight "java" >}}

Query Xml Map from Path - /MiscData

Aspose.Cells.CellArea(A1:A8)[0,0,7,0]Aspose.Cells.CellArea(B1:B8)[0,1,7,1]Aspose.Cells.CellArea(C1:C8)[0,2,7,2]Aspose.Cells.CellArea(D1:D8)[0,3,7,3]Aspose.Cells.CellArea(E1:E8)[0,4,7,4]Query Xml Map from Path - /MiscData/row/Color

Aspose.Cells.CellArea(D1:D8)[0,3,7,3]{{< /highlight >}}

## **リスト オブジェクト/テーブルから XML パスを取得する**

XML データをワークシートにインポートできます。ワークシートの ListObjects からの XML パスが必要になる場合があります。この機能は、Sheet1.ListObjects(1).XmlMap.DataBinding のような式を使用して Excel で利用できます。同じ機能は、Aspose.Cells に電話することで利用できます。[**ListObject.getXmlMap().getDataBinding().getUrl()**](https://reference.aspose.com/cells/java/com.aspose.cells/xmldatabinding#Url).次の例は、この機能を示しています。テンプレート ファイルとその他のソース ファイルは、次のリンクからダウンロードできます。

1. [XMLData.xlsx](XMLData.xlsx)
1. [CountryList.xml](CountryList.xml)
1. [FoodList.xml](FoodList.xml)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-XmlMaps-GetXMLPathFromListObject.java" >}}
