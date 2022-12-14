---
title: تحميل المصنف بحجم ورق طابعة محدد
type: docs
weight: 790
url: /ar/java/load-workbook-with-specified-printer-paper-size/
---
{{% alert color="primary" %}} 

 يمكنك تحديد حجم ورق الطابعة الذي تختاره أثناء تحميل المصنف باستخدام ملف[LoadOptions.setPaperSize ()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)) طريقة. يرجى ملاحظة أنه إذا قمت بإنشاء ملف جديد في MS Excel ، فستجد أن حجم الورق هو نفس إعداد الطابعة الافتراضية في جهازك.

{{% /alert %}} 
## **تحميل المصنف بحجم ورق طابعة محدد**
 يوضح نموذج التعليمات البرمجية التالي استخدام[LoadOptions.setPaperSize ()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\) طريقة. يقوم أولاً بإنشاء مصنف ، ثم يحفظه في دفق صفيف بايت بتنسيق XLSX. ثم يتم تحميله بحجم ورق A5 وحفظه بتنسيق PDF. ثم يقوم بتحميله مرة أخرى بحجم ورق A3 وحفظه مرة أخرى بتنسيق PDF. إذا فتحت ملفات PDF الناتجة وتحققت من حجم الورق ، فسترى أنها مختلفة. أحدهما A5 والآخر A3. يرجى تنزيل ملف[A5 إخراج PDF](5473435.pdf) و[إخراج A3 PDF](5473436.pdf) التي تم إنشاؤها بواسطة رمز للرجوع اليها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
