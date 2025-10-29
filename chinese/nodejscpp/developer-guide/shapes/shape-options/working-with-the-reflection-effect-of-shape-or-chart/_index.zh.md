---
title: 通过Node.js使用C++处理Shape或Chart的反射效果
linktitle: 处理形状或图表的倒影效果
type: docs
weight: 210
url: /zh/nodejs-cpp/working-with-the-reflection-effect-of-shape-or-chart/
description: 学习如何使用Aspose.Cells for Node.js via C++处理形状或图表的反射效果。设置各种反射属性以达到预期效果。
---

## **可能的使用场景**
Aspose.Cells for Node.js via C++提供[Shape.getReflection()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getReflection--)属性和[ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect)类，用于处理形状或图表的反射效果。 [ReflectionEffect](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect)类包含若干属性，可根据应用需求设置以实现不同效果。

- [ReflectionEffect.getBlur()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getBlur--)
- [ReflectionEffect.getDirection()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getDirection--)
- [ReflectionEffect.getDistance()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getDistance--)
- [ReflectionEffect.getFadeDirection()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getFadeDirection--)
- [ReflectionEffect.getRotWithShape()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getRotWithShape--)
- [ReflectionEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getSize--)
- [ReflectionEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getTransparency--)
- [ReflectionEffect.getType()](https://reference.aspose.com/cells/nodejs-cpp/reflectioneffect/#getType--)

## **使用形状或图表的反射效果**
以下示例代码加载[源Excel文件](5115424.xlsx)，访问第一个工作表中的第一个形状，设置[Shape.getReflection()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getReflection--)属性的子属性，然后将工作簿保存为[输出Excel文件](5115423.xlsx)。

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source excel file
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sample.xlsx"));

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Set the reflection effect of the shape, set its Blur, Size, Transparency and Distance properties
const reflectionEffect = shape.getReflection();
reflectionEffect.setBlur(30);
reflectionEffect.setSize(90);
reflectionEffect.setTransparency(0);
reflectionEffect.setDistance(80);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
