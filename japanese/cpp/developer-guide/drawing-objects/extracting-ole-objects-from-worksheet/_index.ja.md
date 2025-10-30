---
title: ワークシートから OLE オブジェクトを抽出
type: docs
weight: 10
url: /ja/cpp/extracting-ole-objects-from-worksheet/
---

## **可能な使用シナリオ**
Aspose.Cells を使用すると、ワークシートからあらゆる種類の OLE オブジェクトを抽出できます。[Worksheet->GetOleObjects()](https://reference.aspose.com/cells/cpp/aspose.cells/worksheet/getoleobjects/) メソッドを使用して、ワークシート内のすべての OLE オブジェクトにアクセスできます。各 OLE オブジェクトには [ProgID](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getprogid/) と [ObjectData](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/oleobject/getobjectdata/) プロパティがあり、OLE オブジェクトのタイプを特定し、正常に抽出するのに役立ちます。
## **ワークシートからOLEオブジェクトを抽出する**
次のサンプルコードでは、3つのOLEオブジェクトを含む[サンプルExcelファイル](66519077.xlsx)をロードします。コードはOLEオブジェクトの種類を識別し、次のファイルとして1つずつ抽出します。

- [outputExtractOleObject.pptx](66519080.pptx)
- [outputExtractOleObject.pdf](66519079.pdf)
- [outputExtractOleObject.docx](66519078.docx)
## **サンプルコード**
{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "DrawingObjects-ExtractingOLEObjectsFromWorksheet-new.cpp" >}}
{{< app/cells/assistant language="cpp" >}}
