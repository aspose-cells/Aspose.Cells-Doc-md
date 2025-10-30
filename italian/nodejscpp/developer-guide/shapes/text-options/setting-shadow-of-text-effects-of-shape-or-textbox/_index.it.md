---  
title: Impostare l ombra sugli effetti di testo di forma o casella di testo con Node.js via C++  
linktitle: Impostazione dell ombra degli effetti di testo della forma o del riquadro di testo  
type: docs  
weight: 250  
url: /it/nodejs-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/  
description: Impara come impostare l ombra sugli effetti di testo per qualsiasi forma o casella di testo usando Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Puoi impostare l'**Ombra** degli **Effetti di Testo** di qualsiasi Forma o Casella di Testo. Usa la proprietà [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--). Essa rappresenta l'impostazione del testo della forma e ritorna gli oggetti [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting). Dopo averla accessibile, imposta l'**Ombra** tramite la proprietà [**FontSetting.getPresetType()**](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--). Questa proprietà è di tipo [**PresetShadowType**](https://reference.aspose.com/cells/nodejs-cpp/presetshadowtype) che ha diversi valori, alcuni dei quali sono  

- DiagonaleOffsetInferioreDestra  
- OffsetInferiore  
- DiagonaleOffsetSuperioreDestra  
- SinistraInterno  
- CentroInterno  
- DiagonaleSuperioreSinistraProspettiva  
- DiagonaleInferioreDestraProspettiva  

{{% /alert %}}  

Il seguente frammento di codice dimostra l'uso della proprietà [**FontSetting.getPresetType()**](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--) per impostare l'ombra sugli effetti di testo di Forma o Casella di Testo.  

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
