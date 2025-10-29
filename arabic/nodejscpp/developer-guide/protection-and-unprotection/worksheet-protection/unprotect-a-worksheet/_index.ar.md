---
title: إلغاء حماية ورقة العمل مع Node.js عبر C++
linktitle: إلغاء حماية ورقة العمل
type: docs
weight: 20
url: /ar/nodejs-cpp/unprotect-a-worksheet/
---

{{% alert color="primary" %}}

إذا كان هناك حاجة لإزالة الحماية من ورقة العمل المحمية في وقت التشغيل بحيث يمكن إجراء بعض التغييرات على الملف؟ يمكن القيام بذلك بسهولة مع Aspose.Cells.

{{% /alert %}}

## **إلغاء حماية ورقة العمل**

### **استخدام Microsoft Excel**

لإزالة الحماية من ورقة العمل:

من قائمة **الأدوات**، اختر **الحماية** ثم **إلغاء حماية الورقة**. ستتم إزالة الحماية ما لم تكن ورقة العمل محمية بكلمة مرور. في هذه الحالة، يُطلب إدخال كلمة المرور. أدخل كلمة المرور وسيتوقف الحماية عن العمل.

### **إزالة الحماية من ورقة العمل المحمية بشكل بسيط باستخدام Aspose.Cells**

يمكن إلغاء حماية ورقة العمل من خلال استدعاء طريقة [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--) من فئة [**Worksheet**](https://reference.aspose.com/cells/nodejs-cpp/worksheet). ورقة العمل المحمية ببساطة هي تلك التي ليست محمية بكلمة مرور. يمكن إلغاء حماية هذه الأوراق من خلال استدعاء طريقة [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--) بدون تمرير معلمة.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unprotecting the worksheet without a password
worksheet.unprotect();

// Saving the Workbook
workbook.save(path.join(dataDir, "output.xls"), AsposeCells.SaveFormat.Excel97To2003);
```

### **إلغاء حماية ورقة العمل المحمية بكلمة المرور باستخدام Aspose.Cells**

ورقة العمل المحمية بكلمة مرور هي تلك المحمية باستخدام كلمة مرور. يمكن إلغاء حماية هذه الأوراق من خلال استدعاء نسخة محملة من الطريقة [**unprotect()**](https://reference.aspose.com/cells/nodejs-cpp/worksheet/#unprotect--) التي تأخذ كلمة المرور كمعامل.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");
const filePath = path.join(dataDir, "book1.xls");

// Instantiating a Workbook object
const workbook = new AsposeCells.Workbook(filePath);

// Accessing the first worksheet in the Excel file
const worksheet = workbook.getWorksheets().get(0);

// Unprotecting the worksheet with a password
worksheet.unprotect("");

// Save Workbook
workbook.save(path.join(dataDir, "output.out.xls"));
```
{{< app/cells/assistant language="nodejs-cpp" >}}
