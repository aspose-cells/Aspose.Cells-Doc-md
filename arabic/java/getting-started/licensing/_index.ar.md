---
title: Licensing
type: docs
weight: 50
url: /ar/java/licensing/
description: يوفر Aspose.Cells لـ JAVA خططًا مختلفة للشراء أو يقدم نسخة تجريبية مجانية وترخيصًا مؤقتًا لمدة 30 يومًا للتقييم باستخدام Licensing وسياسات الاشتراك في Java.
keywords: Java Apply License from Disk or Stream. Java Set License from Disk or Stream. Apply License in Aspose.Cells for Java.
---
##  **كيفية تقديم طلب ترخيص في مكون Aspose.Cells**

الترخيص عبارة عن ملف XML نصي عادي يحتوي على تفاصيل مثل اسم المنتج وعدد المطورين المرخص لهم وتاريخ انتهاء صلاحية الاشتراك وما إلى ذلك. تم توقيع الملف رقميًا، لذا لا تقم بتعديل الملف؛ حتى الإضافة غير المقصودة لفاصل أسطر إضافي في الملف ستؤدي إلى إبطاله.

تحتاج إلى تعيين ترخيص قبل استخدام Aspose.Cells إذا كنت تريد تجنب قيود التقييم الخاصة به. لا يُطلب منك سوى تعيين ترخيص مرة واحدة لكل تطبيق أو عملية.

يمكن تحميل الترخيص من دفق أو ملف في المواقع التالية:

1. المسار الصريح.
1. المجلد الذي يحتوي على Aspose.Cells.jar.

 استخدم ال[License.setLicense](https://reference.aspose.com/cells/java/com.aspose.cells/license#setLicense(java.io.InputStream)) طريقة ترخيص المكون. غالبًا ما تكون أسهل طريقة لتعيين ترخيص هي وضع ملف الترخيص في نفس المجلد مثل Aspose.Cells.jar وتحديد اسم الملف فقط بدون مسار كما هو موضح في المثال التالي:

###  **كيفية تطبيق ترخيص من القرص**

 في هذا المثال**Aspose.Cells** سيحاول العثور على ملف الترخيص في المجلد الذي يحتوي على ملفات JAR الخاصة بتطبيقك.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense("Aspose.Cells.Java.lic");

{{< /highlight >}}

###  **كيفية تطبيق ترخيص من Stream**

تهيئة الترخيص من الدفق.

{{< highlight "csharp" >}}

com.aspose.cells.License license = new com.aspose.cells.License();

license.setLicense(new java.io.FileInputStream("Aspose.Cells.Java.lic"));

{{< /highlight >}}

###  **كيفية تقديم طلب ترخيص في Aspose.Cells.GridWeb**

يوصى بوضع رمز الترخيص في مكان في تطبيق الويب الخاص بك حيث يجب معالجته أولاً.

{{< highlight "csharp" >}}

//Instantiate an instance of license and set the license file through its path

com.aspose.gridweb.License lic = new com.aspose.gridweb.License();

lic.setLicense("Aspose.Cells.lic");

{{< /highlight >}}

##  **كيفية تطبيق الترخيص المقنن**

Aspose.Cells يسمح للمطورين بتطبيق المفتاح المقنن. إنها آلية ترخيص جديدة. وسيتم استخدام آلية الترخيص الجديدة إلى جانب طريقة الترخيص الحالية. يمكن لهؤلاء العملاء الذين يريدون أن تتم محاسبتهم على أساس استخدام ميزات API استخدام الترخيص المقنن. لمزيد من التفاصيل، يرجى الرجوع إلى[عداد Licensing الأسئلة الشائعة](https://purchase.aspose.com/faqs/licensing/metered)قسم.

فئة جديدة[مقننة](https://reference.aspose.com/cells/java/com.aspose.cells/Metered)تم تقديمه لتطبيق المفتاح المقنن. فيما يلي نموذج التعليمات البرمجية الذي يوضح كيفية تعيين المفتاح العام والخاص.

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
