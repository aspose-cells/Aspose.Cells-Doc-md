---
title: تصدير ملف Microsoft Excel
type: docs
weight: 50
url: /ar/net/aspose-cells-gridweb/export-microsoft-excel-file/
keywords: GridWeb، تصدير
description: يقدم هذا المقال كيفية تصدير الملف في GridWeb.
---

{{% alert color="primary" %}} 

من الممكن إنشاء ملفات Microsoft Excel جديدة أو تلاعب الملفات الحالية على مواقع الويب في وضع واجهة المستخدم الرسومية باستخدام عنصر تحكم Aspose.Cells.GridWeb. يمكن حفظ الملفات ثم في ملفات Excel. يعمل Aspose.Cells.GridWeb بشكل فعال كمحرر جداول بيانات عبر الإنترنت. يصف هذا الموضوع كيفية حفظ محتوى الجدول في ملفات Excel.

{{% /alert %}} 
## **تصدير ملفات Excel**
### **تصدير كملف**
لحفظ محتوى عنصر تحكم Aspose.Cells.GridWeb كملف إكسل:

1. أضف عنصر تحكم Aspose.Cells.GridWeb إلى نموذج الويب الخاص بك.
1. احفظ عملك كملف إكسل في مسار محدد.
1. قم بتشغيل التطبيق.

{{% alert color="primary" %}} 

إذا لم تكن تعرف كيفية إضافة عنصر تحكم Aspose.Cells.GridWeb إلى نموذج الويب الخاص بك، فيجب عليك الرجوع إلى [إضافة GridWeb إلى نموذج الويب](/cells/ar/net/aspose-cells-gridweb/add-gridweb-to-web-form/)

{{% /alert %}} 

عندما يتم إضافة عنصر تحكم Aspose.Cells.GridWeb إلى نموذج نافذة، يتم إنشاء العنصر تلقائيًا وإضافته إلى النموذج بحجم افتراضي. لا يلزمك إنشاء كائن عنصر تحكم Aspose.Cells.GridWeb، كل ما عليك فعله هو سحب العنصر التحكم وإفلاته وبدء استخدامه.

يوضح المثال البرمجي أدناه كيفية حفظ محتوى الجدول في ملف إكسل.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-SaveExcelFile.cs" >}}

{{% alert color="primary" %}} 

إذا كان نظام الملفات الخاص بك NTFS، قم بمنح صلاحيات القراءة/الكتابة لحسابات ASPNET أو الجميع، وإلا فسوف تواجه استثناء الوصول مرفوض أثناء التشغيل.

{{% /alert %}} 

يمكن استخدام مقتطف الكود أعلاه بعدة طرق. الطريقة الشائعة هي إضافة زر يقوم بحفظ محتوى الجدول في ملف إكسل عند النقر. عنصر تحكم Aspose.Cells.GridWeb يقدم نهجًا أسهل لهذه المهمة. يتوفر عنصر تحكم Aspose.Cells.GridWeb بحدث يسمى SaveCommand. يمكن إضافة مقتطف الكود أعلاه إلى معالج حدث SaveCommand مما يسمح للمستخدمين بحفظ عملهم عن طريق النقر على زر **حفظ** المدمج في Aspose.Cells.GridWeb.

**حدث SaveCommand في GridWeb** 

![todo:image_alt_text](export-microsoft-excel-file_1.jpg)

**حفظ محتوى الجدول إلى Excel عن طريق النقر على زر الحفظ المدمج في GridWeb** 

![todo:image_alt_text](export-microsoft-excel-file_2.png)

{{% alert color="primary" %}} 

إذا كنت تعمل في بيئة Visual Studio، يمكنك بسهولة إنشاء معالج حدث SaveCommand عن طريق النقر المزدوج على الحدث في لوحة الخصائص. لمعرفة المزيد حول هذا، يرجى الرجوع إلى [العمل مع أحداث GridWeb](/cells/ar/net/aspose-cells-gridweb/working-with-gridweb-events/)

{{% /alert %}} 
### **تصدير كمسار**
من الممكن أيضًا حفظ محتوى الجدول في تدفق (على سبيل المثال MemoryStream).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-SaveExcelFileUsingStream.cs" >}}
