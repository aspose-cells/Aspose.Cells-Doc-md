---
title: تطبيق Aspose.Cells الأول  مرحبًا بالعالم
type: docs
weight: 30
url: /ar/net/your-first-aspose-cells-application-hello-world/
description: قم بإنشاء، تحرير وحفظ ملف Excel الأول في أي تنسيق مدعوم باستخدام Aspose.Cells for .NET لتجربة بساطته وقوته في C#.
keywords: C# مرحبًا بالعالم، Aspose.Cells for .NET مرحبًا بالعالم، أول تطبيق باستخدام Aspose.Cells for .NET، أول برنامج عبر Aspose.Cells for .NET.
---

{{% alert color="primary" %}}

يوضح هذا البرنامج التعليمي كيفية إنشاء أول تطبيق (مرحبًا بالعالم) باستخدام واجهة برمجة التطبيقات البسيطة لـ Aspose.Cells. يقوم هذا التطبيق البسيط بإنشاء ملف Microsoft Excel بنص 'مرحبًا بالعالم' في خلية ورقة العمل المحددة.

{{% /alert %}}

## **كيفية إنشاء تطبيق مرحبًا بالعالم**

تقوم الخطوات التالية بإنشاء تطبيق مرحبًا بالعالم باستخدام واجهة برمجة التطبيقات لـ Aspose.Cells:

1. قم بإنشاء مثيل من [فئة المصنف](https://reference.aspose.com/cells/ar/net/aspose.cells/workbook).
1. إذا كان لديك ترخيص، ثم [قم بتطبيقه](/cells/ar/net/licensing/).
   إذا كنت تستخدم النسخة التجريبية، فتخطى خطوط الكود المتعلقة بالترخيص.
١. إنشاء ملف إكسل جديد أو فتح ملف إكسل موجود.
١. الوصول إلى أي خلية مرغوبة في ورقة العمل في ملف إكسل.
1. إدراج كلمات **Hello World!** في الخلية التي تم الوصول إليها.
1. إنشاء ملف Microsoft Excel المعدل.

يتم توضيح تنفيذ الخطوات أعلاه في الأمثلة أدناه.

### **كيفية إنشاء دفتر عمل جديد**

المثال التالي يقوم بإنشاء دفتر عمل جديد من البداية، يكتب Hello World! في خلية A1 على ورقة العمل الأولى ويحفظ ملف إكسل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-FirstApplication-1.cs" >}}

### **كيفية فتح ملف موجود**

المثال التالي يفتح ملف قالب Microsoft Excel موجود بالاسم "Sample.xlsx"، يدخل نص "Hello World!" في الخلية A1 في ورقة العمل الأولى ويحفظ دفتر العمل.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Introduction-OpenExistingFile-1.cs" >}}
