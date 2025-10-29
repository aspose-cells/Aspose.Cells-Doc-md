---  
title: تعيين الظل لتأثيرات النص في الشكل أو مربع النص باستخدام Node.js عبر C++  
linktitle: ضبط الظلال لتأثيرات النص للشكل أو مربع النص  
type: docs  
weight: 250  
url: /ar/nodejs-cpp/setting-shadow-of-text-effects-of-shape-or-textbox/  
description: تعلم كيف تضبط ظل تأثيرات النص لأي شكل أو مربع نص باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

يمكنك ضبط **ظل** **تأثيرات النص** لأي شكل أو مربع نص. يرجى استخدام خاصية [**Shape.getTextBody()**](https://reference.aspose.com/cells/nodejs-cpp/shape/#getTextBody--). تقدم إعداد النص الخاص بالشكل وتعيد كائنات من نوع [**FontSetting**](https://reference.aspose.com/cells/nodejs-cpp/fontsetting). بعد الوصول إليه، يرجى ضبط **الظل** عبر خاصية [**FontSetting.getPresetType()**](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--). هذه الخاصية من نوع [**PresetShadowType**](https://reference.aspose.com/cells/nodejs-cpp/presetshadowtype) الذي يحتوي على عدة قيم. بعض هذه القيم:  

- إزاحة قطرية لأسفل اليمين  
- إزاحة لأسفل  
- إزاحة قطرية لأعلى اليمين  
- داخل اليسار  
- داخل الوسط  
- زاوية رؤية قطرية العلوي الأيسر  
- زاوية رؤية قطرية السفلي الأيمن  

{{% /alert %}}  

يُظهر مقتطف الكود التالي استخدام خاصية [**FontSetting.getPresetType()**](https://reference.aspose.com/cells/nodejs-cpp/shadoweffect/#getPresetType--) لضبط ظل تأثيرات النص في الشكل أو مربع النص.  

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
