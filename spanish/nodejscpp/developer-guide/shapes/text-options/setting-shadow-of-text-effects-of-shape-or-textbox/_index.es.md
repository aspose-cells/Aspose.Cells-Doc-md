---  
title: Configurar sombra de efectos de texto de forma o cuadro de texto con Node.js vía C++  
linktitle: Establecer sombra de efectos de texto de forma o cuadro de texto  
type: docs  
weight: 250  
url: /es/nodejs-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/  
description: Aprende cómo establecer la sombra de los efectos de texto para cualquier forma o cuadro de texto usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Puedes establecer la **Sombra** de los **Efectos de texto** de cualquier forma o cuadro de texto. Por favor, usa la propiedad [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--). Esta presenta la configuración del texto de la forma y devuelve objetos [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting). Después de acceder a ella, configura la **Sombra** mediante la propiedad [**FontSetting.getPresetType()**](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--). Esta propiedad es del tipo [**PresetShadowType**](https://reference.aspose.com/cells/nodejs-cpp/presetshadowtype) y tiene varios valores. Algunos de ellos son  

- Diagonal inferior derecha  
- Inferior  
- Diagonal superior derecha  
- Interior izquierdo  
- Centro interior  
PerspectiveDiagonalUpperLeft  
PerspectiveDiagonalLowerRight  

{{% /alert %}}  

El siguiente fragmento de código demuestra el uso de la propiedad [**FontSetting.getPresetType()**](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--) para establecer la sombra de efectos de texto de Forma o Cuadro de texto.  

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
