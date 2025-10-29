---
title: استخراج كائنات OLE من دفتر العمل باستخدام جولانج عبر C++
linktitle: استخراج كائنات Ole من الدفتر
type: docs
weight: 110
url: /ar/go-cpp/extract-ole-objects-from-workbook/
description: تعلم كيفية استخراج كائنات OLE من دفتر عمل باستخدام Aspose.Cells مع جولانج عبر C++
---

{{% alert color="primary" %}}

في بعض الأحيان، تحتاج إلى استخراج كائنات OLE من دفتر العمل. يدعم Aspose.Cells استخراج وتخزين تلك الكائنات OLE.

توضح هذه المقالة كيفية إنشاء تطبيق وحدة تحكم في Visual Studio واستخراج كائنات OLE المختلفة من دفتر العمل مع بضع أسطر بسيطة من التعليمات البرمجية.

{{% /alert %}}

## **استخراج كائنات Ole من دفتر عمل**

### **إنشاء دفتر عمل قالب**

1. أنشئ دفتر عمل في Microsoft Excel.
1. أضف مستند Word، ودفتر عمل Excel، ومستند PDF كعناصر تحكم OLE على الورقة الأولى.

|**مستند القالب مع كائنات OLE (OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

التالي، استخرج كائنات OLE واحفظها على القرص الصلب مع أنواع ملفاتها الخاصة.

### **تنزيل وتثبيت Aspose.Cells**

1. [تنزيل Aspose.Cells for C++](https://downloads.aspose.com/cells/go-cpp/).
1. قم بتثبيته على كمبيوتر التطوير الخاص بك.

جميع مكونات Aspose، عند التثبيت، تعمل في وضع التقييم. وضع التقييم لا يحتوي على حد زمني ويقوم فقط بحقن العلامات المائية إلى الوثائق المنتجة.

### **إنشاء مشروع**

ابدأ **Visual Studio** وأنشئ تطبيق وحدة تحكم جديد. سوف يُظهر هذا المثال تطبيق وحدة تحكم C++.

1. إضافة المراجع
   1. أضف مرجعًا إلى مكون Aspose.Cells إلى مشروعك، على سبيل المثال، أضف مرجعًا إلى ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll.

### **استخراج كائنات Ole**

الرمز أدناه يقوم بالعمل الفعلي للبحث واستخراج كائنات OLE. يتم حفظ كائنات الـ OLE (ملفات DOC، XLS، و PDF) على القرص.

{{< gist "aspose-cells-gists" "b414abd53259bbc47d2c3c0fe985395b" "Examples-Go-CPP-ExtractOleObjectsFromWorkbook.go" >}}
