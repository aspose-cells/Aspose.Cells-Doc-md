---  
title: تحويل التواريخ إلى تواريخ يابانية باستخدام Node.js عبر C++  
linktitle: تحويل التواريخ إلى تواريخ يابانية  
type: docs  
weight: 350  
url: /ar/nodejs-cpp/convert-dates-to-japanese-dates/  
description: تعلم كيفية تحويل تواريخ الميلادي إلى التواريخ اليابانية باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  

في التقويم الياباني، تبدأ حقبة جديدة مع تولي إمبراطور جديد. في 1 مايو 2019، تولى إمبراطور جديد السلطة حيث انتهت حقبة هيسي وبدأت حقبة ريوا.  

{{% /alert %}}  

توفر Aspose.Cells وسيلة لتحويل تواريخ الميلادي إلى تواريخ يابانية. أثناء هذا التحويل، يتم أيضًا أخذ تغييرات العهد في الاعتبار. يُحوّل مقتطف الكود التالي ملف [Excel المصدر](90112015.xlsx) الذي يحتوي على تواريخ ميلادية إلى ملف [PDF الناتج](90112016.pdf) بتواريخ يابانية كما هو موضح في الصورة أدناه.  

![todo:image_alt_text](convert-dates-to-japanese-dates_1.jpg)  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// Source directory
const sourceDir = path.join(__dirname, "data");

// Output directory
const outputDir = path.join(__dirname, "output");

const options = new AsposeCells.LoadOptions(AsposeCells.LoadFormat.Xlsx);
options.setLanguageCode(AsposeCells.CountryCode.Japan);
options.setRegion(AsposeCells.CountryCode.Japan);

const workbook = new AsposeCells.Workbook(path.join(sourceDir, "JapaneseDates.xlsx"), options);
workbook.save(outputDir + "JapaneseDates.pdf", AsposeCells.SaveFormat.Pdf);
```  

{{< app/cells/assistant language="nodejs-cpp" >}}
