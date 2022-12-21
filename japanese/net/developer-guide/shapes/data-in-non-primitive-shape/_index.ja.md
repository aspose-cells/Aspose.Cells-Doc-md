---
title: 非プリミティブ形状のデータ
type: docs
weight: 300
url: /ja/net/data-in-non-primitive-shape/
---
## **非プリミティブ形状のデータへのアクセス**

組み込みではない図形からデータにアクセスする必要がある場合があります。組み込みシェイプはプリミティブ シェイプと呼ばれます。そうでないものは、非プリミティブと呼ばれます。たとえば、さまざまな曲線を接続した線を使用して、独自の形状を定義できます。

## **非原始的な形状**

Aspose.Cells では、非プリミティブ シェイプにタイプが割り当てられます。[**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/net/aspose.cells.drawing/autoshapetype) .を使用してそれらのタイプを確認できます[**Shape.AutoShapeType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/autoshapetype)財産。

を使用して形状データにアクセスします。[**シェイプ.パス**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/paths)財産。非プリミティブ形状を構成するすべての接続されたパスを返します。これらのパスのタイプは[**シェイプパス**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapepath)これは、各セグメントのポイントを順番に含むすべてのセグメントのリストを保持します。

|**非プリミティブ形状の例を示します**|
|:- |
|![todo:画像_代替_文章](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-AccessNonPrimitiveShape-1.cs" >}}
