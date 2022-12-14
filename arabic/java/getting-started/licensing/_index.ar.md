---
title: الترخيص
type: docs
weight: 50
url: /ar/java/licensing/
---
{{% alert color="primary" %}} 

 يمكنك تنزيل إصدار تقييم من**Aspose.Cells** for Java من[صفحة التنزيل الخاصة به](https://repository.aspose.com/webapp/#/artifacts/browse/tree/General/repo/com/aspose/aspose-cells) @ Maven الريبو. يوفر الإصدار التقييمي نفس الإمكانات تمامًا مثل الإصدار المرخص للمنتج. علاوة على ذلك ، يصبح الإصدار التقييمي مرخصًا ببساطة عند شراء ترخيص وإضافة سطرين من التعليمات البرمجية لتطبيق الترخيص.

 بمجرد أن تكون سعيدًا بتقييمك لـ**Aspose.Cells** ، تستطيع[شراء رخصة](https://purchase.aspose.com)على موقع الويب Aspose. تعرف على أنواع الاشتراكات المختلفة المعروضة. إذا كان لديك أي أسئلة ، فلا تتردد في الاتصال بفريق المبيعات Aspose.

يحمل كل ترخيص Aspose اشتراكًا لمدة عام واحد للترقيات المجانية لأي إصدارات جديدة أو إصلاحات تظهر خلال هذا الوقت. الدعم الفني مجاني وغير محدود ومقدم لكل من المستخدمين المرخصين والمقيّمين.

{{% /alert %}} {{% alert color="primary" %}} 

 إذا كنت تريد الاختبار**Aspose.Cells** بدون قيود الإصدار التقييمي ، اطلب ترخيصًا مؤقتًا لمدة 30 يومًا. يرجى الرجوع إلى[كيف تحصل على رخصة مؤقتة؟](https://purchase.aspose.com/temporary-license) للمزيد من المعلومات.

{{% /alert %}}

## **قيود إصدار التقييم**

 نسخة تقييم**Aspose.Cells** يوفر المنتج (بدون ترخيص محدد) وظائف المنتج الكاملة ، ولكنه يقتصر على فتح 100 ملف في برنامج واحد وورقة عمل إضافية مع علامة مائية للتقييم.

القيود موضحة أدناه:

### **القيد الأول: عدد الملفات المفتوحة**

عند تشغيل برنامجك ، يمكنك فقط فتح 100 ملف Excel. إذا تجاوز التطبيق الخاص بك هذا الرقم ، فسيتم طرح استثناء.

### **القيد الثاني: ورقة عمل مع علامة مائية للتقييم**

![ما يجب القيام به: image_بديل_نص](licensing_1.png)

ستظهر ورقة العمل هذه دائمًا على أنها ورقة العمل النشطة. فقط في الإصدار المرخص ، يمكنك تعيين ورقة العمل النشطة على أوراق عمل أخرى.

## **تحديد الترخيص**

الترخيص عبارة عن ملف XML نص عادي يحتوي على تفاصيل مثل اسم المنتج وعدد المطورين المرخص لهم وتاريخ انتهاء الاشتراك وما إلى ذلك. الملف موقّع رقميًا ، لذا لا تقم بتعديل الملف ؛ حتى الإضافة غير المقصودة لكسر أسطر إضافي في الملف ستؤدي إلى إبطالها.

تحتاج إلى تعيين ترخيص قبل استخدام Aspose.Cells إذا كنت تريد تجنب قيود التقييم الخاصة به. أنت مطالب فقط بتعيين ترخيص مرة واحدة لكل تطبيق أو عملية.

يمكن تحميل الترخيص من دفق أو ملف في المواقع التالية:

1. مسار صريح.
1. المجلد الذي يحتوي على Aspose.Cells.jar.

 استخدم ال[License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream)) طريقة لترخيص المكون. غالبًا ما تكون أسهل طريقة لتعيين ترخيص هي وضع ملف الترخيص في نفس المجلد مثل Aspose.Cells.jar وتحديد اسم الملف فقط بدون مسار كما هو موضح في المثال التالي:

### **مثال 1**

 في هذا المثال**Aspose.Cells** سيحاول العثور على ملف الترخيص في المجلد الذي يحتوي على JARs للتطبيق الخاص بك.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

### **مثال 2**

يقوم بتهيئة ترخيص من دفق.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

### **ملاحظات حول تطبيق ترخيص في Aspose.Cells.GridWeb**

يوصى بوضع كود الترخيص في مكان ما في تطبيق الويب الخاص بك حيث يجب معالجته أولاً.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **طلب ترخيص مقنن**

Aspose.Cells يسمح للمطورين بتطبيق المفتاح المقنن. إنها آلية ترخيص جديدة. سيتم استخدام آلية الترخيص الجديدة جنبًا إلى جنب مع طريقة الترخيص الحالية. يمكن للعملاء الذين يريدون أن تتم محاسبتهم بناءً على استخدام ميزات API استخدام الترخيص المقنن. لمزيد من التفاصيل ، يرجى الرجوع إلى[الأسئلة الشائعة حول الترخيص المقنن](https://purchase.aspose.com/faqs/licensing/metered)الجزء.

فئة جديدة[مقننة](https://reference.aspose.com/cells/java/com.aspose.cells/Metered)تم تقديمه لتطبيق المفتاح المقنن. فيما يلي نموذج التعليمات البرمجية الذي يوضح كيفية تعيين المفتاح العام والخاص الذي تم قياسه.

{{< highlight "java" >}}

//Set metered public and private keys

Metered metered = new Metered();

//Access the setMeteredKey property and pass public and private keys as parameters

metered.setMeteredKey("************", "************");

//Instantiate a new Workbook

Workbook workbook = new Workbook();

//Check if the license is set

System.out.println(workbook.isLicensed());

//Get the Consumption quantity

double amountBefore = Metered.getConsumptionQuantity();

System.out.println(amountBefore);

Workbook workbook2 = new Workbook("Book1.xlsx");

workbook2.save("out1.xlsx");

//Get the Consumption quantity again which should be greater a bit

double amountAfter = Metered.getConsumptionQuantity();

System.out.println(amountAfter);

{{< /highlight >}}
