---
title: أول طلب Aspose.Cells - Hello World
type: docs
weight: 30
url: /ar/java/your-first-aspose-cells-application-hello-world/
---
{{% alert color="primary" %}}

يوضح موضوع المبتدئين هذا كيف يمكن للمطورين إنشاء تطبيق أول بسيط (Hello World) باستخدام Aspose.Cells 'API بسيطًا. يقوم التطبيق بإنشاء ملف Excel Microsoft بالكلمات Hello World في خلية محددة من ورقة العمل.

{{% /alert %}}

### **إنشاء تطبيق Hello World**

لإنشاء تطبيق Hello World باستخدام Aspose.Cells API:

1.  قم بإنشاء مثيل لـ**[مصنف] (https://reference.aspose.com/cells/java/com.aspose.cells/workbook)**صف دراسي.
1. تطبيق الرخصة:
1. إذا كنت قد اشتريت ترخيصًا ، فاستخدم الترخيص الموجود في التطبيق الخاص بك للوصول إلى الوظائف الكاملة Aspose.Cells
 1. إذا كنت تستخدم الإصدار التقييمي للمكون (إذا كنت تستخدم Aspose.Cells بدون ترخيص) ، فتخط هذه الخطوة.
1. قم بإنشاء ملف Excel Microsoft جديد ، أو افتح ملفًا موجودًا تريد إضافة / تحديث بعض النصوص فيه.
1. قم بالوصول إلى أي خلية في ورقة العمل في ملف Excel Microsoft.
1.  أدخل الكلمات**Hello World!** في خلية تم الوصول إليها.
1. قم بإنشاء ملف Excel Microsoft المعدل.

توضح الأمثلة أدناه الخطوات المذكورة أعلاه.

#### **إنشاء مصنف**

يقوم المثال التالي بإنشاء مصنف جديد من البداية ، ويكتب الكلمات "Hello World!" في الخلية A1 في ورقة العمل الأولى ، ويحفظ الملف.

**جدول البيانات الذي تم إنشاؤه** 

![ما يجب القيام به: image_بديل_نص](your-first-aspose-cells-application-hello-world_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CreatingWorkbook-1.java" >}}

#### **فتح ملف موجود**

 يفتح المثال التالي ملف قالب Excel Microsoft موجود يسمى**book1.xls**، يكتب عبارة "Hello World!" في الخلية A1 في ورقة العمل الأولى ، ويحفظ المصنف كملف جديد.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-OpeningExistingFile-1.java" >}}
