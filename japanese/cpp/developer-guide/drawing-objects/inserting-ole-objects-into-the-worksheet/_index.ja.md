---
title: ワークシートにOLEオブジェクトを挿入する
type: docs
weight: 20
url: /ja/cpp/inserting-ole-objects-into-the-worksheet/
---

## **可能な使用シナリオ**
Aspose.Cellsを使用すると、ワークシート内にOLEオブジェクトを挿入できます。この目的のために[Worksheet->GetOleObjects()->Add()](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobjectcollection/add/)メソッドを使用してください。OLEオブジェクトをワークシート内に挿入するために使用されるイメージバイト配列と、実際のオブジェクトであるOleオブジェクトデータバイトが必要です。 
## **ワークシートにOLEオブジェクトを挿入する**
The following sample code creates the workbook object and inserts the Ole object inside the first worksheet and saves it as [output Excel file](66519074.xlsx). Please see the <a href="66519075.png" download="66519075.png">Aspose ロゴ</a> used as image bytes and [input Excel file](66519081.xlsx) used as Ole object data inside the code for reference.
## **サンプルコード**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-InsertingOLEObjectsIntoWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
