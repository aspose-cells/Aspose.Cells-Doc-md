---
title: كيفية تثبيت خطوط TrueType على نظام Linux
type: docs
weight: 20
url: /ar/java/how-to-install-truetype-fonts-on-linux/
---

{{% alert color="primary" %}}

السيناريو الأكثر احتمالًا هو أنك تستخدم Aspose.Cells لتحويل جداول البيانات إلى مستندات PDF. إذا كنت تقوم بذلك على نظام تشغيل لا يعتمد على Windows مثل Linux، فإن هذا الموضوع يشرح كيفية ضمان أن Aspose.Cells يقدم جداول البيانات بأقصى ملاءمة.

للتأكد من أن جداول البيانات التي تم تحويلها بواسطة Aspose.Cells تبدو بأقرب ما يكون إلى الأصل، قد تحتاج إلى تثبيت "خطوط Windows" أو "خطوط TrueType" على نظام Linux الخاص بك لأن الخطوط TrueType الأكثر استخدامًا لا تكون مثبتة مسبقًا مع توزيعات Linux بشكل افتراضي.

هناك طريقتان رئيسيتان للحصول على خطوط TrueType على نظام Linux:

1. نسخ ملفات الخطوط (.TTF و .TTC) من جهاز كمبيوتر Windows إلى جهاز كمبيوتر Linux الخاص بك.
1. تثبيت حزمة الخطوط TrueType، مثل msttcorefonts.

{{% /alert %}}

## **نسخ الخطوط من جهاز كمبيوتر Windows**

طريقة سهلة وسريعة هي نسخ ملفات .TTF و .TTC من دليل C:\Windows\Fonts على جهاز كمبيوتر Windows إلى دليل ما على جهاز كمبيوتر Linux الخاص بك. لا يلزم تثبيت أو تسجيل هذه الخطوط على نظام Linux بأي شكل، يكفي تحديد موقع الخطوط باستخدام طريقة FontConfigs.setFontFolder في تطبيقك.

{{% alert color="primary" %}}

بقدر ما نعرف، ترخص Microsoft بالخطوط للجميع لاستخدامها بحرية، ولكن يرجى التحقق من تراخيص الخطوط بنفسك.

{{% /alert %}}

## **تثبيت حزمة خطوط TrueType**

المعلومات المقدمة أدناه سترشدك خطوة بخطوة لتثبيت أشهر خطوط TrueType الخاصة بمايكروسوفت على توزيعات Linux مثل Fedora و Red Hat Enterprise Linux (RHEL).

{{% alert color="primary" %}}

قد تحتاج إلى امتيازات مستوى 'root'، لذا قم بتسجيل الدخول كـ 'root' أو قم بتكوين sudo.

{{% /alert %}}

فيما يلي كيفية القيام بذلك باستخدام Terminal.

1. تأكد من أن لديك حزم RPM التالية مثبتة.
   1. **rpm-build**: إذا لم يكن مثبتًا، استخدم الأمر التالي لتثبيت حزمة rpm-build.

{{< highlight java >}}

yum install rpm-build cabextract ttmkfdir

{{< /highlight >}}

1. **wget**: إذا لم يكن مثبتًا، استخدم الأمر التالي

{{< highlight java >}}

yum \-y install wget

{{< /highlight >}}

1. قم بتنزيل ملف msttcorefonts الأحدث من SourceForge باستخدام الأمر التالي

{{< highlight java >}}

wget http://corefonts.sourceforge.net/msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. قم ببناء ملف RPM باستخدام ملف المواصفات المنزلق الذي تم تنزيله سابقًا والأمر التالي

{{< highlight java >}}

rpmbuild \-ba msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. سيتم تخزين ملف RPM في: /root/rpmbuild/RPMS/noarch/, قم بتثبيته كما يلي

{{< highlight java >}}

rpm \-ivh /root/rpmbuild/RPMS/noarch/msttcorefonts-2.5-1.noarch.rpm

{{< /highlight >}}

1. أعد تشغيل الجهاز لجعل التغييرات تأتي بمفعولها

التعليمات المذكورة أعلاه ستقوم بتثبيت حزمة Microsoft TTFs بما في ذلك عائلات الخطوط التالية

1. Andale Mono
1. Arial Black/Arial (غامق، مائل، جريء مائل)
1. Comic Sans MS (غامق)
1. Courier New (غامق، مائل، جريء مائل)
1. جورجيا (عريض، مائل، عريض مائل)
1. Impact
1. Tahoma
1. تايمز نيو رومان (عريض، مائل، عريض مائل)
1. Trebuchet (جريء, مائل, جريء مائل)
1. Verdana (جريء, مائل, جريء مائل)
1. Webdings

{{% alert color="primary" %}}

على Ubuntu، اذهب إلى Synaptic Package Manager. ابحث وقم بتثبيت حزمة **ttf-mscorefonts-installer**

{{% /alert %}}
{{< app/cells/assistant language="java" >}}
