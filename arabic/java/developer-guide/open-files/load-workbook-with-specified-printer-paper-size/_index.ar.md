---
title: تحميل الدفتر بحجم ورقة الطابعة المحدد
type: docs
weight: 790
url: /ar/java/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}} 

يمكنك تحديد حجم الورق للطابعة الذي تختاره أثناء تحميل ملف العمل باستخدام طريقة [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize-int-). يرجى ملاحظة أنه إذا قمت بإنشاء ملف جديد في MS Excel، ستجد أن حجم الورقة هو نفس إعداد الطابعة الافتراضية على جهازك.

{{% /alert %}} 
## **تحميل الدفتر بحجم ورقة الطابعة المحدد**
الشيفرة النموذجية التالية توضح استخدام طريقة [LoadOptions.setPaperSize()](https://reference.aspose.com/cells/java/com.aspose.cells/loadoptions#setPaperSize-int-). في البداية ينشئ ملف عمل، ثم يحفظه في تدفق مصفوفة بايتات بصيغة XLSX. ثم يقوم بتحميله بحجم ورق A5 ويحفظه بصيغة PDF. ثم يحمله مرة أخرى بحجم ورق A3 ويحفظه مرة أخرى بصيغة PDF. إذا فتحت ملفات PDF الناتجة وتحققت من حجم الورق، سترى أنها مختلفة. واحدة A5 والأخرى A3. يرجى تحميل ملف PDF الناتج بـ [A5](5473435.pdf) و[PDF بحجم A3](5473436.pdf) الذي تم إنشاؤه بواسطة الكود للمرجعة.

{{< gist "aspose-cells-gists" "5876dc77e47649b66bdb5deefb4b5639" "Examples-src-main-java-com-aspose-cells-examples-articles-LoadWorkbook-LoadWorkbook.java" >}}
{{< app/cells/assistant language="java" >}}
