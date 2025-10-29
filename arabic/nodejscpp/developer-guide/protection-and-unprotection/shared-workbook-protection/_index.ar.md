---
title: حماية أو إلغاء حماية المصنف المشترك باستخدام Node.js عبر C++
linktitle: حماية كلمة المرور أو إلغاء حمايتها لكتاب العمل المشترك
type: docs
weight: 10
url: /ar/nodejs-cpp/password-protect-or-unprotect-the-shared-workbook/
---

## **سيناريوهات الاستخدام المحتملة**

يمكنك حماية أو إلغاء حماية المصنف المشترك باستخدام Microsoft Excel كما يظهر في لقطة الشاشة التالية. يدعم Aspose.Cells for Node.js via C++ أيضًا هذه الميزة باستخدام طريقتي [**Workbook.protectSharedWorkbook(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#protectSharedWorkbook-string-) و [**Workbook.unprotectSharedWorkbook(string)**](https://reference.aspose.com/cells/nodejs-cpp/workbook/#unprotectSharedWorkbook-string-).

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_1.png)

## **حماية كلمة المرور أو إلغاء حمايتها لكتاب العمل المشترك**

الرمز البريدي العيني التالي ينشئ كتاب عمل ويحميه أثناء تمكين العمل المشترك ويحفظه كملف Excel الناتج. تبين لقطة الشاشة أنه عند محاولة إلغاء حمايته ، يطلب منك Microsoft Excel إدخال كلمة المرور لإلغاء حمايته.

![todo:image_alt_text](password-protect-or-unprotect-the-shared-workbook_2.png)

## **الكود المثالي**

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// Create empty Excel file
const workbook = new AsposeCells.Workbook();

// Protect the Shared Workbook with Password
workbook.protectSharedWorkbook("1234");

// Uncomment this line to Unprotect the Shared Workbook
// workbook.unprotectSharedWorkbook("1234");

// Save the output Excel file
workbook.save("outputProtectSharedWorkbook.xlsx");
```
{{< app/cells/assistant language="nodejs-cpp" >}}
