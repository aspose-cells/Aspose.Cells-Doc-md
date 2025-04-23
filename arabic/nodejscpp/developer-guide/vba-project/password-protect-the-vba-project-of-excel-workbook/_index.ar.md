---  
title: حماية مشروع VBA من خلال كلمة مرور لمصنف Excel باستخدام Node.js عبر C++  
linktitle: حماية كلمة السر لمشروع VBA لسجل العمل الخاص بـ Excel  
type: docs  
weight: 10  
url: /ar/nodejs-cpp/password-protect-the-vba-project-of-excel-workbook/  
description: تعلم كيفية حماية مشروع VBA بكلمة مرور لمصنف Excel باستخدام Aspose.Cells for Node.js via C++.  
---  

## ** حماية مشروع VBA لكتيب Excel بكلمة مرور في Node.js**  

 يمكنك حماية مشروع VBA (محدد اللغة) لمصنف باستخدام Aspose.Cells باستخدام طريقة [**VbaProject.protect(boolean, string)**](https://reference.aspose.com/cells/nodejs-cpp/vbaproject/#protect-boolean-string-).  

## **الكود المثالي**  

الرمز النموذجي التالي يحمل [ملف إكسل النموذجي](43352067.xlsm)، يصل إلى مشروع VBA الخاص به ويحميه بكلمة مرور. أخيرًا، يحفظه كـ [ملف إكسل المخرجات](43352068.xlsm).  

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Load your source Excel file.
const workbook = new AsposeCells.Workbook(path.join(dataDir, "samplePasswordProtectVBAProject.xlsm"));

// Access the VBA project of the workbook.
const vbaProject = workbook.getVbaProject();

// Lock the VBA project for viewing with password.
vbaProject.protect(true, "11");

// Save the output Excel file
workbook.save(path.join(dataDir, "outputPasswordProtectVBAProject.xlsm"));
```  

