---
title: تشفير وفك تشفير ملفات ODS
type: docs
weight: 10
url: /ar/java/encrypt-and-decrypt-ods-files/
description: حماية كلمة المرور وتشفير ملفات ODS باستخدام Aspose.Cells for Java وهي مكتبة Java خالصة.
---
{{% alert color="primary" %}}
 OpenOffice.org عبارة عن مجموعة مكتبية كاملة الميزات تدعم حماية كلمة المرور وتشفير الملفات. ومع ذلك ، لا يمكن فتح ملف ODS المشفر إلا بواسطة OpenOffice بعد توفير كلمة المرور. لا يمكن لبرنامج Excel فتح ملف ODS المشفر وقد يرفع رسالة تحذير. لا تنطبق خيارات التشفير على ملف ODS بخلاف أنواع الملفات الأخرى.
 Aspose.Cells يسمح بتشفير وفك تشفير ملف ODS. يمكن فتح ملف ODS الذي تم فك تشفيره في كل من Excel و OpenOffice ،
{{% /alert %}}

## **تشفير باستخدام OpenOffice Calc**
1.  يختار**حفظ باسم** وانقر فوق ملف**حفظ بكلمة مرور** علبة.
1.  انقر على**يحفظ** زر.
1.  اكتب كلمة المرور التي تريدها في كلا الملفين**أدخل كلمة المرور للفتح** و**تأكيد كلمة المرور** الحقول في نافذة تعيين كلمة المرور التي تفتح.
1.  انقر على**نعم** زر لحفظ الملف.

## **تشفير / فك تشفير ملف ODS:**

 لتشفير ملف ODS ، قم بتحميل الملف ومرر كلمة المرور الفعلية إلى[**WorkbookSettings.setPassword ()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password) قبل حفظه. يمكن فتح ملف ODS المشفر الناتج في OpenOffice فقط. لفك تشفير ملف ODS ، قم بتحميل الملف عن طريق توفير كلمة المرور في ملف[**LoadOptions.setPassword ()**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#Password) . بمجرد تحميل الملف ، قم باستدعاء الوظيفة[**Workbook.unprotect ()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotect(java.lang.String) ) باستخدام كلمة المرور الفعلية كوسيطة وأخيراً تمرير قيمة فارغة إلى[**Workbook.getWorkbookSettings (). setPassword ()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password).

### **عينة من الرموز:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingODSFiles-EncryptingODSFiles.java" >}}
