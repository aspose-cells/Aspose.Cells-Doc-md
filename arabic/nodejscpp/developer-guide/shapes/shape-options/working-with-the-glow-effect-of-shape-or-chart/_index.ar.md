---  
title: العمل مع تأثير التوهج للشكل أو الرسم البياني باستخدام Node.js عبر C++  
linktitle: العمل مع تأثير التوهج الداخلي للشكل أو الرسم البياني  
type: docs  
weight: 240  
url: /ar/nodejs-cpp/working-with-the-glow-effect-of-shape-or-chart/  
description: تعلم كيف تتعامل مع تأثير التوهج للأشكال أو الرسوم البيانية في Node.js باستخدام Aspose.Cells for Node.js via C++.  
---  

## **سيناريوهات الاستخدام المحتملة**  
 تقدم Aspose.Cells الخاصية [Shape.getGlow()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGlow--) مع فئة [GlowEffect](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/) للعمل مع تأثير التوهج للشكل أو الرسم البياني. تحتوي فئة [GlowEffect](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/) على الخصائص التالية التي يمكن ضبطها لتحقيق نتائج مختلفة حسب متطلبات التطبيق.  

- [GlowEffect.getSize()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getSize--)  
- [GlowEffect.getTransparency()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getTransparency--)  
- [GlowEffect.getColor()](https://reference.aspose.com/cells/nodejs-cpp/gloweffect/#getColor--)  

## **العمل مع تأثير التوهج الداخلي للشكل أو الرسم البياني**  
يحمّل الكود النموذجي التالي ملف Excel المصدر (5115407.xlsx) ويصل إلى الشكل الأول في ورقة العمل الأولى ويضبط الخاصيات الفرعية لخصائص [Shape.getGlow()](https://reference.aspose.com/cells/nodejs-cpp/shape/#getGlow--) ثم يحفظ المصنف في ملف Excel الناتج (5115414.xlsx).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");
// Load your source excel file
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet
const worksheet = workbook.getWorksheets().get(0);

// Access first shape
const shape = worksheet.getShapes().get(0);

// Set the glow effect of the shape, Set its Size and Transparency properties
const glowEffect = shape.getGlow();
glowEffect.setSize(30);
glowEffect.setTransparency(0.4);

// Save the workbook in xlsx format
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  
{{< app/cells/assistant language="nodejs-cpp" >}}
