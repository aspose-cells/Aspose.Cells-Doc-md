---
title: الضغط HTTP
type: docs
weight: 10
url: /ar/net/http-compression/
---

## **مشكلة الضغط HTTP**
يقوم بعض المستخدمين بالإبلاغ عن أنه إذا قاموا بتكوين ضغط HTTP في IIS، يجدون أخطاء أثناء إرسال الملفات المولدة إلى متصفحي العملاء.
### **تفسير**
نحن نستخدم رأس **"Content-disposition", "inline; filename=test.xls"** لإجبار المتصفح على فتح الملف ورأس **"Content-disposition", "attachment; filename=test.xls"** لإجبار المتصفح على فتح حوار **Save As** واستخدام Microsoft Excel لفتح الملف. ومع ذلك، هناك بعض الاستثناءات التي توجد.
### **الاستثناءات**
يمكنك استخدام الكود التالي للتحقق من أنه ليس خطأ في Aspose.

{{< gist "aspose-cells-gists" "7c644a93d33d24299a618c1dda1a2385" "Examples.GridWeb-CSharp-KnowledgeBase-KnownIssues-HTTPCompression.aspx-HTTPCompression.cs" >}}
### **الحلول**
يمكنك استخدام واحدة من التقنيات البديلة التالية لحل هذه المشكلة:

- نقل تلك الملفات المحددة ASP.NET (التي تحتوي على رمز يدعو Aspose.Cells) إلى مجلد آخر غير مضغوط.
- تعطيل ضغط HTTP للمحتوى الديناميكي.
- حفظ الملف المولد على خادمك وتوفير رابط لمستخدميك.

إذا كنت ترغب في استخدام ضغط HTTP، يرجى دائمًا استخدام الخيار *OpenInExcel* بدلاً من الخيار *OpenInBrowser* عندما تعلم أنك قمت بتمكين ضغط IIS.
{{< app/cells/assistant language="csharp" >}}
