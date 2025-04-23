---
title: 非原始の形のデータ
type: docs
weight: 500
url: /ja/java/data-in-non-primitive-shape/
---

## **非原始の形のデータへのアクセス**

時々、ビルトインでない形状からデータにアクセスする必要があります。ビルトインの形状は原始形状と呼ばれ、そうでないものは非原始形状と呼ばれます。例えば、異なる曲線接続線を使用して独自の形状を定義することができます。

## **非原始の形状**

Aspose.Cellsでは、非プリミティブ形状にはタイプ[**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/java/com.aspose.cells/autoshapetype#NOT-PRIMITIVE)が割り当てられます。[**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#AutoShapeType)メソッドを使用してタイプを確認できます。

[**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)メソッドを使用して形状データにアクセスします。非プリミティブ形状を構成するすべての接続パスを返します。これらのパスは、各セグメント内の点を含むすべてのセグメントを保持するShapePathのタイプである。

次のコードスニペットは、非プリミティブ形状のパス情報にアクセスする[**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)メソッドの使用例を示しています。

非プリミティブ形状の例を示します 

![todo:image_alt_text](data-in-non-primitive-shape_1.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-NonPrimitiveShape-1.java" >}}
{{< app/cells/assistant language="java" >}}
