---  
title: 使用Node.js通过C++设置形状或文本框的文本效果阴影  
linktitle: 设置形状或文本框的文本效果的阴影  
type: docs  
weight: 250  
url: /zh/nodejs-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/  
description: 了解如何使用Aspose.Cells for Node.js via C++设置任何形状或文本框的文本效果阴影。  
---  

{{% alert color="primary" %}}  

您可以使用[**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--)属性设置任何形状或文本框的**文本效果**的**阴影**。访问后，请通过[**FontSetting.getPresetType()**](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--)属性设置阴影，该属性属于[**PresetShadowType**](https://reference.aspose.com/cells/nodejs-cpp/presetshadowtype)类型，具有多种值，包括....  

- 偏移对角线底部右  
- 偏移底部  
- 偏移对角线顶部右  
- 内部左  
- 内部中心  
- 透视对角线左上  
- 透视对角线右下  

{{% /alert %}}  

以下代码片段演示了如何使用[**FontSetting.getPresetType()**](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--)属性为形状或文本框设置文本效果的阴影。  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Output directory
const outputDir = path.join(__dirname, "output");

// Create workbook object
const wb = new AsposeCells.Workbook();

// Access first worksheet
const ws = wb.getWorksheets().get(0);

// Add text box with these dimensions
const tb = ws.getShapes().addTextBox(2, 0, 2, 0, 100, 400);

// Set the text of the textbox
tb.setText("This text has the following settings.\n\nText Effects > Shadow > Offset Bottom");

// Set all the text runs shadow to preset offset bottom
for (let i = 0; i < tb.getTextBody().getCount(); i++) {
tb.getTextBody().get(i).getTextOptions().getShadow().setPresetType(AsposeCells.PresetShadowType.OffsetBottom);
}

// Set the font color and size of the textbox
tb.getFont().setColor(AsposeCells.Color.Red);
tb.getFont().setSize(16);

// Save the output file
wb.save(path.join(outputDir, "outputSettingTextEffectsShadowOfShapeOrTextbox.xlsx"), AsposeCells.SaveFormat.Xlsx);
```  

