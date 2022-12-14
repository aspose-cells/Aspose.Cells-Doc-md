---
title: كيفية تحديد موقع خطوط TrueType
type: docs
weight: 30
url: /ar/java/how-to-specify-truetype-fonts-location/
---
{{% alert color="primary" %}}

توضح هذه المقالة:

1. [حيث يبحث Aspose.Cells API عن خطوط TrueType](/cells/ar/java/how-to-specify-truetype-fonts-location/#where-asposecells-looks-for-truetype-fonts-on-windows).
1. [كيفية تحديد مجلدات خطوط TrueType بشكل صريح لـ Aspose.Cells API](/cells/ar/java/how-to-specify-truetype-fonts-location/#how-to-explicitly-specify-a-font-folder).
1. [كيفية تقييد Aspose.Cells API لاستخدام موقع واحد فقط لخطوط TrueType](/cells/ar/java/how-to-specify-truetype-fonts-location/#how-to-restrict-the-asposecells-to-use-only-one-font-folder).

{{% /alert %}}

## **العمل مع الخطوط**

### **حيث يبحث Aspose.Cells عن خطوط TrueType على Windows**

 Aspose.Cells يبحث عن الخطوط في**Windows \ الخطوط** مجلد. يعمل هذا الإعداد الافتراضي في معظم الأوقات ، لذا حدد مجلدات الخطوط الخاصة بك فقط إذا كنت تريد ذلك حقًا.

### **حيث يبحث Aspose.Cells عن خطوط TrueType على نظام Linux**

بشكل افتراضي ، يبحث Aspose.Cells API عن الخطوط في كل المواقع التالية ، على الرغم من أن توزيعات Linux المختلفة تخزن الخطوط في مجلدات مختلفة.

1. / usr / share / الخطوط
1. / usr / local / share / الخطوط

{{% alert color="primary" %}}

 سيعمل هذا السلوك الافتراضي مع معظم توزيعات Linux ، ولكن ليس مضمونًا أنه يعمل طوال الوقت. قد تحتاج إلى تحديد موقع خطوط TrueType بشكل صريح.

{{% /alert %}}

### **كيفية تحديد مجلد الخطوط بشكل صريح**

كشفت واجهات برمجة التطبيقات Aspose.Cells عن العديد من طرق المصنع لفئة FontConfigs لتحديد الخطوط أو مجلدات الخطوط كما هو موضح أدناه.

1. تقبل طريقة setFontFolder المعلمة الأولى من النوع String مع الموقع إلى دليل الخطوط بينما المعلمة الثانية من النوع Boolean هي توجيه Aspose.Cells APis للبحث في المجلدات بشكل متكرر عن ملفات الخطوط.
1. يقبل التابع setFontFolders مصفوفة من النوع String لذا يمكنك تحديد العديد من دلائل الخطوط باستخدام هذا الأسلوب. يمكنك أيضًا توجيه Aspose.Cells APis للبحث في المجلدات بشكل متكرر عن طريق تحديد true كمعامل ثانٍ.
1. يقبل الأسلوب setFontSources مصفوفة من نوع FontSourceBase لتتمكن من تحديد قائمة بمواقع الخطوط الفردية.

{{% alert color="primary" %}}

عند تحديد مجلد الخطوط باستخدام أي من الطرق المذكورة أعلاه ، نوصي بتعيين موقع الخط في بداية التطبيق وإلا فقد تتلقى نتائج سيئة التنسيق.

{{% /alert %}} {{% alert color="primary" %}}

لا يضمن ضبط مجلد الخطوط باستخدام أي من الطرق المذكورة أعلاه أن Aspose.Cells API لن يبحث عن الخطوط في المواقع الافتراضية مثل مجلد خطوط النظام.

{{% /alert %}}

### **كيفية تقييد Aspose.Cells لاستخدام مجلد خط واحد فقط**

 بدءًا من Aspose.Cells for Java 8.1.0 ، قم بتعيين وسيطات JVM على أنها**-DAspose.Cells.FontDirExc = "YourFontDir**سيضمن أن Aspose.Cells API سيستخدم فقط موقع الخطوط كما هو محدد.

قم بتعيين الوسائط المحددة باستخدام طريقة System.setProperty كما هو موضح أدناه.

{{< highlight "java" >}}

System.setProperty("Aspose.Cells.FontDirExc", "FontDirSet");

{{< /highlight >}}

{{% alert color="primary" %}}

يرجى ملاحظة ما يلي:

- يجب أن يكون البيان أعلاه في بداية طلبك.
- لا يتطلب استخدام الأسلوب أعلاه تعيين دليل الخطوط باستخدام أي من طرق FontConfigs التي تمت مناقشتها أعلاه.
- يجب أن تكون السلسلة "FontDirSet" هي المسار الكامل للمجلد الذي يحتوي على الخطوط المطلوبة.

{{% /alert %}}
