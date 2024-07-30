---
title: تحميل الدفتر بحجم ورقة الطابعة المحدد
type: docs
weight: 430
url: /ar/cpp/load-workbook-with-specified-printer-paper-size/
---

{{% alert color="primary" %}}

يمكنك تحديد حجم ورق الطابعة الخاص بك أثناء تحميل دفتر العمل الخاص بك باستخدام الطريقة [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/). يُرجى ملاحظة أنه إذا قمت بإنشاء ملف جديد في MS Excel، ستجد أن حجم الورق هو نفس إعداد طابعة الافتراضي في جهازك.

{{% /alert %}}

يوضح الكود عينة التالية استخدام الطريقة [**LoadOptions.SetPaperSize()**](https://reference.aspose.com/cells/cpp/aspose.cells/loadoptions/setpapersize/). يقوم أولاً بإنشاء دفتر عمل ، ثم يحفظه في تدفق الذاكرة بتنسيق XLSX. ثم يقوم بتحميله بحجم ورق A5 ويحفظه بصيغة PDF. ثم يقوم بتحميله مرة أخرى بحجم ورق A3 ويحفظه مرة أخرى بتنسيق PDF. إذا فتحت ملفات PDF الناتجة وفحصت حجم الورق الخاص بها ، سترى أنها مختلفة. إحداها بحجم A5 والأخرى بحجم A3. يرجى تنزيل [ملف PDF الناتج بحجم A5](PrinterSize-a5_out.pdf) و [ملف PDF الناتج بحجم A3](PrinterSize-a3_out.pdf) الذي تم إنشاؤه بواسطة الكود للرجوع إليه.

{{< gist "aspose-cells-gists" "6f7d9819d85793c3a3b5d040af42e1a9" "LoadWorkbookWithPrinterSize-1.cpp" >}}
