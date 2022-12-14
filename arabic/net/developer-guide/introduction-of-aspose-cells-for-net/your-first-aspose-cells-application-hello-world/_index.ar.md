---
title: أول طلب Aspose.Cells - Hello World
type: docs
weight: 30
url: /ar/net/your-first-aspose-cells-application-hello-world/
---
{{% alert color="primary" %}}

يوضح هذا البرنامج التعليمي كيفية إنشاء أول تطبيق (Hello World) باستخدام Aspose.Cells 'API البسيط. يقوم هذا التطبيق البسيط بإنشاء ملف Excel Microsoft بالنص "Hello World" في خلية ورقة عمل محددة.

{{% /alert %}}

## **إنشاء تطبيق Hello World**

تؤدي الخطوات أدناه إلى إنشاء تطبيق Hello World باستخدام Aspose.Cells API:

1.  قم بإنشاء مثيل لـ[دفتر العمل](https://reference.aspose.com/cells/net/aspose.cells/workbook) صف دراسي.
1.  إذا كان لديك ترخيص ، إذن[قم بتطبيقه](/cells/ar/net/licensing/).
 إذا كنت تستخدم الإصدار التقييمي ، فتخط سطور التعليمات البرمجية المتعلقة بالترخيص.
1. قم بإنشاء ملف Excel جديد ، أو افتح ملف Excel موجود.
1. قم بالوصول إلى أي خلية مرغوبة من ورقة العمل في ملف Excel.
1.  أدخل الكلمات**Hello World!** في خلية تم الوصول إليها.
1. قم بإنشاء ملف Excel Microsoft المعدل.

يتم توضيح تنفيذ الخطوات المذكورة أعلاه في الأمثلة أدناه.

### **نموذج التعليمات البرمجية: إنشاء مصنف جديد**

المثال التالي ينشئ مصنفًا جديدًا من البداية ، يكتب Hello World! في الخلية A1 في ورقة العمل الأولى ويحفظ ملف Excel.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **نموذج التعليمات البرمجية: فتح ملف موجود**

يفتح المثال التالي ملف قالب Excel Microsoft موجود باسم "Sample.xlsx" ، بإدخال "Hello World!" نص في الخلية A1 في ورقة العمل الأولى ويحفظ المصنف.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
