---
title: تحميل الدفتر بحجم ورقة الطابعة المحدد
type: docs
weight: 790
url: /ar/java/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}} 

يمكنك تحديد حجم ورقة الطابعة التي تفضلها أثناء تحميل دفتر العمل الخاص بك باستخدام طريقة [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)). يرجى ملاحظة أنه إذا قمت بإنشاء ملف جديد في MS Excel ، فستجد أن حجم الورق هو نفسه كضبط الطابعة الافتراضي في جهازك.

{{% /alert %}} 
## **تحميل الدفتر بحجم ورقة الطابعة المحدد**
الكود العيني التالي يوضح استخدام [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize\(int\)). يقوم أولاً بإنشاء دفتر عمل ، ثم يحفظه في تيار بيانات بتنسيق XLSX. ثم يقوم بتحميله بحجم ورق A5 ويحفظه كـ ملف PDF. ثم يقوم بتحميله مرة أخرى بحجم ورق A3 ويحفظه مرة أخرى بتنسيق PDF. إذا قمت بفتح ملفات PDF الناتجة وتحققت من حجم ورقها ، سترى أنها مختلفة. أحدها هو A5 والآخر هو A3. يرجى تنزيل [ملف PDF الناتج A5](5473435.pdf) و [ملف PDF الناتج A3](5473436.pdf) الناتجة عن الكود للرجوع إليها.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
