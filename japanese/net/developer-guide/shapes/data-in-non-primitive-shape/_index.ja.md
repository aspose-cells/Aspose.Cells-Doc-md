---
title: 非原始の形のデータ
type: docs
weight: 300
url: /ja/net/data-in-non-primitive-shape/
---

## **非原始の形のデータへのアクセス**

時々、ビルトインでない形状からデータにアクセスする必要があります。ビルトインの形状は原始形状と呼ばれ、そうでないものは非原始形状と呼ばれます。例えば、異なる曲線接続線を使用して独自の形状を定義することができます。

## **非原始の形状**

Aspose.Cellsでは、非原始の形状にはタイプ[**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/net/aspose.cells.drawing/autoshapetype)が割り当てられます。[**Shape.AutoShapeType**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/autoshapetype)プロパティを使用してそのタイプを確認できます。

[**Shape.Paths**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shape/properties/paths)プロパティを使用して形状データにアクセスします。これにより、非原始の形状を構成するすべての接続パスが返されます。これらのパスは、各セグメント内のポイントを含むセグメントのリストを保持する[**ShapePath**](https://reference.aspose.com/cells/net/aspose.cells.drawing/shapepath)タイプです。

|**非原始の形状の例を示す**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-DrawingObjects-AccessNonPrimitiveShape-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
