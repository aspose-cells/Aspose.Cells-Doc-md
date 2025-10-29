---
title: 用C++的Golang处理Shape或Chart的反射效果
linktitle: 处理形状或图表的倒影效果
type: docs
weight: 210
url: /zh/go-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: 学习如何用Aspose.Cells和C++的Golang处理Shape或Chart的反射效果
---

## **可能的使用场景**
Aspose.Cells 提供 [Shape.Reflection](https://reference.aspose.com/cells/go-cpp/shape/getreflection/) 属性和 [ReflectionEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/) 类，用于处理形状或图表的反射效果。 [ReflectionEffect](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/reflectioneffect/) 类包含以下属性，可以根据应用需求设置以达到不同的效果。

- [模糊](https://reference.aspose.com/cells/go-cpp/reflectioneffect/getblur/)
- [方向](https://reference.aspose.com/cells/go-cpp/reflectioneffect/getdirection/)
- [距离](https://reference.aspose.com/cells/go-cpp/reflectioneffect/getdistance/)
- [渐变方向](https://reference.aspose.com/cells/go-cpp/reflectioneffect/getfadedirection/)
- [随形状旋转](https://reference.aspose.com/cells/go-cpp/reflectioneffect/getrotwithshape/)
- [大小](https://reference.aspose.com/cells/go-cpp/reflectioneffect/getsize/)
- [透明度](https://reference.aspose.com/cells/go-cpp/reflectioneffect/gettransparency/)
- [类型](https://reference.aspose.com/cells/go-cpp/reflectioneffect/gettype/)

## **使用形状或图表的反射效果**
以下示例代码加载[源Excel文件](5115424.xlsx)，访问默认工作表中的第一个形状，设置[Shape.Reflection](https://reference.aspose.com/cells/cpp/aspose.cells.drawing/shape/getreflection/)类的不同属性，然后将工作簿保存为[输出Excel文件](5115423.xlsx)。

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-WorkingWithTheReflectionEffectOfShapeOrChart.go" >}}
