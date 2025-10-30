---  
title: Node.js kullanarak C++ ile Şekil veya Metin Kutusu nun Metin Efektlerinin Gölgesini Ayarla  
linktitle: Şekil veya Metin Kutusunun Metin Efektlerinin Gölgesini Ayarlama  
type: docs  
weight: 250  
url: /tr/nodejs-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/  
description: Aspose.Cells for Node.js via C++ kullanarak herhangi bir şekil veya Metin Kutusu için metin efektlerinin gölgesini nasıl ayarlayacağınızı öğrenin.  
---  

{{% alert color="primary" %}}  

Herhangi bir Şekil veya Metin Kutusu'nun **Metin Efektleri** gölgesini ayarlayabilirsiniz. Lütfen [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--) özelliğini kullanın. Bu özellik şeklin metninin ayarını gösterir ve [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting) nesnelerini döner. Ona eriştikten sonra, lütfen **Gölge**yi [**FontSetting.getPresetType()**](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--) özelliği aracılığıyla ayarlayın. Bu özellik [**PresetShadowType**](https://reference.aspose.com/cells/nodejs-cpp/presetshadowtype) türündedir ve birkaç değere sahiptir, bunlardan bazıları  

- Dikey Sağa Ofset  
- Alt Ofset  
- OffsetDiagonalTopRight  
- InsideLeft  
- InsideCenter  
- PerspectiveDiagonalUpperLeft  
- PerspectiveDiagonalLowerRight  

{{% /alert %}}  

Aşağıdaki kod parçası, Shape veya TextBox'un metin efektleri gölgesini ayarlamak için [**FontSetting.getPresetType()**](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--) özelliğinin kullanımını gösterir.  

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
