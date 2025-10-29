---
title: تثبيت Aspose.Cells لنظام Android via Java
type: docs
weight: 30
url: /ar/java/aspose-cells-for-android-via-java-installation/
---

## **متطلبات النظام**
Aspose.Cells for Android via Java هو منصة مستقلة عن النظام ويمكن استخدامه على أي منصة حيث تم تثبيت بيئة التشغيل Android Runtime وسيتم تشغيله على أنظمة Android التي تعمل بنظام التشغيل Android OS 2.0 أو أحدث. حتى الآن، تم اختبار المكون مع:

- Android 5.1 v 22
## **تثبيت Aspose.Cells for Android via Java من مستودع Maven**
1. أضف مستودع Maven إلى build.gradle الخاص بك 
1. أضف JAR 'Aspose.Cells for Android via Java' كتبعية

{{< highlight java >}}

 // 1. Add maven repository into your build.gradle 

repositories {

    mavenCentral()

    maven { url "http://repository.aspose.com/repo/" }

}

// 2. Add 'Aspose.Cells for Android via Java' JAR as a dependency

dependencies {

    ...

    ...

    compile (group: 'com.aspose', name: 'aspose-cells', version: '25.9', classifier: 'android.via.java')

}

{{< /highlight >}}
## **كيفية استخدام Aspose.Cells for Android via Java**
سيقوم هذا الموضوع بإرشادك خلال الخطوات الضرورية لإعداد Aspose.Cells for Android via Java في بيئة تطوير Android Studio، بافتراض أن لديك بالفعل أحدث إصدار من Android Studio مثبت على جهازك وقد اكتسبت أيضًا أحدث إصدار من حزمة Aspose.Cells for Android via Java.

{{% alert color="primary" %}} 

إذا لم تكن قد قمت بتثبيت Android Studio بعد، يتعين عليك الحصول أولاً على إعداد Android Studio وتثبيته على جهازك. يمكنك تنزيل أحدث إصدار من Android Studio من [هنا](https://developer.android.com/studio/index.html#win-bundle) بينما تتوفر التفاصيل حول كيفية تثبيت البيئة المتكاملة للتطوير (IDE) [هنا](https://developer.android.com/studio/install.html).

{{% /alert %}} {{% alert color="primary" %}} 

يمكن تنزيل حزمة Aspose.Cells for Android via Java من [هنا](https://downloads.aspose.com/cells/androidjava). يرجى ملاحظة، تتكون كل حزمة إصدار من Aspose.Cells for Android via Java أساسًا من 2 ملفات كما هو موضح أدناه.

- **aspose-cells-x.x.x.jar** هو ملف المكتبة الرئيسي الذي يحتوي على جميع الفضاءات الاسمية من واجهة برمجة التطبيقات Aspose.Cells for Android via Java.
- **aspose-cells-x.x.x-libs.apk** هو ملف APK الذي يحتوي على ملف bcprov-jdk15-146.jar من طرف ثالث يستخدم لتوفير مرافق التشفير والفك تشفير التي تقدمها واجهة برمجة التطبيقات Aspose.Cells for Android via Java.

{{% /alert %}} 
### **البدء مع Aspose.Cells for Android via Java في Android Studio**
بمجرد تحميل بيئة تطوير Android Studio، انقر على File > New > New Project كما هو موضح أدناه.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_1.png)

يمكنك أيضًا إنشاء مشروع جديد من شاشة الترحيب في Android Studio كما هو موضح أدناه.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_2.png)

بعد ذلك، سيُطلب منك تحديد اسم التطبيق والنطاق وموقع تخزين ملفات المشروع. يمكنك اختيار تغيير القيم الافتراضية حسب اختيارك أو الاحتفاظ بها كما هي، وانقر على Next.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_3.png)

في الخطوة التالية، يجب عليك تحديد جهاز Android الذي ترغب في استضافة/تشغيل تطبيقك عليه. بمجرد تحديد الجهاز، انقر على الزر Next.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_4.png)

