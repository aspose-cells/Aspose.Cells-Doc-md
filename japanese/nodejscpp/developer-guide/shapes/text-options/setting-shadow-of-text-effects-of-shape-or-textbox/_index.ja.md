---  
title: シェイプやテキストボックスのシャドウの設定方法（Node.jsとC++）  
linktitle: シェイプまたはテキストボックスのテキスト効果の影の設定  
type: docs  
weight: 250  
url: /ja/nodejs-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/  
description: Aspose.Cells for Node.js via C++を使用して、任意のシェイプやテキストボックスのテキスト効果のシャドウを設定する方法を学びます。  
---  

{{% alert color="primary" %}}  

どのシェイプまたはテキストボックスの「テキスト効果」のシャドウを設定できます。[**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--)プロパティを使用してください。これはシェイプのテキスト設定を示し、[**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting)オブジェクトを返します。それにアクセスした後、[**FontSetting.getPresetType()**](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--) プロパティを通じて**Shadow**を設定してください。このプロパティは [**PresetShadowType**](https://reference.aspose.com/cells/nodejs-cpp/presetshadowtype) 型で、いくつかの値を持ちます。  

- DiagonalBottomRightのOffset  
- ボトムのオフセット  
- DiagonalTopRightのOffset  
- 左内部  
- 中央内部  
- PerspectiveDiagonalUpperLeft  
- PerspectiveDiagonalLowerRight  

{{% /alert %}}  

以下のコードスニペットは、[**FontSetting.getPresetType()**](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--) プロパティを使用してShapeまたはTextBoxのテキスト効果のシャドウを設定する例です。  

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
