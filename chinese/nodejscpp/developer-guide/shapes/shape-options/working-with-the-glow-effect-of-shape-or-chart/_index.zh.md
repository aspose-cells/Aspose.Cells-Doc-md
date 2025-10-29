---  
title: 处理形状或图表的发光效果的工作流程  
linktitle: 处理形状或图表的发光效果  
type: docs  
weight: 240  
url: /zh/nodejs-cpp/working-with-the-glow-effect-of-shape-or-chart/  
description: 学习如何用 Aspose.Cells for Node.js via C++ 在 Node.js 中操作形状或图表的发光效果  
---  

## **可能的使用场景**  
Aspose.Cells 提供 [Shape.getGlow()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGlow--) 属性和 [GlowEffect](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/) 类，用于处理形状或图表的发光效果。 [GlowEffect](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/) 类含有多个属性，可根据应用需求设置以实现不同效果。  

- [GlowEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getSize--)  
- [GlowEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getTransparency--)  
- [GlowEffect.getColor()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getColor--)  

## **处理形状或图表的发光效果**  
以下示例代码加载[源Excel文件](5115407.xlsx)，访问第一个工作表中的第一个形状，并设置[Shape.getGlow()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGlow--)属性的子属性，然后将工作簿保存为[输出Excel文件](5115414.xlsx)。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load your source excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Set the glow effect of the shape, Set its Size and Transparency properties
const glowEffect = shape.getGlow();
glowEffect.setSize(30);
glowEffect.setTransparency(0.4);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
