---
title: كيفية تثبيت خطوط TrueType على نظام Linux
type: docs
weight: 20
url: /ar/java/how-to-install-truetype-fonts-on-linux/
---
{{% alert color="primary" %}}

السيناريو الأكثر احتمالا هو أنك تستخدم Aspose.Cells لتحويل جداول البيانات إلى PDF. إذا كنت تقوم بذلك على نظام تشغيل لا يعتمد على Windows مثل Linux ، فإن هذا الموضوع يشرح كيفية التأكد من أن Aspose.Cells يعرض جداول البيانات الخاصة بك بأفضل دقة.

للتأكد من أن جداول البيانات المحولة بواسطة Aspose.Cells تظهر أقرب ما يمكن من الأصل ، قد تحتاج إلى تثبيت "خطوط Windows" أو "خطوط تروتايب" على نظام Linux الخاص بك لأن خطوط TrueType الأكثر استخدامًا لا تأتي مثبتة مسبقًا مع توزيعات Linux بشكل افتراضي.

هناك طريقتان رئيسيتان للحصول على خطوط TrueType على نظام Linux:

1. انسخ ملفات الخط (.TTF و. TTC) من جهاز Windows إلى جهاز Linux الخاص بك.
1. قم بتثبيت حزمة خطوط تروتايب ، مثل msttcorefonts.

{{% /alert %}}

## **نسخ الخطوط من آلة Windows**

طريقة سهلة وسريعة هي نسخ ملفات .TTF و. TTC من دليل C: \ Windows \ Fonts على جهاز Windows إلى دليل ما على جهاز Linux الخاص بك. لا تحتاج إلى تثبيت أو تسجيل هذه الخطوط على Linux بأي شكل من الأشكال ، ما عليك سوى تحديد موقع الخطوط باستخدام طريقة FontConfigs.setFontFolder في التطبيق الخاص بك.

{{% alert color="primary" %}}

بقدر ما يمكننا أن نقول ، Microsoft يرخص الخطوط لأي شخص لاستخدامها بحرية ، ولكن يرجى التحقق من ترخيص الخط بنفسك.

{{% /alert %}}

## **قم بتثبيت حزمة خطوط TrueType**

ستوجهك المعلومات الواردة أدناه خطوة بخطوة لتثبيت خطوط تروتايب الأكثر شهرة في Microsoft على توزيعات Linux مثل Fedora و Red Hat Enterprise Linux (RHEL).

{{% alert color="primary" %}}

قد تحتاج إلى امتيازات مستوى "الجذر" ، لذا قم بتسجيل الدخول كـ "جذر" أو تكوين sudo.

{{% /alert %}}

إليك كيفية القيام بذلك باستخدام Terminal.

1. تأكد من تثبيت حزم RPM التالية.
   1. **دورة في الدقيقة البناء**: إذا لم يكن مثبتًا ، فاستخدم الأمر التالي لتثبيت حزمة rpm-build

{{< highlight "java" >}}

yum install rpm-build cabextract ttmkfdir

{{< /highlight >}}

1. **wget**: إذا لم يكن مثبتًا ، فاستخدم الأمر التالي

{{< highlight "java" >}}

yum \-y install wget

{{< /highlight >}}

1. قم بتنزيل أحدث ملف مواصفات msttcorefonts من SourceForge باستخدام الأمر كما يلي ،

{{< highlight "java" >}}

wget http://corefonts.sourceforge.net/msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. قم بإنشاء ملف RPM باستخدام ملف المواصفات الذي تم تنزيله مسبقًا والأمر التالي ،

{{< highlight "java" >}}

rpmbuild \-ba msttcorefonts-2.5-1.spec

{{< /highlight >}}

1. سيتم تخزين ملف RPM في: / root / rpmbuild / RPMS / noarch / ، قم بتثبيته على النحو التالي ،

{{< highlight "java" >}}

rpm \-ivh /root/rpmbuild/RPMS/noarch/msttcorefonts-2.5-1.noarch.rpm

{{< /highlight >}}

1. أعد تشغيل الجهاز لجعل التغييرات سارية المفعول.

ستقوم الإرشادات الواردة أعلاه بتثبيت حزمة Microsoft TTFs بما في ذلك مجموعات الخطوط التالية:

1. أندال Mono
1. Arial Black / Arial (غامق ، مائل ، غامق مائل)
1. Comic Sans MS (بولد)
1. Courier New (Bold، Italic، Bold Italic)
1. جورجيا (بولد ، مائل ، بولد مائل)
1. تأثير
1. تاهوما
1. Times New Roman (غامق ، مائل ، غامق مائل)
1. Trebuchet (بولد ، مائل ، غامق مائل)
1. Verdana (غامق ، مائل ، غامق مائل)
1. Webdings

{{% alert color="primary" %}}

 في Ubuntu ، انتقل إلى مدير الحزم Synaptic. ابحث عن ملف**ttf-mscorefonts المثبت** حزمة.

{{% /alert %}}
