---
title: استيراد ملف Microsoft Excel
type: docs
weight: 40
url: /ar/net/aspose-cells-gridweb/import-microsoft-excel-file/
keywords: GridWeb، الاستيراد
description: يقدم هذا المقال كيفية استيراد الملف في GridWeb.
---

{{% alert color="primary" %}} 

مثل Aspose.Cells.GridDesktop، يمكن للتحكم Aspose.Cells.GridWeb فتح وتحميل ملفات Microsoft Excel - مع البيانات والتنسيق والرسوم البيانية والصور وما إلى ذلك - ولكن في تطبيقات الويب. يشرح هذا الموضوع كيفية ذلك.

{{% /alert %}} 
## **استيراد ملفات Excel**
### **استيراد من ملف**
لفتح ملف Excel باستخدام تحكم Aspose.Cells.GridWeb:

1. أضف تحكم Aspose.Cells.GridWeb إلى نموذج الويب.
1. استيراد ملف Excel عن طريق تحديد مسار الملف.
1. قم بتشغيل التطبيق.

{{% alert color="primary" %}} 

إذا لم تكن تعرف كيفية إضافة التحكم إلى نموذج الويب، يُرجى الرجوع إلى [إضافة GridWeb إلى نموذج الويب](/cells/ar/net/aspose-cells-gridweb/add-gridweb-to-web-form/).

{{% /alert %}} 

عند إضافة تحكم Aspose.Cells.GridWeb إلى نموذج الويب، يتم إنشاء التحكم تلقائيًا وإضافته إلى النموذج بحجم افتراضي. لا داعي لك لإنشاء كائن تحكم Aspose.Cells.GridWeb، كل ما عليك فعله هو سحب التحكم وإسقاطه والبدء في استخدامه.

ومع ذلك، يجب عليك فيما يتعلق بتحميل المحتوى من ملف Excel إلى تحكم Aspose.Cells.GridWeb، استدعاء الطريقة ImportExcelFile لتحديد مسار ملف Excel. بعد ذلك، سيجد تحكم Aspose.Cells.GridWeb بشكل تلقائي الملف من المسار المحدد وعرض محتوياته. يتم توفير قصاصة الشفرة التي تحمل محتويات ملف Excel أدناه.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-LoadExcelFile.cs" >}}


يمكن استخدام قصاصة الشفرة أعلاه بأي شكل تريده. على سبيل المثال، لتحميل ملف Excel تلقائيًا عند تحميل نموذج ويب، أضف هذا الكود إلى حدث Page_Load للنموذج. إذا كنت ترغب في فتح ملف عند النقر فوق زر ما، أضف زرًا إلى نموذج الويب وأكتب الكود أعلاه تحت حدث Click للزر.

**يتم تحميل ملف Excel عند النقر فوق زر** 

![todo:image_alt_text](import-microsoft-excel-file_1.png)

{{% alert color="primary" %}} 

إذا كان نظام الملفات الخاص بك من نوع NTFS، يجب منح إذن الوصول لقراءة حسابات مستخدمي ASPNET أو الجميع أو ستحصل على استثناء لا يمكن الوصول إليه أثناء التشغيل.

{{% /alert %}} 
### **الاستيراد من التيار**
بالإضافة إلى فتح ملفات Excel من الملف، يمكن لتحكم Aspose.Cells.GridWeb تحميل ملفات Excel من تيار. استخدام الملف كتيار هو نهج أفضل لمنع أي مشاكل في الوصول إلى الملف أو مشكلات مشاركة الوصول لأن هذا النهج يضمن إغلاق جميع الاتصالات بالملفات عن طريق إغلاق التيار.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-LoadExcelFileFromStream.cs" >}}
