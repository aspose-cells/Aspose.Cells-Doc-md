---  
title: إضافة أيقونات إلى ورقة العمل باستخدام Node.js عبر C++  
linktitle: إدارة الرموز  
type: docs  
weight: 100  
url: /ar/nodejs-cpp/insert-svg-to-excel/  
---  

## إضافة أيقونات إلى ورقة العمل في Aspose.Cells for Node.js via C++

إذا كنت بحاجة إلى استخدام [Aspose.Cells](https://products.aspose.com/cells/) لإضافة 'رموز' في ملف Excel، فإن هذا المستند يمكن أن يوفر لك بعض المساعدة.

واجهة Excel المقابلة لعملية إدراج الرمز كما يلي:

![](1.png)

- حدد موقع رمز الاختيار ليتم إدراجه في ورقة العمل
- انقر يمينا على *إدراج*->*رموز*
- في النافذة التي تفتح، حدد الرمز في المربع الأحمر في الشكل أعلاه
- انقر بزر الماوس الأيسر *إدراج*، سيتم إدراجه في ملف إكسل.

التأثير كما يلي:

![](2.png)

هنا، قمنا بإعداد *رمز عينة* لمساعدتك على إدراج الأيقونات باستخدام [Aspose.Cells](https://products.aspose.com/cells/). يوجد أيضًا [ملف عينة](sample.xlsx) ضروري وملف [موارد الأيقونة](icon.zip). استخدمنا واجهة إكسل لإدراج أيقونة بنفس تأثير العرض كما هو في [ملف الموارد](icon.zip) في [ملف العينة](sample.xlsx).

### Node.js

```javascript
const fs = require("fs");
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "sample.xlsx");

// Read icon resource file data
const fileName = path.join(dataDir, "icon.svg");
const bytes = fs.readFileSync(fileName).buffer;

// Loads the workbook which contains hidden external links
const workbook = new AsposeCells.Workbook(filePath);

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the icon to the worksheet
sheet.getShapes().addIcons(3, 0, 7, 0, 100, 100, bytes, null);

// Set a prompt message
const c = sheet.getCells().get(8, 7);
c.putValue("Insert via Aspose.Cells");
const s = c.getStyle();
s.getFont().setColor(AsposeCells.Color.Blue);
c.setStyle(s);

// Save. You can check your icon in this way.
workbook.save("sample2.xlsx", AsposeCells.SaveFormat.Xlsx);
```

عند تنفيذ الكود أعلاه في مشروعك، ستحصل على النتائج التالية:

![](3.png)  

{{< app/cells/assistant language="nodejs-cpp" >}}
