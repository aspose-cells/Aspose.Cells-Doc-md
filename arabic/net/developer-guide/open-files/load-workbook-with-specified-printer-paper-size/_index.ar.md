---
title: تحميل المصنف بحجم ورق طابعة محدد
type: docs
weight: 430
url: /ar/net/load-workbook-with-specified-printer-paper-size/
---
{{% alert color="primary" %}}

 يمكنك تحديد حجم ورق الطابعة الذي تختاره أثناء تحميل المصنف باستخدام ملف[**LoadOptions.SetPaperSize ()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize) طريقة. يرجى ملاحظة أنه إذا قمت بإنشاء ملف جديد في MS Excel ، فستجد أن حجم الورق هو نفس إعداد الطابعة الافتراضية في جهازك.

{{% /alert %}}

 يوضح نموذج التعليمات البرمجية التالي استخدام[**LoadOptions.SetPaperSize ()**](https://reference.aspose.com/cells/net/aspose.cells/loadoptions/methods/setpapersize) طريقة. يقوم أولاً بإنشاء مصنف ، ثم يحفظه في دفق الذاكرة بتنسيق XLSX. ثم يتم تحميله بحجم ورق A5 وحفظه بتنسيق PDF. ثم يقوم بتحميله مرة أخرى بحجم ورق A3 وحفظه مرة أخرى بتنسيق PDF. إذا فتحت ملفات PDF الناتجة وتحققت من حجم الورق ، فسترى أنها مختلفة. أحدهما A5 والآخر A3. يرجى تنزيل ملف[A5 الإخراج PDF](5115234.pdf) و[خرج A3 PDF](5115233.pdf) التي تم إنشاؤها بواسطة رمز للرجوع اليها.

{{< gist "aspose-cells-gists" "88c9872508ec3150c552eb5155edf06e" "Examples-CSharp-Articles-LoadWorkbookWithPrinterSize-1.cs" >}}
