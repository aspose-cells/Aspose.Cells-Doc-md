---
title: طلب ترخيص
type: docs
weight: 40
url: /ar/java/applying-a-license/
---
{{% alert color="primary" %}}

 بمجرد أن تكون سعيدًا بتقييمك لـ Aspose.Cells ،[شراء رخصة](https://purchase.aspose.com/buy) على موقع الويب Aspose. اجعل نفسك على دراية بالاختلاف[أنواع التراخيص](https://purchase.aspose.com/policies/license-types/) تقدم. إذا كان لديك أي أسئلة ، فلا تتردد في ذلك[اتصل بفريق المبيعات Aspose](https://about.aspose.com/contact).

يحمل كل ترخيص Aspose اشتراكًا لمدة عام واحد للترقيات المجانية لأي إصدارات جديدة أو إصلاحات تظهر خلال هذا الوقت. الدعم الفني مجاني وغير محدود ومقدم لكل من المستخدمين المرخصين والمقيّمين.

الترخيص عبارة عن ملف XML نص عادي يحتوي على تفاصيل مثل اسم المنتج وعدد المطورين المرخصين وتاريخ انتهاء الاشتراك وما إلى ذلك. الملف موقّع رقميًا ، لذا لا تقم بتعديل الملف: حتى إضافة فاصل أسطر إضافي في الملف سيؤدي إلى إبطاله.

تحتاج إلى تعيين ترخيص قبل إجراء أي عمليات مع المستندات. تأكد من القيام بذلك قبل إنشاء كائن المستند. أنت مطالب فقط بتعيين ترخيص مرة واحدة لكل تطبيق أو عملية.

{{% /alert %}}

## **تحميل ملف الترخيص**

 في Aspose.Cells for Android via Java ، يمكن أن يكون الترخيص[جزءا لا يتجزأ من الموارد](/cells/ar/java/applying-a-license/#applying-a-license-from-an-embedded-resource)، أو محملة من دفق:

1.  ضع ملف الترخيص في أي مكان على**/ mnt / sdcard /**.
1. قم بإنشاء دفق يشير إلى ملف.
1. قم بتمرير الدفق (الذي يحتوي على ملف الترخيص) إلى طريقة SetLicense.

**Java**

{{< highlight "java" >}}

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

1.  أضف ملف الترخيص كمورد لتطبيقك**الدقة / الخام** مجلد.
 يجب أن يكون ملف الترخيص مرئيًا في ملف**الدقة / الخام** مجلد.
1. الوصول / تحميل الترخيص من المورد باستخدام نموذج التعليمات البرمجية التالي.

**Java**

{{< highlight "java" >}}

 License license = new License();

InputStream inputStream = getResources().openRawResource(R.raw.license);

license.setLicense(inputStream);

{{< /highlight >}}
