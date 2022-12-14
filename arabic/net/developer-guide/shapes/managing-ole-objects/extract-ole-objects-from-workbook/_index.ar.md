---
title: استخراج كائنات OLE من المصنف
type: docs
weight: 110
url: /ar/net/extract-ole-objects-from-workbook/
---
{{% alert color="primary" %}}

في بعض الأحيان ، تحتاج إلى استخراج كائنات OLE من مصنف. يدعم Aspose.Cells استخراج وحفظ عناصر Ole هذه.

يوضح هذا المقال كيفية إنشاء تطبيق وحدة تحكم في Visual Studio.Net واستخراج كائنات OLE مختلفة من مصنف باستخدام بضعة أسطر بسيطة من التعليمات البرمجية.

{{% /alert %}}

## **استخراج كائنات OLE من مصنف**

### **إنشاء قالب مصنف**

1. إنشاء مصنف في Microsoft Excel.
1. قم بإضافة مستند Word Microsoft ، ومصنف Excel ، ووثيقة PDF ككائنات OLE في ورقة العمل الأولى.

|**مستند قالب به كائنات OLE (OleFile.xls)**|
|:- |
|![ما يجب القيام به: image_بديل_نص](extract-ole-objects-from-workbook_1.png)|

قم بعد ذلك باستخراج كائنات OLE وحفظها على القرص الثابت مع أنواع الملفات الخاصة بها.

### **قم بتنزيل وتثبيت Aspose.Cells**

1. [تحميل Aspose.Cells for .NET](https://downloads.aspose.com/cells/net).
1. قم بتثبيته على جهاز الكمبيوتر الخاص بك.

جميع مكونات Aspose ، عند تثبيتها ، تعمل في وضع التقييم. لا يوجد حد زمني لوضع التقييم ويقوم فقط بحقن العلامات المائية في المستندات المنتجة.

### **أنشئ مشروعًا**

بداية**مرئي Studio.Net** وإنشاء تطبيق وحدة تحكم جديد. سيعرض هذا المثال تطبيق وحدة تحكم C# ، ولكن يمكنك استخدام VB.NET أيضًا.

1. أضف المراجع
 1. أضف مرجعًا إلى مكون Aspose.Cells إلى مشروعك ، على سبيل المثال أضف مرجعًا إلى ... \ Program Files \ Aspose \ Aspose.Cells \ Bin \ Net1.0 \ Aspose.Cells.dll

### **استخراج كائنات OLE**

يقوم الكود أدناه بالعمل الفعلي لإيجاد واستخراج كائنات OLE. يتم حفظ كائنات OLE (ملفات DOC و XLS و PDF) على القرص.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-ExtractOLEObjects-1.cs" >}}
