---
title: ワークシート.XmlMapQueryメソッドを使用して、XMLマップパスにマップされたセルエリアをクエリします。
type: docs
weight: 60
url: /ja/net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **可能な使用シナリオ**

Aspose.Cellsを使用してXMLマップパスにマッピングされたセル領域をクエリすることができます。パスが存在する場合、XMLマップ内のそのパスに関連するセル領域のリストを返します。 [**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery)メソッドの最初のパラメーターはXML要素パスを指定し、2番目のパラメーターはクエリしたいXMLマップを指定します。

## **ワークシート.XmlMapQueryメソッドを使用して、XMLマップパスにマップされたセルエリアをクエリします。**

次のスクリーンショットは、コードで使用される[sample Excel file](55541790.xlsx)内のXMLマップを表示するMicrosoft Excelを示しています。コードはXMLマップを2回クエリし、[**Worksheet.XmlMapQuery()**](https://reference.aspose.com/cells/net/aspose.cells/worksheet/methods/xmlmapquery)メソッドによって返されたセル領域のリストを下記のようにコンソールに出力します。

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **サンプルコード**

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-QueryCellAreasMappedToXmlMapPath.cs" >}}

### **コンソール出力**

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

XMLデータはワークシートにインポートすることができます。時にはワークシートのListObjectsからXMLパスが必要になります。この機能は、ExcelでSheet1.ListObjects(1).XmlMap.DataBindingのような式を使用することで利用できます。Aspose.Cellsでも [**ListObject.XmlMap.DataBinding.Url**](https://reference.aspose.com/cells/net/aspose.cells/xmldatabinding/properties/url) を呼び出すことで同じ機能が利用できます。以下の例がこの機能を示しています。テンプレートファイルおよびその他のソースファイルは、以下のリンクからダウンロードできます。

1. [XML Data.xlsx](72417285.xlsx)
1. [Country List.xml](72417287.xml)
1. [Food List.xml](72417286.xml)

{{< gist "aspose-cells-gists" "59a1901d62ea9ceb08456a818431a898" "Examples-CSharp-XmlMaps-GetXMLPathFromListObject.cs" >}}
