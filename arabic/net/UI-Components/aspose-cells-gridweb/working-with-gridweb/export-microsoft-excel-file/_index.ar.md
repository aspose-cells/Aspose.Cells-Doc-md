---
title: تصدير ملف إكسل Microsoft
type: docs
weight: 50
url: /ar/net/export-microsoft-excel-file/
---
{{% alert color="primary" %}} 

من الممكن إنشاء ملفات Excel جديدة أو معالجة Microsoft موجودة ، على مواقع الويب في وضع واجهة المستخدم الرسومية باستخدام Aspose.Cells.GridWeb control. يمكن بعد ذلك حفظ الملفات في ملفات Excel. Aspose.Cells.GridWeb يعمل بشكل فعال كمحرر جداول بيانات على الإنترنت. يصف هذا الموضوع كيفية حفظ محتوى الشبكة في ملفات Excel.

{{% /alert %}} 
## **تصدير ملفات Excel**
### **تصدير كملف**
لحفظ محتوى عنصر تحكم Aspose.Cells.GridWeb كملف Excel:

1. قم بإضافة عنصر تحكم Aspose.Cells.GridWeb إلى نموذج الويب الخاص بك.
1. احفظ عملك كملف Excel في مسار محدد.
1. قم بتشغيل التطبيق.

{{% alert color="primary" %}} 

 إذا كنت لا تعرف كيفية إضافة Aspose.Cells.GridWeb control إلى نموذج الويب الخاص بك ، فعليك الرجوع إلى[أضف GridWeb إلى نموذج الويب](/cells/ar/net/add-gridweb-to-web-form/)

{{% /alert %}} 

عند إضافة عنصر تحكم ويب Aspose.Cells.GridWeb إلى نموذج windows ، يتم إنشاء عنصر التحكم تلقائيًا وإضافته إلى النموذج بالحجم الافتراضي. ليس عليك إنشاء عنصر تحكم Aspose.Cells.GridWeb ، كل ما عليك فعله هو سحب عنصر التحكم وإفلاته والبدء في استخدامه.

يوضح مثال الكود أدناه كيفية حفظ محتوى الشبكة في ملف Excel.



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFile.aspx-SaveExcelFile.cs" >}}

{{% alert color="primary" %}} 

إذا كان نظام الملفات لديك هو NTFS ، امنح حق الوصول للقراءة / الكتابة إلى حسابات المستخدمين ASPNET أو Everyone أو ستحصل على استثناء مرفوض في وقت التشغيل.

{{% /alert %}} 

يمكن استخدام مقتطف الشفرة أعلاه بعدة طرق. من الطرق الشائعة إضافة زر يحفظ محتوى الشبكة في ملف Excel عند النقر فوقه. Aspose.Cells.GridWeb يقدم طريقة أسهل للمهمة. Aspose.Cells.GridWeb له حدث يسمى SaveCommand. يمكن إضافة مقتطف الشفرة أعلاه إلى معالج الحدث SaveCommand والذي يسمح للمستخدمين بحفظ عملهم بالنقر فوق Aspose.Cells.GridWeb's المدمج**يحفظ** زر.

**حدث SaveCommand الخاص بـ GridWeb** 

![ما يجب القيام به: image_بديل_نص](export-microsoft-excel-file_1.jpg)

**حفظ محتوى الشبكة في Excel عن طريق النقر فوق الزر حفظ المدمج في GridWeb** 

![ما يجب القيام به: image_بديل_نص](export-microsoft-excel-file_2.png)

{{% alert color="primary" %}} 

 إذا كنت تعمل في Visual Studio ، يمكنك بسهولة إنشاء معالج حدث SaveCommand الخاص بالحدث عن طريق النقر نقرًا مزدوجًا فوق الحدث في**الخصائص** جزء. لمعرفة المزيد حول هذا ، يرجى الرجوع إلى[العمل مع أحداث GridWeb](/cells/ar/net/working-with-gridweb-events/)

{{% /alert %}} 
### **تصدير كتيار**
من الممكن أيضًا حفظ محتوى الشبكة إلى دفق (على سبيل المثال MemoryStream).



{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-GridWebBasics-ImportExportFileFromStream.aspx-SaveExcelFileUsingStream.cs" >}}
