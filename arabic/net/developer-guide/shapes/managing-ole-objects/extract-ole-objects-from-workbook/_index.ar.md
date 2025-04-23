---
title: استخراج كائنات Ole من الدفتر
type: docs
weight: 110
url: /ar/net/extract-ole-objects-from-workbook/
---

{{% alert color="primary" %}}

في بعض الأحيان، قد تحتاج إلى استخراج كائنات Ole من دفتر العمل. تدعم Aspose.Cells استخراج وحفظ تلك الكائنات Ole.

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

### **تنزيل وتثبيت Aspose.Cells**

1. [تنزيل Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1. قم بتثبيته على كمبيوتر التطوير الخاص بك.

جميع مكونات Aspose، عند التثبيت، تعمل في وضع التقييم. وضع التقييم لا يحتوي على حد زمني ويقوم فقط بحقن العلامات المائية إلى الوثائق المنتجة.

### **إنشاء مشروع**

ابدأ **Visual Studio.Net** وقم بإنشاء تطبيق وحدة التحكم جديد. سيعرض هذا المثال تطبيق وحدة التحكم C#، ولكن يمكنك أيضًا استخدام VB.NET.

1. إضافة المراجع
   1. أضف مرجعًا لمكون Aspose.Cells إلى مشروعك، على سبيل المثال، أضف مرجعًا إلى ...\Program Files\Aspose\Aspose.Cells\Bin\Net1.0\Aspose.Cells.dll

### **استخراج كائنات Ole**

الكود أدناه يقوم بالعمل الفعلي للعثور على واستخراج كائنات OLE. يتم حفظ كائنات OLE (ملفات DOC وXLS وPDF) على القرص.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExtractOLEObjects-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
