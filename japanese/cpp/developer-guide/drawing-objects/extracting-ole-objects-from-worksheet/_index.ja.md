---
title: ワークシートからの OLE オブジェクトの抽出
type: docs
weight: 10
url: /ja/cpp/extracting-ole-objects-from-worksheet/
---
##  **考えられる使用シナリオ**
Aspose.Cells を使用すると、ワークシートからすべての種類の OLE オブジェクトを抽出できます。使ってください[ワークシート -> GetOleObjects()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoleobjects/)メソッドを使用して、ワークシート内のすべての OLE オブジェクトにアクセスします。各 OLE オブジェクトには、[プログID](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getprogid/)そして[オブジェクトデータ](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/)これらのプロパティは、OLE オブジェクトの種類を識別し、正常に抽出するのに役立ちます。
##  **ワークシートからの OLE オブジェクトの抽出**
次のサンプルコードは、[サンプル Excel ファイル](66519077.xlsx)これには 3 つの OLE オブジェクトがあります。このコードは、OLE オブジェクトの種類を識別し、それらを 1 つずつ次のファイルとして抽出します。

- [出力ExtractOleObject.pptx](66519080.pptx)
- [出力ExtractOleObject.pdf](66519079.pdf)
- [OutputExtractOleObject.docx](66519078.docx)
##  **サンプルコード**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet-new.cpp" >}}
