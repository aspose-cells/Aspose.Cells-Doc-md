---  
title: 通过Node.js使用C++处理Shape或Chart的阴影效果  
linktitle: 使用形状或图表的阴影效果  
type: docs  
weight: 220  
url: /zh/nodejs-cpp/working-with-the-shadow-effect-of-shape-or-chart/  
description: 学习如何使用Aspose.Cells for Node.js via C++处理形状或图表的阴影效果。  
---  

## **可能的使用场景**  
Aspose.Cells for Node.js via C++提供[Shape.getShadowEffect()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getShadowEffect--)属性和[ShadowEffect](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect)类，用于处理形状或图表的阴影效果。[ShadowEffect](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect)类包含若干属性，可根据应用需求设置以实现不同效果。  

- [ShadowEffect.getAngle()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getAngle--)  
- [ShadowEffect.getBlur()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getBlur--)  
- [ShadowEffect.getColor()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getColor--)  
- [ShadowEffect.getDistance()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getDistance--)  
- [ShadowEffect.getPresetType()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--)  
- [ShadowEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getSize--)  
- [ShadowEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getTransparency--)  

## **使用 Aspose.Cells 处理形状或图表的阴影效果**  
以下示例代码加载[源Excel文件](5115425.xlsx)，访问第一个工作表中的第一个形状，设置[Shape.getShadowEffect()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getShadowEffect--)属性的子属性，然后将工作簿保存为[输出Excel文件](5115411.xlsx)。  

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

// Set the shadow effect of the shape, set its Angle, Blur, Distance and Transparency properties
const shadowEffect = shape.getShadowEffect();
shadowEffect.setAngle(150);
shadowEffect.setBlur(4);
shadowEffect.setDistance(45);
shadowEffect.setTransparency(0.3);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
