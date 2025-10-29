---
title: تشفير ملفات Excel
type: docs
weight: 90
url: /ar/python-net/encrypting-excel-files/
---

{{% alert color="primary" %}}

Microsoft Excel (97 - 365) يتيح لك تشفير وحماية كلمة مرور جداول البيانات الخاصة بك. تستخدم خوارزميات المزود الخدمي الكريبتوجرافي، أو CSP، مجموعة من الخوارزميات الكريبتوجرافية ذات خصائص مختلفة. CSP الافتراضي هو 'Office 97/2000 Compatible' أو 'Weak Encryption (XOR)'. من المهم اختيار طول مفتاح التشفير المناسب. بعض CSPs لا تدعم أكثر من 40 أو 56 بت. يعتبر ذلك تشفير ضعيف. للحصول على تشفير قوي، يتطلب طول مفتاح أدنى لـ 128 بت. تحتوي نوافذ Microsoft على CSPs تقدم أنواع تشفير قوية أيضًا، على سبيل المثال 'مزود تشفير قوي من Microsoft'. لإعطائك فكرة، تشفير 128 بت هو ما تستخدمه البنوك لتشفير الاتصال مع أنظمة الخدمات المصرفية عبر الإنترنت الخاصة بهم.

يسمح Aspose.Cells للبايثون via .NET بتشفير وحماية ملفات Microsoft Excel بكلمة مرور ونوع التشفير الذي تريده.

{{% /alert %}}

## **استخدام Microsoft Excel**

لضبط إعدادات تشفير الملف في Microsoft Excel (هنا Microsoft Excel 2003):

1. من قائمة **الأدوات**، حدد **الخيارات**. ستظهر نافذة حوارية.
١. حدد علامة التبويب **الأمان**.
1. أدخل كلمة مرور وانقر **متقدم**
١. اختر نوع التشفير وقم بتأكيد كلمة المرور.

## **التشفير مع Aspose.Cells**

يعرض المثال التالي كيفية تشفير وحماية كلمة مرور لملف إكسل باستخدام واجهة برمجة التطبيقات Aspose.Cells لبايثون via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingFiles-1.py" >}}

### **تحديد كلمة المرور لخيار تعديل**

يعرض المثال التالي كيفية تعيين خيار **كلمة المرور للتعديل** لملف إكسل Microsoft Excel لملف موجود باستخدام واجهة برمجة التطبيقات Aspose.Cells لبايثون via .NET.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-SpecifyPasswordToModifyOption.py" >}}

## **تحقق من كلمة المرور للملف المُشفر**

للتحقق من كلمة مرور الملف المشفر، يوفر Aspose.Cells for Python via .NET طريقة [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password). تقبل هذه الطرق معامليْن، تيار الملف وكلمة المرور التي تحتاج للتحقق.
يوضح مقتطف الشيفرة التالي استخدام الطريقة [**verify_password**](https://reference.aspose.com/cells/python-net/aspose.cells/fileformatutil/verify_password) للتحقق مما إذا كانت كلمة المرور المقدمة صالحة أم لا.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-VerifyPassword-1.py" >}}

## **تشفير/فك تشفير ملف ODS**

يسمح Aspose.Cells للبايثون via .NET بتشفير وفك تشفير ملفات ODS. يمكن فتح ملف ODS غير المشفر في Excel وOpenOffice، ولكن الملف المشفر يمكن فتحه فقط بواسطة OpenOffice بعد إدخال كلمة المرور. لا يمكن لـ Excel فتح ملف ODS المشفر وقد يعرض رسالة تحذير. خيارات التشفير غير قابلة للتطبيق على ملفات ODS على عكس أنواع الملفات الأخرى. لتشفير ملف ODS، قم بتحميل الملف وضبط قيمة [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) على كلمة المرور الفعلية قبل الحفظ. يمكن فتح ملف ODS المشفر الناتج فقط في OpenOffice.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-EncryptingODSFiles-1.py" >}}

لفك تشفير ملف ODS، قم بتحميل الملف عن طريق تقديم كلمة مرور في [**LoadOptions.password**](https://reference.aspose.com/cells/python-net/aspose.cells/loadoptions/password). بمجرد تحميل الملف، ضبط السلسلة [**WorkbookSettings.password**](https://reference.aspose.com/cells/python-net/aspose.cells/workbooksettings/password) على القيمة الخالية.

{{< gist "aspose-cells-gists" "7bb30376b4d40cdfd596286870fb9752" "Protection-and-unprotection-DecryptingODSFiles-1.py" >}}

{{< app/cells/assistant language="python-net" >}}
