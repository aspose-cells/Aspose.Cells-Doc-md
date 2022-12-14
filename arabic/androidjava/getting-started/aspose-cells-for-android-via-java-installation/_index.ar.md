---
title: Aspose.Cells لنظام Android عبر تثبيت Java
type: docs
weight: 30
url: /ar/java/aspose-cells-for-android-via-java-installation/
---
## **متطلبات النظام**
Aspose.Cells لنظام Android عبر Java مستقل عن النظام الأساسي ويمكن استخدامه على أي نظام أساسي حيث يتم تثبيت بيئة Android Runtime وسيعمل على أنظمة Android التي تعمل بنظام التشغيل Android OS 2.0 أو إصدار أحدث. في الوقت الحاضر ، تم اختبار المكون باستخدام:

- اندرويد 5.1 v 22
## **قم بتثبيت Aspose.Cells لنظام Android عبر Java من مستودع Maven**
1. أضف مستودع maven إلى الإصدار الخاص بك
1. أضف "Aspose.Cells لـ Android عبر Java" JAR كاعتماد

{{< highlight "java" >}}

 // 1. Add maven repository into your build.gradle 

repositories {

    mavenCentral()

    maven { url "http://repository.aspose.com/repo/" }

}

// 2. Add 'Aspose.Cells for Android via Java' JAR as a dependency

dependencies {

    ...

    ...

    compile (group: 'com.aspose', name: 'aspose-cells', version: '20.6', classifier: 'android.via.java')

}

{{< /highlight >}}
## **كيفية استخدام Aspose.Cells لنظام Android عبر Java**
سيرشدك هذا الموضوع إلى الخطوات اللازمة لإعداد Aspose.Cells لنظام Android عبر Java في Android Studio IDE ، بافتراض أن لديك بالفعل أحدث إصدار من Android Studio مثبتًا على جهازك وأنك حصلت أيضًا على أحدث إصدار من Aspose.Cells لنظام Android عبر Java حزمة.

{{% alert color="primary" %}} 

