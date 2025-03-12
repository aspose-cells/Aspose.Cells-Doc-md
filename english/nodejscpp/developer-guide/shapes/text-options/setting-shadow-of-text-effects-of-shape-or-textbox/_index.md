---  
title: Setting Shadow of Text Effects of Shape or TextBox with Node.js via C++  
linktitle: Setting Shadow of Text Effects of Shape or TextBox  
type: docs  
weight: 250  
url: /nodejs-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/  
description: Learn how to set the shadow of text effects for any shape or TextBox using Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

You can set the **Shadow** of **Text Effects** of any Shape or TextBox. Please use the [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--) property. It presents the setting of the shape's text and returns [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) objects. After accessing it, please set the **Shadow** via [**FontSetting.getPresetType()**](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--) property. This property is of the type [**PresetShadowType**](https://reference.aspose.com/cells/nodejs-cpp/presetshadowtype) which has several values. Some of these are  

- OffsetDiagonalBottomRight  
- OffsetBottom  
- OffsetDiagonalTopRight  
- InsideLeft  
- InsideCenter  
- PerspectiveDiagonalUpperLeft  
- PerspectiveDiagonalLowerRight  

{{% /alert %}}  

The following code snippet demonstrates the use of [**FontSetting.getPresetType()**](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--) property to set shadow of text effects of Shape or TextBox.  

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
  