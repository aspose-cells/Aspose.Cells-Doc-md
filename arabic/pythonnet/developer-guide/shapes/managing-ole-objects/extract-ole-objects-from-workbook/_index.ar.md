---
title: استخراج كائنات Ole من الدفتر
type: docs
weight: 110
url: /ar/python-net/extract-ole-objects-from-workbook/
---

{{% alert color="primary" %}}

 في بعض الأحيان، تحتاج إلى استخراج عناصر OLE من دفتر العمل. تدعم Aspose.Cells لـ Python via .NET استخراج وحفظ تلك العناصر Ole.

يوضح هذا المقال كيفية إنشاء تطبيق وحدة تحكم في الوحدة التحكم في Visual Studio.Net واستخراج كائنات OLE مختلفة من دفتر العمل ببضعة أسطر بسيطة من الكود.

{{% /alert %}}

## **استخراج كائنات Ole من دفتر عمل**

### **إنشاء دفتر عمل قالب**

1. أنشئ دفتر عمل في Microsoft Excel.
1. أضف مستند Microsoft Word ودفتر عمل Excel ومستند PDF ككائنات Ole في الورقة العمل الأولى.

|**مستند القالب مع كائنات OLE (OleFile.xls)**|
| :- |
|![todo:image_alt_text](extract-ole-objects-from-workbook_1.png)|

الخطوة التالية هي استخراج كائنات OLE وحفظها على القرص الصلب مع أنواع الملفات الخاصة بها.

### **استخراج عناصر OLE باستخدام مكتبة Aspose.Cells لـ Python Excel**

الكود أدناه يقوم بالعمل الفعلي للعثور على واستخراج كائنات OLE. يتم حفظ كائنات OLE (ملفات DOC وXLS وPDF) على القرص.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Shapes-DrawingObjects-ExtractOLEObjects-1.py" >}}
