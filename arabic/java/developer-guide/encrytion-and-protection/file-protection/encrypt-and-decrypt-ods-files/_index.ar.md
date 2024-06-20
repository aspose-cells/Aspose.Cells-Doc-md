---
title: تشفير وفك تشفير ملفات ODS
type: docs
weight: 10
url: /ar/java/encrypt-and-decrypt-ods-files/
description: حماية كلمة المرور وتشفير ملفات ODS باستخدام Aspose.Cells for Java وهو مكتبة جافا نقية.
---

{{% alert color="primary" %}}
OpenOffice.org هو حزمة مكتبية كاملة الميزات تدعم حماية كلمة المرور وتشفير الملفات. ومع ذلك، يمكن فتح ملف ODS المُشفر فقط بواسطة OpenOffice بعد تقديم كلمة المرور. لا يمكن لإكسيل فتح ملف ODS المُشفر وقد يُعرِض رسالة تحذير. خيارات التشفير غير قابلة للتطبيق على ملفات ODS على عكس أنواع الملفات الأخرى. 
يسمح Aspose.Cells بتشفير وفك تشفير ملف ODS. يمكن فتح ملف ODS المفكك في كل من إكسيل وOpenOffice. 
{{% /alert %}}

## **التشفير باستخدام OpenOffice Calc**
1. حدد **حفظ ك** وانقر على مربع **حفظ بكلمة مرور**.
1. انقر على زر **حفظ**.
1. اكتب كلمة المرور المطلوبة في حقلي **أدخل كلمة المرور للفتح** و **تأكيد كلمة المرور** في نافذة تعيين كلمة المرور التي تفتح. 
1. انقر على زر **موافق** لحفظ الملف.

## **تشفير/فك تشفير ملف ODS:**

لتشفير ملف ODS، قم بتحميل الملف وتمرير كلمة المرور الفعلية إلى [**WorkbookSettings.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password) قبل حفظه. يمكن فتح ملف ODS المشفر الناتج في OpenOffice فقط. لفك تشفير ملف ODS، قم بتحميل الملف بتقديم كلمة المرور في ال [**LoadOptions.setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#Password). بمجرد تحميل الملف، قم باستدعاء الوظيفة [**Workbook.unprotect()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbook#unprotect(java.lang.String)) بكلمة المرور الفعلية كمعلمة ثم قم بتمرير قيمة فارغة إلى [**Workbook.getWorkbookSettings().setPassword()**](https://reference.aspose.com/cells/java/com.aspose.cells/workbooksettings#Password).

### **كود عينة:**

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-loading_saving-EncryptingODSFiles-EncryptingODSFiles.java" >}}
