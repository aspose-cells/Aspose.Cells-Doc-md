---
title: كيفية تحديد موقع الخطوط TrueType
type: docs
weight: 30
url: /ar/java/how-to-specify-truetype-fonts-location/
---

{{% alert color="primary" %}}

يصف هذا المقال:

1. [حيث تبحث واجهة برمجة تطبيقات Aspose.Cells عن خطوط TrueType](/cells/ar/java/how-to-specify-truetype-fonts-location/#where-asposecells-looks-for-truetype-fonts-on-windows).
1. [كيفية تحديد مجلدات خطوط TrueType بشكل صريح لواجهة برمجة تطبيقات Aspose.Cells](/cells/ar/java/how-to-specify-truetype-fonts-location/#how-to-explicitly-specify-a-font-folder).
1. [كيفية قيد استخدام واجهة برمجة تطبيقات Aspose.Cells لاستخدام موقع واحد فقط لخطوط TrueType](/cells/ar/java/how-to-specify-truetype-fonts-location/#how-to-restrict-the-asposecells-to-use-only-one-font-folder).

{{% /alert %}}

## **العمل مع الخطوط**

### **حيث تبحث واجهة برمجة تطبيقات Aspose.Cells عن خطوط TrueType على نظام ويندوز**

تبحث واجهة برمجة تطبيقات Aspose.Cells عن الخطوط في مجلد **Windows\Fonts** بشكل افتراضي. يعمل هذا الإعداد الافتراضي في معظم الأحيان، لذا يُنصح فقط بتحديد مجلدات الخطوط الخاصة إذا كنت في حاجة حقيقية إلى ذلك.

### **حيث تبحث واجهة برمجة تطبيقات Aspose.Cells عن خطوط TrueType على نظام لينكس**

بشكل افتراضي، تبحث واجهة برمجة تطبيقات Aspose.Cells عن الخطوط في جميع المواقع التالية، على الرغم من أن توزيعات لينكس المختلفة تخزن الخطوط في مجلدات مختلفة.

1. /usr/share/fonts
1. /usr/local/share/fonts

{{% alert color="primary" %}}

سيعمل هذا السلوك الافتراضي لمعظم توزيعات لينكس، ولكن لا يضمن العمل في كل الأوقات. قد تحتاج إلى تحديد موقع خطوط TrueType بشكل صريح. 

{{% /alert %}}

### **كيفية تحديد مجلد خطوط بشكل صريح**

قد قامت واجهة برمجة تطبيقات Aspose.Cells بتعريض الكثير من أساليب المصنع لفئة FontConfigs لتحديد الخطوط أو مجلدات الخطوط كما هو موضح أدناه.

1. تقبل طريقة setFontFolder المعلمة الأولى من النوع String بموقع مجلد الخطوط، في حين أن المعلمة الثانية من النوع Boolean هي لتوجيه واجهة برمجة تطبيقات Aspose.Cells للبحث في المجلدات بشكل متكرر عن ملفات الخطوط.
1. تقبل طريقة setFontFolders مصفوفة من النوع String حتى يُمكنك تحديد العديد من مجلدات الخطوط باستخدام هذا النهج. يُمكنك أيضًا توجيه واجهة برمجة تطبيقات Aspose.Cells للبحث في المجلدات بشكل متكرر عن طريق تحديد true كمعلمة ثانوية.
1. تقبل طريقة setFontSources مصفوفة من النوع FontSourceBase لتحديد قائمة مواقع الخطوط الفردية.

{{% alert color="primary" %}}

عند تحديد مجلد الخطوط باستخدام أي من الطرق المذكورة أعلاه، نوصي بتعيين موقع الخط في بداية التطبيق، وإلا فقد تتلقى نتائج غير مهيئة بشكل جيد.

{{% /alert %}} {{% alert color="primary" %}}

تحديد مجلد الخطوط باستخدام أي من الطرق المذكورة أعلاه لا يضمن أن واجهة برمجة تطبيقات Aspose.Cells لن تبحث عن الخطوط في المواقع الافتراضية مثل مجلد الخطوط في النظام.

{{% /alert %}}

### **كيفية قيد استخدام واجهة برمجة تطبيقات Aspose.Cells لاستخدام مجلد خط واحد فقط**

ابتداءً من الإصدار 8.1.0 Aspose.Cells for Java، سيضمن تحديد معطيات JVM على النحو التالي **-DAspose.Cells.FontDirExc="YourFontDir** أن واجهة برمجة تطبيقات Aspose.Cells ستستخدم فقط موقع الخطوط كما هو محدد.

قم بتعيين الوسائط المحددة باستخدام طريقة setProperty في System كما هو موضح أدناه.

{{< highlight java >}}

System.setProperty("Aspose.Cells.FontDirExc", "FontDirSet");

{{< /highlight >}}

{{% alert color="primary" %}}

يرجى ملاحظة ما يلي:

- يجب أن تكون البيانات أعلاه في بداية تطبيقك.
- استخدام الطريقة أعلاه لا يتطلب ضبط مجلد الخط باستخدام أي من طرق FontConfigs المناقشة أعلاه.
- يجب أن يكون سلسلة "FontDirSet" هي المسار الكامل إلى المجلد الذي يحتوي على الخطوط المطلوبة.

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
