---  
title: Ställa in Skuggning av Text Effekter för Form eller TextBox med Node.js via C++  
linktitle: Inställning av skugga för texteffekter av form eller textruta  
type: docs  
weight: 250  
url: /sv/nodejs-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/  
description: Lär dig hur du ställer in skugga för text effekter för vilken form eller TextBox som helst med Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Du kan ställa in **Skugga** för **Text Effekter** för vilken form eller TextBox som helst. Använd [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--)-egenskapen. Den visar inställningen av formens text och returnerar [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting)-objekt. När du har fått tillgång till den, ställ in **Skugga** via [**FontSetting.getPresetType()**](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--)-egenskapen. Denna egenskap är av typen [**PresetShadowType**](https://reference.aspose.com/cells/nodejs-cpp/presetshadowtype) och har flera värden. Några av dessa är  

- OffsetDiagonalBottomRight  
- OffsetBottom  
- OffsetDiagonalTopRight  
- InsideLeft  
- InsideCenter  
- PerspectiveDiagonalUpperLeft  
- PerspectiveDiagonalLowerRight  

{{% /alert %}}  

Följande kodexempel demonstrerar användningen av [**FontSetting.getPresetType()**](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--)-egenskapen för att ställa in skuggan för textstilar på form eller textruta.  

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

{{< app/cells/assistant language="nodejs-cpp" >}}
