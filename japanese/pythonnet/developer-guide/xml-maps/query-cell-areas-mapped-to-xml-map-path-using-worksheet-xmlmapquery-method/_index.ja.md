---
title: ワークシート.XmlMapQueryメソッドを使用して、XMLマップパスにマップされたセルエリアをクエリします。
type: docs
weight: 60
url: /ja/python-net/query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method/
---

## **可能な使用シナリオ**

Aspose.Cells for Python via .NETを使い、XMLマップパスにマッピングされたセル範囲を[**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query)メソッドで照会できます。パスが存在すれば、そのパスに関連付けられたセル範囲のリストを返します。第1引数はXML要素のパスを指定し、第2引数は照会したいXMLマップです。

## **ワークシート.XmlMapQueryメソッドを使用して、XMLマップパスにマップされたセルエリアをクエリします。**

次のスクリーンショットは、コードで使用される[sample Excel file](55541790.xlsx)内のXMLマップを表示するMicrosoft Excelを示しています。コードはXMLマップを2回クエリし、[**Worksheet.xml_map_query()**](https://reference.aspose.com/cells/python-net/aspose.cells/worksheet/xml_map_query)メソッドによって返されたセル領域のリストを下記のようにコンソールに出力します。

![todo:image_alt_text](query-cell-areas-mapped-to-xml-map-path-using-worksheet-xmlmapquery-method_1.png)

### **サンプルコード**

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "XmlMaps-QueryCellAreasMappedToXmlMapPath.py" >}}

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

XMLデータはワークシートにインポート可能です。時にはワークシートのListObjectsからXMLパスの取得が必要です。この機能は、ExcelではSheet1.ListObjects(1).XmlMap.DataBindingといった式を使用して利用できます。Aspose.Cells for Python via .NETでも、[**ListObject.xml_map.data_binding.url**](https://reference.aspose.com/cells/python-net/aspose.cells/xmldatabinding/url)を呼び出すことで同じ機能が使用可能です。以下はこの機能を示す例です。テンプレートファイルおよびその他のソースファイルはリンクからダウンロードできます：

1. [XML Data.xlsx](72417285.xlsx)
1. [Country List.xml](72417287.xml)
1. [Food List.xml](72417286.xml)

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "XmlMaps-GetXMLPathFromListObject.py" >}}

{{< app/cells/assistant language="python-net" >}}
