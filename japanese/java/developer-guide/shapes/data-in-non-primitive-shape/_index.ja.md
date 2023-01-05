---
title: 非プリミティブ形状のデータ
type: docs
weight: 500
url: /ja/java/data-in-non-primitive-shape/
---
## **非プリミティブ形状のデータへのアクセス**

組み込みではない図形からデータにアクセスする必要がある場合があります。組み込みシェイプはプリミティブ シェイプと呼ばれます。そうでないものは、非プリミティブと呼ばれます。たとえば、さまざまな曲線を接続した線を使用して、独自の形状を定義できます。

## **非原始的な形状**

Aspose.Cells では、非プリミティブ シェイプにタイプが割り当てられます。[**AutoShapeType.NOT_PRIMITIVE**](https://reference.aspose.com/cells/java/com.aspose.cells/autoshapetype#NOT_PRIMITIVE) .を使用してそれらのタイプを確認できます[**Shape.getAutoShapeType()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#AutoShapeType)方法。

を使用して形状データにアクセスします。[**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)方法。非プリミティブ形状を構成するすべての接続されたパスを返します。これらのパスは、各セグメントのポイントを含むすべてのセグメントのリストを保持する ShapePath タイプです。

次のコード スニペットは、[**Shape.getPaths()**](https://reference.aspose.com/cells/java/com.aspose.cells/shape#Paths)非プリミティブ形状のパス情報にアクセスするメソッド。

**非プリミティブ形状の例を示します** 

![todo:画像_代替_文章](data-in-non-primitive-shape_1.jpg)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-AsposeCellsExamples-DrawingObjects-NonPrimitiveShape-1.java" >}}
