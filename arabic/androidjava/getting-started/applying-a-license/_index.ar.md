---
title: تطبيق ترخيص
type: docs
weight: 40
url: /ar/java/applying-a-license/
---

{{% alert color="primary" %}}

بمجرد أن تكون راضيًا عن تقييمك لـ Aspose.Cells، [قم بشراء ترخيص](https://purchase.aspose.com/buy) على موقع Aspose. قم بإتقان أنواع التراخيص المختلفة المقدمة. إذا كان لديك أي أسئلة، فلا تتردد في [الاتصال بفريق مبيعات Aspose](https://about.aspose.com/contact).

يحمل كل ترخيص من Aspose اشتراكًا سنويًا للترقيات المجانية إلى أي إصدارات جديدة أو إصلاحات تصدر خلال هذا الوقت. الدعم الفني مجاني وغير محدود ومتاح للمستخدمين المرخصين والمستخدمين التجريبيين على حد سواء.

الترخيص هو ملف نصي عادي XML يحتوي على تفاصيل مثل اسم المنتج، عدد المطورين المرخص لهم، تاريخ انتهاء الاشتراك وما إلى ذلك. الملف موقع رقمياً، لذلك لا تقم بتعديل الملف: حتى إضافة فاصلة إلى الملف سيجعله غير صالح.

تحتاج إلى تعيين ترخيص قبل أداء أي عمليات على المستندات. تأكد من القيام بذلك قبل إنشاء كائن Document. سيُطلب منك ضبط ترخيص مرة واحدة فقط لكل تطبيق أو عملية.

{{% /alert %}}

## **تحميل ملف الترخيص**

في Aspose.Cells لـ Android via Java، يمكن تضمين الترخيص ك [مورد](/cells/ar/java/applying-a-license/#applying-a-license-from-an-embedded-resource)، أو تحميله من تيار:

1. ضع ملف الترخيص في أي مكان في **/mnt/sdcard/**.
1. أنشئ تيارًا يشير إلى الملف.
1. قم بتمرير التيار (الذي يحتوي على ملف الترخيص) إلى طريقة SetLicense.

**Java**

{{< highlight java >}}

 String dataDir = Environment.getExternalStorageDirectory().getPath() + "/";

// Create a stream object containing the license file

FileInputStream fstream = new FileInputStream(dataDir + "Aspose.Cells.Android.lic");

// Instantiate the License class

License license = new License();

//Set the license through the stream object

license.setLicense(fstream);

{{< /highlight >}}

### **تطبيق ترخيص من مورد مضمن**

للوصول إلى الترخيص كمورد بالاسم من ملف حزمة Android:

1. أضف ملف الترخيص كمورد في مجلد **res/raw** لتطبيقك.
   يجب ظهور ملف الترخيص في مجلد **res/raw**.
1. الوصول/تحميل الترخيص من المورد باستخدام الشفرة النموذجية التالية.

**Java**

{{< highlight java >}}

 License license = new License();

InputStream inputStream = getResources().openRawResource(R.raw.license);

license.setLicense(inputStream);

{{< /highlight >}}
