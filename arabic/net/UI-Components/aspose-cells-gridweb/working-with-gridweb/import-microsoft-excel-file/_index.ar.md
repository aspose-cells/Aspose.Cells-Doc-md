---
title: قم باستيراد ملف إكسل Microsoft
type: docs
weight: 40
url: /ar/net/import-microsoft-excel-file/
---
{{% alert color="primary" %}} 

مثل Aspose.Cells.GridDesktop ، Aspose.Cells. يمكن للتحكم في شبكة الويب فتح وتحميل Microsoft ملفات Excel - كاملة مع البيانات والتنسيق والمخططات والصور وما إلى ذلك - ولكن في تطبيقات الويب. يشرح هذا الموضوع كيف.

{{% /alert %}} 
## **استيراد ملفات Excel**
### **استيراد من ملف**
لفتح ملف Excel باستخدام عنصر تحكم Aspose.Cells.GridWeb:

1. قم بإضافة عنصر تحكم Aspose.Cells.GridWeb إلى نموذج ويب.
1. قم باستيراد ملف Excel عن طريق تحديد مسار الملف.
1. قم بتشغيل التطبيق.

{{% alert color="primary" %}} 

 إذا كنت لا تعرف كيفية إضافة عنصر التحكم إلى نموذج ويب ، فارجع إلى[أضف GridWeb إلى نموذج الويب](/cells/ar/net/add-gridweb-to-web-form/).

{{% /alert %}} 

عند إضافة عنصر تحكم ويب Aspose.Cells.GridWeb إلى نموذج ويب ، يتم إنشاء عنصر التحكم تلقائيًا وإضافته إلى النموذج بالحجم الافتراضي. ليس عليك إنشاء عنصر تحكم Aspose.Cells.GridWeb ، كل ما عليك فعله هو سحب عنصر التحكم وإفلاته والبدء في استخدامه.

ومع ذلك ، لتحميل المحتوى من ملف Excel إلى عنصر تحكم Aspose.Cells.GridWeb ، يجب عليك استدعاء الأسلوب ImportExcelFile لتحديد مسار ملف Excel. بعد ذلك ، سيجد عنصر تحكم Aspose.Cells.GridWeb الملف تلقائيًا من المسار المحدد ويعرض محتوياته. يتم توفير مقتطف التعليمات البرمجية الذي يقوم بتحميل محتويات ملف Excel أدناه.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-LoadExcelFile.cs" >}}


يمكن استخدام مقتطف الشفرة أعلاه بالطريقة التي تريدها. على سبيل المثال ، لتحميل ملف Excel تلقائيًا عند تحميل نموذج ويب ، أضف هذا الرمز إلى حدث Page_Load للنموذج. إذا كنت تريد فتح ملف عند النقر فوق الزر ، فأضف زرًا إلى نموذج الويب واكتب الرمز أعلاه ضمن حدث النقر على الزر.

**يتم تحميل ملف Excel عند النقر فوق الزر** 

![ما يجب القيام به: image_بديل_نص](import-microsoft-excel-file_1.png)

{{% alert color="primary" %}} 

إذا كان نظام الملفات لديك هو NTFS ، فيجب منح إذن وصول للقراءة إلى حسابات المستخدمين ASPNET أو Everyone أو ستحصل على استثناء مرفوض في وقت التشغيل.

{{% /alert %}} 
### **الاستيراد من الدفق**
بالإضافة إلى فتح ملفات Excel من ملف ، يمكن لعنصر التحكم Aspose.Cells.GridWeb تحميل ملفات Excel من دفق. يعد استخدام الملف كتدفق طريقة أفضل لمنع أي نوع من الوصول إلى الملفات أو مشاركة مشكلات الانتهاك لأن هذا الأسلوب يضمن إغلاق جميع الاتصالات بالملفات عن طريق إغلاق الدفق.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-LoadExcelFileFromStream.cs" >}}
