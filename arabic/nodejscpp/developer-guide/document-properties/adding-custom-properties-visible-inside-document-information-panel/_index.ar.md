---
title: إضافة خصائص مخصصة تظهر داخل لوحة معلومات المستند باستخدام Node.js عبر C++
linktitle: إضافة خصائص مخصصة مرئية داخل لوحة معلومات المستند
type: docs
weight: 300
url: /ar/nodejs-cpp/adding-custom-properties-visible-inside-document-information-panel/
description: تعلم كيفية إضافة خصائص مخصصة إلى كائن دفتر العمل باستخدام Aspose.Cells for Node.js via C++. يمكن عرض هذه الخصائص في لوحة معلومات المستند.
---

## **إضافة خصائص مخصصة مرئية داخل لوحة معلومات الوثيقة**

 يمكن استخدام Aspose.Cells for Node.js via C++ لإضافة خصائص مخصصة داخل كائن دفتر العمل والتي تظهر داخل لوحة معلومات المستند. يمكنك فتح لوحة معلومات المستند في Microsoft Excel باستخدام أوامر القائمة ملف > معلومات > خصائص > عرض أوامر قائمة لوحة المعلومات للمستند.

 يرجى استخدام طريقة [**ContentTypePropertyCollection.add(string, string)**](https://reference.aspose.com/cells/nodejs-cpp/contenttypepropertycollection/#add-string-string-) لإضافة خاصية مخصصة ستكون مرئية في لوحة معلومات المستند.

 يضيف رمز النموذج التالي خاصيتين مخصصتين. الخاصية الأولى بدون نوع معين والخاصية الثانية من نوع تاريخ ووقت. بمجرد فتح ملف إكسل الناتج الذي تم إنشاؤه بواسطة هذا الرمز، سترى هاتين الخاصيتين داخل لوحة معلومات المستند.

```javascript
const path = require("path");
const AsposeCells = require("aspose.cells.node");

// The path to the documents directory.
const dataDir = path.join(__dirname, "data");

// Create workbook object
const workbook = new AsposeCells.Workbook(AsposeCells.FileFormatType.Xlsx);

// Add simple property without any type
workbook.getContentTypeProperties().add("MK31", "Simple Data");

// Add date time property with type
workbook.getContentTypeProperties().add("MK32", "04-Mar-2015", "DateTime");

// Save the workbook
workbook.save(path.join(dataDir, "AddingCustomPropertiesVisible_out.xlsx"));
```

### **مقال ذو صلة**

{{% alert color="primary" %}}

- [استخدام أجزاء XML المخصصة في Aspose.Cells](/cells/ar/net/use-custom-xml-parts-in-aspose-cells/)

{{% /alert %}}
