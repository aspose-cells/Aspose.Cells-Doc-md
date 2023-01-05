---
title: ワークシートへの OLE オブジェクトの挿入
type: docs
weight: 20
url: /ja/cpp/inserting-ole-objects-into-the-worksheet/
---
## **考えられる使用シナリオ**
Aspose.Cells を使用すると、ワークシート内に OLE オブジェクトを挿入できます。使ってください[IWorksheet->GetIOleObjects()->Add()](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object_collection#af230dd65a00cefabcc4b9f165b5dc7ba)この目的のためのメソッド。ワークシート内に OLE オブジェクトを挿入するために使用されるイメージ バイト配列と、ワークシート内に Ole オブジェクトを挿入するために、実際のオブジェクトとなる Ole オブジェクト データ バイトが必要です。
## **ワークシートへの OLE オブジェクトの挿入**
次のサンプル コードでは、workbook オブジェクトを作成し、最初のワークシート内に Ole オブジェクトを挿入して、それを次のように保存します。[出力エクセルファイル](66519074.xlsx) .をご覧ください[Aspose ロゴ](66519075.png)画像バイトとして使用され、[エクセルファイル入力](66519081.xlsx)参照用にコード内で Ole オブジェクト データとして使用されます。
## **サンプルコード**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-InsertingOLEObjectsIntoWorksheet.cpp" >}}