الآن تحتاج إلى تحديد النشاط من قائمة محددة مسبقًا للقوالب. من أجل إبقاء العرض بسيطًا، قمنا باختيار قالب النشاط الفارغ كما هو موضح أدناه.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_5.png)

انقر على زر Finish على مربع الحوار التخصيص للنشاط حيث سنحتفظ بجميع الإعدادات الافتراضية كما هي.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_6.png)

بمجرد النقر على الزر Finish في الخطوة السابقة، سيبدأ البيئة المتكاملة للتطوير (IDE) في بناء المشروع كما هو موضح أدناه. دعه ينتهي أو انقر على الزر Cancel.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_7.png)

الآن تم تحميل المشروع في البيئة المتكاملة للتطوير (IDE)، ومع ذلك، قد ترغب في تغيير العرض إلى Project حتى تتمكن من عرض التسلسل الهرمي الكامل لملفات المشروع. من أجل تغيير العرض، يرجى التحقق من لقطة الشاشة التالية.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_8.png)

بعد تغيير العرض إلى مشروع، اعثر على ملف build.gradle وقم بتحميله في المحرر وألصق المقطع التالي كما هو موضح أدناه.

{{< highlight java >}}

 dexOptions{

    javaMaxHeapSize "4g"

}

{{< /highlight >}}

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_9.png)

الخطوة التالية، سنقوم بإضافة مكتبة Aspose.Cells لـ Android via Java Jar إلى المشروع. هناك ٢ خطوة مهمتان كما هو موضح أدناه.

 - انسخ مكتبة Aspose.Cells لـ Android via Java Jar يدويًا إلى المجلد \app\libs.
- أضف مكتبة Aspose.Cells لـ Android via Java Jar كمكتبة إلى الوحدة كما هو موضح أدناه.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_10.png)

سيُطلب منك اختيار الوحدة التي ترغب في إضافة Aspose.Cells for Java.Android Jar كمكتبة إليها. يُرجى اختيار الوحدة المناسبة والنقر فوق موافق.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_11.png)

يجب أيضًا إضافة ملف APK إلى المشروع. يجب نسخ ملف APK إلى المجلد \app\src\main\assets. إذا لم يكن لديك مجلد assets تحت المجلد الرئيسي، يمكنك إنشاؤه عن طريق النقر بزر الماوس الأيمن على العقدة الرئيسية في العرض الخاص بالمشروع. حدد جديد > مجلد > مجلد الأصول.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_12.png)

بمجرد إضافة ملف APK إلى المشر. ع، يجب التحميل من قبل المشروع. هناك ٢ طريقة لتحميل ملف APK كما يلي.

- قم بتحميل ملف APK في فئة التطبيق المخصص باستخدام المقطع المقدم أدناه، وسجل فئة التطبيق المخصصة في AndroidManifest.xml.

{{< highlight java >}}

 LibsLoadHelper.loadLibs(this);

{{< /highlight >}}

- تحميل ملف APK في طريقة OnCreate في MainActivity.

{{< highlight java >}}

 LibsLoadHelper.loadLibs(getApplicationContext());

{{< /highlight >}}

الآن نحن جاهزون لكتابة الكود. من أجل الحفاظ على سهولة فهم التوضيح، قمنا بإضافة ويدجت Button إلى التخطيط وسنقوم بمعالجة حدث النقر عليه كما يلي.

{{< highlight java >}}

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

عند تشغيل التطبيق باستخدام زر التشغيل على واجهة الـ IDE (أو باستخدام SHIFT + F10)، سيرقي المحاكي التطبيق كما هو موضح أدناه.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_13.png)

بفصل الزر على المحاكي سيُنفّذ الكود لإنشاء جدول بيانات جديد في مجلد التخزين الخارجي للمحاكي. يمكنك الوصول إلى الملف من مدير الجهاز Android كما هو موضح أدناه.

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_14.png)

![todo:image_alt_text](aspose-cells-for-android-via-java-installation_15.png)