إذا لم تكن قد قمت بتثبيت Android Studio حتى الآن ، فيجب عليك أولاً الحصول على إعداد Android Studio وتثبيته على جهازك. يمكنك تنزيل أحدث إصدار من Android Studio من[هنا](https://developer.android.com/studio/index.html#win-bundle) بينما تتوفر تفاصيل حول كيفية تثبيت IDE[هنا](https://developer.android.com/studio/install.html).

{{% /alert %}} {{% alert color="primary" %}} 

 يمكن تنزيل Aspose.Cells لنظام Android عبر حزمة Java من[هنا](https://downloads.aspose.com/cells/androidjava). يرجى ملاحظة أن كل حزمة إصدار Aspose.Cells لنظام Android عبر Java تتكون أساسًا من ملفين كما هو مفصل أدناه.

- **aspose- الخلايا- xxxjar** هو ملف المكتبة الرئيسي الذي يحتوي على جميع مساحات الأسماء من Aspose.Cells لنظام Android عبر Java API.
- **aspose- خلايا- xxx-libs.apk** هو ملف APK يحتوي على الطرف الثالث bcprov-jdk15-146.jar المستخدم لمرافق التشفير وفك التشفير التي يقدمها Aspose.Cells لنظام Android عبر Java API.

{{% /alert %}} 
### **الشروع في العمل مع Aspose.Cells لنظام Android عبر Java في Android Studio**
بمجرد تحميل Android Studio IDE ، انقر فوق ملف> جديد> مشروع جديد كما هو موضح أدناه.

![ما يجب القيام به: image_بديل_نص](aspose-cells-for-android-via-java-installation_1.png)

يمكنك أيضًا إنشاء مشروع جديد من شاشة الترحيب الخاصة بـ Android Studio كما هو موضح أدناه.

![ما يجب القيام به: image_بديل_نص](aspose-cells-for-android-via-java-installation_2.png)

بعد ذلك ، ستتم مطالبتك بتحديد اسم التطبيق والمجال والموقع لتخزين ملفات المشروع. يمكنك اختيار تغيير القيم الافتراضية حسب اختيارك أو تركها كما هي ، والنقر فوق التالي.

![ما يجب القيام به: image_بديل_نص](aspose-cells-for-android-via-java-installation_3.png)

في الخطوة التالية ، يجب عليك تحديد جهاز Android الذي ترغب في استضافة / تشغيل تطبيقك. بمجرد التحديد ، انقر فوق زر التالي.

![ما يجب القيام به: image_بديل_نص](aspose-cells-for-android-via-java-installation_4.png)

أنت الآن بحاجة إلى تحديد النشاط من قائمة قوالب محددة مسبقًا. من أجل الحفاظ على العرض التوضيحي بسيطًا ، اخترنا نموذج نشاط فارغ كما هو موضح أدناه.

![ما يجب القيام به: image_بديل_نص](aspose-cells-for-android-via-java-installation_5.png)

انقر فوق الزر "إنهاء" في مربع حوار "تخصيص النشاط" حيث سنحتفظ بجميع الإعدادات الافتراضية كما هي.

![ما يجب القيام به: image_بديل_نص](aspose-cells-for-android-via-java-installation_6.png)

بمجرد النقر فوق الزر "إنهاء" في الخطوة السابقة ، سيبدأ IDE في إنشاء المشروع كما هو موضح أدناه. دعها تنتهي أو انقر فوق الزر "إلغاء الأمر".

![ما يجب القيام به: image_بديل_نص](aspose-cells-for-android-via-java-installation_7.png)

الآن تم تحميل المشروع في IDE ، ومع ذلك ، قد ترغب في تغيير طريقة العرض إلى Project حتى تتمكن من عرض التسلسل الهرمي الكامل لملفات المشروع. لتغيير العرض ، يرجى التحقق من اللقطة التالية.

![ما يجب القيام به: image_بديل_نص](aspose-cells-for-android-via-java-installation_8.png)

 بعد تغيير العرض إلى Project ، ابحث عن ملف**بناء gradle** ملف في المحرر والصق المقتطف التالي كما هو موضح أدناه.

{{< highlight "java" >}}

 dexOptions{

    javaMaxHeapSize "4g"

}

{{< /highlight >}}

![ما يجب القيام به: image_بديل_نص](aspose-cells-for-android-via-java-installation_9.png)

بعد ذلك ، سنضيف Aspose.Cells لنظام Android عبر Java Jar إلى المشروع. هناك خطوتان مهمتان كما هو مفصل أدناه.

-  انسخ Aspose.Cells لنظام Android يدويًا عبر Java Jar إلى ملف**\ التطبيق \ ليبس** مجلد.
- أضف Aspose.Cells لنظام Android عبر Java Jar كمكتبة إلى الوحدة النمطية كما هو موضح أدناه.

![ما يجب القيام به: image_بديل_نص](aspose-cells-for-android-via-java-installation_10.png)

ستتم مطالبتك بتحديد الوحدة التي ترغب في إضافة Aspose.Cells for Java.Android Jar كمكتبة. الرجاء الاختيار المناسب والنقر فوق "موافق".

![ما يجب القيام به: image_بديل_نص](aspose-cells-for-android-via-java-installation_11.png)

 تحتاج أيضًا إلى إضافة ملف APK إلى المشروع. يجب عليك نسخ ملف APK إلى ملف**\ التطبيق \ src \ main \ الأصول**مجلد. إذا لم يكن لديك مجلد الأصول ضمن المجلد الرئيسي ، فيمكنك إنشاء مجلد بالنقر بزر الماوس الأيمن فوق العقدة الرئيسية في عرض المشروع. حدد New> Folder> Asset Folder.

![ما يجب القيام به: image_بديل_نص](aspose-cells-for-android-via-java-installation_12.png)

بمجرد إضافة ملف APK إلى المشروع ، يجب تحميله بواسطة المشروع. هناك طريقتان لتحميل APK على النحو التالي.

- قم بتحميل APK في فئة تطبيق مخصصة باستخدام المقتطف المقدم أدناه ، وقم بتسجيل فئة التطبيق المخصصة في AndroidManifest.xml.

{{< highlight "java" >}}

 LibsLoadHelper.loadLibs(this);

{{< /highlight >}}

- قم بتحميل APK في طريقة OnCreate الخاصة بـ MainActivity.

{{< highlight "java" >}}

 LibsLoadHelper.loadLibs(getApplicationContext());

{{< /highlight >}}

الآن نحن جاهزون لكتابة الكود. من أجل الحفاظ على سهولة فهم العرض التوضيحي ، أضفنا عنصر واجهة مستخدم زر إلى التخطيط وسنقوم بمعالجة حدث النقر الخاص به على النحو التالي.

{{< highlight "java" >}}

 private class TestTask extends AsyncTask<Void, String, Boolean> {

    @Override

    protected Boolean doInBackground(Void... params) {

        Boolean result = false;

        Workbook book = new Workbook();

        Worksheet sheet = book.getWorksheets().get(0);

        Cells cells = sheet.getCells();

        Cell cell = cells.get("A1");

        cell.putValue("Hello World!");

        try {

            book.save(SD_PATH + "output.xlsx");

        } catch (Exception e) {

            e.printStackTrace();

        }

        return result;

    }

}

{{< /highlight >}}

عند تشغيل التطبيق باستخدام زر التشغيل على واجهة IDE (أو باستخدام SHIFT + F10) ، سيقوم المحاكي بتحميل التطبيق كما هو موضح أدناه.

![ما يجب القيام به: image_بديل_نص](aspose-cells-for-android-via-java-installation_13.png)

سيؤدي النقر فوق الزر الموجود على المحاكي إلى تنفيذ التعليمات البرمجية لإنشاء جدول بيانات جديد في مجلد التخزين الخارجي للمحاكي. يمكنك الوصول إلى الملف من Android Device Monitor كما هو موضح أدناه.

![ما يجب القيام به: image_بديل_نص](aspose-cells-for-android-via-java-installation_14.png)

![ما يجب القيام به: image_بديل_نص](aspose-cells-for-android-via-java-installation_15.png)


