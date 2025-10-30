---  
title: Schlagschatten der Texteffekte einer Form oder Textbox mit Node.js über C++ einstellen  
linktitle: Einstellen des Schattens von Texteffekten von Form oder TextBox  
type: docs  
weight: 250  
url: /de/nodejs-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/  
description: Lernen Sie, wie man den Schatten der Texteffekte für jede Form oder Textbox mit Aspose.Cells for Node.js via C++ einstellt.  
---  

{{% alert color="primary" %}}  

Sie können den **Schatten** der **Texteffekte** jeder Form oder Textbox festlegen. Bitte verwenden Sie die [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--)-Eigenschaft. Sie zeigt die Einstellung des Texts der Form an und gibt [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting)-Objekte zurück. Nach dem Zugriff legen Sie den **Schatten** über die [**FontSetting.getPresetType()**](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--)-Eigenschaft fest. Diese Eigenschaft ist vom Typ [**PresetShadowType**](https://reference.aspose.com/cells/nodejs-cpp/presetshadowtype) und hat mehrere Werte. Einige davon sind  

- OffsetDiagonal-unten-rechts  
- OffsetBottom  
- OffsetDiagonal-oben-rechts  
- Innen-links  
- Innen-mitte  
- PerspektiveDiagonalObenLinks  
- PerspektiveDiagonalUntenRechts  

{{% /alert %}}  

Das folgende Codesnippet zeigt die Verwendung der [**FontSetting.getPresetType()**](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--)-Eigenschaft zum Festlegen des Schattens der Texteffekte von Shape oder TextBox.  

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
