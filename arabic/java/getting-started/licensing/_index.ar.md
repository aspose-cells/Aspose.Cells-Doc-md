---
title: ترخيص
type: docs
weight: 50
url: /ar/java/licensing/
description: توفر Aspose.Cells for JAVA خططًا مختلفة للشراء أو تقدم تجربة مجانية وترخيصًا مؤقتًا لمدة 30 يومًا للتقييم باستخدام سياسات الترخيص والاشتراك في جافا.
keywords: تطبيق ترخيص جافا من القرص أو التيار. تعيين الترخيص في جافا من القرص أو التيار. تطبيق الترخيص في Aspose.Cells for Java.
---

## **كيفية تطبيق ترخيص في مكون Aspose.Cells**

الترخيص هو ملف نصي عادي بتنسيق XML يحتوي على تفاصيل مثل اسم المنتج، عدد المطورين الذين يتم ترخيصهم، تاريخ انتهاء الاشتراك وما إلى ذلك. يتم توقيع الملف رقمياً، لذلك لا تقم بتعديل الملف؛ حتى إضافة عرضية لسطر إضافي إلى الملف ستجعله غير صالح.

يجب عليك تعيين ترخيص قبل استخدام Aspose.Cells إذا كنت ترغب في تجنب قيود التقييم الخاصة به. أنت مطالب بتعيين ترخيص مرة واحدة فقط لكل تطبيق أو عملية.

يمكن تحميل الترخيص من تيار أو ملف في المواقع التالية:

1. المسار الصريح.
1. المجلد الذي يحتوي على Aspose.Cells.jar.

استخدم طريقة [License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream)) لترخيص العنصر. غالبًا ما يكون أسهل طريقة لتعيين ترخيص هو وضع ملف الترخيص في نفس مجلد Aspose.Cells.jar وتحديد اسم الملف فقط دون مسار كما هو موضح في المثال التالي:

### **كيفية تطبيق ترخيص من القرص**

في هذا المثال سيحاول **Aspose.Cells** العثور على ملف الترخيص في المجلد الذي يحتوي على ملفات JARs لتطبيقك.

{{< highlight csharp >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

### **كيفية تطبيق ترخيص من التيار**

يقوم بتهيئة ترخيص من تيار.

{{< highlight csharp >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

### **كيفية تطبيق ترخيص في Aspose.Cells.GridWeb**

يُوصى بوضع رمز الترخيص في مكان في تطبيق الويب الخاص بك حيث يجب معالجته أولا.

{{< highlight csharp >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

## **كيفية تطبيق ترخيص معتمد على الاستخدام**

تسمح Aspose.Cells للمطورين بتطبيق مفتاح معتمد. إنه آلية ترخيص جديدة. سيتم استخدام آلية الترخيص الجديدة إلى جانب الطريقة الترخيص الموجودة. يمكن لأولئك العملاء الذين يرغبون في الفوترة استنادًا إلى استخدام ميزات واجهة برمجة التطبيقات استخدام الترخيص المعتمد. لمزيد من التفاصيل، يرجى الرجوع إلى قسم [معتمد الاستخدام الترخيص الأكثر مبيعًا](https://purchase.aspose.com/faqs/licensing/metered).

تم إدخال فئة جديدة [Metered](https://reference.aspose.com/cells/java/com.aspose.cells/Metered) لتطبيق المفتاح القياسي. يتضمن الكود العيني التالي كيفية ضبط المفتاح العام والخاص للفئة المقاسة.

{{< highlight java >}}

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
