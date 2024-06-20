---
title: تطبيق Aspose.Cells الأول  مرحبًا بالعالم
type: docs
weight: 30
url: /ar/java/your-first-aspose-cells-application-hello-world/
---

{{% alert color="primary" %}}

يوضح هذا الموضوع للمبتدئين كيف يمكن للمطورين إنشاء تطبيق أول بسيط (مرحبًا بالعالم) باستخدام واجهة برمجة التطبيقات البسيطة لـ Aspose.Cells. يقوم التطبيق بإنشاء ملف Microsoft Excel يحتوي على كلمة مرحبًا بالعالم في خلية محددة من ورقة البيانات.

{{% /alert %}}

### **إنشاء تطبيق مرحبًا بالعالم**

لإنشاء تطبيق مرحبًا بالعالم باستخدام واجهة برمجة التطبيقات الخاصة بـ Aspose.Cells:

1. إنشاء مثيل من فئة [**Workbook**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook).
1. تطبيق الترخيص:
   1. إذا قمت بشراء ترخيص ، فاستخدم الترخيص في تطبيقك للحصول على وصول إلى وظائف Aspose.Cells الكاملة
   1. إذا كنت تستخدم الإصدار التجريبي من المكون (إذا كنت تستخدم Aspose.Cells بدون ترخيص) ، فتخطى هذه الخطوة.
1. إنشاء ملف Microsoft Excel جديد ، أو فتح ملف موجود ترغب في إضافة / تحديث بعض النص فيه.
1. الوصول إلى أي خلية في ورقة العمل في ملف Microsoft Excel.
1. إدراج كلمات **Hello World!** في الخلية التي تم الوصول إليها.
1. إنشاء ملف Microsoft Excel المعدل.

الأمثلة أدناه تظهر الخطوات أعلاه.

#### **إنشاء دفتر العمل**

المثال التالي ينشئ دفتر عمل جديد من البداية ، يكتب كلمة "Hello World!" في الخلية A1 في ورق العمل الأول ، ثم يحفظ الملف.

**الجدول الإنشائي المولد** 

![todo:image_alt_text](your-first-aspose-cells-application-hello-world_1.png)

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-CreatingWorkbook-1.java" >}}

#### **فتح ملف موجود**

المثال التالي يفتح ملف قالب Microsoft Excel موجود يسمى **book1.xls** ، يكتب كلمة "Hello World!" في الخلية A1 في الورقة العمل الأولى ، ثم يحفظ دفتر العمل كملف جديد.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-introduction-OpeningExistingFile-1.java" >}}
