---  
title: حماية وإلغاء حماية ورقة العمل باستخدام Node.js عبر C++  
linktitle: حماية وإلغاء الحماية لورق العمل  
type: docs  
weight: 40  
url: /ar/nodejs-cpp/protect-and-unprotect-worksheets/  
description: حماية وإلغاء حماية ورقة العمل لملفات إكسل باستخدام Aspose.Cells for Node.js via C++.  
---  

{{% alert color="primary" %}}  
لمنع مستخدمين آخرين من تغيير البيانات في ورقة العمل عن طريق الخطأ أو بشكل متعمد، يمكنك قفل الخلايا في ورقة العمل الخاصة بك ثم حماية الورقة بكلمة مرور.  
{{% /alert %}}  

## **حماية وإلغاء حماية ورقة العمل في MS Excel**  

**![حماية وإلغاء حماية ورقة العمل](protect-and-unprotect-worksheet.png)**  

١. انقر فوق **مراجعة > حماية ورقة عمل**.  
١. أدخل كلمة مرور في **مربع الكلمة السرية**.  
١. حدد خيارات **السماح**.  
١. حدد **موافق**, أدخل كلمة المرور مرة أخرى لتأكيدها، ثم حدد **موافق** مجددًا.  

## **حماية ورقة العمل باستخدام Aspose.Cells for Node.js via C++**  
متطلبات الترميز البسيطة التالية فقط لتنفيذ حماية هيكل دفتر العمل لملفات Excel.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
// Create a new file.
const workbook = new AsposeCells.Workbook();
// Gets the first worksheet.
const sheet = workbook.getWorksheets().get(0);
// Protect contents of the worksheet.
sheet.protect(AsposeCells.ProtectionType.Contents);
// Protect worksheet with password.
sheet.getProtection().setPassword("test");
// Save as Excel file.
workbook.save("Book1.xlsx");
```  

## **إلغاء حماية ورقة العمل باستخدام Aspose.Cells for Node.js via C++**  
سهولة إلغاء حماية ورقة العمل باستخدام API Aspose.Cells. إذا كانت ورقة العمل محمية بكلمة مرور، يتطلب الأمر كلمة مرور صحيحة.  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "Book1.xlsx");
// Create a new file.
const workbook = new AsposeCells.Workbook(filePath);
// Gets the first worksheet.
const sheet = workbook.getWorksheets().get(0);
// Protect contents of the worksheet.
sheet.unprotect("password");
// Save Excel file.
workbook.save("Book1.xlsx");
```  

## **مواضيع متقدمة**  
- [إعدادات الحماية المتقدمة منذ Excel XP](/cells/ar/nodejs-cpp/advanced-protection-settings-since-excel-xp/)  
- [الكشف عما إذا كانت ورقة العمل محمية بكلمة مرور](/cells/ar/nodejs-cpp/detect-if-worksheet-is-password-protected/)  
- [حماية ورق العمل](/cells/ar/nodejs-cpp/protecting-worksheets/)  
- [إلغاء حماية ورقة العمل](/cells/ar/nodejs-cpp/unprotect-a-worksheet/)  
- [التحقق من الكلمة المستخدمة لحماية ورقة العمل](/cells/ar/nodejs-cpp/verify-password-used-to-protect-the-worksheet/)  

{{< app/cells/assistant language="nodejs-cpp" >}}
