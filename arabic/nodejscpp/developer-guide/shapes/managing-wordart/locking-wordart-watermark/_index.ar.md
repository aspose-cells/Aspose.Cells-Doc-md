---  
title: قفل علامة مائية WordArt باستخدام Node.js عبر C++  
linktitle: قفل علامة الماؤ  
type: docs  
weight: 170  
url: /ar/nodejs-cpp/locking-wordart-watermark/  
description: تعلم كيفية قفل العلامات المائية WordArt في Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

 تسمح واجهات برمجة التطبيقات Aspose.Cells بإضافة علامات مائية WordArt على ورقة العمل بطريقة تجعل WordArt ككائن يمكنك تحريكه وتوضيحه على ورقة العمل. من الممكن أيضًا قفل الكائن WordArt لأي تفاعل مثل التحرير، التحريك والتحديد. يشرح هذا المقال استخدام طريقة [**Shape.setLockedProperty(ShapeLockType, boolean)**](https://reference.aspose.com/cells/nodejs-cpp/shape/#setLockedProperty-shapelocktype-boolean-) لقفل بعض جوانب العلامة المائية.

{{% /alert %}}  

 تسمح واجهات برمجة التطبيقات Aspose.Cells بقفل جوانب معينة من العلامة المائية بحيث يمكن تقييد أو حظر تفاعل المستخدم تمامًا. يوضح مقتطف الكود التالي استخدام Aspose.Cells for Node.js via C++ لقفل تحديد، تحريك، تحرير وتغيير حجم العلامة المائية من خلال إنشاء جدول بيانات من الصفر.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Instantiate a new Workbook
const workbook = new AsposeCells.Workbook();

// Get the first default sheet
const sheet = workbook.getWorksheets().get(0);

// Add Watermark
const wordart = sheet.getShapes().addTextEffect(AsposeCells.MsoPresetTextEffect.TextEffect1,
"CONFIDENTIAL", "Arial Black", 50, false, true, 18, 8, 1, 1, 130, 800);

// Lock Shape Aspects
wordart.setIsLocked(true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Selection, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.ShapeType, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Move, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Resize, true);
wordart.setLockedProperty(AsposeCells.ShapeLockType.Text, true);

// Get the fill format of the word art
const wordArtFormat = wordart.getFill();

// Set the color
wordArtFormat.setOneColorGradient(AsposeCells.Color.Red, 0.2, AsposeCells.GradientStyleType.Horizontal, 2);

// Set the transparency
wordArtFormat.setTransparency(0.9);

// Make the line invisible
wordart.setHasLine(false);

// Save the file
workbook.save(path.join(dataDir, "output_out.xlsx"));
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
