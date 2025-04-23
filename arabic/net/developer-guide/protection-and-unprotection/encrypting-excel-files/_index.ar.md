---
title: تشفير ملفات Excel
type: docs
weight: 90
url: /ar/net/encrypting-excel-files/
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) يتيح لك تشفير وحماية كلمة مرور جداول البيانات الخاصة بك. تستخدم خوارزميات المزود الخدمي الكريبتوجرافي، أو CSP، مجموعة من الخوارزميات الكريبتوجرافية ذات خصائص مختلفة. CSP الافتراضي هو 'Office 97/2000 Compatible' أو 'Weak Encryption (XOR)'. من المهم اختيار طول مفتاح التشفير المناسب. بعض CSPs لا تدعم أكثر من 40 أو 56 بت. يعتبر ذلك تشفير ضعيف. للحصول على تشفير قوي، يتطلب طول مفتاح أدنى لـ 128 بت. تحتوي نوافذ Microsoft على CSPs تقدم أنواع تشفير قوية أيضًا، على سبيل المثال 'مزود تشفير قوي من Microsoft'. لإعطائك فكرة، تشفير 128 بت هو ما تستخدمه البنوك لتشفير الاتصال مع أنظمة الخدمات المصرفية عبر الإنترنت الخاصة بهم.

تسمح Aspose.Cells لك بتشفير وحماية ملفات Microsoft Excel بنوع التشفير الذي ترغب فيه.

{{% /alert %}}

## **استخدام Microsoft Excel**

لضبط إعدادات تشفير الملف في Microsoft Excel (هنا Microsoft Excel 2003):

1. من قائمة **الأدوات**، حدد **الخيارات**. ستظهر نافذة حوارية.
١. حدد علامة التبويب **الأمان**.
1. أدخل كلمة مرور وانقر **متقدم**
١. اختر نوع التشفير وقم بتأكيد كلمة المرور.

## **التشفير مع Aspose.Cells**

المثال التالي يوضح كيفية تشفير وحماية ملف Excel بكلمة مرور باستخدام واجهة برمجة التطبيقات Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-1.cs" >}}

### **تحديد كلمة المرور لخيار تعديل**

المثال التالي يوضح كيفية ضبط خيار Microsoft Excel **كلمة المرور للتعديل** لملف موجود باستخدام واجهة برمجة التطبيقات Aspose.Cells.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingFiles-SpecifyPasswordToModifyOption.cs" >}}

## **تحقق من كلمة المرور للملف المُشفر**

للتحقق من كلمة المرور للملف المشفر، يوفر Aspose.Cells for .NET الدوال التالية. تقبل هذه الدوال معلمتين، تيار الملف وكلمة المرور التي يجب التحقق منها.
يوضح مقتطف الشيفرة التالي استخدام الطريقة [**VerifyPassword**](https://reference.aspose.com/cells/net/aspose.cells/fileformatutil/methods/verifypassword) للتحقق مما إذا كانت كلمة المرور المقدمة صالحة أم لا.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-VerifyPassword-1.cs" >}}

## **تشفير/فك تشفير ملف ODS بـ Aspose.Cells**

يسمح Aspose.Cells بتشفير وفك تشفير ملف ODS. يمكن فتح ملف ODS المفك شفرته في كل من Excel و OpenOffice، ومع ذلك، يمكن فتح ملف ODS المشفر شفرته فقط بواسطة OpenOffice بعد تقديم كلمة المرور. لا يمكن لـ Excel فتح ملف ODS المشفر وقد يثير رسالة تحذير. خيارات التشفير غير مطبقة على ملفات ODS على عكس أنواع الملفات الأخرى. لتشفير ملف ODS، قم بتحميل الملف وضبط [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) بنفس كلمة المرور الفعلية قبل حفظه. يمكن فتح ملف ODS المشفر الناتج في OpenOffice فقط.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-EncryptingODSFiles-1.cs" >}}

لفك تشفير ملف ODS، قم بتحميل الملف عن طريق تقديم كلمة مرور في [**LoadOptions.Password**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/properties/password). بمجرد تحميل الملف، ضبط السلسلة [**WorkbookSettings.Password**](https://reference.aspose.com/cells/net/aspose.cells/workbooksettings/properties/password) على القيمة الخالية.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Files-Utility-DecryptingODSFiles-1.cs" >}}
{{< app/cells/assistant language="csharp" >}}
