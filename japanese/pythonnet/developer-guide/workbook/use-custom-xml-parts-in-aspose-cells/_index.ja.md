---
title: Aspose.Cells でカスタムXMLパーツを使用する
type: docs
weight: 390
url: /ja/python-net/use-custom-xml-parts-in-aspose-cells/
---

## Aspose.Cells for Python via .NETでのカスタムXMLパーツの使用

カスタムXMLパーツは、SharePointなどの異なるアプリケーションによってExcelファイル内に保存されるXMLデータです。このデータは、それを必要とする異なるアプリケーションによって消費されます。Microsoft Excelはこのデータを使用しないため、追加するためのGUIはありません。 **.xlsx** の拡張子を **.zip** に変更し、**WinZip** を使用して開くことで、このデータを表示することができます。また、WinRARやWinZipなどの第3者Windows zipユーティリティを使用してZIPファイルを開くこともできます。データは **customXml** フォルダ内に存在します。

Aspose.Cellsを使用してカスタムXMLパーツを追加する場合は、 [**Workbook.content_type_properties.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/contenttypepropertycollection/add/#str-str) メソッドを使用します。

以下のサンプルコードは、 [**Workbook.content_type_properties.add()**](https://reference.aspose.com/cells/python-net/aspose.cells.properties/contenttypepropertycollection/add/#str-str) メソッドを使用し、**Book Catalog XML** を追加し、その名前を **BookStore** に設定しています。次の画像は、このコードの結果を示しています。Book Catalog XMLが **BookStore** ノード内に追加されていることがわかります。

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_1.png)

![todo:image_alt_text](use-custom-xml-parts-in-aspose-cells_2.png)

## カスタムXMLパーツを使用するC#コード

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Workbook-UsingCustomXmlParts.py" >}}



