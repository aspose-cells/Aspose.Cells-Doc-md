---  
title: Установка тени эффектов текста для фигуры или текстового поля с помощью Node.js через C++  
linktitle: Установка тени текстовых эффектов формы или текстового поля  
type: docs  
weight: 250  
url: /ru/nodejs-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/  
description: Изучите, как установить тень эффектов текста для любой фигуры или текстового поля с помощью Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

Вы можете установить **Тень** эффекта **Текстовых эффектов** любой фигуры или текстового поля. Пожалуйста, используйте свойство [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--). Оно представляет настройку текста фигуры и возвращает объекты [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting). После получения доступа установите **Тень** через свойство [**FontSetting.getPresetType()**](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--). Это свойство типа [**PresetShadowType**](https://reference.aspose.com/cells/nodejs-cpp/presetshadowtype), которое имеет несколько значений. Некоторые из них  

- Смещение по диагонали вниз и вправо  
- Смещение вниз  
- Смещение по диагонали вверх и вправо  
- Слева внутри  
- По центру внутри  
- Диагональная перспектива вверху слева  
- ПерспективаДиагональНижнийПравый  

{{% /alert %}}  

Следующий фрагмент кода демонстрирует использование свойства [**FontSetting.getPresetType()**](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--) для установки тени эффектов текста фигуры или текстового поля.  

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

