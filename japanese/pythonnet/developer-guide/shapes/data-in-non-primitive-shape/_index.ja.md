---
title: 非原始の形のデータ
type: docs
weight: 300
url: /ja/python-net/data-in-non-primitive-shape/
description: この記事では、Aspose.Cells for Python via .NET APIを使用して非プリミティブ形状のデータを表示する方法を説明します。
keywords: Python Excelライブラリ、非プリミティブ形状のデータ、非プリミティブ形状のデータへのアクセス方法。
---

## **非原始の形のデータへのアクセス**

時々、ビルトインでない形状からデータにアクセスする必要があります。ビルトインの形状は原始形状と呼ばれ、そうでないものは非原始形状と呼ばれます。例えば、異なる曲線接続線を使用して独自の形状を定義することができます。

## **非原始の形状**

Aspose.Cells for Python via .NETでは、非プリミティブ形状に[**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/autoshapetype)タイプが割り当てられます。[**Shape.auto_shape_type**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/auto_shape_type)プロパティを使用してそのタイプを確認できます。

[**Shape.paths**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shape/paths)プロパティを使用して形状データにアクセスします。これにより、非原始の形状を構成するすべての接続パスが返されます。これらのパスは、各セグメント内のポイントを含むセグメントのリストを保持する[**ShapePath**](https://reference.aspose.com/cells/python-net/aspose.cells.drawing/shapepath)タイプです。

|**非原始の形状の例を示す**|
| :- |
|![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)|

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-AccessNonPrimitiveShape-1.py" >}}
