---
title: تشفير ملفات اكسل
type: docs
weight: 90
url: /ar/net/encrypting-excel-files/
---
{{% alert color="primary" %}}

يمكّنك Microsoft Excel (97 - 365) من تشفير جداول البيانات وحمايتها بكلمة مرور. يستخدم الخوارزميات التي يوفرها مزود خدمة التشفير ، أو CSP ، وهي مجموعة من خوارزميات التشفير ذات الخصائص المختلفة. CSP الافتراضي هو "متوافق مع Office 97/2000" أو "تشفير ضعيف (XOR)". من المهم اختيار طول مفتاح التشفير المناسب. لا يدعم بعض CSPs أكثر من 40 أو 56 بت. يعتبر هذا تشفير ضعيف. للتشفير القوي ، يجب ألا يقل طول المفتاح عن 128 بت. يحتوي Microsoft Windows على CSPs الذين يقدمون أنواع تشفير قوية أيضًا ، على سبيل المثال "موفر التشفير القوي Microsoft". لإعطائك فكرة ، تشفير 128 بت هو ما تستخدمه البنوك لتشفير الاتصال بأنظمتها المصرفية عبر الإنترنت.

يسمح لك Aspose.Cells بتشفير وحماية كلمة مرور Microsoft ملفات Excel بنوع التشفير المطلوب.

{{% /alert %}}

## **باستخدام Microsoft إكسل**

لتعيين إعدادات تشفير الملفات في Microsoft Excel (هنا Microsoft Excel 2003):

1.  من**أدوات** القائمة ، حدد**خيارات**سيظهر مربع حوار.
1.  حدد ملف**حماية** التبويب.
1.  أدخل كلمة مرور وانقر**متقدم**
1. اختر نوع التشفير وقم بتأكيد كلمة المرور.

## **التشفير مع Aspose.Cells**

يوضح المثال التالي كيفية تشفير وحماية كلمة المرور لملف excel باستخدام Aspose.Cells API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **تحديد كلمة المرور لتعديل الخيار**

 يوضح المثال التالي كيفية تعيين ملف**كلمة مرور للتعديل** خيار Microsoft Excel لملف موجود باستخدام Aspose.Cells API.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}

## **تحقق من كلمة مرور الملف المشفر**

 للتحقق من كلمة المرور الخاصة بالملف المشفر ، يوفر Aspose.Cells for .NET الامتداد[**اكد كلمة المرور**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) طريقة. تقبل هذه الطرق معلمتين ، دفق الملف وكلمة المرور التي يجب التحقق منها.
يوضح مقتطف الشفرة التالي استخدام ملف[**اكد كلمة المرور**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) طريقة للتحقق مما إذا كانت كلمة المرور المقدمة صالحة أم لا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

## **تشفير / فك تشفير ملف ODS بواسطة Aspose.Cells**

Aspose.Cells يسمح بتشفير وفك تشفير ملف ODS. يمكن فتح ملف ODS الذي تم فك تشفيره في كل من Excel و OpenOffice ، ولكن لا يمكن فتح ملف ODS المشفر إلا بواسطة OpenOffice بعد توفير كلمة المرور. لا يستطيع Excel فتح ملف ODS المشفر وقد يرفع رسالة تحذير. لا تنطبق خيارات التشفير على ملف ODS بخلاف أنواع الملفات الأخرى. لتشفير ملف ODS ، قم بتحميل الملف واضبط الامتداد[**إعدادات المصنف**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) قيمة كلمة المرور الفعلية قبل حفظها. يمكن فتح ملف ODS المشفر الناتج في OpenOffice فقط.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

 لفك تشفير ملف ODS ، قم بتحميل الملف عن طريق توفير كلمة مرور في ملف[**LoadOptions**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password) . بمجرد تحميل الملف ، اضبط ملف[**إعدادات المصنف**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) سلسلة لاغية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
