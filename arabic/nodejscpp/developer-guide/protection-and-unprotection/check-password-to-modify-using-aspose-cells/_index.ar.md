---  
title: التحقق من كلمة المرور للتعديل باستخدام Aspose.Cells for Node.js via C++  
linktitle: التحقق من كلمة المرور للتعديل  
type: docs  
weight: 2400  
url: /ar/nodejs-cpp/check-password-to-modify-using-aspose-cells/  
description: تعلم كيف تتحقق مما إذا كانت كلمة المرور للتعديل تطابق باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
أحيانًا، تحتاج إلى التحقق من أن كلمة المرور المعطاة تتطابق مع **كلمة المرور للتعديل** برمجياً. يوفر Aspose.Cells طريقة `WorkbookSettings.writeProtection.validatePassword()` التي يمكنك استخدامها للتحقق مما إذا كانت كلمة المرور للتعديل صحيحة أم لا.  
{{% /alert %}}  

## **التحقق من كلمة المرور للتعديل في Microsoft Excel**  

يمكنك تعيين **كلمة السر للفتح** و**كلمة السر للتعديل** أثناء إنشاء جداول البيانات الخاصة بك في Microsoft Excel. يُرجى الرجوع إلى هذا اللقط الشاشة الذي يظهر واجهة Microsoft Excel المُقدمة لتحديد هذه الكلمات السرية.  

|![todo:image_alt_text](check-password-to-modify-using-aspose-cells_1.png)|  
| :- |  

## **التحقق من كلمة المرور للتعديل باستخدام Aspose.Cells for Node.js via C++**  

يحمّل الأمثلة التالية ملف Excel المصدر (5112232.xlsx). يحتوي على كلمة مرور عند الفتح وهي 1234 وكلمة مرور للتعديل وهي 5678. يبحث الكود أولاً عن صحة كلمة المرور 567 ويعيد false، ثم يبحث عن كلمة المرور 5678 ويعيد true.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Specify password to open inside the load options
const opts = new AsposeCells.LoadOptions();
opts.setPassword("1234");

// Open the source Excel file with load options
const workbook = new AsposeCells.Workbook(path.join(dataDir, "sampleBook.xlsx"), opts);

// Check if 567 is Password to modify
let ret = workbook.getSettings().getWriteProtection().validatePassword("567");
console.log("Is 567 correct Password to modify: " + ret);

// Check if 5678 is Password to modify
ret = workbook.getSettings().getWriteProtection().validatePassword("5678");
console.log("Is 5678 correct Password to modify: " + ret);
```  

### **مخرجات الوحدة**  

إليك مخرجات الكونسول للشيفرة العينة أعلاه بعد تحميل ملف الإكسل المصدري.  

{{< highlight java >}}  
Is 567 correct Password to modify: False  
Is 5678 correct Password to modify: True  
{{< /highlight >}}  
{{< app/cells/assistant language="nodejs-cpp" >}}
