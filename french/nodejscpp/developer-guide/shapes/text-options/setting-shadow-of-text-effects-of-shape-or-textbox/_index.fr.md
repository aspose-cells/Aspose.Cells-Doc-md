---  
title: Définir l ombre des effets de texte d une forme ou zone de texte avec Node.js via C++  
linktitle: Définir l ombre des effets de texte de la forme ou de la zone de texte  
type: docs  
weight: 250  
url: /fr/nodejs-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/  
description: Apprenez à définir l ombre des effets de texte pour n importe quelle forme ou zone de texte en utilisant Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Vous pouvez définir l'**Ombré** des **Effets de texte** de n'importe quelle forme ou zone de texte. Veuillez utiliser la propriété [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--). Elle présente le paramètre de texte de la forme et retourne des objets [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting). Après y avoir accédé, veuillez définir l'**Ombre** via la propriété [**FontSetting.getPresetType()**](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--). Cette propriété est de type [**PresetShadowType**](https://reference.aspose.com/cells/nodejs-cpp/presetshadowtype) et possède plusieurs valeurs. Certaines d'entre elles sont  

- DécalageDiagonaleInférieureDroite  
- DécalageBas  
- DécalageDiagonaleSupérieureDroite  
- ÀL'intérieurGauche  
- ÀL'IntérieurCentre  
- DiagonalePerspectiveSupérieureGauche  
- DiagonalePerspectiveInférieureDroite  

{{% /alert %}}  

Le snippet de code suivant démontre l'utilisation de la propriété [**FontSetting.getPresetType()**](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--) pour définir l'ombre des effets de texte de la forme ou zone de texte.  

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
