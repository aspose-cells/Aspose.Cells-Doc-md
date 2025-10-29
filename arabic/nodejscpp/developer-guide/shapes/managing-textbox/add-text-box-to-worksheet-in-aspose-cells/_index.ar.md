---
title: كيفية إضافة/إدراج صندوق النص إلى ورقة العمل باستخدام Node.js عبر C++
linktitle: إضافة مربع نص إلى ورقة العمل
type: docs
weight: 10
url: /ar/nodejs-cpp/add-text-box-to-worksheet-in-aspose-cells/
description: كيفية إضافة/إدراج صندوق نص إلى ورقة العمل في Aspose.Cells for Node.js via C++.
keywords: إضافة/إدراج صندوق النص في Excel باستخدام Aspose و Node.js عبر C++
---

## إضافة مربع نص إلى ورقة العمل في إكسل

في برنامج Excel (الإصدار 07 وما فوق)، هناك مكانان يمكن إدراج صناديق النص فيهما. واحد في "إدراج - أشكال"، الآخر على الجهة اليمنى من الشريط العلوي لخيار "إدراج".

### الطريقة الأولى:

![1](1.png)

### الطريقة الثانية:

![2](2.png)

## كيفية الإنشاء

يمكنك إنشاء مربعات نص بنص أفقي أو رأسي.

- حدد الخيار المقابل (أفقي أو عمودي)
- انقر بالزر الأيسر على الصفحة
- اضغط على الزر الأيسر واسحب مسافة على الصفحة
- أفلت الزر الأيسر

الآن حصلت على صندوق نص.

## إضافة صندوق النص إلى ورقة العمل في Aspose.Cells for Node.js via C++

عند الحاجة إلى إدراج العديد من صناديق النص في ورقة العمل دفعة واحدة، فإن طريقة الإدراج اليدوي تعتبر كارثة. إذا كان هذا يزعجك، أعتقد أن هذا المستند سيساعدك. يوفر لك [Aspose.Cells](https://products.aspose.com/cells/) واجهة برمجة تطبيقات لإجراء عمليات إدراج جماعية بسهولة في كودك.

الكود النموذجي التالي ينشئ مربع نص.

```javascript
const AsposeCells = require("aspose.cells.node");
const path = require("path");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create an object of the Workbook class
const workbook = new AsposeCells.Workbook();

// Access first worksheet from the collection
const sheet = workbook.getWorksheets().get(0);

// Add the TextBox to the worksheet
sheet.getTextBoxes().add(6, 10, 100, 200);

// Save. You can check your text box in this way.
workbook.save("result.xlsx", AsposeCells.SaveFormat.Xlsx);
```

ستحصل على ملف مشابه لـ [نتيجة الملف](result.xlsx). في الملف، سترى ما يلي:

![](52449.png)

{{< app/cells/assistant language="nodejs-cpp" >}}
