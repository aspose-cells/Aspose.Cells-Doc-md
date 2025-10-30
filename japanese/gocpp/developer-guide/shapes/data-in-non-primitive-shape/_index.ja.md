---
title: GolangとC++を使用した非プリミティブシェイプ内のデータ
linktitle: 非原始の形のデータ
type: docs
weight: 300
url: /ja/go-cpp/data-in-non-primitive-shape/
description: Aspose.Cellsを使用してGolangとC++で非プリミティブシェイプ内のデータにアクセス・操作
---

## **非原始の形のデータへのアクセス**

時々、ビルトインでない形状からデータにアクセスする必要があります。ビルトインの形状は原始形状と呼ばれ、そうでないものは非原始形状と呼ばれます。例えば、異なる曲線接続線を使用して独自の形状を定義することができます。

## **非原始の形状**

Aspose.Cellsでは、非原始の形状にはタイプ[**AutoShapeType.NotPrimitive**](https://reference.aspose.com/cells/go-cpp/autoshapetype/)が割り当てられます。[**Shape.AutoShapeType**](https://reference.aspose.com/cells/go-cpp/autoshapetype/)プロパティを使用してそのタイプを確認できます。

[**Shape.GetPaths()**](https://reference.aspose.com/cells/go-cpp/shape/getpaths/)プロパティを使用して形状データにアクセスします。これにより、非原始の形状を構成するすべての接続パスが返されます。これらのパスは、各セグメント内のポイントを含むセグメントのリストを保持する[**ShapePath**](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shapepath/)タイプです。

|**非原始の形状の例を示す**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-DataInNonPrimitiveShape.go" >}}
