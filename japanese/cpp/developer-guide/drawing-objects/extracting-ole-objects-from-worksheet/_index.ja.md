---
title: ワークシートからの OLE オブジェクトの抽出
type: docs
weight: 10
url: /ja/cpp/extracting-ole-objects-from-worksheet/
---
## **考えられる使用シナリオ**
Aspose.Cells では、ワークシートからすべてのタイプの OLE オブジェクトを抽出できます。使ってください[IWorksheet->GetIOleObjects()](https://reference.aspose.com/cells/cpp/class/aspose.cells.i_worksheet#a4c59d95cdd871ecfe18274480831a728)メソッドを使用して、ワークシート内のすべての OLE オブジェクトにアクセスします。各 OLE オブジェクトには[プログラム ID](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object#abb2ea6872025fe4724d9613cd6b81752)と[オブジェクトデータ](https://reference.aspose.com/cells/cpp/class/aspose.cells.drawing.i_ole_object#a4a200a03478d3553798360cd6a911d70)OLE オブジェクトのタイプを識別して正常に抽出するのに役立つプロパティ。
## **ワークシートからの OLE オブジェクトの抽出**
次のサンプル コードは、[サンプル Excel ファイル](66519077.xlsx)これには 3 つの OLE オブジェクトがあります。このコードは、OLE オブジェクトの種類を識別し、次のファイルとして 1 つずつ抽出します。

- [outputExtractOleObject.pptx](66519080.pptx)
- [outputExtractOleObject.pdf](66519079.pdf)
- [outputExtractOleObject.docx](66519078.docx)
## **サンプルコード**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet.cpp" >}}
